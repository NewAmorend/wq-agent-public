---
title: close
type: field
tags: [field, pv1, price, matrix, price-volume]
sources: [worldquantbrain-api]
created: 2026-06-03
field_id: close
dataset_id: pv1
field_type: MATRIX
---

# `close`

**Dataset**: [[pv1]]  **Type**: MATRIX

## 语义

日收盘价，是价量类 alpha 的核心价格锚点。直接使用绝对价格通常会引入价格水平和拆股尺度问题，更常见的做法是转成收益、相对位置、趋势或反转信号。

## 常见构造

- 短期反转：`reverse(ts_delta(close, 5))` 或 `reverse(ts_rank(close, 20))`
- 中期动量：`ts_rank(ts_delta(close, 60), 252)`
- 价格位置：`rank(divide(subtract(close, ts_min(close, 252)), subtract(ts_max(close, 252), ts_min(close, 252))))`
- 配合 [[volume]] / [[vwap]] 做价量背离

## 使用注意

- 优先用 [[returns]] 或价格变化，而不是裸 `close`。
- 价格字段通常要 `rank`、`ts_rank`、`ts_delta` 后再参与横截面组合。
- 与基本面字段混合时先分别标准化，避免价格尺度吞掉信号。

## 相关

[[momentum-reversal-pv]]、[[recipes/price-volume-reversal]]、[[patterns/direction-sign-error]]
