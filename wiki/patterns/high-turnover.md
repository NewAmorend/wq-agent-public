---
title: 高换手失败模式
type: pattern
tags: [pattern, turnover, risk-control, decay]
created: 2026-06-03
---

# 高换手失败模式

## 症状

回测 Sharpe 或 Fitness 看起来不错，但 turnover 超过 70%，或者加入中性化后交易过于频繁，导致无法提交。

## 常见原因

- 使用 [[returns]]、[[volume]]、[[vwap]] 这类短周期字段，但没有平滑。
- 窗口过短，例如 `ts_delta(x, 3)`、`ts_rank(x, 5)`。
- 信号每天都重新排序，没有事件过滤或交易门控。
- 多个高频信号叠加后 self-correlation 很高。

## 修复处方

- 先试 [[ts_decay_linear]] 或 `ts_mean`，把 5-20 日信号平滑到 20-60 日。
- 用 [[hump]] 限制单日信号变化。
- 用 [[trade_when]] 只在事件、异常成交或显著修正时交易。
- 如果信号本质是基本面或分析师修正，窗口优先 60-252。

## 相关

[[recipes/turnover-control]]、[[factor-construction-best-practices]]、[[patterns/self-correlation-crowding]]
