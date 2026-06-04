---
title: 质量与盈利能力 recipe
type: recipe
tags: [recipe, quality, profitability, fundamental]
created: 2026-06-03
---

# 质量与盈利能力 recipe

## 适用假设

高质量公司通常具有更稳定的现金流、更低财务压力和更好的资产使用效率；这类信号更新慢，但更适合构造低 turnover、跨周期稳定的 alpha。

## 推荐字段

- [[cashflow_op]]：经营现金流
- [[assets]]：规模和资产效率分母
- [[debt]]：杠杆和财务风险
- [[eps]]：盈利结果
- [[enterprise_value]]：估值和规模控制

## 基础表达式骨架

```text
rank(divide(cashflow_op, assets))

subtract(
  rank(divide(cashflow_op, assets)),
  rank(divide(debt, assets))
)

add(
  rank(divide(cashflow_op, assets)),
  reverse(rank(divide(debt, assets)))
)
```

## 稳定化步骤

1. 先构造有经济意义的比率，再 rank。
2. 必须做 [[group_neutralize]]，至少到行业或 subindustry。
3. 基本面信号窗口用 60-252 起步，避免短窗口过拟合。
4. 与 [[low-volatility-anomaly]] 或 [[value-factors]] 组合时，先检查重复暴露。

## 常见失败

- [[patterns/direction-sign-error]]：债务、资产增长等字段方向容易反。
- [[patterns/overfit-parameter-search]]：基本面字段不适合靠小窗口微调。
- [[patterns/self-correlation-crowding]]：质量、价值、低波动常有重叠。

## 相关

[[quality-factors]]、[[2019-asness-frazzini-pedersen-quality-minus-junk]]、[[2013-novy-marx-other-side-of-value]]
