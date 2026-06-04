---
title: debt
type: field
tags: [field, fundamental6, leverage, balance-sheet, matrix]
sources: [worldquantbrain-api]
created: 2026-06-03
field_id: debt
dataset_id: fundamental6
field_type: MATRIX
---

# `debt`

**Dataset**: [[fundamental6]]  **Type**: MATRIX

## 语义

债务总量。常用于杠杆、财务风险、质量因子和困境风险代理。

## 常见构造

- 杠杆风险：`rank(divide(debt, assets))`，多数情况下方向偏负
- 变化信号：`ts_delta(divide(debt, assets), 252)` 捕捉杠杆恶化
- 质量组合：与现金流、盈利能力、低波动共同使用

## 使用注意

- 银行、保险等行业口径特殊，必须行业中性化或过滤。
- 裸 debt 强烈暴露规模，优先除以 [[assets]] 或 [[enterprise_value]]。
- 方向很容易反，需要用 [[patterns/direction-sign-error]] 检查。

## 相关

[[assets]]、[[quality-factors]]、[[patterns/direction-sign-error]]
