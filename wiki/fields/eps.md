---
title: eps
type: field
tags: [field, fundamental6, earnings, profitability, matrix]
sources: [worldquantbrain-api]
created: 2026-06-03
field_id: eps
dataset_id: fundamental6
field_type: MATRIX
---

# `eps`

**Dataset**: [[fundamental6]]  **Type**: MATRIX

## 语义

每股收益。适合构造盈利能力、盈利改善和估值相关信号，但容易受一次性项目和会计处理影响。

## 常见构造

- 盈利改善：`ts_delta(eps, 252)`
- 盈利动量：`ts_rank(ts_delta(eps, 252), 504)`
- 估值近似：与价格或 book value 结合，但要注意尺度

## 使用注意

- 单独使用 EPS 容易混入价格和股份数变化，最好与资产、账面价值或预测修正配合。
- EPS 为负时比率会不稳定，必要时用 rank 或 winsorize。
- 和分析师 EPS 预测字段结合时，需要避免重复暴露。

## 相关

[[analyst-revisions]]、[[recipes/analyst-revision-momentum]]、[[quality-factors]]
