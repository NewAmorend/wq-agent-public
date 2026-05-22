---
title: Value and Momentum Everywhere
type: concept
tags: [paper, value, momentum, global, asset-classes]
sources: [https://onlinelibrary.wiley.com/doi/10.1111/jofi.12021]
created: 2026-05-22
authors: [Clifford S. Asness, Tobias J. Moskowitz, Lasse H. Pedersen]
year: 2013
paper_source: manual
---

# Value and Momentum Everywhere

**作者**：Asness, Moskowitz, Pedersen　**年份**：2013　**期刊**：Journal of Finance

## 核心结论

价值与动量这两个因子在**所有大类资产**（股票、债券、商品、外汇、国别指数）和**所有市场**（美、英、欧、日）都稳健显著，且彼此**负相关**——配对组合能大幅降低波动并提升夏普。

## Key Takeaway

- 价值与动量是真正的"全球共同因子"，可能反映流动性 / 风险溢价
- **配对组合**：50% 价值 + 50% 动量，远胜单独任一
- 在 region=GLB 或多 region 组合时尤其值得复现

## WQ Brain 实现示例

```
# Value-momentum 复合因子（横截面，单一 region）
add(rank(value_signal), rank(momentum_signal))

# 国别 / 行业层面适合 group_neutralize
group_neutralize(
    add(rank(value_signal), rank(momentum_signal)),
    industry
)
```

## 相关

- 动量起源 [[1993-jegadeesh-titman-returns-to-buying-winners]]
- 价值起源 [[1993-fama-french-common-risk-factors]]
- 配对原理参考 [[2014-frazzini-pedersen-betting-against-beta]]
