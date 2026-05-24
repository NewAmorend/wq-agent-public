---
title: 价值因子库（Value Factors）
type: concept
tags: [value, fundamental, fundamental6, fundamental2, ratio, cookbook]
created: 2026-05-22
---

# 价值因子库

把"便宜的资产"做多、"贵的资产"做空。**所有价值因子都要 cross-sectional rank + 行业中性**，否则被行业 beta 吃掉。

## 经济直觉

便宜并不意味着"值得拥有"——它意味着 **预期收益的折现要求高**。低 B/M、低 P/E 的公司未来回报溢价由 Fama-French (1993) 与无数后续工作证实，详见 [[1993-fama-french-common-risk-factors]]。

## 可用字段（来自 `fundamental6` / `fundamental2`）

| 类别 | 字段 | 用法 |
| --- | --- | --- |
| 账面 | `bookvalue_ps`, `equity`, `assets` | book-to-market：`divide(equity, cap)` |
| 盈利 | `eps`, `cashflow_op`, `cashflow` | earnings yield：`divide(eps, close)` |
| 销售 | 通过 anl4 的 `actual_sales_value_quarterly` | sales yield： `divide(actual_sales_value_quarterly, cap)` |
| 现金 | `cash`, `cashflow_op`, `enterprise_value` | EV/Cash、FCF yield |
| 企业 | `enterprise_value`, `debt`, `equity` | EV/EBITDA 类 |

`cap` 来自 [[pv1]]，做 PV 比率必备。

## 实现模板

```
# 经典 book-to-market
rank(divide(equity, cap))

# 行业中性后效果更稳
group_neutralize(rank(divide(equity, cap)), subindustry)

# 价值 + 质量复合（Asness-Pedersen 路线）
add(
    rank(divide(equity, cap)),
    rank(divide(cashflow_op, assets))
)

# 用 EV/Cashflow 替代 P/E（避开零盈利公司）
rank(divide(cashflow_op, enterprise_value))
```

## 踩坑

- 不要直接除（`close / bookvalue_ps`）—— 价格量纲让大盘股主导。**必须 rank 或 zscore**
- `eps` 在亏损公司是负数，rank 后正常但绝对值除会反号 → 用 `divide(eps, close)` 再 rank
- 单纯 P/E 在熊市跑赢、牛市跑输 → **配 [[quality-factors]] 或 [[momentum-factors]] 做对冲**
- HML 在 FF5 加入 RMW/CMA 后变得"多余"——价值需要质量护身

## 参考论文

- [[1993-fama-french-common-risk-factors]] HML 起源
- [[2013-asness-moskowitz-pedersen-value-momentum-everywhere]] 全资产 value
- [[2013-novy-marx-other-side-of-value]] 价值 + 盈利能力
