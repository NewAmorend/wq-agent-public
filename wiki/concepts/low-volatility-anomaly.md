---
title: 低波动异象
type: concept
tags: [low-volatility, ivol, beta, anomaly, pv1, cookbook]
created: 2026-05-22
---

# 低波动异象

低波动股票长期跑赢高波动股票 —— 与 CAPM 预测相反，是 [[2011-baker-bradley-wurgler-benchmarks-low-vol]] 与 [[2006-ang-hodrick-xing-zhang-cross-section-volatility]] 揭示的最稳健异象之一。

## 经济直觉

- **机构受 benchmark 约束**：追求相对回报 → 抢高 beta 股票 → 推高估值 → 低波动股相对便宜
- **杠杆约束**：投资者用不了杠杆 → 只能在 risky asset 内"加杠杆"= 选高 beta → BAB ([[2014-frazzini-pedersen-betting-against-beta]])
- **行为偏差**：散户偏爱"彩票型"高波动股票

## 字段（基于 `pv1` 计算）

| 维度 | 实现 |
| --- | --- |
| Total volatility | `ts_std_dev(returns, 252)` |
| IVOL（特异波动） | `ts_std_dev(subtract(returns, market_returns), 252)` |
| Beta | `ts_regression(returns, market_returns, 252, 0, 1)` |
| Downside vol | `ts_std_dev(if_else(returns < 0, returns, 0), 252)` |

## 实现模板

```
# 经典低波动（年化 std 反向）
reverse(rank(ts_std_dev(returns, 252)))

# 行业中性的低波动（最重要的调整）
group_neutralize(
    reverse(rank(ts_std_dev(returns, 252))),
    subindustry
)

# 低 beta（BAB 简化版，未做 leverage scaling）
reverse(rank(ts_regression(returns, market_returns, 252, 0, 1)))

# IVOL 反向（Ang et al 的 IVOL puzzle）
reverse(rank(ts_std_dev(subtract(returns, market_returns), 252)))

# 低波动 + 质量复合（防御型策略经典配方）
add(
    reverse(rank(ts_std_dev(returns, 252))),
    rank(divide(cashflow_op, assets))     # GP/A 来自 [[quality-factors]]
)
```

## 踩坑

- 短窗口（<60）波动率波动太大 → 用 252 或更长
- 低波动信号与 size 高相关（小盘波动大）→ 控 size 或行业中性
- 在牛市初期可能跑输（参与不足）→ 不适合短期择时
- BAB 严格版需要 leverage scaling，FASTEXPR 实现不了完整版

## 参考

- [[2011-baker-bradley-wurgler-benchmarks-low-vol]] 制度解释
- [[2006-ang-hodrick-xing-zhang-cross-section-volatility]] IVOL puzzle
- [[2014-frazzini-pedersen-betting-against-beta]] BAB 因子
- [[2019-asness-frazzini-pedersen-quality-minus-junk]] QMJ 中的 safety 维度
