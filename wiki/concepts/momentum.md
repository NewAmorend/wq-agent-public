---
title: 动量因子家族
type: concept
tags: [momentum, ts_delta, ts_rank, trend]
created: 2026-05-22
---

# 动量因子家族

**经济直觉**：横截面上过去一段时间表现好的股票，在未来短期（1 周 - 3 个月）继续跑赢，源于投资者反应不足与机构追涨。

## 常用实现模板

- `ts_delta(close_field, d)` — 简单价格变化，`d ∈ [5, 20, 60]`
- `rank(ts_delta(close_field, d))` — 横截面排名化，降低规模偏差
- `ts_rank(ts_delta(close_field, d), 252)` — 把当前动量水位放到长窗口里看
- `divide(ts_delta(x, d), ts_std_dev(x, d))` — 风险调整后的动量（[[factor-construction-best-practices|risk-adjusted momentum]]）

## 与之常配的技巧

- 与 [[momentum-reversal-pv|reversal]] 反向叠加，构成"短期反转 + 中期动量"组合
- 用 [[group_neutralize]] 做行业中性，避开行业 beta
- 用 [[ts_decay_linear]] 平滑信号，降低换手率

## 经典踩坑

- 在 `delay=1` 下用过短窗口（d < 5）几乎等同于噪声
- 直接用未中性化的动量在中国市场行业暴露严重
- `ts_delta` 不做 rank 时，价格量纲会让大盘股主导信号
