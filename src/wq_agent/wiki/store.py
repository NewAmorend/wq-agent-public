from __future__ import annotations

from pathlib import Path
from typing import Iterator

from loguru import logger

from .schema import Page, parse_page


_RESERVED_DIRS = {"dictionary"}
_RESERVED_FILES = {"SCHEMA.md", "index.md", "log.md"}


class WikiStore:
    """File-system view of the wiki/ tree."""

    def __init__(self, root: str | Path):
        self.root = Path(root)

    def exists(self) -> bool:
        return self.root.is_dir()

    def iter_page_paths(self) -> Iterator[Path]:
        if not self.exists():
            return
        for path in sorted(self.root.rglob("*.md")):
            rel = path.relative_to(self.root)
            if rel.parts and rel.parts[0] in _RESERVED_DIRS:
                continue
            if rel.name in _RESERVED_FILES and len(rel.parts) == 1:
                continue
            yield path

    def load_pages(self) -> tuple[list[Page], list[tuple[Path, str]]]:
        pages: list[Page] = []
        errors: list[tuple[Path, str]] = []
        for path in self.iter_page_paths():
            try:
                pages.append(parse_page(path))
            except Exception as exc:
                logger.warning(f"Skipping {path}: {exc}")
                errors.append((path, str(exc)))
        return pages, errors

    def find_broken_links(self, pages: list[Page]) -> list[tuple[Page, list[str]]]:
        slug_set = {p.slug for p in pages}
        title_set = {p.title for p in pages}
        broken: list[tuple[Page, list[str]]] = []
        for p in pages:
            misses = [
                link for link in p.wikilinks
                if link not in slug_set and link not in title_set
            ]
            if misses:
                broken.append((p, misses))
        return broken

    def dictionary_path(self) -> Path:
        return self.root / "dictionary" / "base.txt"

    def auto_dictionary_path(self) -> Path:
        return self.root / "dictionary" / "auto.txt"

    def synonyms_path(self) -> Path:
        return self.root / "dictionary" / "synonyms.yaml"

    def graph_index_path(self) -> Path:
        return self.root / "graph_index.json"
