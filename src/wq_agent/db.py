from __future__ import annotations

import json
import re
import struct
from datetime import datetime
from typing import Any

import aiosqlite
from loguru import logger

from .models import AlphaRecord, AlphaStatus, BacktestResult, GenerationStrategy, QualityGrade


# Structural-skeleton normalizer for exemplar diversification.
# 把表达式里的字段名（>=3 字符的小写标识符）替换成 FIELD、数字替换成 N，
# 得到 "结构骨架"。两个 alpha 同骨架意味着只是换了字段/窗口，本质上结构相同。
_FIELD_RE = re.compile(r"\b[a-z_][a-z0-9_]{2,}\b")
_NUM_RE = re.compile(r"\b\d+(\.\d+)?\b")
# 不视为 field 的关键字（算子名、分组名等）—— 必须保留以区分结构。
_SKELETON_KEEP = {
    "rank", "zscore", "scale", "normalize", "winsorize", "quantile", "log", "abs",
    "sign", "sqrt", "inverse", "reverse", "power", "signed_power", "tanh", "sigmoid",
    "exp", "min", "max", "median",
    "ts_mean", "ts_std_dev", "ts_sum", "ts_max", "ts_min", "ts_delta", "ts_delay",
    "ts_shift", "ts_rank", "ts_corr", "ts_covariance", "ts_decay_linear", "ts_zscore",
    "ts_av_diff", "ts_backfill", "ts_scale", "ts_quantile", "ts_argmax", "ts_argmin",
    "ts_arg_max", "ts_arg_min", "ts_product", "ts_step", "ts_count_nans", "ts_regression",
    "decay_linear", "hump", "jump_decay", "days_from_last_change", "trade_when",
    "group_neutralize", "group_rank", "group_zscore", "group_mean", "group_min",
    "group_max", "group_scale", "group_backfill", "group_cartesian_product",
    "vector_neut", "vec_avg", "vec_max", "vec_min", "vec_sum",
    "add", "subtract", "multiply", "divide", "densify", "to_nan",
    "bucket", "combo_a", "trade_when", "if_else", "is_nan",
    "and", "or", "not", "where",
    "reduce_avg", "reduce_choose", "reduce_count", "reduce_ir", "reduce_max",
    "reduce_min", "reduce_norm", "reduce_powersum", "reduce_range", "reduce_skewness",
    "reduce_stddev", "reduce_sum", "self_corr",
    "subindustry", "industry", "sector", "country", "currency", "exchange",
}


def expression_skeleton(expr: str) -> str:
    """规约表达式为"结构骨架"，用于 exemplar 多样性去重。

    示例：
      ts_decay_linear(rank(mdl177_x), 20) -> ts_decay_linear(rank(FIELD), N)
      ts_decay_linear(rank(fnd6_y), 60)   -> ts_decay_linear(rank(FIELD), N)   ← 同骨架
      add(rank(close), ts_corr(vwap, volume, 10)) -> add(rank(FIELD), ts_corr(FIELD, FIELD, N))
    """
    if not expr:
        return ""

    def _replace(m: re.Match) -> str:
        tok = m.group(0)
        return tok if tok in _SKELETON_KEEP else "FIELD"

    skel = _FIELD_RE.sub(_replace, expr.lower())
    skel = _NUM_RE.sub("N", skel)
    skel = re.sub(r"\s+", "", skel)
    return skel


def expression_outer_signature(expr: str, levels: int = 2) -> str:
    """提取表达式最外层 N 个算子链作为"外壳签名"，用于阻止同 wrapper 家族霸屏。

    full skeleton 看整个结构，outer signature 只看最外两层算子。例如：
      ts_decay_linear(group_neutralize(rank(F), subindustry), N)  ← outer 2: ts_decay_linear(group_neutralize)
      ts_decay_linear(group_neutralize(rank(signed_power(F,N)), subindustry), N)  ← 同 outer 2

    所以两个 alpha 即使骨架不同，只要外壳是同一组 wrapper 就被视为同 family。
    """
    if not expr:
        return ""
    # 用 skeleton 形式再扫前 N 个开括号前的算子名
    skel = expression_skeleton(expr)
    sig_ops: list[str] = []
    i = 0
    while i < len(skel) and len(sig_ops) < levels:
        # 找下一个算子（以字母开头，跟到 "(" 前）
        m = re.match(r"([a-z_][a-z0-9_]*)\(", skel[i:])
        if not m:
            break
        op = m.group(1)
        sig_ops.append(op)
        i += m.end()
    return "(".join(sig_ops)

_SCHEMA = """
CREATE TABLE IF NOT EXISTS alphas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    expression TEXT NOT NULL,
    strategy TEXT NOT NULL,
    llm_model TEXT,
    status TEXT NOT NULL DEFAULT 'generated',
    created_at TIMESTAMP NOT NULL,
    submitted_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS backtest_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    alpha_id INTEGER NOT NULL REFERENCES alphas(id),
    region TEXT NOT NULL,
    universe TEXT NOT NULL,
    delay INTEGER NOT NULL,
    decay INTEGER NOT NULL,
    neutralization TEXT NOT NULL,
    sharpe REAL,
    turnover REAL,
    fitness REAL,
    returns REAL,
    drawdown REAL,
    grade TEXT,
    checks TEXT,
    wq_alpha_id TEXT,
    created_at TIMESTAMP NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_alphas_status ON alphas(status);
CREATE INDEX IF NOT EXISTS idx_backtest_alpha_id ON backtest_results(alpha_id);
CREATE INDEX IF NOT EXISTS idx_backtest_fitness ON backtest_results(fitness);

CREATE TABLE IF NOT EXISTS wiki_pages (
    path TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    type TEXT NOT NULL,
    tags TEXT,
    sources TEXT,
    content_hash TEXT NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS wiki_embeddings_blob (
    page_path TEXT PRIMARY KEY REFERENCES wiki_pages(path) ON DELETE CASCADE,
    dim INTEGER NOT NULL,
    embedding BLOB NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS field_blacklist (
    field_id TEXT PRIMARY KEY,
    fail_count INTEGER NOT NULL DEFAULT 0,
    last_reason TEXT,
    last_seen TIMESTAMP NOT NULL
);
"""


class Database:
    def __init__(self, db_path: str = "./wq_agent.db"):
        self.db_path = db_path
        self._conn: aiosqlite.Connection | None = None

    async def connect(self) -> None:
        self._conn = await aiosqlite.connect(self.db_path)
        self._conn.row_factory = aiosqlite.Row
        self.vec_extension_loaded = await self._try_load_sqlite_vec()
        await self._exec_script(_SCHEMA)

    async def _try_load_sqlite_vec(self) -> bool:
        assert self._conn is not None
        try:
            import sqlite_vec  # type: ignore
        except ImportError:
            return False
        try:
            await self._conn.enable_load_extension(True)
            await self._conn.load_extension(sqlite_vec.loadable_path())
            await self._conn.enable_load_extension(False)
            logger.debug("Loaded sqlite-vec extension")
            return True
        except Exception as exc:
            logger.debug(f"sqlite-vec not available: {exc}")
            return False

    async def close(self) -> None:
        if self._conn:
            await self._conn.close()
            self._conn = None

    async def _exec_script(self, sql: str) -> None:
        assert self._conn is not None
        await self._conn.executescript(sql)
        await self._conn.commit()

    async def insert_alpha(self, alpha: AlphaRecord) -> int:
        assert self._conn is not None
        cursor = await self._conn.execute(
            """INSERT INTO alphas (expression, strategy, llm_model, status, created_at)
               VALUES (?, ?, ?, ?, ?)""",
            (alpha.expression, alpha.strategy.value, alpha.llm_model, alpha.status.value, alpha.created_at.isoformat()),
        )
        await self._conn.commit()
        return cursor.lastrowid

    async def batch_insert_alphas(self, alphas: list[AlphaRecord]) -> list[int]:
        assert self._conn is not None
        ids = []
        for alpha in alphas:
            cursor = await self._conn.execute(
                """INSERT INTO alphas (expression, strategy, llm_model, status, created_at)
                   VALUES (?, ?, ?, ?, ?)""",
                (alpha.expression, alpha.strategy.value, alpha.llm_model, alpha.status.value, alpha.created_at.isoformat()),
            )
            ids.append(cursor.lastrowid)
        await self._conn.commit()
        return ids

    async def update_alpha_status(self, alpha_id: int, status: AlphaStatus) -> None:
        assert self._conn is not None
        await self._conn.execute(
            "UPDATE alphas SET status = ? WHERE id = ?",
            (status.value, alpha_id),
        )
        await self._conn.commit()

    async def get_alpha(self, alpha_id: int) -> AlphaRecord | None:
        assert self._conn is not None
        row = await self._conn.execute("SELECT * FROM alphas WHERE id = ?", (alpha_id,))
        record = await row.fetchone()
        if not record:
            return None
        return AlphaRecord(
            id=record["id"],
            expression=record["expression"],
            strategy=GenerationStrategy(record["strategy"]),
            llm_model=record["llm_model"],
            status=AlphaStatus(record["status"]),
            created_at=datetime.fromisoformat(record["created_at"]),
            submitted_at=datetime.fromisoformat(record["submitted_at"]) if record["submitted_at"] else None,
        )

    async def list_alphas(
        self,
        status: AlphaStatus | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> list[AlphaRecord]:
        assert self._conn is not None
        if status:
            cursor = await self._conn.execute(
                "SELECT * FROM alphas WHERE status = ? ORDER BY created_at DESC LIMIT ? OFFSET ?",
                (status.value, limit, offset),
            )
        else:
            cursor = await self._conn.execute(
                "SELECT * FROM alphas ORDER BY created_at DESC LIMIT ? OFFSET ?",
                (limit, offset),
            )
        rows = await cursor.fetchall()
        results = []
        for r in rows:
            results.append(
                AlphaRecord(
                    id=r["id"],
                    expression=r["expression"],
                    strategy=GenerationStrategy(r["strategy"]),
                    llm_model=r["llm_model"],
                    status=AlphaStatus(r["status"]),
                    created_at=datetime.fromisoformat(r["created_at"]),
                    submitted_at=datetime.fromisoformat(r["submitted_at"]) if r["submitted_at"] else None,
                )
            )
        return results

    async def insert_backtest_result(self, result: BacktestResult) -> int:
        assert self._conn is not None
        checks_json = json.dumps(result.checks) if result.checks else None
        grade_val = result.grade.value if result.grade else None
        cursor = await self._conn.execute(
            """INSERT INTO backtest_results
               (alpha_id, region, universe, delay, decay, neutralization,
                sharpe, turnover, fitness, returns, drawdown, grade, checks, wq_alpha_id, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                result.alpha_id, result.region, result.universe, result.delay,
                result.decay, result.neutralization, result.sharpe, result.turnover,
                result.fitness, result.returns, result.drawdown, grade_val,
                checks_json, result.wq_alpha_id, result.created_at.isoformat(),
            ),
        )
        await self._conn.commit()
        return cursor.lastrowid

    async def get_backtest_result(self, alpha_id: int) -> BacktestResult | None:
        assert self._conn is not None
        cursor = await self._conn.execute(
            "SELECT * FROM backtest_results WHERE alpha_id = ? ORDER BY created_at DESC LIMIT 1",
            (alpha_id,),
        )
        r = await cursor.fetchone()
        if not r:
            return None
        checks = json.loads(r["checks"]) if r["checks"] else None
        grade = QualityGrade(r["grade"]) if r["grade"] else None
        return BacktestResult(
            id=r["id"],
            alpha_id=r["alpha_id"],
            region=r["region"],
            universe=r["universe"],
            delay=r["delay"],
            decay=r["decay"],
            neutralization=r["neutralization"],
            sharpe=r["sharpe"],
            turnover=r["turnover"],
            fitness=r["fitness"],
            returns=r["returns"],
            drawdown=r["drawdown"],
            grade=grade,
            checks=checks,
            wq_alpha_id=r["wq_alpha_id"],
            created_at=datetime.fromisoformat(r["created_at"]),
        )

    async def list_recent_backtested_alphas(self, limit: int = 20) -> list[dict[str, Any]]:
        """最近回测过的 alpha + 关键指标，供 generator 当 previous_results 喂回 LLM。"""
        assert self._conn is not None
        cursor = await self._conn.execute(
            """SELECT a.id AS alpha_id, a.expression, a.strategy, a.created_at,
                      b.fitness, b.sharpe, b.turnover, b.returns, b.grade, b.checks
               FROM alphas a
               JOIN backtest_results b ON a.id = b.alpha_id
               WHERE b.fitness IS NOT NULL
               ORDER BY b.created_at DESC
               LIMIT ?""",
            (limit,),
        )
        rows = await cursor.fetchall()
        out: list[dict[str, Any]] = []
        for r in rows:
            checks_raw = r["checks"]
            checks: list[dict] = []
            if checks_raw:
                try:
                    checks = json.loads(checks_raw)
                except (json.JSONDecodeError, TypeError):
                    checks = []
            failed = [
                str(c.get("name", ""))
                for c in checks
                if isinstance(c, dict) and str(c.get("result", "")).upper() == "FAIL"
            ]
            out.append({
                "alpha_id": r["alpha_id"],
                "alpha": r["expression"],
                "strategy": r["strategy"],
                "performance": {
                    "fitness": r["fitness"],
                    "sharpe": r["sharpe"],
                    "turnover": r["turnover"],
                    "returns": r["returns"],
                    "grade": r["grade"],
                },
                "failed_checks": failed,
            })
        return out

    async def list_refine_candidates(self, limit: int = 10, low_fitness_floor: float = 0.5) -> list[dict[str, Any]]:
        """差一点就过的 alpha：MEDIUM 全部 + 高 fitness 的 LOW。按 fitness 倒序。

        - MEDIUM：只差 1 项 WQ 关键检查 FAIL，refine 性价比最高
        - LOW with fitness >= low_fitness_floor：信号已经出来（fitness 高），但有 2+ 项 check
          fail（典型是 sharpe 不达标），refine 可以同时修多项
        - REJECT 不进——信号本身就是噪声，refine 也救不回来
        - HIGH 已可提交无需 refine

        改前：只挑 MEDIUM，但冷启动时常无 MEDIUM，refine 命令直接返回 0。
        """
        assert self._conn is not None
        cursor = await self._conn.execute(
            """SELECT a.id AS alpha_id, a.expression, b.fitness, b.sharpe, b.turnover,
                      b.returns, b.grade, b.checks, b.created_at
               FROM alphas a
               JOIN backtest_results b ON a.id = b.alpha_id
               WHERE b.fitness IS NOT NULL
                 AND (b.grade = 'medium' OR (b.grade = 'low' AND b.fitness >= ?))
               ORDER BY
                  CASE b.grade WHEN 'medium' THEN 0 ELSE 1 END,
                  b.fitness DESC, b.created_at DESC
               LIMIT ?""",
            (low_fitness_floor, limit),
        )
        rows = await cursor.fetchall()
        out: list[dict[str, Any]] = []
        for r in rows:
            checks: list[dict] = []
            if r["checks"]:
                try:
                    checks = json.loads(r["checks"])
                except (json.JSONDecodeError, TypeError):
                    pass
            failed = [
                str(c.get("name", ""))
                for c in checks
                if isinstance(c, dict) and str(c.get("result", "")).upper() == "FAIL"
            ]
            out.append({
                "alpha_id": r["alpha_id"],
                "expression": r["expression"],
                "fitness": r["fitness"],
                "sharpe": r["sharpe"],
                "turnover": r["turnover"],
                "returns": r["returns"],
                "grade": r["grade"],
                "failed_checks": failed,
            })
        return out

    async def list_high_quality_alphas(self, min_fitness: float = 1.0) -> list[dict[str, Any]]:
        assert self._conn is not None
        cursor = await self._conn.execute(
            """SELECT a.*, b.sharpe, b.turnover, b.fitness, b.returns, b.drawdown, b.grade, b.wq_alpha_id
               FROM alphas a
               JOIN backtest_results b ON a.id = b.alpha_id
               WHERE b.fitness >= ?
               ORDER BY b.fitness DESC""",
            (min_fitness,),
        )
        rows = await cursor.fetchall()
        return [dict(r) for r in rows]

    async def list_top_fitness_alphas(
        self, limit: int = 5, min_fitness: float = 0.0,
        diversify_by_skeleton: bool = True,
    ) -> list[dict[str, Any]]:
        """按 fitness 降序取 top-N，只要 fitness > min_fitness。用于 LLM prompt 的"历史模板"段。

        和 list_high_quality_alphas 的区别：那个是用 MIN_FITNESS 阈值（通常 1.0）筛"可提交"的，
        冷启动时永远为空。这个是 "把目前最好的 N 个端给 LLM 看"，哪怕 fitness 只有 0.4 也总比没有强。

        diversify_by_skeleton（默认 True）：拉 top 4*limit，按"结构骨架"去重再取 top-N。
        防止 exemplar mono-culture——比如 ts_decay_linear(group_neutralize(rank(F),subindustry),N)
        这种结构占满 top-5 后，LLM 强行往别的字段套同样结构，反而把生成质量拖垮。
        """
        assert self._conn is not None
        # 多拉一些候选给去重留余量
        fetch_limit = limit * 4 if diversify_by_skeleton else limit
        cursor = await self._conn.execute(
            """SELECT a.expression, b.fitness, b.sharpe, b.turnover, b.returns, b.grade
               FROM alphas a
               JOIN backtest_results b ON a.id = b.alpha_id
               WHERE b.fitness IS NOT NULL AND b.fitness > ?
               ORDER BY b.fitness DESC
               LIMIT ?""",
            (min_fitness, fetch_limit),
        )
        rows = await cursor.fetchall()
        candidates = [dict(r) for r in rows]

        if not diversify_by_skeleton:
            return candidates[:limit]

        # 两阶段去重：先按 outer signature（前 2 层算子）防 wrapper 家族霸屏，
        # 再按 full skeleton 兜底（同 outer 但内层不同也算不同）。
        # 每个 outer 家族只许 1 个代表（fitness 最高）。
        seen_outer: set[str] = set()
        seen_skeletons: set[str] = set()
        diversified: list[dict[str, Any]] = []
        for row in candidates:
            expr = row.get("expression", "")
            outer = expression_outer_signature(expr, levels=2)
            if outer and outer in seen_outer:
                continue
            skel = expression_skeleton(expr)
            if skel in seen_skeletons:
                continue
            seen_outer.add(outer)
            seen_skeletons.add(skel)
            diversified.append(row)
            if len(diversified) >= limit:
                break

        # 如果去重后不够 limit 个（库里架构种类太少），fallback 放宽到只看 skeleton
        if len(diversified) < limit:
            for row in candidates:
                if row in diversified:
                    continue
                skel = expression_skeleton(row.get("expression", ""))
                if skel in seen_skeletons:
                    continue
                seen_skeletons.add(skel)
                diversified.append(row)
                if len(diversified) >= limit:
                    break

        return diversified[:limit]

    async def get_stats(self) -> dict[str, int]:
        assert self._conn is not None
        stats = {}
        for status in AlphaStatus:
            cursor = await self._conn.execute(
                "SELECT COUNT(*) as cnt FROM alphas WHERE status = ?", (status.value,)
            )
            row = await cursor.fetchone()
            stats[status.value] = row["cnt"]
        cursor = await self._conn.execute("SELECT COUNT(*) as cnt FROM backtest_results WHERE fitness >= 1.0")
        row = await cursor.fetchone()
        stats["high_quality_count"] = row["cnt"]
        return stats

    async def upsert_wiki_page(
        self,
        path: str,
        title: str,
        type_: str,
        tags: list[str],
        sources: list[str],
        content_hash: str,
    ) -> None:
        assert self._conn is not None
        await self._conn.execute(
            """INSERT INTO wiki_pages (path, title, type, tags, sources, content_hash, updated_at)
               VALUES (?, ?, ?, ?, ?, ?, ?)
               ON CONFLICT(path) DO UPDATE SET
                   title=excluded.title,
                   type=excluded.type,
                   tags=excluded.tags,
                   sources=excluded.sources,
                   content_hash=excluded.content_hash,
                   updated_at=excluded.updated_at""",
            (
                path,
                title,
                type_,
                json.dumps(tags, ensure_ascii=False),
                json.dumps(sources, ensure_ascii=False),
                content_hash,
                datetime.now().isoformat(),
            ),
        )
        await self._conn.commit()

    async def bulk_upsert_wiki_pages(self, rows: list[dict]) -> None:
        """Single-transaction batch upsert. Each row needs path/title/type_/tags/sources/content_hash."""
        assert self._conn is not None
        if not rows:
            return
        now = datetime.now().isoformat()
        payload = [
            (
                r["path"],
                r["title"],
                r["type_"],
                json.dumps(r["tags"], ensure_ascii=False),
                json.dumps(r["sources"], ensure_ascii=False),
                r["content_hash"],
                now,
            )
            for r in rows
        ]
        await self._conn.executemany(
            """INSERT INTO wiki_pages (path, title, type, tags, sources, content_hash, updated_at)
               VALUES (?, ?, ?, ?, ?, ?, ?)
               ON CONFLICT(path) DO UPDATE SET
                   title=excluded.title,
                   type=excluded.type,
                   tags=excluded.tags,
                   sources=excluded.sources,
                   content_hash=excluded.content_hash,
                   updated_at=excluded.updated_at""",
            payload,
        )
        await self._conn.commit()

    async def delete_wiki_pages(self, keep_paths: set[str]) -> int:
        assert self._conn is not None
        cursor = await self._conn.execute("SELECT path FROM wiki_pages")
        rows = await cursor.fetchall()
        to_drop = [(r["path"],) for r in rows if r["path"] not in keep_paths]
        if not to_drop:
            return 0
        await self._conn.executemany("DELETE FROM wiki_pages WHERE path = ?", to_drop)
        await self._conn.executemany(
            "DELETE FROM wiki_embeddings_blob WHERE page_path = ?", to_drop
        )
        await self._conn.commit()
        return len(to_drop)

    async def get_wiki_hashes(self) -> dict[str, str]:
        assert self._conn is not None
        cursor = await self._conn.execute("SELECT path, content_hash FROM wiki_pages")
        rows = await cursor.fetchall()
        return {r["path"]: r["content_hash"] for r in rows}

    async def upsert_wiki_embedding(self, path: str, embedding: list[float]) -> None:
        assert self._conn is not None
        blob = struct.pack(f"{len(embedding)}f", *embedding)
        await self._conn.execute(
            """INSERT INTO wiki_embeddings_blob (page_path, dim, embedding, updated_at)
               VALUES (?, ?, ?, ?)
               ON CONFLICT(page_path) DO UPDATE SET
                   dim=excluded.dim,
                   embedding=excluded.embedding,
                   updated_at=excluded.updated_at""",
            (path, len(embedding), blob, datetime.now().isoformat()),
        )
        await self._conn.commit()

    async def load_wiki_embeddings(self) -> dict[str, list[float]]:
        assert self._conn is not None
        cursor = await self._conn.execute(
            "SELECT page_path, dim, embedding FROM wiki_embeddings_blob"
        )
        rows = await cursor.fetchall()
        out: dict[str, list[float]] = {}
        for r in rows:
            dim = r["dim"]
            out[r["page_path"]] = list(struct.unpack(f"{dim}f", r["embedding"]))
        return out

    async def reset_stuck_backtesting(self) -> int:
        """启动时回收上次被杀掉留下的 backtesting 状态。"""
        assert self._conn is not None
        cursor = await self._conn.execute(
            "UPDATE alphas SET status = 'generated' WHERE status = 'backtesting'"
        )
        n = cursor.rowcount
        await self._conn.commit()
        return n

    async def bump_field_blacklist(self, field_ids: list[str], reason: str = "sim_error") -> None:
        assert self._conn is not None
        if not field_ids:
            return
        now = datetime.now().isoformat()
        for fid in field_ids:
            await self._conn.execute(
                """INSERT INTO field_blacklist (field_id, fail_count, last_reason, last_seen)
                   VALUES (?, 1, ?, ?)
                   ON CONFLICT(field_id) DO UPDATE SET
                       fail_count = fail_count + 1,
                       last_reason = excluded.last_reason,
                       last_seen = excluded.last_seen""",
                (fid, reason, now),
            )
        await self._conn.commit()

    async def get_blacklisted_fields(self, min_fail_count: int = 3) -> set[str]:
        assert self._conn is not None
        cursor = await self._conn.execute(
            "SELECT field_id FROM field_blacklist WHERE fail_count >= ?",
            (min_fail_count,),
        )
        rows = await cursor.fetchall()
        return {r["field_id"] for r in rows}

    async def list_field_blacklist(self) -> list[dict[str, Any]]:
        assert self._conn is not None
        cursor = await self._conn.execute(
            "SELECT field_id, fail_count, last_reason, last_seen FROM field_blacklist ORDER BY fail_count DESC"
        )
        rows = await cursor.fetchall()
        return [dict(r) for r in rows]

    async def clear_field_blacklist(self) -> int:
        assert self._conn is not None
        cursor = await self._conn.execute("DELETE FROM field_blacklist")
        await self._conn.commit()
        return cursor.rowcount

    async def wiki_counts(self) -> dict[str, int]:
        assert self._conn is not None
        c = await self._conn.execute("SELECT COUNT(*) AS n FROM wiki_pages")
        pages = (await c.fetchone())["n"]
        c = await self._conn.execute("SELECT COUNT(*) AS n FROM wiki_embeddings_blob")
        embeds = (await c.fetchone())["n"]
        return {"wiki_pages": pages, "wiki_embeddings": embeds}
