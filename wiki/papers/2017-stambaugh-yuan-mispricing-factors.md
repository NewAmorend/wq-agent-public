---
title: Mispricing Factors
type: concept
tags: [paper, factor-model, mispricing, short-selling]
sources: [https://academic.oup.com/rfs/article/30/4/1270/2965095]
created: 2026-05-22
authors: [Robert F. Stambaugh, Yu Yuan]
year: 2017
paper_source: manual
---

# Mispricing Factors

**作者**：Stambaugh & Yuan　**年份**：2017　**期刊**：Review of Financial Studies

## 核心结论

将 11 个异象按方向归并成两个**错误定价复合指标**：

- **MGMT**（management-related）：公司行为类异象（净增发、应计、资产增长、投资、盈利能力等）
- **PERF**（performance-related）：业绩类异象（动量、毛利率、ROA、不良信用、扭转等）

加上 MKT、SMB 构成四因子模型，解释力优于 FF5。

## Key Takeaway

- 异象本质是**错误定价**，做多被低估、做空被高估
- 限制套利（高 idiosyncratic vol、低流动性）的股票上异象更强
- 短端 leg 贡献了大部分超额收益（短卖限制是关键摩擦）

## WQ Brain 实现示例

```
# MGMT 简化版（净增发反向 + 资产增长反向 + 盈利能力）
mgmt = add(
    reverse(rank(fnd_net_share_issuance)),
    reverse(rank(divide(ts_delta(fnd_total_assets, 252), ts_delay(fnd_total_assets, 252)))),
    rank(divide(fnd_gross_profit, fnd_total_assets))
)
```

## 相关

- 限制套利 [[2011-baker-bradley-wurgler-benchmarks-low-vol]]
- 异象数量级 [[2016-harvey-liu-zhu-cross-section]]
