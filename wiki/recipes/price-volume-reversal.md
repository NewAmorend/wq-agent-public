---
title: 价量反转 recipe
type: recipe
tags: [recipe, price-volume, reversal, turnover]
created: 2026-06-03
---

# 价量反转 recipe

## 适用假设

短期价格冲击如果缺少持续信息支持，随后容易均值回归；如果冲击伴随异常成交，既可能代表过度反应，也可能代表信息泄露，需要用窗口和方向区分。

## 推荐字段

- [[returns]]：直接表示短期价格冲击
- [[close]] / [[vwap]]：构造收盘偏离、价格位置
- [[volume]] / [[adv20]]：确认异常成交和流动性状态

## 基础表达式骨架

```text
reverse(rank(ts_sum(returns, 5)))

reverse(rank(ts_delta(close, 5)))

add(
  reverse(rank(ts_delta(close, 10))),
  rank(divide(volume, adv20))
)
```

## 稳定化步骤

1. 先对价格腿和成交量腿分别 `rank`。
2. 用 [[group_neutralize]] 去掉行业交易活跃度差异。
3. turnover 偏高时加 [[ts_decay_linear]] 或 [[hump]]。
4. 如果 self-correlation 高，加入非 PV 信息源，如 [[analyst-revisions]] 或 [[news-sentiment-events]]。

## 常见失败

- [[patterns/high-turnover]]：短窗口反转最常见。
- [[patterns/self-correlation-crowding]]：容易和已有价量 alpha 重复。
- [[patterns/direction-sign-error]]：5 日像反转，60-252 日可能变成动量。

## 相关

[[momentum-reversal-pv]]、[[liquidity-microstructure]]、[[recipes/turnover-control]]
