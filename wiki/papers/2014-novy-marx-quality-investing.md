---
title: Quality Investing
type: concept
tags: [paper, quality, profitability, value]
sources: [https://rnm.simon.rochester.edu/research/QDoVI.pdf]
created: 2026-05-22
authors: [Robert Novy-Marx]
year: 2014
paper_source: manual
---

# Quality Investing

**作者**：Novy-Marx　**年份**：2014　**Working paper / Book chapter**

## 核心结论

"质量"是个被滥用的词。Novy-Marx 论证：在数据上真正有定价能力的"质量"主要是**毛利率（gross profits-to-assets）** + **盈利稳定性**，其他诸如 ROE、margin、payout 等更弱。把"质量"与"价值"组合是最佳实践。

## Key Takeaway

- 别用过多指标拼"质量"，会因相关性低而稀释信号
- GP/A 是最简单也最有效的质量代理
- 与价值组合的负相关性使 Sharpe 显著提升

## WQ Brain 实现示例

```
# 高质量 + 便宜 = "good company, fair price"
add(
    rank(divide(fnd_gross_profit, fnd_total_assets)),
    rank(divide(fnd_book_equity, market_cap))
)
```

## 相关

- 同作者 GP/A 原文 [[2013-novy-marx-other-side-of-value]]
- QMJ 复合实践 [[2019-asness-frazzini-pedersen-quality-minus-junk]]
