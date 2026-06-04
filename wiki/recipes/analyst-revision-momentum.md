---
title: 分析师修正动量 recipe
type: recipe
tags: [recipe, analyst, revision, earnings, sparse-data]
created: 2026-06-03
---

# 分析师修正动量 recipe

## 适用假设

分析师上调盈利预期通常不是一次性完成，市场对基本面改善的反应可能滞后；预期修正如果没有被价格完全吸收，后续收益仍可能延续。

## 推荐字段

- [[anl4_afv4_eps_mean]]：年度 EPS 一致预期均值
- [[eps]]：已披露盈利结果，可与预期对照
- [[returns]]：检查价格是否已经提前反应
- [[volume]]：确认修正是否伴随关注度提升

## 基础表达式骨架

```text
rank(ts_delta(ts_backfill(anl4_afv4_eps_mean, 60), 20))

trade_when(
  is_nan(anl4_afv4_eps_mean) == 0,
  rank(ts_delta(ts_backfill(anl4_afv4_eps_mean, 60), 60)),
  -1
)
```

## 稳定化步骤

1. 先 [[ts_backfill]]，再做 `ts_delta`。
2. 对修正强度做 `rank` 或 `zscore`，避免少数极端上调支配组合。
3. 如果 turnover 高，用 [[trade_when]] 只在修正事件附近交易。
4. 如果追涨明显，把短期 [[returns]] 作为反向过滤腿。

## 常见失败

- [[patterns/low-coverage-nan]]：分析师覆盖天然不均。
- [[patterns/high-turnover]]：事件日信号太密集。
- [[patterns/self-correlation-crowding]]：和新闻情绪、价格动量可能重复。

## 相关

[[analyst-revisions]]、[[recipes/turnover-control]]、[[quality-factors]]
