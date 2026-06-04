---
title: (Re-)Imag(in)ing Price Trends
type: concept
tags: [paper, machine-learning, price-trends, technical-analysis, momentum-reversal]
sources: [https://ideas.repec.org/a/bla/jfinan/v78y2023i6p3193-3249.html]
created: 2026-06-03
authors: [Jingwen Jiang, Bryan Kelly, Dacheng Xiu]
year: 2023
journal: Journal of Finance
paper_source: curator
---

# (Re-)Imag(in)ing Price Trends

**作者**：Jiang, Kelly, Xiu　**年份**：2023　**期刊**：Journal of Finance

## 核心结论

论文不用预先定义 momentum / reversal 形态，而是用灵活学习方法从历史价格图形里寻找对未来收益有预测力的 pattern。结论是：价格趋势中仍有可学习的非线性结构，传统线性动量/反转只是其中很粗的一类近似。

## Key Takeaway

- 价量信号不应只局限于 `ts_delta(close, d)` 或固定窗口 momentum。
- 非线性价格形态可能同时包含短期反转、中期动量和波动状态。
- 技术形态要特别警惕 [[patterns/overfit-parameter-search]]，需要 bench 和跨窗口稳定性。

## 给 wq-agent 的启示

- 扩展 [[recipes/price-volume-reversal]]：加入 `close` / [[returns]] / [[vwap]] 的多窗口组合，而不是只做单一窗口差分。
- 对价格形态类 alpha，优先记录其窗口族和经济解释，避免只记录偶然参数。
- 生成器可以把 PV 类信号拆成价格腿、成交量确认腿、平滑腿。

## 相关

[[momentum-reversal-pv]]、[[recipes/price-volume-reversal]]、[[fields/close]]、[[fields/returns]]、[[patterns/self-correlation-crowding]]
