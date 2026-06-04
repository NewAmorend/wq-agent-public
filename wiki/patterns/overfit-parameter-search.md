---
title: 参数搜索过拟合
type: pattern
tags: [pattern, overfit, parameter-search, validation]
created: 2026-06-03
---

# 参数搜索过拟合

## 症状

某一组窗口和 decay 在单一 region/universe 上非常好，但换 universe、delay 或轻微改参数后指标迅速下降。

## 常见原因

- 没有经济叙事，直接围绕 Fitness 调窗口。
- 同一信号尝试过多参数，没有记录失败样本。
- 使用极短窗口或非常尖锐的条件门控。

## 修复处方

- 先确定假设，再只测试少量有解释的窗口。
- 将成功和失败都沉淀到 `lessons/` / `entries/`，避免幸存者偏差。
- 对同一 recipe 做跨 region/universe 稳定性检查。
- 如果只靠一个 magic number 通过，优先降级为待观察，不进入提交候选。

## 相关

[[2016-harvey-liu-zhu-cross-section]]、[[factor-construction-best-practices]]
