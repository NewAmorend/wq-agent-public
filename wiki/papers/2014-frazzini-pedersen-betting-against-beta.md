---
title: Betting Against Beta
type: concept
tags: [paper, beta, leverage, low-volatility]
sources: [https://www.sciencedirect.com/science/article/abs/pii/S0304405X13002675]
created: 2026-05-22
authors: [Andrea Frazzini, Lasse H. Pedersen]
year: 2014
paper_source: manual
---

# Betting Against Beta

**作者**：Frazzini & Pedersen　**年份**：2014　**期刊**：Journal of Financial Economics

## 核心结论

由于杠杆约束，受限投资者会高估高 beta 资产、低估低 beta 资产。**BAB 因子**：做多 leverage-adjusted 低 beta 组合，做空 leverage-adjusted 高 beta 组合，全球稳健正收益。

## Key Takeaway

- 安全资产 / 低 beta 在风险调整后跑赢
- 关键技巧：**两边都按 beta 缩放到 1**（杠杆做多低 beta，去杠杆做空高 beta）
- 解释了 [[2011-baker-bradley-wurgler-benchmarks-low-vol]] 报告的低波动异象

## WQ Brain 实现示例

```
# Beta 估计
b = ts_regression(returns, market_returns, 252, 0, 1)

# 简化 BAB：rank 反转 → 低 beta 排名靠前
reverse(rank(b))

# 严格版需要 leverage scaling，超出 FASTEXPR 范围
```

## 相关

- 低波动 [[2011-baker-bradley-wurgler-benchmarks-low-vol]]
- 质量 [[2019-asness-frazzini-pedersen-quality-minus-junk]]
