---
title: cashflow_op
type: field
tags: [field, fundamental6, cashflow, profitability, matrix]
sources: [worldquantbrain-api]
created: 2026-06-03
field_id: cashflow_op
dataset_id: fundamental6
field_type: MATRIX
---

# `cashflow_op`

**Dataset**: [[fundamental6]]  **Type**: MATRIX

## 语义

经营活动现金流。它通常比会计利润更难被短期会计处理扭曲，是质量和盈利能力因子的核心候选字段。

## 常见构造

- 现金流盈利能力：`rank(divide(cashflow_op, assets))`
- 改善趋势：`ts_delta(divide(cashflow_op, assets), 252)`
- 质量复合：与低债务、稳定收益、低波动组合

## 使用注意

- 基本面更新频率低，不适合过短 lookback。
- 现金流口径行业差异明显，需要 [[group_neutralize]]。
- 和 `eps` / `ebit` 同源性较高，复合时注意 self-correlation。

## 相关

[[assets]]、[[eps]]、[[recipes/quality-profitability]]、[[quality-factors]]
