---
title: enterprise_value
type: field
tags: [field, fundamental6, valuation, size, matrix]
sources: [worldquantbrain-api]
created: 2026-06-03
field_id: enterprise_value
dataset_id: fundamental6
field_type: MATRIX
---

# `enterprise_value`

**Dataset**: [[fundamental6]]  **Type**: MATRIX

## 语义

企业价值，通常用于估值归一化和规模控制。相比市值，它把债务和现金结构也纳入考虑。

## 常见构造

- 估值代理：盈利、现金流或销售额除以 enterprise value
- 规模控制：用于区分大公司暴露和真实质量信号
- 杠杆分析：与 [[debt]]、[[assets]] 一起判断资本结构压力

## 使用注意

- 与价格和市值高度相关，混合价量信号时注意 self-correlation。
- 不同行业资本结构差异大，通常需要 [[group_neutralize]]。
- 估值比率遇到负值或极端值时优先 rank / winsorize。

## 相关

[[value-factors]]、[[quality-factors]]、[[recipes/quality-profitability]]
