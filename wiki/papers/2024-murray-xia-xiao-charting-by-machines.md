---
title: Charting by Machines
type: concept
tags: [paper, machine-learning, charting, technical-analysis, price-patterns]
sources: [https://econpapers.repec.org/article/eeejfinec/v_3a153_3ay_3a2024_3ai_3ac_3as0304405x2400014x.htm]
created: 2026-06-03
authors: [Scott Murray, Yusen Xia, Houping Xiao]
year: 2024
journal: Journal of Financial Economics
paper_source: curator
---

# Charting by Machines

**作者**：Murray, Xia, Xiao　**年份**：2024　**期刊**：Journal of Financial Economics

## 核心结论

论文用机器学习从历史价格表现中预测股票横截面收益，发现这些预测不仅显著，而且不同于传统 momentum、reversal 和已知技术信号。这为“机器学习式技术分析”提供了顶刊证据。

## Key Takeaway

- 历史价格路径中可能有非线性形态，不能只用单个 `ts_delta` 概括。
- 技术分析的有效性要用 out-of-sample 和大股票样本验证。
- ML 优化表现好的模型仍需检查交易成本、换手和 self-correlation。

## 给 wq-agent 的启示

- [[recipes/price-volume-reversal]] 可扩展为多窗口 price-pattern recipe。
- 价量 alpha 应记录是否区别于已有 momentum/reversal，避免 [[patterns/self-correlation-crowding]]。
- 对 [[fields/close]]、[[fields/vwap]]、[[fields/volume]] 增加“路径形态”用法。

## 相关

[[2023-jiang-kelly-xiu-reimagining-price-trends]]、[[recipes/price-volume-reversal]]、[[patterns/high-turnover]]
