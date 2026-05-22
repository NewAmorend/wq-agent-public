---
title: Digesting Anomalies — An Investment Approach (q-factor model)
type: concept
tags: [paper, factor-model, investment, profitability, q-factor]
sources: [https://academic.oup.com/rfs/article/28/3/650/1574802]
created: 2026-05-22
authors: [Kewei Hou, Chen Xue, Lu Zhang]
year: 2015
paper_source: manual
---

# Digesting Anomalies: An Investment Approach

**作者**：Hou, Xue, Zhang　**年份**：2015　**期刊**：Review of Financial Studies

## 核心结论

提出四因子 **q-model**：MKT、ME（市值）、I/A（投资率，反向）、ROE（盈利能力）。在解释 80+ 个异象上整体优于 Carhart 四因子和 FF5。

## Key Takeaway

- I/A（资产增长率）的反向溢价非常稳健
- ROE 优于 GP/A 作为盈利能力代理
- "投资 + 盈利"是 q-theory 的两大支柱

## WQ Brain 实现示例

```
# I/A 投资因子（资产增长反向）
ia = reverse(rank(divide(
    ts_delta(fnd_total_assets, 252),
    ts_delay(fnd_total_assets, 252)
)))

# ROE 盈利能力
roe = rank(divide(fnd_net_income, fnd_book_equity))

# q-factor 复合
add(ia, roe)
```

## 相关

- 五因子对比 [[2015-fama-french-five-factor]]
- 复现争议 [[2019-hou-mo-xue-zhang-which-factors]]
