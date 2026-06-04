---
title: vwap
type: field
tags: [field, pv1, price, volume, matrix]
sources: [worldquantbrain-api]
created: 2026-06-03
field_id: vwap
dataset_id: pv1
field_type: MATRIX
---

# `vwap`

**Dataset**: [[pv1]]  **Type**: MATRIX

## 语义

成交量加权平均价。相比 `close`，`vwap` 更贴近全天成交成本，常用于捕捉日内价格压力、流动性冲击和收盘偏离。

## 常见构造

- 收盘偏离：`rank(divide(subtract(close, vwap), vwap))`
- 成交压力：`ts_rank(subtract(vwap, ts_delay(vwap, 5)), 60)`
- 反转确认：价格偏离 vwap 且成交量异常时，短期反转更强

## 使用注意

- 与 `close` 的差值通常比单独使用 `vwap` 更有解释性。
- 价量偏离信号容易短周期高换手，需要 [[hump]] 或 [[trade_when]]。
- 注意和价格动量信号的 self-correlation。

## 相关

[[close]]、[[volume]]、[[recipes/price-volume-reversal]]、[[patterns/high-turnover]]
