---
title: 流动性与微观结构
type: concept
tags: [liquidity, microstructure, pv1, illiq, turnover, cookbook]
created: 2026-05-22
---

# 流动性与微观结构

低流动性 → 高预期回报（流动性溢价）。Amihud (2002) 的 ILLIQ 是最广泛使用的代理。

## 经济直觉

投资者需要补偿持有难以变现的资产的成本。**ILLIQ 高 → 未来回报高**（横截面）+ **市场整体 ILLIQ 升高 → 下期市场回报高**（时间序列）。详见 [[2002-amihud-illiquidity]] 与 [[2003-pastor-stambaugh-liquidity-risk]]。

## 可用字段（来自 `pv1`）

| 字段 | 用法 |
| --- | --- |
| `volume` | 日成交股数 |
| `adv20` | 20 日均成交额（已可直接用） |
| `cap` | 市值 |
| `returns` | 日收益 |
| `close` × `volume` | 日成交额（手动计算） |

## 实现模板

```
# Amihud ILLIQ：|return| / 成交额（20 日均值）
rank(ts_mean(divide(abs(returns), multiply(volume, close)), 20))

# Turnover 反向（流动性高 = 不值得溢价）
reverse(rank(divide(volume, cap)))

# 成交额变化（流动性冲击）
rank(ts_delta(adv20, 20))

# 行业中性后效果更纯
group_neutralize(
    rank(ts_mean(divide(abs(returns), multiply(volume, close)), 20)),
    subindustry
)

# 流动性 beta（个股对市场流动性的暴露）
ts_regression(returns, ts_mean(divide(abs(returns), multiply(volume, close)), 20), 252, 0, 1)
```

## 踩坑

- ILLIQ 在小盘股上数值极大 → **必须 rank 或 winsorize**，否则一只股票主导
- `divide(_, volume)` 当 volume=0（停牌/无交易）时爆炸 → 加 `to_nan` 或先过滤
- 流动性因子与 size 高相关（小盘流动性差）→ 控 size 是常规操作
- Turnover 高 → 你的 alpha 也会换手快，注意 `MAX_TURNOVER` 阈值（WQ 上限 70%）

## 参考

- [[2002-amihud-illiquidity]] ILLIQ
- [[2003-pastor-stambaugh-liquidity-risk]] 流动性风险因子
