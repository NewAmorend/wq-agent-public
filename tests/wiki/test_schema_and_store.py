from __future__ import annotations

from pathlib import Path

import pytest

from wq_agent.wiki.schema import PageType, parse_page
from wq_agent.wiki.store import WikiStore


def test_parse_page_extracts_frontmatter_and_links(wiki_root: Path):
    page = parse_page(wiki_root / "concepts/momentum.md")
    assert page.title == "动量"
    assert page.type is PageType.CONCEPT
    assert "momentum" in page.tags
    assert "ts_delta" in page.wikilinks
    assert "ts_decay_linear" in page.wikilinks
    assert page.summary(40).endswith("…") or len(page.summary(40)) <= 40


def test_parse_page_rejects_missing_frontmatter(tmp_path: Path):
    p = tmp_path / "bad.md"
    p.write_text("no frontmatter here\n", encoding="utf-8")
    with pytest.raises(ValueError):
        parse_page(p)


def test_store_iterates_real_pages_only(wiki_root: Path):
    store = WikiStore(wiki_root)
    pages, errors = store.load_pages()
    assert errors == []
    assert len(pages) == 4  # 2 concepts + 2 operators


def test_store_finds_broken_links(wiki_root: Path):
    (wiki_root / "concepts/orphan_link.md").write_text(
        "---\ntitle: 孤儿\ntype: concept\ntags: [test]\ncreated: 2026-05-22\n---\n\n看 [[不存在的页]]。\n",
        encoding="utf-8",
    )
    store = WikiStore(wiki_root)
    pages, _ = store.load_pages()
    broken = store.find_broken_links(pages)
    assert any("不存在的页" in misses for _, misses in broken)
