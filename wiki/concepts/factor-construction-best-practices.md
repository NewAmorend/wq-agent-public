---
title: 因子构造最佳实践
type: concept
tags: [best-practice, methodology, neutralization, ranking, decay, cookbook]
created: 2026-05-22
---

# 因子构造最佳实践

不是 cookbook，是 **WQ Brain 上跑出可提交 alpha 的元规则**。每个新 alpha 设计前过一遍。

## 1. 数据预处理（先于任何信号）

| 问题 | 处方 |
| --- | --- |
| NaN | `ts_backfill(x, d, k=1)` 或 `to_nan(x, 0)` |
| 极端值 | `winsorize(x, std=4)` 或先 rank |
| 尺度差异 | `rank(x)` / `zscore(x)` / `scale(x)` |
| 时序非平稳 | `ts_zscore(x, 252)` 把绝对值转成"现在偏离过去多远" |

## 2. 信号方向与单调性

- **方向不确定时优先反向尝试**：很多基本面比率（debt/equity、asset growth）反向才有正 alpha
- **WQ checks 给的 fitness 是绝对值**：负 fitness 接近 0.5 意味着信号反了，加 `reverse()` 即可

## 3. 中性化（几乎所有 alpha 都该做）

```
group_neutralize(signal, subindustry)   # 行业中性（最常用）
group_neutralize(signal, sector)        # 更粗，保留行业内偏离
vector_neut(signal, market_return)      # 市场中性
```

行业中性可去掉行业 beta，让 sharpe 提升 0.1-0.3，**几乎是免费午餐**。

## 4. 衰减（控 turnover）

| 算子 | 用法 |
| --- | --- |
| `ts_decay_linear(x, d)` | 线性加权平均，最自然 |
| `ts_mean(x, d)` | 等权平滑 |
| `hump(x, hump=0.01)` | 限制单期变化幅度 |
| `jump_decay(x, d, sensitivity=0.5)` | 处理跳跃 |

WQ 要求 turnover ≤ 70%，长期信号常需要平滑才能落到该区间。

## 5. 复合：rank-then-add 是黄金法则

```
# 错：量纲完全不一致
add(eps_growth, returns_60d)

# 对：rank 后再 add，分布对齐
add(rank(eps_growth), rank(returns_60d))
```

## 6. 不同时间尺度匹配

| 信号类型 | 推荐窗口 |
| --- | --- |
| 短期反转 | 5-20 |
| 中期动量 | 60-252 |
| 长期反转 | 500-1000 |
| 波动率 | 252+ |
| 基本面 | 60-252 |

## 7. WQ 提交 checklist（[[factor-construction-best-practices|WQ 提交 checklist]] 同源）

- [ ] Fitness ≥ 1.0
- [ ] Sharpe ≥ 1.25
- [ ] Sub-universe Sharpe ≥ 0.67
- [ ] Turnover ∈ [1%, 70%]
- [ ] Weight 分布均匀
- [ ] 行业不集中

## 8. 警惕过拟合

- 不要为了 fitness 高在 USA 上调到 1.5+ 而后 CHN/EUR 跑出 -0.3
- 同一逻辑要 **多 region/universe/delay 都为正** 才可信
- 详见 [[2016-harvey-liu-zhu-cross-section]] 与 [[2019-hou-mo-xue-zhang-which-factors]]

## 9. 经济叙事先于参数

LLM 生成因子最大的陷阱是"参数搜索过拟合"。**先写明因子的经济直觉**（"低 GP/A 的公司质量差，长期跑输"），再翻译成表达式 —— 比反过来稳得多。
