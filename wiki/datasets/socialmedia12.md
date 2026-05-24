---
title: socialmedia12 数据集
type: entity
tags:
- dataset
- socialmedia
- usa
sources:
- worldquantbrain-api
created: '2026-05-24'
dataset_id: socialmedia12
category: socialmedia
delay: 1
region: USA
universe: TOP3000
---

<!-- managed by wq-agent wiki import-wq; manual edits below -->

# Sentiment Data for Equity

**ID**：`socialmedia12`　**Category**：socialmedia　**Region**：USA　**Universe**：TOP3000　**Delay**：1

## 描述

This dataset aggregates and analyzes social media posts and news articles related to financial markets, covering thousands of sources and several years of historical data. It quantifies market sentiment and buzz for individual assets, sectors, and indices using advanced natural language processing and machine learning techniques. The data includes sentiment scores, buzz indicators, and trading signals, which are statistically validated and can be used to identify shifts in market mood, anticipate volatility, and generate actionable buy/sell signals. By monitoring real-time and historical sentiment, traders and analysts can enhance their price movement predictions and improve portfolio performance through timely, data-driven decisions.

**字段数**：18

**已用 alpha 数**：47133

## 字段清单（18 项）

| id | type | description |
| --- | --- | --- |
| `scl12_alltype_buzzvec` | VECTOR | sentiment volume |
| `scl12_alltype_sentvec` | VECTOR | sentiment |
| `scl12_alltype_typevec` | VECTOR | instrument type index |
| `scl12_buzz` | MATRIX | relative sentiment volume |
| `scl12_buzz_fast_d1` | MATRIX | relative sentiment volume |
| `scl12_buzzvec` | VECTOR | Vector representing the volume of social media sentiment/mentions related to the instrument |
| `scl12_sentiment` | MATRIX | sentiment |
| `scl12_sentiment_fast_d1` | MATRIX | sentiment |
| `scl12_sentvec` | VECTOR | Vector representing the sentiment score (bullish/bearish/neutral) derived from social media data for the instrument |
| `scl12_typevec` | VECTOR | Vector containing the type indices identifying the categories of instruments in the dataset |
| `snt_buzz` | MATRIX | Negative relative sentiment volume measure for current day, with missing values filled as 0 |
| `snt_buzz_bfl` | MATRIX | Negative relative sentiment volume measure for current day, with missing values filled as 1 |
| `snt_buzz_bfl_fast_d1` | MATRIX | Negative relative sentiment volume measure for current day, with missing values filled as 1 |
| `snt_buzz_fast_d1` | MATRIX | Negative relative sentiment volume measure for current day, with missing values filled as 0 |
| `snt_buzz_ret` | MATRIX | negative return of relative sentiment volume |
| `snt_buzz_ret_fast_d1` | MATRIX | negative return of relative sentiment volume |
| `snt_value` | MATRIX | Negative sentiment score/indicator for current day, with missing values filled as 0 |
| `snt_value_fast_d1` | MATRIX | Negative sentiment score/indicator for current day, with missing values filled as 0 |

## 用法提示（人工补充）

- TODO：典型组合方式、相关的 concept 页面
