---
title: socialmedia8 数据集
type: entity
tags:
- dataset
- socialmedia
- usa
sources:
- worldquantbrain-api
created: '2026-05-24'
dataset_id: socialmedia8
category: socialmedia
delay: 1
region: USA
universe: TOP3000
---

<!-- managed by wq-agent wiki import-wq; manual edits below -->

# Social Media Data for Equity

**ID**：`socialmedia8`　**Category**：socialmedia　**Region**：USA　**Universe**：TOP3000　**Delay**：1

## 描述

This dataset provides quantitative sentiment metrics for US equities based on Twitter messages, covering the Russell 3000 universe since December 2011. It includes a suite of S-Factors such as S-Score (normalized sentiment), S-Volume (tweet volume), S-Dispersion (source diversity), S-Buzz (abnormal activity), and S-Delta (sentiment trend), all calculated using both unweighted and exponentially weighted methods. The methodology incorporates a 20-day lookback window to smooth signals for stocks with sparse tweet activity, reducing noise and spurious spikes. These metrics are updated at minute-level granularity and can be used to identify sentiment-driven price movements, forecast short-term returns, detect market events, and enhance quantitative trading strategies by providing real-time and historical sentiment signals.

**字段数**：4

**已用 alpha 数**：9521

## 字段清单（4 项）

| id | type | description |
| --- | --- | --- |
| `snt_social_value` | MATRIX | Z-score of sentiment |
| `snt_social_value_fast_d1` | MATRIX | Z-score of sentiment |
| `snt_social_volume` | MATRIX | Normalized tweet volume |
| `snt_social_volume_fast_d1` | MATRIX | Normalized tweet volume |

## 用法提示（人工补充）

- TODO：典型组合方式、相关的 concept 页面
