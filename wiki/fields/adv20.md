---
title: adv20
type: field
tags: [field, pv1, volume, liquidity, matrix]
sources: [worldquantbrain-api]
created: 2026-06-03
field_id: adv20
dataset_id: pv1
field_type: MATRIX
---

# `adv20`

**Dataset**: [[pv1]]  **Type**: MATRIX

## 语义

过去 20 日平均成交量，常作为成交活跃度和流动性基准。

## 常见构造

- 相对成交量：`divide(volume, adv20)`
- 流动性变化：`ts_delta(rank(adv20), 60)`
- 流动性风险：与 [[liquidity-microstructure]] 相关的低流动性溢价或交易成本代理

## 使用注意

- `adv20` 本身通常更像控制变量，不一定直接给方向。
- 相对成交量比绝对成交量更稳。
- 与市值、价格水平相关，建议 `rank` 后再与其他信号混合。

## 相关

[[volume]]、[[liquidity-microstructure]]、[[patterns/self-correlation-crowding]]
