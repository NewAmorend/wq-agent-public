---
title: ts_arg_min 算子
type: operator
tags:
- operator
- time_series
sources:
- worldquantbrain-api
created: '2026-05-24'
operator_name: ts_arg_min
category: Time Series
operator_type: SCALAR
---

<!-- managed by wq-agent wiki import-wq; manual edits below -->

# `ts_arg_min`

**Category**：Time Series　**Type**：SCALAR

## 签名

```
ts_arg_min(x, d)
```

## 官方说明

Returns the number of days since the minimum value occurred in a time series over the past d days. If today's value is the minimum, returns 0; if it was yesterday, returns 1, and so on.

## 使用提示（人工补充）

- TODO：典型适用场景、常配合的算子（如需互链，请填写真实页面名）、参数范围、踩坑
