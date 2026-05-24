from __future__ import annotations

import asyncio
import sys
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table
from loguru import logger

from .config import get_settings
from .models import GenerationStrategy, AlphaStatus
from .agent.orchestrator import Orchestrator

app = typer.Typer(
    name="wq-agent",
    help="WorldQuant Alpha Generation & Backtesting Agent Harness",
    add_completion=False,
)
wiki_app = typer.Typer(name="wiki", help="Quant Wiki maintenance commands", add_completion=False)
app.add_typer(wiki_app, name="wiki")
console = Console()


def _setup_logging(verbose: bool = False) -> None:
    level = "DEBUG" if verbose else "INFO"
    logger.remove()
    logger.add(sys.stderr, level=level, format="<level>{time:HH:mm:ss}</level> | <level>{message}</level>")
    logger.add("wq_agent.log", level="DEBUG", rotation="10 MB")


@app.command()
def generate(
    strategy: str = typer.Option("llm", "--strategy", "-s", help="Generation strategy: llm, template, factor_mining"),
    count: int = typer.Option(18, "--count", "-n", help="Number of alphas to generate"),
    no_backtest: bool = typer.Option(False, "--no-backtest", help="Skip auto-backtest"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
):
    """Generate new alpha expressions."""
    _setup_logging(verbose)

    async def _run():
        orch = Orchestrator()
        try:
            await orch.initialize()
            records = await orch.run(
                strategy=GenerationStrategy(strategy),
                count=count,
                auto_backtest=not no_backtest,
            )
            console.print(f"\n[bold green]Generated {len(records)} alphas[/bold green]")
        except Exception as e:
            console.print(f"[bold red]Error: {e}[/bold red]")
            raise typer.Exit(1)
        finally:
            await orch.close()

    asyncio.run(_run())


@app.command()
def backtest(
    ids: Optional[str] = typer.Option(None, "--ids", "-i", help="Comma-separated alpha IDs"),
    pending: bool = typer.Option(False, "--pending", help="Backtest all pending alphas"),
    all_generated: bool = typer.Option(False, "--all", help="Backtest all generated alphas"),
    max_concurrent: int = typer.Option(5, "--concurrent", "-c", help="Max concurrent simulations"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
):
    """Run backtests on generated alphas."""
    _setup_logging(verbose)

    async def _run():
        settings = get_settings()
        settings.WQ_MAX_CONCURRENT = max_concurrent
        orch = Orchestrator(settings)
        try:
            await orch.initialize()

            alpha_ids: list[int] = []
            if ids:
                alpha_ids = [int(x.strip()) for x in ids.split(",")]
            elif pending:
                all_alphas = await orch.db.list_alphas(status=AlphaStatus.GENERATED, limit=1000)
                alpha_ids = [a.id for a in all_alphas if a.id]
            elif all_generated:
                generated = await orch.db.list_alphas(status=AlphaStatus.GENERATED, limit=1000)
                failed = await orch.db.list_alphas(status=AlphaStatus.FAILED, limit=1000)
                alpha_ids = [a.id for a in generated + failed if a.id]
            else:
                console.print("[yellow]Specify --ids, --pending, or --all[/yellow]")
                raise typer.Exit(1)

            if not alpha_ids:
                console.print("[yellow]No alphas to backtest[/yellow]")
                return

            console.print(f"[bold cyan]Backtesting {len(alpha_ids)} alphas...[/bold cyan]")
            results = await orch.backtest(alpha_ids)
            console.print(f"[bold green]Backtest complete: {len(results)} results[/bold green]")
        except Exception as e:
            console.print(f"[bold red]Error: {e}[/bold red]")
            raise typer.Exit(1)
        finally:
            await orch.close()

    asyncio.run(_run())


@app.command(name="list")
def list_alphas(
    quality: Optional[str] = typer.Option(None, "--quality", "-q", help="Filter by quality: high, medium"),
    min_fitness: Optional[float] = typer.Option(None, "--min-fitness", help="Minimum fitness threshold"),
    status: Optional[str] = typer.Option(None, "--status", help="Filter by status"),
    limit: int = typer.Option(50, "--limit", "-n", help="Max results"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
):
    """List alphas and their results."""
    _setup_logging(verbose)

    async def _run():
        orch = Orchestrator()
        try:
            await orch.initialize()

            if quality or min_fitness:
                threshold = min_fitness or 0.5
                items = await orch.list_high_quality(threshold)
                if items:
                    table = Table(title=f"Alphas (fitness >= {threshold})")
                    table.add_column("ID", style="cyan", justify="right")
                    table.add_column("Expression", max_width=50)
                    table.add_column("Fitness", style="green", justify="right")
                    table.add_column("Sharpe", justify="right")
                    table.add_column("Turnover", justify="right")
                    table.add_column("Returns", justify="right")
                    table.add_column("Grade", justify="center")
                    for item in items:
                        table.add_row(
                            str(item["id"]),
                            item["expression"][:50],
                            f"{item['fitness']:.4f}" if item.get("fitness") else "N/A",
                            f"{item['sharpe']:.4f}" if item.get("sharpe") else "N/A",
                            f"{item['turnover']:.4f}" if item.get("turnover") else "N/A",
                            f"{item['returns']:.4f}" if item.get("returns") else "N/A",
                            str(item.get("grade", "")),
                        )
                    console.print(table)
                else:
                    console.print("[yellow]No alphas matching criteria[/yellow]")
            else:
                alpha_status = AlphaStatus(status) if status else None
                alphas = await orch.db.list_alphas(status=alpha_status, limit=limit)
                if alphas:
                    table = Table(title="Alphas")
                    table.add_column("ID", style="cyan", justify="right")
                    table.add_column("Expression", max_width=50)
                    table.add_column("Strategy", justify="center")
                    table.add_column("Status", justify="center")
                    table.add_column("Created", justify="right")
                    for a in alphas:
                        table.add_row(
                            str(a.id),
                            a.expression[:50],
                            a.strategy.value,
                            a.status.value,
                            a.created_at.strftime("%m-%d %H:%M"),
                        )
                    console.print(table)
                else:
                    console.print("[yellow]No alphas found[/yellow]")
        finally:
            await orch.close()

    asyncio.run(_run())


@app.command()
def run(
    strategy: str = typer.Option("llm", "--strategy", "-s", help="Generation strategy"),
    count: int = typer.Option(18, "--count", "-n", help="Alphas per batch"),
    batches: int = typer.Option(1, "--batches", "-b", help="Number of batches"),
    interval: int = typer.Option(60, "--interval", help="Seconds between batches"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
):
    """Full pipeline: generate → backtest → evaluate → display."""
    _setup_logging(verbose)

    async def _run():
        orch = Orchestrator()
        try:
            await orch.initialize()
            strat = GenerationStrategy(strategy)
            for batch_num in range(1, batches + 1):
                console.print(f"\n[bold magenta]═══ Batch {batch_num}/{batches} ═══[/bold magenta]")
                await orch.run(strategy=strat, count=count, auto_backtest=True)
                if batch_num < batches:
                    console.print(f"\n[dim]Waiting {interval}s before next batch...[/dim]")
                    await asyncio.sleep(interval)
        except Exception as e:
            console.print(f"[bold red]Error: {e}[/bold red]")
            raise typer.Exit(1)
        finally:
            await orch.close()

    asyncio.run(_run())


@app.command()
def status(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
):
    """Show overall statistics."""
    _setup_logging(verbose)

    async def _run():
        orch = Orchestrator()
        try:
            await orch.initialize()
            stats = await orch.status()
            table = Table(title="WQ Agent Status")
            table.add_column("Metric", style="cyan")
            table.add_column("Count", justify="right")
            for key, val in stats.items():
                table.add_row(key, str(val))
            console.print(table)
        finally:
            await orch.close()

    asyncio.run(_run())


@wiki_app.command("stats")
def wiki_stats(verbose: bool = typer.Option(False, "--verbose", "-v")):
    """Show wiki page / edge / embedding counts."""
    _setup_logging(verbose)
    from .wiki.store import WikiStore
    from .db import Database

    async def _run():
        settings = get_settings()
        store = WikiStore(settings.WIKI_DIR)
        db = Database(settings.DB_PATH)
        await db.connect()
        try:
            counts = await db.wiki_counts()
            pages, errors = store.load_pages() if store.exists() else ([], [])
            table = Table(title="Quant Wiki Stats")
            table.add_column("Metric", style="cyan")
            table.add_column("Value", justify="right")
            table.add_row("wiki dir exists", str(store.exists()))
            table.add_row("pages on disk", str(len(pages)))
            table.add_row("parse errors", str(len(errors)))
            table.add_row("pages in db", str(counts["wiki_pages"]))
            table.add_row("embeddings in db", str(counts["wiki_embeddings"]))
            table.add_row("sqlite-vec loaded", str(getattr(db, "vec_extension_loaded", False)))
            console.print(table)
        finally:
            await db.close()

    asyncio.run(_run())


@wiki_app.command("index")
def wiki_index(
    incremental: bool = typer.Option(False, "--incremental", help="Skip pages whose hash didn't change"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
):
    """(Re)build wiki indexes: page metadata, embeddings, graph."""
    _setup_logging(verbose)
    from .wiki.store import WikiStore
    from .wiki.index import WikiIndex
    from .wiki.embeddings import make_embedding_provider
    from .db import Database

    async def _run():
        settings = get_settings()
        store = WikiStore(settings.WIKI_DIR)
        if not store.exists():
            console.print(f"[yellow]Wiki dir not found at {settings.WIKI_DIR}[/yellow]")
            raise typer.Exit(0)
        db = Database(settings.DB_PATH)
        await db.connect()
        embedder = make_embedding_provider(settings)
        index = WikiIndex(
            store=store,
            db=db,
            embedder=embedder,
            grep_weight=settings.WIKI_GREP_WEIGHT,
            vector_weight=settings.WIKI_VECTOR_WEIGHT,
        )
        try:
            stats = await index.build(incremental=incremental)
            table = Table(title="Index built")
            table.add_column("Metric", style="cyan")
            table.add_column("Value", justify="right")
            for k, v in stats.__dict__.items():
                table.add_row(k, str(v))
            console.print(table)
        finally:
            await embedder.close()
            await db.close()

    asyncio.run(_run())


@wiki_app.command("search")
def wiki_search(
    query: str = typer.Argument(..., help="Query string"),
    top_k: int = typer.Option(5, "--top-k", "-k"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
):
    """Debug retrieval: run hybrid search and print hits."""
    _setup_logging(verbose)
    from .wiki.store import WikiStore
    from .wiki.index import WikiIndex
    from .wiki.embeddings import make_embedding_provider
    from .db import Database

    async def _run():
        settings = get_settings()
        store = WikiStore(settings.WIKI_DIR)
        if not store.exists():
            console.print(f"[yellow]Wiki dir not found at {settings.WIKI_DIR}[/yellow]")
            raise typer.Exit(1)
        db = Database(settings.DB_PATH)
        await db.connect()
        embedder = make_embedding_provider(settings)
        index = WikiIndex(
            store=store,
            db=db,
            embedder=embedder,
            grep_weight=settings.WIKI_GREP_WEIGHT,
            vector_weight=settings.WIKI_VECTOR_WEIGHT,
        )
        try:
            await index.build(incremental=True)
            retriever = index.retriever
            if retriever is None:
                console.print("[yellow]Retriever unavailable[/yellow]")
                raise typer.Exit(1)
            hits = await retriever.search(query, top_k=top_k)
            if not hits:
                console.print("[yellow]No hits[/yellow]")
                return
            table = Table(title=f'Results for "{query}"')
            table.add_column("#", justify="right")
            table.add_column("Score", justify="right", style="green")
            table.add_column("Page", style="cyan")
            table.add_column("Type")
            table.add_column("Sources")
            for i, h in enumerate(hits, 1):
                table.add_row(
                    str(i),
                    f"{h.score:.3f}",
                    h.page.title,
                    h.page.type.value,
                    ", ".join(h.sources),
                )
            console.print(table)
        finally:
            await embedder.close()
            await db.close()

    asyncio.run(_run())


@wiki_app.command("import-wq")
def wiki_import_wq(
    region: Optional[str] = typer.Option(None, "--region", help="Override WQ_REGION"),
    universe: Optional[str] = typer.Option(None, "--universe", help="Override WQ_UNIVERSE"),
    delay: Optional[int] = typer.Option(None, "--delay", help="Override WQ_DELAY"),
    limit_per_dataset: Optional[int] = typer.Option(None, "--limit-per-dataset", help="Cap fields per dataset (only matters with --with-fields)"),
    with_fields: bool = typer.Option(False, "--with-fields", help="Also write 7000+ per-field pages (usually unneeded; metadata is already inlined into dataset pages + dictionary)"),
    reindex: bool = typer.Option(True, "--reindex/--no-reindex", help="Rebuild wiki index after import"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
):
    """Import official WQ Brain docs (operators / datasets, optionally per-field pages) into wiki/."""
    _setup_logging(verbose)
    from .wq.client import WQClient
    from .wiki.importers import WQDocImporter
    from .wiki.store import WikiStore
    from .wiki.index import WikiIndex
    from .wiki.embeddings import make_embedding_provider
    from .db import Database
    from pathlib import Path

    async def _run():
        settings = get_settings()
        client = WQClient(settings)
        await client.connect()
        try:
            importer = WQDocImporter(Path(settings.WIKI_DIR), client)
            stats = await importer.import_all(
                region=region,
                universe=universe,
                delay=delay,
                limit_per_dataset=limit_per_dataset,
                include_fields=with_fields,
            )
            table = Table(title="WQ docs imported")
            table.add_column("Kind", style="cyan")
            table.add_column("Pages written", justify="right")
            for k, v in stats.__dict__.items():
                table.add_row(k, str(v))
            console.print(table)
        finally:
            await client.close()

        if reindex:
            store = WikiStore(settings.WIKI_DIR)
            db = Database(settings.DB_PATH)
            await db.connect()
            embedder = make_embedding_provider(settings)
            idx = WikiIndex(store=store, db=db, embedder=embedder,
                             grep_weight=settings.WIKI_GREP_WEIGHT,
                             vector_weight=settings.WIKI_VECTOR_WEIGHT)
            try:
                istats = await idx.build(incremental=True)
                console.print(f"[dim]Reindexed: {istats.pages} pages, {istats.embeddings} embeddings[/dim]")
            finally:
                await embedder.close()
                await db.close()

    asyncio.run(_run())


@wiki_app.command("import-paper")
def wiki_import_paper(
    url: Optional[str] = typer.Option(None, "--url", help="arxiv.org/abs/<id> or papers.ssrn.com/...?abstract_id=<id>"),
    manual: bool = typer.Option(False, "--manual", help="Provide all fields by flag instead of fetching"),
    title: Optional[str] = typer.Option(None, "--title"),
    authors: Optional[str] = typer.Option(None, "--authors", help="Comma-separated"),
    year: Optional[int] = typer.Option(None, "--year"),
    abstract: Optional[str] = typer.Option(None, "--abstract"),
    tags: Optional[str] = typer.Option(None, "--tags", help="Comma-separated extra tags"),
    reindex: bool = typer.Option(False, "--reindex", help="Rebuild wiki index after writing"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
):
    """Import a research paper into wiki/papers/ (arxiv / SSRN auto-fetch, or --manual)."""
    _setup_logging(verbose)
    from .wiki.importers import PaperImporter
    from .wiki.store import WikiStore
    from .wiki.index import WikiIndex
    from .wiki.embeddings import make_embedding_provider
    from .db import Database
    from pathlib import Path

    tag_list = [t.strip() for t in (tags or "").split(",") if t.strip()]

    async def _run():
        settings = get_settings()
        importer = PaperImporter(Path(settings.WIKI_DIR))
        if manual:
            if not title:
                console.print("[red]--manual requires --title (and optionally --authors / --year / --url / --abstract)[/red]")
                raise typer.Exit(1)
            path = importer.import_manual(
                title=title,
                authors=[a.strip() for a in (authors or "").split(",") if a.strip()],
                year=year,
                url=url or "",
                abstract=abstract or "",
                tags=tag_list,
            )
        else:
            if not url:
                console.print("[red]Provide --url or use --manual[/red]")
                raise typer.Exit(1)
            path = await importer.import_url(url, tags=tag_list)
        console.print(f"[green]Wrote {path}[/green]")

        if reindex:
            store = WikiStore(settings.WIKI_DIR)
            db = Database(settings.DB_PATH)
            await db.connect()
            embedder = make_embedding_provider(settings)
            idx = WikiIndex(store=store, db=db, embedder=embedder,
                             grep_weight=settings.WIKI_GREP_WEIGHT,
                             vector_weight=settings.WIKI_VECTOR_WEIGHT)
            try:
                await idx.build(incremental=True)
            finally:
                await embedder.close()
                await db.close()

    asyncio.run(_run())


if __name__ == "__main__":
    app()
