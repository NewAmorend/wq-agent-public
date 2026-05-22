---
title: Which Factors?
type: concept
tags: [paper, factor-zoo, replication, q-factor]
sources: [https://academic.oup.com/rof/article/23/1/1/5133564]
created: 2026-05-22
authors: [Kewei Hou, Haitao Mo, Chen Xue, Lu Zhang]
year: 2019
paper_source: manual
---

# Which Factors?

**作者**：Hou, Mo, Xue, Zhang　**年份**：2019　**期刊**：Review of Finance

## 核心结论

系统复现了 447 个因子，发现 65% 在严格样本外测试下**不可复现**。q-factor 模型可解释剩余可复现因子中的大多数。

## Key Takeaway

- 因子复现性是定价文献最大问题
- 替换"等权 quintile"为"NYSE breakpoints + value-weighted"会让很多异象消失
- 印证 [[2016-harvey-liu-zhu-cross-section]] 的多重检验担忧

## 给 wq-agent 的启示

- 用 LLM 生成因子时，重视"在多个 universe / delay 下表现是否稳健"
- 不要追求 fitness 最大化，追求 fitness 稳定性
- 优先级：经济学叙事 > 多市场稳健 > IS fitness

## 相关

- q-factor 原文 [[2015-hou-xue-zhang-q-factor]]
- 因子动物园 [[2016-harvey-liu-zhu-cross-section]]
