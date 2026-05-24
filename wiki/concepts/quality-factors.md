---
title: 质量因子库（Quality Factors）
type: concept
tags: [quality, profitability, fundamental6, gp, cookbook]
created: 2026-05-22
---

# 质量因子库

"好公司" → 高盈利能力 + 低杠杆 + 盈利稳定。Quality Minus Junk（[[2019-asness-frazzini-pedersen-quality-minus-junk]]）证明 QMJ 在 24 个国家都为正。

## 经济直觉

市场长期低估"无聊但稳健"的公司。质量异象的核心驱动是 **行为偏差**（投资者偏好彩票型股票）+ **限制套利**（机构受 benchmark 约束做不了空）。详见 [[2019-asness-frazzini-pedersen-quality-minus-junk]] + [[2011-baker-bradley-wurgler-benchmarks-low-vol]]。

## 可用字段（来自 `fundamental6`）

| 子维度 | 字段 | 实现 |
| --- | --- | --- |
| **Profitability** | `cashflow_op` / `assets`、`eps` / `equity` | `divide(cashflow_op, assets)` = GP/A 代理 |
| **Growth** | `cashflow_op` 的 `ts_delta(_, 252)` | 盈利同比 |
| **Safety** | `debt` / `equity`、`ts_std_dev(returns, 252)` | 杠杆 + 收益波动 |
| **Payout** | `cashflow_dividends` / `equity` | 分红率 |

## 实现模板

```
# Novy-Marx GP/A（最简单最有效的质量指标）
rank(divide(cashflow_op, assets))

# QMJ 简化版（profitability + safety 复合）
add(
    rank(divide(cashflow_op, assets)),
    reverse(rank(divide(debt, equity)))    # 低杠杆为佳，反向 rank
)

# 行业中性的 QMJ
group_neutralize(
    add(rank(divide(cashflow_op, assets)),
        reverse(rank(divide(debt, equity)))),
    subindustry
)

# 加入低波动的 safety
add(
    rank(divide(cashflow_op, assets)),
    reverse(rank(ts_std_dev(returns, 252)))
)
```

## 踩坑

- 多指标合成时**先 rank 再 add**，不要直接 add 原值（量纲会主导）
- ROE 类比 GP/A 弱 → 因为 net income 受会计调整污染。优先 cashflow_op
- Safety 与 value 通常相关（高质量公司估值高），单独看 QMJ 跟 [[value-factors]] 是天然对冲

## 参考

- [[2019-asness-frazzini-pedersen-quality-minus-junk]] QMJ 原文
- [[2013-novy-marx-other-side-of-value]] GP/A 起源
- [[2014-novy-marx-quality-investing]] 质量陷阱说明
