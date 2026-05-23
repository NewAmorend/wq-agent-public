from __future__ import annotations

import math
import re
from dataclasses import dataclass

from ..schema import Page
from ..tokenize import Tokenizer


@dataclass
class GrepHit:
    page: Page
    score: float
    matched_originals: set[str]
    matched_all_originals: bool


class GrepChannel:
    """In-memory IDF + Coverage scoring (no BM25).

    旧版每个 (token, page) 起一次 ripgrep 子进程，7700 页时阻塞十几分钟。
    现在 pages.body 本来就在内存里，全部预先 lowercase 一次，per-token 走 str.count
    避免 77K 次 fork。
    """

    SCORE_CAP = 0.85

    def __init__(
        self,
        pages: list[Page],
        tokenizer: Tokenizer,
        df: dict[str, int] | None = None,
    ):
        self.pages = pages
        self.tokenizer = tokenizer
        self.n_pages = max(len(pages), 1)
        # 预先 lowercase 一份大文本，搜的时候只做 str.count
        self._haystack: list[tuple[Page, str]] = [
            (p, (p.title + "\n" + p.body).lower()) for p in pages
        ]
        self.df = df if df is not None else self._build_df(pages)

    @staticmethod
    def _build_df(pages: list[Page]) -> dict[str, int]:
        df: dict[str, int] = {}
        token_re = re.compile(r"[a-z0-9_]+|[一-鿿]+")
        for p in pages:
            seen: set[str] = set()
            text = (p.title + "\n" + p.body).lower()
            for word in token_re.findall(text):
                if word in seen:
                    continue
                seen.add(word)
                df[word] = df.get(word, 0) + 1
        return df

    def idf(self, token: str) -> float:
        token = token.lower()
        d = self.df.get(token, 0)
        if d == 0:
            return math.log(self.n_pages + 1)
        return math.log(self.n_pages / d)

    def search(self, query: str, top_k: int = 10) -> list[GrepHit]:
        tokens = self.tokenizer.tokenize(query)
        if not tokens:
            return []
        weighted, originals = self.tokenizer.expand_synonyms(tokens)
        if not weighted:
            return []

        # 预先 lowercase 全部 query tokens；过滤空 token
        weighted_lc: list[tuple[str, float]] = [
            (t.lower(), w) for t, w in weighted if t
        ]
        originals_lc = {t.lower() for t in originals if t}

        denom = sum(self.idf(t) * w for t, w in weighted_lc) or 1.0
        original_count = len(originals_lc) or 1
        idf_cache = {t: self.idf(t) for t, _ in weighted_lc}

        hits: list[GrepHit] = []
        for page, haystack in self._haystack:
            matched_weighted = 0.0
            matched_originals: set[str] = set()
            for tok, weight in weighted_lc:
                if tok and tok in haystack:
                    matched_weighted += idf_cache[tok] * weight
                    if tok in originals_lc:
                        matched_originals.add(tok)
            # 命中 0 个 token → 跳过；命中但 IDF=0（query 全是高频词）→ 仍按 coverage 计分
            if not matched_originals:
                continue
            coverage = len(matched_originals) / original_count
            score = 0.6 * (matched_weighted / denom) + 0.25 * coverage
            score = min(score, self.SCORE_CAP)
            hits.append(
                GrepHit(
                    page=page,
                    score=score,
                    matched_originals=matched_originals,
                    matched_all_originals=len(matched_originals) == original_count,
                )
            )

        hits.sort(key=lambda h: h.score, reverse=True)
        return hits[:top_k]
