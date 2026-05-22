---
title: When Are Contrarian Profits Due to Stock Market Overreaction?
type: concept
tags: [paper, short-term-reversal, mean-reversion, microstructure]
sources: [https://academic.oup.com/rfs/article-abstract/3/2/175/1572770]
created: 2026-05-22
authors: [Andrew W. Lo, A. Craig MacKinlay]
year: 1990
paper_source: manual
---

# When Are Contrarian Profits Due to Stock Market Overreaction?

**作者**：Lo & MacKinlay　**年份**：1990　**期刊**：Review of Financial Studies

## 核心结论

**短期反向策略**（买入上周输家、卖出上周赢家）盈利不全是"过度反应"——大部分来自**横截面自相关**与**领先-滞后效应**（大盘股领先小盘股）。

## Key Takeaway

- 1 周到 1 个月内的反转主要源于流动性提供 / 做市补偿
- 与中期 [[1993-jegadeesh-titman-returns-to-buying-winners|momentum]] 不矛盾，是不同的时间尺度
- WQ Brain 上常表现为 `ts_zscore(returns, 5-20)` 的反向信号

## WQ Brain 实现示例

```
# 短期反转
reverse(ts_zscore(returns, 5))

# 行业中性后效果更稳
group_neutralize(reverse(ts_zscore(returns, 5)), industry)
```

## 相关

- 动量 [[1993-jegadeesh-titman-returns-to-buying-winners]]
- 流动性补偿 [[2002-amihud-illiquidity]]
