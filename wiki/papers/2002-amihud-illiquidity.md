---
title: Illiquidity and Stock Returns — Cross-Section and Time-Series Effects
type: concept
tags: [paper, liquidity, microstructure, amihud]
sources: [https://www.sciencedirect.com/science/article/abs/pii/S1386418101000246]
created: 2026-05-22
authors: [Yakov Amihud]
year: 2002
paper_source: manual
---

# Illiquidity and Stock Returns: Cross-Section and Time-Series Effects

**作者**：Amihud　**年份**：2002　**期刊**：Journal of Financial Markets

## 核心结论

提出 **ILLIQ 度量**：日均「|return| / 美元成交量」，简单但稳健。横截面上 ILLIQ 高的股票预期收益高（流动性溢价），时间序列上市场整体 ILLIQ 升高时下期市场预期收益升高。

## Key Takeaway

- ILLIQ 是事实上最被广泛使用的流动性代理（不需要日内数据）
- 既是定价因子，也是市场状态指标
- 与 [[2003-pastor-stambaugh-liquidity-risk]] 互补

## WQ Brain 实现示例

```
# Amihud ILLIQ：|return| / 成交额，20 日均值
illiq = ts_mean(divide(abs(returns), volume * close), 20)
rank(illiq)
```

## 相关

- 流动性风险 [[2003-pastor-stambaugh-liquidity-risk]]
- 微观结构反转 [[1990-lo-mackinlay-contrarian-profits]]
