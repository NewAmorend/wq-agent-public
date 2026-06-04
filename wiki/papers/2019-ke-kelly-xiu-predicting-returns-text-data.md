---
title: Predicting Returns With Text Data
type: concept
tags: [paper, text-data, news, sentiment, machine-learning]
sources: [https://www.nber.org/papers/w26186]
created: 2026-06-03
authors: [Zheng Tracy Ke, Bryan Kelly, Dacheng Xiu]
year: 2019
journal: NBER Working Paper
paper_source: curator
---

# Predicting Returns With Text Data

**作者**：Ke, Kelly, Xiu　**年份**：2019　**来源**：NBER Working Paper

## 核心结论

论文提出监督式文本挖掘方法，从新闻文本中学习对收益预测有用的 sentiment 表达，而不是依赖通用情绪词典。其关键思想是：金融文本的“情绪”应该服务于 return prediction 目标。

## Key Takeaway

- 通用 sentiment score 未必适合预测收益，最好训练 return-aware 文本信号。
- 新闻信号要区分事件强度、文本方向、市场是否已反应。
- 文本类 alpha 天然存在覆盖和事件稀疏问题。

## 给 wq-agent 的启示

- 扩展 [[news-sentiment-events]]：新闻字段应配合价格反应和成交量确认。
- 对 text/news alpha，优先用 [[trade_when]] 或事件门控，避免无事件日交易。
- 需要特别检查 [[patterns/low-coverage-nan]] 和 [[patterns/high-turnover]]。

## 相关

[[news-sentiment-events]]、[[recipes/analyst-revision-momentum]]、[[fields/volume]]、[[patterns/low-coverage-nan]]
