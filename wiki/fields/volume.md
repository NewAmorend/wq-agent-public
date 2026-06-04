---
title: volume
type: field
tags: [field, pv1, volume, liquidity, matrix]
sources: [worldquantbrain-api]
created: 2026-06-03
field_id: volume
dataset_id: pv1
field_type: MATRIX
---

# `volume`

**Dataset**: [[pv1]]  **Type**: MATRIX

## 语义

日成交量。它既能代表流动性，也能作为注意力、拥挤、信息冲击的代理变量。

## 常见构造

- 异常成交：`ts_rank(divide(volume, adv20), 60)`
- 量价背离：`rank(ts_delta(volume, 20))` 与 `reverse(rank(ts_delta(close, 20)))`
- 流动性过滤：低流动性股票的价量信号更容易噪声化
- 事件确认：新闻/分析师信号如果伴随 volume 扩张，可信度更高

## 使用注意

- 裸 `volume` 有强烈市值暴露，常用 `divide(volume, adv20)` 或先做行业中性化。
- `volume` 信号通常换手偏高，要配合 [[ts_decay_linear]] / [[hump]]。
- 避免把 volume 当成收益方向，最好和价格、情绪或事件变量共同解释。

## 相关

[[adv20]]、[[vwap]]、[[liquidity-microstructure]]、[[recipes/price-volume-reversal]]
