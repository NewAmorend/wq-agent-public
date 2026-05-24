---
title: 期权隐含信号
type: concept
tags: [option, option8, option9, put-call, implied-vol, cookbook]
created: 2026-05-22
---

# 期权隐含信号

`option8`（64 字段，历史波动率）+ `option9`（74 字段，put/call、forward）。期权市场常常**领先**现货 1-5 个交易日。

## 经济直觉

- 期权波动率/skew 反映 informed traders 的预期
- Put/Call 极值是反向指标（put 极高 → 接下来反弹）
- Forward 价格 vs 现价 = 隐含远期回报

## 可用字段

### `option9`（put/call + forward）
- `call_breakeven_10` ~ `call_breakeven_1080` — call 各到期日隐含 breakeven
- 类似 `put_breakeven_*`、`put_call_ratio_*`、`forward_price_*`
- 时间跨度 10 / 20 / 30 / 60 / 90 / 120 / 150 / 180 / 270 / 360 / 540 / 720 / 1080 天

### `option8`（实现波动率，14 个时间窗）
- `historical_volatility_10` ~ `historical_volatility_180`

## 实现模板

```
# Put/Call 极值反向（短期均值回归）
reverse(ts_zscore(put_call_ratio_30, 60))

# 隐含波动率压缩 → 即将爆发（vol selling）
rank(ts_delta(historical_volatility_30, 20))

# IV/HV 差（隐含波动率溢价）
divide(historical_volatility_10, historical_volatility_60)

# 期权偏度反转（远期 breakeven vs 短期）
divide(call_breakeven_180, call_breakeven_30)

# 隐含上涨空间（forward / close）
rank(divide(call_breakeven_30, close))
```

## 踩坑

- 期权数据覆盖率有限（option9 = "2500+ US equities"），中小盘 NaN 多
- Put/call 比率在低位（<0.5）也常见噪声 → 用 zscore 而非 raw level
- 隐含波动率与已实现波动率分布差异大 → 不要直接 add，要先标准化
- 期权信号的最佳保留期很短（1-5 天），延迟太长信号衰减
