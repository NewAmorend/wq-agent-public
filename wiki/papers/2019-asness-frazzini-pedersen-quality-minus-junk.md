---
title: Quality Minus Junk
type: concept
tags: [paper, quality, profitability, growth, safety]
sources: [https://link.springer.com/article/10.1007/s11142-018-9477-8]
created: 2026-05-22
authors: [Clifford S. Asness, Andrea Frazzini, Lasse H. Pedersen]
year: 2019
paper_source: manual
---

# Quality Minus Junk

**作者**：Asness, Frazzini, Pedersen　**年份**：2019　**期刊**：Review of Accounting Studies

## 核心结论

将"质量"定义为四个子维度的合成：

- **Profitability**：盈利能力（毛利率、ROE、ROA）
- **Growth**：盈利增长稳定性
- **Safety**：低 beta、低杠杆、低盈利波动率
- **Payout**：高分红率、低增发

QMJ 因子（做多高质量、做空低质量）夏普在 24 个国家都为正，年化超额 5-9%。

## Key Takeaway

- "质量"不是单一指标，是多维合成
- 与 [[momentum]] 相关性低，与 [[1993-fama-french-common-risk-factors|value]] 负相关 — 适合做组合分散
- 在熊市表现尤其突出（safety 维度起作用）

## WQ Brain 实现示例

```
# Profitability 子维度
prof = add(rank(divide(fnd_gross_profit, fnd_assets)),
           rank(divide(fnd_operating_profit, fnd_book_equity)))

# Safety 子维度（低 beta + 低杠杆 + 低盈利波动）
safety = reverse(add(
    rank(ts_std_dev(returns, 252)),
    rank(divide(fnd_total_debt, fnd_total_assets))
))

# 复合 QMJ
add(prof, safety)
```

## 相关

- 盈利能力溢价 [[2013-novy-marx-other-side-of-value]]
- 低波动异象 [[2011-baker-bradley-wurgler-benchmarks-low-vol]]
