---
title: …and the Cross-Section of Expected Returns
type: concept
tags: [paper, factor-zoo, multiple-testing, statistical-rigor]
sources: [https://academic.oup.com/rfs/article/29/1/5/1843824]
created: 2026-05-22
authors: [Campbell R. Harvey, Yan Liu, Heqing Zhu]
year: 2016
paper_source: manual
---

# …and the Cross-Section of Expected Returns

**作者**：Harvey, Liu, Zhu　**年份**：2016　**期刊**：Review of Financial Studies

## 核心结论

总结了 50 年学术文献中提出的 **316 个**因子（"factor zoo"），并指出：考虑多重检验问题后，新因子的 t 统计量阈值应从 2.0 提高到 **3.0+**。

## Key Takeaway

- 因子绝大多数是**数据挖掘伪发现**
- WQ Brain 上做 alpha 必须用样本外验证（IS / OS 分割）
- 高 fitness 不等于真信号——需经济学叙事 + 多市场稳健

## 给 wq-agent 的启示

- 不能只看 fitness 排名；同一逻辑在多 region/universe/delay 下保持正即可信
- 对 LLM 生成的"创新"因子尤其要警惕：很可能复现了文献中的伪发现
- 优先复现 [[1993-jegadeesh-titman-returns-to-buying-winners|经典因子]]，再考虑变体

## 相关

- 复现争议 [[2019-hou-mo-xue-zhang-which-factors]]
- 错误定价归纳 [[2017-stambaugh-yuan-mispricing-factors]]
