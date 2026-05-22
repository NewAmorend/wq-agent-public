---
title: Short- and Long-Horizon Behavioral Factors
type: concept
tags: [paper, behavioral, momentum, post-earnings-drift]
sources: [https://academic.oup.com/rfs/article/33/4/1673/5614281]
created: 2026-05-22
authors: [Kent Daniel, David Hirshleifer, Lin Sun]
year: 2020
paper_source: manual
---

# Short- and Long-Horizon Behavioral Factors

**作者**：Daniel, Hirshleifer, Sun　**年份**：2020　**期刊**：Review of Financial Studies

## 核心结论

提出 **PEAD**（短期：post-earnings announcement drift）和 **FIN**（长期：financing-related，含净增发、回购、long-term reversal）两个行为因子。组合解释力优于 FF5 和 q-model。

## Key Takeaway

- 短期反应不足（PEAD） + 长期反应过度（FIN）双管齐下
- PEAD：盈利公告后 60 天内的价格漂移
- FIN：公司外部融资行为是管理层 timing 信号

## WQ Brain 实现示例

```
# PEAD 简化版：盈利惊喜后的 20 日累计收益
pead = ts_sum(if_else(is_nan(earnings_surprise), 0, returns), 20)
rank(pead)

# FIN 简化版：净股票增发反向
reverse(rank(fnd_net_share_issuance))
```

## 相关

- 动量原始 [[1993-jegadeesh-titman-returns-to-buying-winners]]
- 错误定价 [[2017-stambaugh-yuan-mispricing-factors]]
