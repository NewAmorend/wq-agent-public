---
title: Asset Pricing with Omitted Factors
type: concept
tags: [paper, omitted-factors, risk-premia, pca, residualization]
sources: [https://econpapers.repec.org/RePEc%3Aucp%3Ajpolec%3Adoi%3A10.1086/714090]
created: 2026-06-03
authors: [Stefano Giglio, Dacheng Xiu]
year: 2021
journal: Journal of Political Economy
paper_source: curator
---

# Asset Pricing with Omitted Factors

**作者**：Giglio, Xiu　**年份**：2021　**期刊**：Journal of Political Economy

## 核心结论

如果资产定价模型遗漏了 priced factors，传统风险溢价估计会产生偏误。论文提出三步方法，用测试资产收益的主成分恢复潜在因子空间，再估计可观察因子的风险溢价。

## Key Takeaway

- 单个 alpha 的表现可能来自遗漏风险因子，而不是真正 mispricing。
- 残差化、因子剥离和 latent factor 控制对解释收益非常重要。
- 看到高 Sharpe 不等于发现独立 alpha，需要检查共因子暴露。

## 给 wq-agent 的启示

- 对高质量 alpha，curator 应提示检查 [[patterns/self-correlation-crowding]]。
- [[ts_regression]] / neutralization 不只是降噪，也是在控制遗漏风险暴露。
- 与行业中性、市场 beta 中性、模型因子库形成一套解释框架。

## 相关

[[patterns/self-correlation-crowding]]、[[ts_regression]]、[[group_neutralize]]、[[concepts/model-factor-libraries]]
