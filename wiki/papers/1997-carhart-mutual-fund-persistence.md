---
title: On Persistence in Mutual Fund Performance
type: concept
tags: [paper, factor-model, momentum, ff4]
sources: [https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1997.tb03808.x]
created: 2026-05-22
authors: [Mark M. Carhart]
year: 1997
paper_source: manual
---

# On Persistence in Mutual Fund Performance

**作者**：Carhart　**年份**：1997　**期刊**：Journal of Finance

## 核心结论

在 Fama-French 三因子上加 **MOM**（Momentum）因子构成 Carhart 四因子模型。基金"业绩持续性"几乎可以被四因子解释殆尽，剩余 alpha 接近 0。

## Key Takeaway

- 基金选股的"超额收益"很大程度来自暴露 momentum
- MOM 因子 = WML（Winners Minus Losers）：过去 11 个月（跳过最近 1 月）排名最高 30% 减最低 30%
- 是后续所有"factor zoo"研究的基线模型

## WQ Brain 实现示例

```
# WML / MOM 因子
rank(ts_delta(close, 252) - ts_delta(close, 21))
```

## 相关

- 动量原始证据 [[1993-jegadeesh-titman-returns-to-buying-winners]]
- 因子模型基础 [[1993-fama-french-common-risk-factors]]
