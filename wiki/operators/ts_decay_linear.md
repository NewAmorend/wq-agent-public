---
title: ts_decay_linear 算子
type: operator
tags: [ts_decay_linear, smoothing, weighting, turnover]
created: 2026-05-22
---

# ts_decay_linear(x, d, dense=false)

**语义**：对 `x` 在过去 `d` 个时点做线性加权移动平均，最新值权重 d、d 天前权重 1。

## 适用场景

- 把高频信号平滑成持仓友好型，降低 turnover
- 替代 `ts_mean` 作为更"看重近期"的均值
- 经常出现在 [[momentum]] 与 [[momentum-reversal-pv|reversal]] 的最外层做平滑

## 参数经验

| d | 适用 |
| --- | --- |
| 5 - 10 | 日内 / 极短周期信号 |
| 20 - 60 | 中频动量 / 反转 |
| 120 - 250 | 配合长窗口质量因子 |

## 踩坑

- 用 `dense=true` 在多数 region 反而拉高 turnover（缺失值被填充）
- `d` 太大时与 `ts_mean` 区别消失
- 嵌在 `rank(...)` 内层时，外层 rank 会吃掉大部分平滑效果——通常应在外层
