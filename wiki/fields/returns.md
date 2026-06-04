---
title: returns
type: field
tags: [field, pv1, return, matrix, price-volume]
sources: [worldquantbrain-api]
created: 2026-06-03
field_id: returns
dataset_id: pv1
field_type: MATRIX
---

# `returns`

**Dataset**: [[pv1]]  **Type**: MATRIX

## 语义

日收益率。相比裸价格，`returns` 更适合直接做短期反转、波动率、异常交易反应和事件后漂移。

## 常见构造

- 短期反转：`reverse(ts_sum(returns, 5))`
- 波动率惩罚：`reverse(ts_std_dev(returns, 252))`
- 事件后漂移：把新闻/分析师信号与过去短期收益组合，避免追高
- 市场状态过滤：高波动或极端收益后可加 `winsorize`

## 使用注意

- `returns` 很容易带来高 turnover，通常需要 [[ts_decay_linear]]、[[hump]] 或 [[trade_when]]。
- 与 [[volume]] 组合时，先 rank 两侧再相加或相乘。
- 对短窗口非常敏感，参数搜索容易过拟合。

## 相关

[[recipes/price-volume-reversal]]、[[patterns/high-turnover]]、[[low-volatility-anomaly]]
