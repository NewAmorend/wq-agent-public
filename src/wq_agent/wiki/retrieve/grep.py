from __future__ import annotations

import math
import re
import shutil
import subprocess
from dataclasses import dataclass

from loguru import logger

from ..schema import Page
from ..tokenize import Tokenizer


@dataclass
class GrepHit:
    page: Page
    score: float
    matched_originals: set[str]
    matched_all_originals: bool


class GrepChannel:
    """ripgrep + IDF + Coverage scoring (no BM25)."""

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
        self._rg = shutil.which("rg")
        self.df = df if df is not None else self._build_df(pages)

    @staticmethod
    def _build_df(pages: list[Page]) -> dict[str, int]:
        df: dict[str, int] = {}
        for p in pages:
            seen: set[str] = set()
            text = (p.title + "\n" + p.body).lower()
            for word in re.findall(r"[a-z0-9_]+|[一-鿿]+", text):
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

    def _count_in_page(self, page: Page, token: str) -> int:
        haystack = (page.title + "\n" + page.body).lower()
        needle = token.lower()
        if not needle:
            return 0
        if self._rg:
            try:
                proc = subprocess.run(
                    [self._rg, "--count-matches", "-F", "-i", "--", needle, str(page.path)],
                    capture_output=True,
                    text=True,
                    timeout=5,
                )
                if proc.returncode in (0, 1):
                    out = proc.stdout.strip()
                    if not out:
                        return 0
                    parts = out.splitlines()[-1].split(":")
                    try:
                        return int(parts[-1])
                    except ValueError:
                        return 0
            except Exception as exc:
                logger.debug(f"rg failed for {page.path}: {exc}; falling back to python")
        return haystack.count(needle)

    def search(self, query: str, top_k: int = 10) -> list[GrepHit]:
        tokens = self.tokenizer.tokenize(query)
        if not tokens:
            return []
        weighted, originals = self.tokenizer.expand_synonyms(tokens)
        if not weighted:
            return []

        denom = sum(self.idf(t) * w for t, w in weighted) or 1.0
        original_count = len(originals) or 1

        hits: list[GrepHit] = []
        for page in self.pages:
            matched_weighted = 0.0
            matched_originals: set[str] = set()
            for tok, weight in weighted:
                cnt = self._count_in_page(page, tok)
                if cnt > 0:
                    matched_weighted += self.idf(tok) * weight
                    if tok in originals:
                        matched_originals.add(tok)
            if matched_weighted <= 0:
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
