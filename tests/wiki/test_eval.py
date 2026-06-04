from __future__ import annotations

import pytest

from wq_agent.wiki.embeddings import NoOpEmbeddingProvider
from wq_agent.wiki.eval import GoldenQuery, evaluate_retriever, load_golden_queries
from wq_agent.wiki.index import WikiIndex
from wq_agent.wiki.store import WikiStore
from wq_agent.db import Database


@pytest.mark.asyncio
async def test_evaluate_retriever_computes_hit_and_mrr(wiki_root, tmp_path):
    store = WikiStore(wiki_root)
    db = Database(str(tmp_path / "wq.db"))
    await db.connect()
    embedder = NoOpEmbeddingProvider()
    try:
        index = WikiIndex(store=store, db=db, embedder=embedder)
        await index.build(incremental=False)
        assert index.retriever is not None
        report = await evaluate_retriever(
            index.retriever,
            [
                GoldenQuery(query="动量 ts_delta", expected=("concepts/momentum", "operators/ts_delta")),
                GoldenQuery(query="反转", expected=("concepts/reversal",)),
            ],
            top_k=3,
        )
        assert report.n_queries == 2
        assert report.hit_at_k == 1.0
        assert report.mrr > 0
        assert report.results[0].best_rank == 1
        assert "priority" in report.source_counts
    finally:
        await embedder.close()
        await db.close()


def test_load_golden_queries_from_yaml(tmp_path):
    path = tmp_path / "golden.yml"
    path.write_text(
        "- query: 动量\n  expected: [concepts/momentum, ts_delta]\n  note: test\n",
        encoding="utf-8",
    )
    queries = load_golden_queries(path)
    assert len(queries) == 1
    assert queries[0].query == "动量"
    assert queries[0].expected == ("concepts/momentum", "ts_delta")


def test_default_golden_queries_exist():
    queries = load_golden_queries()
    assert len(queries) >= 5
    assert all(q.query and q.expected for q in queries)


def test_repo_bench_file_loads_and_targets_exist():
    from pathlib import Path
    from wq_agent.wiki.store import WikiStore

    root = Path(__file__).resolve().parents[2]
    bench = root / "wiki" / "bench" / "retrieval_golden.yml"
    queries = load_golden_queries(bench)
    assert len(queries) >= 30

    store = WikiStore(root / "wiki")
    pages, errors = store.load_pages()
    assert errors == []
    targets = store._link_targets(pages)

    missing = []
    for q in queries:
        if not any(e in targets or any(t.endswith("/" + e) for t in targets) for e in q.expected):
            missing.append(q.query)
    assert missing == []


@pytest.mark.asyncio
async def test_repo_bench_retrieval_thresholds(tmp_path):
    import shutil
    from pathlib import Path

    root = Path(__file__).resolve().parents[2]
    wiki_copy = tmp_path / "wiki"
    shutil.copytree(
        root / "wiki",
        wiki_copy,
        ignore=shutil.ignore_patterns("graph_index.json"),
    )

    queries = load_golden_queries(wiki_copy / "bench" / "retrieval_golden.yml")
    store = WikiStore(wiki_copy)
    db = Database(str(tmp_path / "wq.db"))
    await db.connect()
    embedder = NoOpEmbeddingProvider()
    try:
        index = WikiIndex(store=store, db=db, embedder=embedder)
        await index.build(incremental=False)
        assert index.retriever is not None

        report = await evaluate_retriever(index.retriever, queries, top_k=5)

        assert report.hit_at_k >= 0.8
        assert report.mrr >= 0.6
    finally:
        await embedder.close()
        await db.close()
