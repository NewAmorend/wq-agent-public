---
title: 新闻、情绪与事件驱动
type: concept
tags: [news, news12, news18, sentiment1, socialmedia, event-driven, cookbook]
created: 2026-05-22
---

# 新闻、情绪与事件驱动

`news12`（875 字段）+ `news18`（121）+ `sentiment1`（19）+ `socialmedia8/12` 合在一起，给事件驱动策略提供原料。最有价值的是**事件后短期价格漂移 (PEAD-like)**。

## 经济直觉

- **反应不足**：盈余惊喜 → 60 天漂移（PEAD）
- **过度反应**：单日异常涨幅常常 1-2 周内回吐
- **关注度溢价**：新闻头条让散户买入推高短期价格

## 可用字段速查

### `news12`（事件 + 即时反应）
- `actual_eps_value`, `actual_earnings_per_share_value` — 真实盈余
- `actual_eps_value_2_1555`, `actual_earnings_per_share_value_afterhours` — 不同时段
- `after_hours_vwap_value`, `afterhours_volume_weighted_avg_price` — 盘后价
- `all_sessions_volume_weighted_avg_price`, `closing_volume` — 全时段成交
- `current_day_traded_volume`, `current_day_trading_volume_2` — 当日量

### `news18`（情绪聚合）
- `composite_sentiment_score_2`
- `equity_sentiment_score`
- `corporate_action_sentiment`
- `earnings_evaluation_sentiment`
- `editorial_commentary_sentiment_2`

### `sentiment1`（周频复合情绪）
- `weekly_equity_mood_index`
- `daily_equity_mood_indicator`
- `snt1_d1_earningsrevision`, `snt1_d1_earningssurprise`, `snt1_d1_earningstorpedo`
- `snt1_d1_analystcoverage`, `snt1_d1_longtermepsgrowthest`

## 实现模板

```
# PEAD：盈余惊喜后的 20 日累计收益
ts_sum(if_else(is_nan(actual_eps_value), 0, returns), 20)

# 情绪动量
rank(ts_delta(composite_sentiment_score_2, 5))

# 情绪 × 价格共振
multiply(
    rank(equity_sentiment_score),
    rank(ts_delta(close, 5))
)

# 短期过度反应反转（5 日大涨后买短期反向）
trade_when(
    abs(ts_delta(close, 1)) > ts_std_dev(returns, 60),  # 触发条件
    reverse(ts_zscore(returns, 5)),                      # alpha
    -1                                                   # 无信号
)

# 盘后异动信号
ts_zscore(subtract(after_hours_vwap_value, close), 20)
```

## 踩坑

- 新闻字段 NaN 极多（多数日没新闻）→ `trade_when` 比 raw rank 更合适
- `actual_eps_value` 等只在财报日有值 → 用 `last_diff_value` 或 `ts_backfill`
- 情绪分数已经标准化过，直接 rank 会丢信息 → 试着用 zscore 或 raw `if_else`
- 盘后字段对小盘股噪声极大

## 参考

- [[2020-daniel-hirshleifer-sun-behavioral-factors]] PEAD + FIN
- [[2017-stambaugh-yuan-mispricing-factors]] mispricing 中的 surprise
