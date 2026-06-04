---
title: Empirical Asset Pricing via Machine Learning
type: concept
tags: [paper, machine-learning, empirical-asset-pricing, benchmark, return-prediction]
sources: [https://academic.oup.com/rfs/article/33/5/2223/5758276]
created: 2026-06-03
authors: [Shihao Gu, Bryan Kelly, Dacheng Xiu]
year: 2020
journal: Review of Financial Studies
paper_source: curator
---

# Empirical Asset Pricing via Machine Learning

**作者**：Gu, Kelly, Xiu　**年份**：2020　**期刊**：Review of Financial Studies

## 核心结论

系统比较多种机器学习方法在横截面收益预测中的表现，发现非线性模型和树模型/神经网络在处理大量 firm characteristics 时有明显优势。论文是 ML empirical asset pricing 的基准文献。

## Key Takeaway

- 特征工程和模型选择会显著影响 out-of-sample 表现。
- 机器学习不是替代经济直觉，而是帮助发现非线性、交互和状态依赖。
- 对 alpha 生成，bench 和统一评估比单次高 fitness 更重要。

## 给 wq-agent 的启示

- 每个新 recipe 应记录字段族、窗口族、验证口径，方便 curator 比较。
- 对字段页，优先补高频 characteristics 的经济含义和方向。
- 对生成器，鼓励多字段 rank 后组合，而不是裸量纲相加。

## 相关

[[concepts/model-factor-libraries]]、[[patterns/overfit-parameter-search]]、[[factor-construction-best-practices]]
