from __future__ import annotations

import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import networkx as nx
from loguru import logger

from ..schema import Page


@dataclass
class GraphHit:
    page: Page
    score: float
    reason: str


class GraphChannel:
    """wikilink + shared_tag(>=3) + shared_source edges → Louvain + PageRank."""

    MIN_SHARED_TAG = 2  # >=2 共享标签建图边（用于社区检测）
    EXPAND_SHARED_TAG = 3  # >=3 共享标签才做邻居扩展（更严格）

    def __init__(self, pages: list[Page]):
        self.pages = pages
        self.pages_by_slug: dict[str, Page] = {p.slug: p for p in pages}
        self.pages_by_title: dict[str, Page] = {p.title: p for p in pages}
        self.graph = self._build_graph(pages)
        self.pagerank: dict[str, float] = {}
        self.communities: dict[str, int] = {}
        if self.graph.number_of_nodes() >= 3:
            try:
                self.pagerank = nx.pagerank(self.graph, alpha=0.85, max_iter=30)
            except Exception as exc:
                logger.debug(f"PageRank failed: {exc}")
                self.pagerank = {n: 1.0 / max(self.graph.number_of_nodes(), 1) for n in self.graph.nodes}
        if self.graph.number_of_edges() > 0:
            try:
                import community as community_louvain  # python-louvain
                undirected = self.graph.to_undirected()
                self.communities = community_louvain.best_partition(undirected, random_state=42)
            except Exception as exc:
                logger.debug(f"Louvain failed: {exc}")
                self.communities = {}

    def _resolve(self, name: str) -> Page | None:
        return self.pages_by_slug.get(name) or self.pages_by_title.get(name)

    def _build_graph(self, pages: list[Page]) -> nx.DiGraph:
        g = nx.DiGraph()
        for p in pages:
            g.add_node(p.slug, type=p.type.value, title=p.title)

        # wikilink edges
        for p in pages:
            for link in p.wikilinks:
                target = self._resolve(link)
                if target and target.slug != p.slug:
                    g.add_edge(p.slug, target.slug, kind="wikilink")

        # shared_tag edges (undirected → add both directions)
        for i, a in enumerate(pages):
            ta = set(a.tags)
            for b in pages[i + 1 :]:
                shared = ta & set(b.tags)
                if len(shared) >= self.MIN_SHARED_TAG:
                    g.add_edge(a.slug, b.slug, kind="shared_tag", weight=len(shared))
                    g.add_edge(b.slug, a.slug, kind="shared_tag", weight=len(shared))

        # shared_source edges
        for i, a in enumerate(pages):
            sa = set(a.sources)
            if not sa:
                continue
            for b in pages[i + 1 :]:
                sb = set(b.sources)
                if sa & sb:
                    g.add_edge(a.slug, b.slug, kind="shared_source")
                    g.add_edge(b.slug, a.slug, kind="shared_source")

        return g

    def expand(self, seed_slugs: Iterable[str], k: int = 2) -> list[GraphHit]:
        if self.graph.number_of_nodes() < 10:
            return []
        seeds = list(seed_slugs)
        if not seeds:
            return []
        candidates: Counter[str] = Counter()
        reasons: dict[str, str] = {}
        for seed in seeds:
            if seed not in self.graph:
                continue
            for nbr in self.graph.successors(seed):
                edge = self.graph.get_edge_data(seed, nbr) or {}
                kind = edge.get("kind", "")
                if kind == "wikilink":
                    candidates[nbr] += 2
                    reasons.setdefault(nbr, "wikilink")
                elif kind == "shared_tag" and edge.get("weight", 0) >= self.EXPAND_SHARED_TAG:
                    candidates[nbr] += 1
                    reasons.setdefault(nbr, f"shared_tag={edge.get('weight')}")
        for s in seeds:
            candidates.pop(s, None)
        ranked = sorted(
            candidates.items(),
            key=lambda kv: (kv[1], self.pagerank.get(kv[0], 0.0)),
            reverse=True,
        )
        hits: list[GraphHit] = []
        for slug, votes in ranked[:k]:
            page = self.pages_by_slug.get(slug)
            if page:
                hits.append(GraphHit(page=page, score=votes * 0.1, reason=reasons[slug]))
        return hits

    def to_json(self) -> dict:
        return {
            "nodes": [
                {
                    "slug": n,
                    "title": self.graph.nodes[n].get("title"),
                    "type": self.graph.nodes[n].get("type"),
                    "pagerank": self.pagerank.get(n, 0.0),
                    "community": self.communities.get(n, -1),
                }
                for n in self.graph.nodes
            ],
            "edges": [
                {"src": u, "dst": v, **self.graph.get_edge_data(u, v)}
                for u, v in self.graph.edges
            ],
            "stats": {
                "nodes": self.graph.number_of_nodes(),
                "edges": self.graph.number_of_edges(),
                "communities": len(set(self.communities.values())) if self.communities else 0,
            },
        }

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_json(), ensure_ascii=False, indent=2), encoding="utf-8")
