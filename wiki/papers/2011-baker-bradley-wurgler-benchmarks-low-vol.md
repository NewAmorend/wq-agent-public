---
title: Benchmarks as Limits to Arbitrage — Understanding the Low-Volatility Anomaly
type: concept
tags: [paper, low-volatility, anomaly, limits-to-arbitrage]
sources: [https://www.tandfonline.com/doi/abs/10.2469/faj.v67.n1.4]
created: 2026-05-22
authors: [Malcolm Baker, Brendan Bradley, Jeffrey Wurgler]
year: 2011
paper_source: manual
---

# Benchmarks as Limits to Arbitrage: Understanding the Low-Volatility Anomaly

**作者**：Baker, Bradley, Wurgler　**年份**：2011　**期刊**：Financial Analysts Journal

## 核心结论

低波动股票长期跑赢高波动股票（与 CAPM 预测相反）。原因是**机构投资者受 benchmark 约束**：基金经理被相对收益考核 → 偏好高 beta 股票去博取超额 → 推高估值 → 低波动股相对被低估。

## Key Takeaway

- 现实中的"limits to arbitrage"造成这个异象长期存在
- [[2014-frazzini-pedersen-betting-against-beta]] 从杠杆约束侧给出互补解释
- 在 risk-aware 配置中是稳定的"防御型"信号

## WQ Brain 实现示例

```
# 简化低波动信号：过去 252 日波动率反向 rank
reverse(rank(ts_std_dev(returns, 252)))

# 行业中性化避免行业暴露
group_neutralize(reverse(rank(ts_std_dev(returns, 252))), industry)
```

## 相关

- BAB 互补 [[2014-frazzini-pedersen-betting-against-beta]]
- Quality safety 子维度 [[2019-asness-frazzini-pedersen-quality-minus-junk]]
