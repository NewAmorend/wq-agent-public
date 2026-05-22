---
title: The Other Side of Value — The Gross Profitability Premium
type: concept
tags: [paper, profitability, value, quality]
sources: [https://www.sciencedirect.com/science/article/abs/pii/S0304405X13000044]
created: 2026-05-22
authors: [Robert Novy-Marx]
year: 2013
paper_source: manual
---

# The Other Side of Value: The Gross Profitability Premium

**作者**：Novy-Marx　**年份**：2013　**期刊**：Journal of Financial Economics

## 核心结论

**毛利率（Gross Profit / Assets）**是预测股票横截面收益最有信息量的盈利能力指标，超过 ROE 和 ROA。高毛利率公司即便估值不便宜，长期也跑赢低毛利率公司。

## Key Takeaway

- 毛利率比净利润更稳定（少受暂时性会计项目影响）
- 与价值因子负相关 → 二者组合显著降低组合波动
- 是 [[2019-asness-frazzini-pedersen-quality-minus-junk|QMJ]] 中 profitability 子维度的主要 driver

## WQ Brain 实现示例

```
# Gross profitability
rank(divide(fnd_gross_profit, fnd_total_assets))

# 价值 + GP 组合：经典 Asness 配方
add(
    rank(divide(fnd_book_equity, market_cap)),
    rank(divide(fnd_gross_profit, fnd_total_assets))
)
```

## 相关

- 质量复合 [[2019-asness-frazzini-pedersen-quality-minus-junk]]
- q-model 中的 ROE [[2015-hou-xue-zhang-q-factor]]
