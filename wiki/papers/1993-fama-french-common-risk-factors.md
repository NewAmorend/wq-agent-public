---
title: Common Risk Factors in the Returns on Stocks and Bonds
type: concept
tags: [paper, factor-model, size, value, ff3]
sources: [https://www.sciencedirect.com/science/article/abs/pii/0304405X93900235]
created: 2026-05-22
authors: [Eugene F. Fama, Kenneth R. French]
year: 1993
paper_source: manual
---

# Common Risk Factors in the Returns on Stocks and Bonds

**作者**：Fama & French　**年份**：1993　**期刊**：Journal of Financial Economics

## 核心结论

横截面股票收益除了市场因子之外，还由两个共同风险因子定价：

- **SMB**（Small Minus Big）— 市值因子
- **HML**（High Minus Low）— BM 价值因子

三因子模型显著优于 CAPM，是现代多因子定价体系的起点。

## Key Takeaway

- 价值股（高 B/M）长期跑赢成长股
- 小盘股长期跑赢大盘股（虽然 21 世纪以来 SMB 显著衰减）
- "异象"在三因子调整后大多收敛，但 [[momentum]] 仍稳健存在

## WQ Brain 实现示例

```
# 价值因子代理（book-to-market）
rank(divide(fnd_book_value, market_cap))

# Size 反向（市值越小越好）
reverse(rank(market_cap))
```

## 相关

- 五因子扩展见 [[2015-fama-french-five-factor]]
- 投资 + 盈利因子的替代体系见 [[2015-hou-xue-zhang-q-factor]]
