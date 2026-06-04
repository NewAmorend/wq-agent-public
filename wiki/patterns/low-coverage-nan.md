---
title: 低覆盖与 NaN 传播
type: pattern
tags: [pattern, coverage, nan, sparse-data]
created: 2026-06-03
---

# 低覆盖与 NaN 传播

## 症状

alpha 在局部股票上有信号，但全市场 coverage 低；回测结果不稳定，或者不同 universe 迁移时 Sharpe 明显塌陷。

## 常见原因

- 分析师、新闻、期权、部分基本面字段天然稀疏。
- 直接对稀疏字段做 `ts_delta`、`divide`，NaN 被进一步放大。
- 字段只覆盖特定行业或大市值股票。

## 修复处方

- 对稀疏字段优先使用 [[ts_backfill]]，再做 rank 或 zscore。
- 用 `is_nan` 或 `trade_when` 区分有事件日和无事件日。
- 与覆盖更高的 [[pv1]] 字段组合时，先单独标准化。
- 在 bench 或回测日志中记录 coverage，不只看 Sharpe。

## 相关

[[anl4_afv4_eps_mean]]、[[analyst-revisions]]、[[recipes/analyst-revision-momentum]]
