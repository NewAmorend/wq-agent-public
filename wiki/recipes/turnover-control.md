---
title: 降换手 recipe
type: recipe
tags: [recipe, turnover, risk-control, smoothing]
created: 2026-06-03
---

# 降换手 recipe

## 适用场景

alpha 逻辑有效，但 turnover 超过提交限制；或者短周期信号在回测中表现好，实盘可交易性差。

## 主要工具

- [[ts_decay_linear]]：最常用的线性平滑
- [[hump]]：限制单期信号变化幅度
- [[trade_when]]：只在满足事件或阈值时更新仓位
- [[ts_mean]]：等权平滑，适合基本面或慢信号

## 处方顺序

1. 先检查信号是否本质高频。如果经济假设只支持短期，不要硬压 turnover。
2. 对原始 signal 加 `ts_decay_linear(signal, 20/60)`。
3. 如果 turnover 仍高，加 `hump(signal, 0.01)`。
4. 如果是事件信号，用 `trade_when(event_condition, signal, -1)`。
5. 重新检查 Sharpe、Fitness、Sub-universe Sharpe，不只看 turnover。

## 表达式骨架

```text
ts_decay_linear(raw_signal, 20)

hump(ts_decay_linear(raw_signal, 20), 0.01)

trade_when(event_condition, rank(raw_signal), -1)
```

## 常见副作用

- 平滑过度会降低 IC 和反应速度。
- `trade_when` 条件太稀疏会触发 [[patterns/low-coverage-nan]]。
- 高度平滑后的信号可能更接近已有慢速 alpha，注意 [[patterns/self-correlation-crowding]]。

## 相关

[[patterns/high-turnover]]、[[factor-construction-best-practices]]、[[recipes/price-volume-reversal]]
