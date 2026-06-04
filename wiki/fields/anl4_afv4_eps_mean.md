---
title: anl4_afv4_eps_mean
type: field
tags: [field, analyst4, eps, revision, estimate, matrix]
sources: [worldquantbrain-api]
created: 2026-06-03
field_id: anl4_afv4_eps_mean
dataset_id: analyst4
field_type: MATRIX
---

# `anl4_afv4_eps_mean`

**Dataset**: [[analyst4]]  **Type**: MATRIX

## 语义

分析师年度 EPS 一致预期均值。它适合做盈利预期修正、预期动量和事件后漂移类信号。

## 常见构造

- 预期修正：`ts_delta(anl4_afv4_eps_mean, 20)`
- 修正强度：`ts_rank(ts_delta(anl4_afv4_eps_mean, 60), 252)`
- 与实际 EPS 或价格反应结合，寻找尚未充分反映的预期变化

## 使用注意

- 分析师字段稀疏，优先 [[ts_backfill]]，并监控 coverage。
- 预期修正常伴随事件和价格跳动，最好配合 [[trade_when]] 降低无事件日交易。
- 注意与新闻情绪、价格动量的重复暴露。

## 相关

[[analyst-revisions]]、[[recipes/analyst-revision-momentum]]、[[patterns/low-coverage-nan]]
