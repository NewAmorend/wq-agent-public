---
title: Open Source Cross-Sectional Asset Pricing
type: concept
tags: [paper, factor-zoo, replication, open-source, benchmark]
sources: [https://www.nowpublishers.com/article/Details/CFR-0112]
created: 2026-06-03
authors: [Andrew Y. Chen, Tom Zimmermann]
year: 2022
journal: Critical Finance Review
paper_source: curator
---

# Open Source Cross-Sectional Asset Pricing

**作者**：Chen, Zimmermann　**年份**：2022　**期刊**：Critical Finance Review

## 核心结论

论文和配套开源项目系统整理、实现并测试大量横截面 anomaly，为因子复现、数据口径和可比 benchmark 提供基础设施。

## Key Takeaway

- 因子研究需要标准化实现，否则同名 anomaly 可能结果差异很大。
- 开源复现能帮助区分真实稳健因子和参数/口径偶然性。
- factor zoo 不只是论文列表，更应该转成可复现字段、窗口和评价协议。

## 给 wq-agent 的启示

- curator 应将重复 lessons 抽象成稳定 [[patterns/overfit-parameter-search]] 或 recipe。
- 字段页要记录口径、方向和替代字段，避免同义字段重复造轮子。
- bench 应覆盖每个重要 recipe / pattern，防止 RAG 检索退化。

## 相关

[[2019-hou-mo-xue-zhang-which-factors]]、[[2016-harvey-liu-zhu-cross-section]]、[[concepts/model-factor-libraries]]
