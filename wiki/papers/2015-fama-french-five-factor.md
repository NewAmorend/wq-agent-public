---
title: A Five-Factor Asset Pricing Model
type: concept
tags: [paper, factor-model, profitability, investment, ff5]
sources: [https://www.sciencedirect.com/science/article/abs/pii/S0304405X14002323]
created: 2026-05-22
authors: [Eugene F. Fama, Kenneth R. French]
year: 2015
paper_source: manual
---

# A Five-Factor Asset Pricing Model

**作者**：Fama & French　**年份**：2015　**期刊**：Journal of Financial Economics

## 核心结论

在原三因子（市场、SMB、HML）上加两个：

- **RMW**（Robust Minus Weak）— 盈利能力因子，以营业利润率衡量
- **CMA**（Conservative Minus Aggressive）— 投资因子，以总资产增长率反向衡量

五因子可解释大部分横截面异象，HML 在加入 RMW + CMA 后变得"多余"。

## Key Takeaway

- 高盈利能力、低资本扩张的公司长期溢价显著
- Asset growth ↑ → 未来收益 ↓（投资过度假说）
- [[momentum]] 仍不在 FF5 体系内

## WQ Brain 实现示例

```
# 盈利能力（RMW 代理）
rank(divide(fnd_operating_profit, fnd_book_equity))

# 投资因子（CMA 代理：资产增长越低越好）
reverse(rank(ts_delta(fnd_total_assets, 252) / ts_delay(fnd_total_assets, 252)))
```

## 相关

- 原始三因子 [[1993-fama-french-common-risk-factors]]
- 投资因子的替代实现 [[2015-hou-xue-zhang-q-factor]]
- 盈利能力溢价 [[2013-novy-marx-other-side-of-value]]
