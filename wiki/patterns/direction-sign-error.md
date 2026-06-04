---
title: 信号方向错误
type: pattern
tags: [pattern, sign, direction, validation]
created: 2026-06-03
---

# 信号方向错误

## 症状

Fitness 为负或接近通过线但方向反；加了合理字段后表现变差，`reverse()` 后反而变好。

## 常见原因

- 基本面字段的经济含义和预期相反，例如资产扩张、债务上升通常不是正质量信号。
- 短期收益更像反转，中期收益更像动量。
- 分析师修正和价格反应同时出现，价格已提前反映。

## 修复处方

- 每个字段先写清“高值意味着买入还是卖出”。
- 对不确定方向的基本面比率，固定做正反两版比较。
- 用 [[rank]] 后再 [[reverse]]，避免尺度差异影响方向判断。
- 对事件类信号加入价格反应过滤，避免追涨。

## 相关

[[debt]]、[[assets]]、[[returns]]、[[factor-construction-best-practices]]
