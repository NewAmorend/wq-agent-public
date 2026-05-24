from __future__ import annotations

import re
from typing import Any

from loguru import logger

from ..llm.base import BaseLLMProvider
from .llm import LLMAlphaGenerator


_FAIL_TO_HINT = {
    "LOW_FITNESS": (
        "fitness 差一点点（< 1.0）→ 试**加复合维度**：`add(rank(原表达式), rank(相关信号))`，"
        "或外层加 `winsorize(_, std=4)` 去掉极端值的影响。"
    ),
    "LOW_SHARPE": (
        "sharpe 偏低 → 信号噪声比差。试外层套 `ts_decay_linear(_, 20)` 平滑，"
        "或在中间一层加 `winsorize(_, std=4)`、`group_neutralize(_, subindustry)`。"
    ),
    "LOW_SUB_UNIVERSE_SHARPE": (
        "在 sub-universe（小盘 / 行业子集）上 sharpe 不达标 → 通常需要"
        "**行业中性化**：`group_neutralize(_, subindustry)` 或换成 `group_rank(_, subindustry)`。"
    ),
    "HIGH_TURNOVER": (
        "换手太快（> 70%）→ 外层套 `ts_decay_linear(_, 60)` 或 `hump(_, hump=0.05)` 强力降换手。"
    ),
    "LOW_TURNOVER": (
        "换手低于 1%（信号几乎不动）→ 可能 ts 窗口太长。试缩短到 60 以下，或换 `ts_zscore` 等更动态的算子。"
    ),
    "CONCENTRATED_WEIGHT": (
        "权重过于集中（少数股票主导信号）→ 必须 `rank(_)` 横截面排名拍平分布，"
        "再叠加 `winsorize(_)` 去极值。"
    ),
}


_REFINE_PROMPT = """你是一位顶尖量化研究员。下面这个 alpha **差一项 WQ Brain 关键检查就能提交**，
你的任务是基于它生成 {count} 个**微调变体**，目标是把它从 MEDIUM 推到 HIGH（可提交）。

## 基础表达式

```
{expression}
```

## 历史指标

- fitness = {fitness}
- sharpe = {sharpe}
- turnover = {turnover}
- returns = {returns}
- 失败检查：{failed}

## 针对此失败检查的优化方向

{hints}

## 你可以做的微调维度（请在 {count} 个变体里覆盖多种维度）

1. **调窗口** —— 把数字参数在 5 / 20 / 60 / 120 / 252 之间调整（保持算子结构）
2. **加中性化** —— 包入 `group_neutralize(_, subindustry)` / `group_rank(_, subindustry)` / `vector_neut(_, ...)`
3. **加平滑** —— 外层套 `ts_decay_linear(_, d)`、`ts_mean(_, d)`、`hump(_, hump=0.05)`
4. **加预处理** —— 包入 `winsorize(_, std=4)` / `rank(_)` / `zscore(_)` / `ts_backfill(_, lookback=120)`
5. **复合** —— `add(rank(原表达式), rank(相关信号))` 把弱信号叠加成强信号
6. **换字段** —— 用同一 dataset 同语义字段替换其中 1 个（如 close↔vwap、cashflow_op↔cashflow）

## 严格规则

- **必须保留原表达式的核心结构** —— 不能完全重写
- **不允许**：把算子语义级别替换（如 `ts_delta` → `ts_corr`、`rank` → `quantile`）
- **不允许**：与原表达式 verbatim 重复
- 每行一个完整表达式，不要解释，不要 `1.` 序号

## 可用字段

{fields}

## 可用算子

{operators}

{knowledge_section}

请直接输出 {count} 个变体表达式，每行一个："""


class RefineAlphaGenerator:
    """对单个 base alpha 生成 K 个微调变体，复用 LLMAlphaGenerator 的 wiki + parse 逻辑。"""

    def __init__(
        self,
        llm: BaseLLMProvider,
        wiki_retriever=None,
        wiki_top_k: int = 3,
        wiki_summary_chars: int = 200,
    ):
        self.llm = llm
        # 复用 LLMAlphaGenerator 的 wiki/parse helpers，避免重复实现
        self._base_gen = LLMAlphaGenerator(
            llm=llm,
            wiki_retriever=wiki_retriever,
            wiki_top_k=wiki_top_k,
            wiki_summary_chars=wiki_summary_chars,
        )

    async def refine(
        self,
        base: dict[str, Any],
        data_fields: list,
        operators: list,
        count: int = 10,
    ) -> list[str]:
        expression = base.get("expression", "")
        if not expression:
            return []

        failed = base.get("failed_checks") or []
        hints = "\n".join(
            f"- {_FAIL_TO_HINT.get(name.upper(), '')}" for name in failed
            if name.upper() in _FAIL_TO_HINT
        ) or "- 无明显失败项，做小幅微调即可"

        fields_str = "\n".join(
            f"{f.id} ({f.description or 'No description'})"
            for f in data_fields[: min(len(data_fields), 30)]
        )
        operators_str = "\n".join(
            f"{op.name} ({op.description or ''})" for op in operators[: min(len(operators), 40)]
        )

        # 复用 wiki 知识注入（用 base 表达式做 query 检索相关 cookbook）
        knowledge_section = ""
        if self._base_gen.wiki_retriever:
            try:
                hits = await self._base_gen.wiki_retriever.search(
                    f"{expression} {' '.join(failed)} 微调 refine", top_k=3,
                )
                if hits:
                    lines = ["", "## 知识库参考", ""]
                    for h in hits:
                        lines.append(
                            f"- [[{h.page.slug}]] · {h.page.type.value}: "
                            f"{h.page.summary(self._base_gen.wiki_summary_chars)}"
                        )
                    knowledge_section = "\n".join(lines)
            except Exception as exc:
                logger.warning(f"Refine wiki retrieval failed: {exc}")

        def _fmt(v):
            if v is None:
                return "—"
            try:
                return f"{float(v):.3f}"
            except (TypeError, ValueError):
                return str(v)

        prompt = _REFINE_PROMPT.format(
            count=count,
            expression=expression,
            fitness=_fmt(base.get("fitness")),
            sharpe=_fmt(base.get("sharpe")),
            turnover=_fmt(base.get("turnover")),
            returns=_fmt(base.get("returns")),
            failed=", ".join(failed) if failed else "—",
            hints=hints,
            fields=fields_str,
            operators=operators_str,
            knowledge_section=knowledge_section,
        )

        logger.info(f"Refining alpha #{base.get('alpha_id')} ({expression[:50]}...)")
        content = await self.llm.generate(prompt, temperature=0.4)
        raw = self._base_gen._parse_response(content)
        cleaned = self._base_gen._clean_expressions(raw)

        # 去掉跟 base 完全相同的（regex 友好的简单 dedup）
        base_norm = re.sub(r"\s+", "", expression)
        deduped = [e for e in cleaned if re.sub(r"\s+", "", e) != base_norm]
        logger.info(
            f"Refine produced {len(deduped)} variants from {len(raw)} raw "
            f"(dropped {len(cleaned) - len(deduped)} duplicates of base)"
        )
        return deduped[:count]
