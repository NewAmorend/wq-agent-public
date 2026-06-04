---
title: Self-correlation 与拥挤信号
type: pattern
tags: [pattern, self-correlation, crowding, diversification]
created: 2026-06-03
---

# Self-correlation 与拥挤信号

## 症状

新 alpha 本身指标可用，但和已有 alpha 或经典动量/反转过于相似，提交时 self-correlation 不通过。

## 常见原因

- 只是换了窗口的 [[momentum]] / [[momentum-reversal-pv]]。
- 多个字段本质同源，比如 [[close]]、[[vwap]]、[[returns]]。
- 只加了 rank/decay，没有改变经济假设。

## 修复处方

- 从不同信息源组合：PV + analyst、fundamental + volatility、news + volume confirmation。
- 先行业中性化，再和已有 alpha 对比。
- 用 residual 思路，例如 [[ts_regression]] 剥离市场或价格趋势暴露。
- recipe 层面优先换假设，不只换参数。

## 相关

[[recipes/price-volume-reversal]]、[[recipes/quality-profitability]]、[[model-factor-libraries]]
