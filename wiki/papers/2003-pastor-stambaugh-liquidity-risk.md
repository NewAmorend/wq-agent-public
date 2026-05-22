---
title: Liquidity Risk and Expected Stock Returns
type: concept
tags: [paper, liquidity, factor-model, risk-premium]
sources: [https://www.journals.uchicago.edu/doi/10.1086/374184]
created: 2026-05-22
authors: [Lubos Pastor, Robert F. Stambaugh]
year: 2003
paper_source: manual
---

# Liquidity Risk and Expected Stock Returns

**作者**：Pastor & Stambaugh　**年份**：2003　**期刊**：Journal of Political Economy

## 核心结论

提出基于"价格反转"度量的**总市场流动性因子**：流动性差时大单造成的临时价格冲击更大，下个时段会有反向。对流动性 beta 高的股票要求 7.5% 年化的额外风险溢价。

## Key Takeaway

- 系统性流动性是定价因子，非仅特征
- 流动性 beta 高的股票在流动性危机时跌得更狠
- 增量于市场、SMB、HML、MOM

## WQ Brain 实现示例

```
# 流动性 beta 代理：股票收益对市场流动性指标的回归 slope
# 简化版（用 ILLIQ 变化代替）
illiq_chg = ts_delta(ts_mean(divide(abs(returns), volume * close), 20), 5)
rank(ts_regression(returns, illiq_chg, 252, 0, 1))
```

## 相关

- ILLIQ 指标 [[2002-amihud-illiquidity]]
