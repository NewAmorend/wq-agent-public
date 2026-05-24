---
title: 因子模型库（model 系列）
type: concept
tags: [model, model16, model51, model77, factor-library, meta, cookbook]
created: 2026-05-22
---

# 因子模型库（model 系列）

WQ Brain 提供三个预制因子库：`model16`、`model51`、`model77`（合计 4000+ 个预计算 alpha 信号）。每个字段本身就是一个 alpha 指标（如 `asset_growth_rate`、`book_leverage_ratio_3`），相当于 350+ 已发表因子的横截面排名。

## 经济直觉

**这是元因子（meta-factor）**：把别人验证过的信号当原始字段用，再做组合 / 中性化 / 时间序列变换。能极大提速研究 cycle。

## 代表字段（model77 中的 350+ 信号样本）

### Value 类
- `book_leverage_ratio_3`
- `asset_growth_rate`, `asset_growth_rate_sensitivityfactor`
- `cash_burn_rate`
- `capex_to_total_assets`, `capex_to_depreciation_linkage`

### Quality / Profitability
- `abnormal_return_earnings_release`

### Geo / Sector
- `asia_pacific_sales_exposure`

`model16` / `model51` 各自侧重不同：model16 偏 micro/short-horizon，model51 偏 macro/long-horizon。具体看 [[datasets/model77]] / [[datasets/model16]] / [[datasets/model51]] 的字段清单。

## 实现模板

```
# 直接用 model 信号 + rank（最简单也最稳）
rank(asset_growth_rate)

# Model 信号 + 时序动量（信号本身的 momentum）
rank(ts_delta(asset_growth_rate, 60))

# 两个 model 信号复合
add(
    rank(reverse(asset_growth_rate)),    # 资产扩张反向（[[2008-cooper-gulen-schill-asset-growth]]）
    rank(book_leverage_ratio_3)
)

# Model 信号 + PV1 价格动量组合
multiply(
    rank(asset_growth_rate),
    rank(ts_delta(close, 60))
)

# 行业中性化的 model 信号
group_neutralize(rank(asset_growth_rate), subindustry)
```

## 踩坑

- **Model 信号已经做过 cross-sectional normalize** → 再 `rank()` 是冗余的但不出错；直接用 raw 反而更准
- 不同 model 库间字段名重复（不同定义）→ 用 dataset 前缀避免歧义
- 多 model 信号叠加容易共线 → 用 [[2018-lopez-de-prado-hrp|HRP]] 风格而非等权
- 这套库本身就是 [[2016-harvey-liu-zhu-cross-section|factor zoo]] 警告的源头 —— 单一信号在 OS 期可能不复现，必须组合

## 参考

- [[2016-harvey-liu-zhu-cross-section]] factor zoo + multiple testing
- [[2019-hou-mo-xue-zhang-which-factors]] 65% 因子不可复现
- [[2018-lopez-de-prado-hrp]] HRP 多 alpha 合成
