---
title: Returns to Buying Winners and Selling Losers
type: concept
tags: [paper, momentum, cross-section, anomaly]
sources: [https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1993.tb04702.x]
created: 2026-05-22
authors: [Narasimhan Jegadeesh, Sheridan Titman]
year: 1993
paper_source: manual
---

# Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency

**作者**：Jegadeesh & Titman　**年份**：1993　**期刊**：Journal of Finance

## 核心结论

过去 3-12 个月的赢家组合在未来 3-12 个月内继续跑赢输家组合，年化超额收益约 12%。这是动量异象（momentum anomaly）最经典的实证证据，无法用 CAPM 或 size/book-to-market 解释。

## Key Takeaway

- **形成期**：J ∈ [3, 12] 月，按累计收益排序
- **跳过期**：1 个月（避免短期反转污染）
- **持有期**：K ∈ [3, 12] 月
- 长期（>24 个月）信号反转

## WQ Brain 实现示例

```
# 经典 12-1 momentum：过去 12 月除最近 1 月的累计收益
rank(ts_delta(close, 252) - ts_delta(close, 21))

# 风险调整版：用 turnover 衡量"被关注度"
rank(divide(ts_delta(close, 252), ts_std_dev(returns, 252)))
```

## 相关

- 与 [[momentum]] 因子家族同源
- 短期反向参见 [[1990-lo-mackinlay-contrarian-profits]]
- 行为解释参见 [[2020-daniel-hirshleifer-sun-behavioral-factors]]
