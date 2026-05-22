---
title: The Cross-Section of Volatility and Expected Returns
type: concept
tags: [paper, idiosyncratic-volatility, low-volatility, anomaly]
sources: [https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.2006.00836.x]
created: 2026-05-22
authors: [Andrew Ang, Robert J. Hodrick, Yuhang Xing, Xiaoyan Zhang]
year: 2006
paper_source: manual
---

# The Cross-Section of Volatility and Expected Returns

**作者**：Ang, Hodrick, Xing, Zhang　**年份**：2006　**期刊**：Journal of Finance

## 核心结论

**特异性波动率（idiosyncratic volatility, IVOL）**与未来收益**负相关**——与教科书预测相反。高 IVOL 的股票未来一个月平均跑输 -1.06%/月。

## Key Takeaway

- "IVOL puzzle"：与传统定价理论冲突，是低波动异象的另一面
- 解释包括：套利限制、投资者偏好彩票型股票、过度信心
- 与 [[2011-baker-bradley-wurgler-benchmarks-low-vol]] 互为补充

## WQ Brain 实现示例

```
# IVOL 代理：FF3 残差的标准差，简化为 252 日波动率减去市场波动
ivol = ts_std_dev(subtract(returns, market_returns), 252)
reverse(rank(ivol))
```

## 相关

- 低波动 [[2011-baker-bradley-wurgler-benchmarks-low-vol]]
- Beta 异象 [[2014-frazzini-pedersen-betting-against-beta]]
