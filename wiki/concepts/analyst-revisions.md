---
title: 分析师预期修正
type: concept
tags: [analyst, analyst4, revisions, surprise, eps, cookbook]
created: 2026-05-22
---

# 分析师预期修正

`analyst4` 提供 800+ broker 的 EPS / 销售 / 现金流预测的实时更新（1324 个字段）。**预期修正动量是最稳健的事件驱动信号之一**。

## 经济直觉

- **修正不对称**：上修信号比下修信号更强（管理层引导偏保守，上修常常表示业绩超预期）
- **羊群效应**：单分析师上修后，其他分析师跟上 → 修正趋势持续 1-3 个月
- 与 [[2020-daniel-hirshleifer-sun-behavioral-factors|PEAD]] 互补

## 可用字段（analyst4，代表性 30+）

| 类别 | 代表字段 | 用法 |
| --- | --- | --- |
| Actual | `actual_eps_value_quarterly`, `actual_sales_value_quarterly`, `actual_dividend_value_quarterly` | 实际值（事后） |
| Consensus | `anl4_af_eps_value`, `anl4_af_cfps_value`, `anl4_af_div_value` | 当前共识 |
| Dispersion | `adj_net_income_stddev`, `adj_net_income_avg`, `adj_net_income_median` | 分歧度 |
| Range | `anl4_adxqfv110_high`, `anl4_adxqfv110_low` | 高低边界 |
| Detail | `anl4_ads1detailqfv110_estvalue`, `anl4_ads1detailqfv110_prevval` | 单分析师当前/上次 |

## 实现模板

```
# 共识 EPS 修正动量（30 日变化）
rank(ts_delta(anl4_af_eps_value, 30))

# 修正强度（标准化）
divide(ts_delta(anl4_af_eps_value, 30), anl4_af_eps_value)

# 分歧度反向（共识越紧 → 信号越可信）
reverse(rank(divide(adj_net_income_stddev, abs(adj_net_income_avg))))

# 销售上修动量（cross-validate EPS 修正）
rank(ts_delta(actual_sales_value_quarterly, 90))

# 修正 + 价格动量组合（共振）
multiply(
    rank(ts_delta(anl4_af_eps_value, 30)),
    rank(ts_delta(close, 30))
)
```

## 踩坑

- `anl4_*` 字段大量 NaN（小盘 / 新上市覆盖差）→ 加 `ts_backfill` 或转用 `to_nan(_, 0)`
- 共识 EPS 在亏损公司（负值）取 ratio 会反号 → 用 abs 或先过滤
- 修正信号在财报季最强（前后 5 个交易日）→ 配 `trade_when` 或 [[news-sentiment-events]]
- Dispersion 在大盘/小盘行为不同 → 行业内 rank 更稳

## 参考

- [[2020-daniel-hirshleifer-sun-behavioral-factors]] PEAD 行为因子
- [[1993-jegadeesh-titman-returns-to-buying-winners]] 修正动量与价格动量同源
