---
title: Asset Growth and the Cross-Section of Stock Returns
type: concept
tags: [paper, investment, asset-growth, anomaly]
sources: [https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.2008.01370.x]
created: 2026-05-22
authors: [Michael J. Cooper, Huseyin Gulen, Michael J. Schill]
year: 2008
paper_source: manual
---

# Asset Growth and the Cross-Section of Stock Returns

**作者**：Cooper, Gulen, Schill　**年份**：2008　**期刊**：Journal of Finance

## 核心结论

**资产增长率（年度总资产变化）**与未来股票收益强烈负相关。资产扩张快的公司（不论是通过收购、增发还是内部投资）未来 5 年都跑输资产缩减的公司，年化差异 ~8%。

## Key Takeaway

- 是 FF5 中 CMA 因子和 q-model 中 I/A 因子的实证基础
- 反映"管理层过度投资 / 帝国建设"行为偏差
- 与 [[2017-stambaugh-yuan-mispricing-factors|MGMT]] 因子同源

## WQ Brain 实现示例

```
# 年度资产增长率反向
reverse(rank(divide(
    ts_delta(fnd_total_assets, 252),
    ts_delay(fnd_total_assets, 252)
)))
```

## 相关

- 投资因子 [[2015-fama-french-five-factor]]
- q-factor [[2015-hou-xue-zhang-q-factor]]
