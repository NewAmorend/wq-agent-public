---
title: Deep Learning in Asset Pricing
type: concept
tags: [paper, deep-learning, asset-pricing, sdf, machine-learning]
sources: [https://pubsonline.informs.org/doi/abs/10.1287/mnsc.2023.4695]
created: 2026-06-03
authors: [Luyang Chen, Markus Pelger, Jason Zhu]
year: 2023
journal: Management Science
paper_source: curator
---

# Deep Learning in Asset Pricing

**作者**：Chen, Pelger, Zhu　**年份**：2023　**期刊**：Management Science

## 核心结论

论文用深度学习估计随机折现因子（SDF）并建模资产收益的非线性结构，强调深度模型可以在大规模特征空间中提取传统线性模型遗漏的信息。

## Key Takeaway

- 非线性组合、交互项和状态依赖是 ML asset pricing 的核心优势。
- 深度学习结果需要解释层：哪些特征、行业、状态贡献了预测力。
- 对 WQ 表达式而言，不能直接复刻深度模型，但可以学习其“多源信息交互”的思想。

## 给 wq-agent 的启示

- recipe 应鼓励跨信息源组合：PV + fundamental + analyst + news，而不是单字段堆窗口。
- 对复杂组合，优先使用 rank/neutralize/decay 保持稳定。
- 可作为 [[concepts/model-factor-libraries]] 的理论背景页。

## 相关

[[concepts/model-factor-libraries]]、[[recipes/quality-profitability]]、[[recipes/analyst-revision-momentum]]、[[patterns/self-correlation-crowding]]
