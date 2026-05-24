---
title: 动量与反转（基于 PV 数据）
type: concept
tags: [momentum, reversal, pv1, price, volume, cookbook]
created: 2026-05-22
---

# 动量与反转（基于 pv1）

`pv1` 是 WQ Brain 上**最常用的数据集**（1.6M alpha 用过）。所有时间尺度的价格/成交量信号都从这里来。

## 经济直觉

- **中期动量**（21-252 日）：投资者反应不足 + 机构追涨 → [[1993-jegadeesh-titman-returns-to-buying-winners]]
- **短期反转**（1-5 日）：流动性提供者补偿、噪声交易 → [[1990-lo-mackinlay-contrarian-profits]]
- **长期反转**（3-5 年）：过度反应衰退

## 可用字段（pv1，24 个全部）

| 字段 | 含义 |
| --- | --- |
| `close`, `open`, `high`, `low` | OHLC |
| `volume` | 日成交股数 |
| `returns` | 日收益率（已调整 split/div）|
| `cap` | 市值 |
| `adv20` | 20 日平均成交额 |
| `vwap` | 加权均价 |
| `dividend` | 当日分红金额 |
| `adjfactor` | 价格复权因子 |

## 实现模板

```
# 12-1 动量（经典 Jegadeesh-Titman）
rank(subtract(ts_delta(close, 252), ts_delta(close, 21)))

# 短期反转（1 周）
reverse(ts_zscore(returns, 5))

# 风险调整动量（除以波动）
rank(divide(ts_delta(close, 60), ts_std_dev(returns, 60)))

# 行业中性动量（避免行业 beta）
group_neutralize(
    rank(ts_delta(close, 60)),
    subindustry
)

# 量价背离（价涨量缩）
multiply(
    rank(ts_delta(close, 20)),
    reverse(rank(ts_delta(volume, 20)))
)
```

## 踩坑

- `delay=1` 下 d<5 的动量基本是噪声
- 直接用 `close` 不做 rank，价格量纲让大盘股主导 → **必须 rank**
- `ts_delta(close, d)` 对分红/拆股敏感，但 `returns` 已经处理过 → **优先 `returns`**
- 中国 / 新兴市场动量信号显著弱于美股 → 别盲用 USA 配方

## 参考

- [[1993-jegadeesh-titman-returns-to-buying-winners]] 中期动量
- [[1990-lo-mackinlay-contrarian-profits]] 短期反转
- [[2013-asness-moskowitz-pedersen-value-momentum-everywhere]] 全球验证
