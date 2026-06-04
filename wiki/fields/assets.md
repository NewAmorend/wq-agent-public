---
title: assets
type: field
tags: [field, fundamental6, assets, balance-sheet, matrix]
sources: [worldquantbrain-api]
created: 2026-06-03
field_id: assets
dataset_id: fundamental6
field_type: MATRIX
---

# `assets`

**Dataset**: [[fundamental6]]  **Type**: MATRIX

## 语义

总资产。常用于规模标准化、资产增长、盈利能力分母和资产质量分析。

## 常见构造

- 盈利能力：`divide(cashflow_op, assets)` 或 `divide(ebit, assets)`
- 资产增长：`ts_delta(assets, 252)`，方向通常要小心，资产扩张过快可能是负信号
- 规模中性：基本面变量除以 assets 后再 rank

## 使用注意

- 总资产有强行业差异，通常要 [[group_neutralize]] 到 subindustry。
- 基本面字段更新慢，窗口宜长，避免短窗口参数搜索。
- 与 [[debt]]、[[cashflow_op]] 组合时，先构造经济比率再标准化。

## 相关

[[quality-factors]]、[[value-factors]]、[[recipes/quality-profitability]]
