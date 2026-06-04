---
title: The Virtue of Complexity in Return Prediction
type: concept
tags: [paper, machine-learning, return-prediction, complexity, overfit]
sources: [https://www.nber.org/papers/w30217]
created: 2026-06-03
authors: [Bryan Kelly, Semyon Malamud, Kangying Zhou]
year: 2024
journal: Journal of Finance
paper_source: curator
---

# The Virtue of Complexity in Return Prediction

**作者**：Kelly, Malamud, Zhou　**年份**：2024　**期刊**：Journal of Finance

## 核心结论

论文认为，在收益预测这种低信噪比问题里，过度简化模型可能系统性低估可预测性；高复杂度模型在合适条件下可以改善组合表现。这不是鼓励乱调参，而是提醒：金融里的“简单优先”也可能导致 underfit。

## Key Takeaway

- 复杂模型是否有价值，要看 out-of-sample、组合收益和稳健性，不只看样本内拟合。
- “复杂”与“过拟合”不是同义词，但复杂模型必须有严格验证。
- 对 LLM 生成 alpha，参数/结构复杂度要有经济叙事和复测规则。

## 给 wq-agent 的启示

- 更新 [[patterns/overfit-parameter-search]]：不要机械拒绝复杂表达式，重点看跨 universe/delay 稳定性。
- 对复杂 alpha，curator 应要求更强的 bench、更多失败记录和更清晰的 why-work。
- 可作为 [[concepts/model-factor-libraries]] 的理论支持：非线性组合可能补充线性因子库。

## 相关

[[patterns/overfit-parameter-search]]、[[concepts/model-factor-libraries]]、[[2020-gu-kelly-xiu-empirical-asset-pricing-ml]]
