---
title: option8 数据集
type: entity
tags:
- dataset
- option
- usa
sources:
- worldquantbrain-api
created: '2026-05-24'
dataset_id: option8
category: option
delay: 1
region: USA
universe: TOP3000
---

<!-- managed by wq-agent wiki import-wq; manual edits below -->

# Volatility Data

**ID**：`option8`　**Category**：option　**Region**：USA　**Universe**：TOP3000　**Delay**：1

## 描述

This dataset provides comprehensive daily volatility metrics for over 2,500 US equities, including both historical and option-implied volatilities across multiple time horizons. It features close-to-close and Parkinson historical volatility calculations, as well as at-the-money implied volatilities for calls, puts, and their averages, spanning durations from 10 to 1080 calendar days. Additionally, it includes skew steepness indicators to capture volatility asymmetries. By analyzing the interplay between historical and implied volatility, as well as volatility skew, traders and quantitative analysts can better anticipate price movements, identify periods of heightened risk, and develop options-based trading strategies that exploit volatility mispricings or forecast market direction.

**字段数**：64

**已用 alpha 数**：117679

## 字段清单（64 项）

| id | type | description |
| --- | --- | --- |
| `historical_volatility_10` | MATRIX | Historical close-to-close volatility for approximately 10 calendar days |
| `historical_volatility_120` | MATRIX | Historical close-to-close volatility for approximately 120 calendar days |
| `historical_volatility_150` | MATRIX | Historical close-to-close volatility for approximately 150 calendar days |
| `historical_volatility_180` | MATRIX | Historical close-to-close volatility for approximately 180 calendar days |
| `historical_volatility_20` | MATRIX | Historical close-to-close volatility for approximately 20 calendar days |
| `historical_volatility_30` | MATRIX | Historical close-to-close volatility for approximately 30 calendar days |
| `historical_volatility_60` | MATRIX | Historical close-to-close volatility for approximately 60 calendar days |
| `historical_volatility_90` | MATRIX | Historical close-to-close volatility for approximately 90 calendar days |
| `implied_volatility_call_10` | MATRIX | Implied volatility of the at-the-money call for the stock with an expiration 10 calendar days from the measurement date |
| `implied_volatility_call_1080` | MATRIX | Implied volatility of the at-the-money call for the stock with an expiration 1080 calendar days from the measurement … |
| `implied_volatility_call_120` | MATRIX | Implied volatility of the at-the-money call for the stock with an expiration 120 calendar days from the measurement date |
| `implied_volatility_call_150` | MATRIX | Implied volatility of the at-the-money call for the stock with an expiration 150 calendar days from the measurement date |
| `implied_volatility_call_180` | MATRIX | Implied volatility of the at-the-money call for the stock with an expiration 180 calendar days from the measurement date |
| `implied_volatility_call_20` | MATRIX | Implied volatility of the at-the-money call for the stock with an expiration 20 calendar days from the measurement date |
| `implied_volatility_call_270` | MATRIX | Implied volatility of the at-the-money call for the stock with an expiration 270 calendar days from the measurement date |
| `implied_volatility_call_30` | MATRIX | Implied volatility of the at-the-money call for the stock with an expiration 30 calendar days from the measurement date |
| `implied_volatility_call_360` | MATRIX | Implied volatility of the at-the-money call for the stock with an expiration 360 calendar days from the measurement date |
| `implied_volatility_call_60` | MATRIX | Implied volatility of the at-the-money call for the stock with an expiration 60 calendar days from the measurement date |
| `implied_volatility_call_720` | MATRIX | Implied volatility of the at-the-money call for the stock with an expiration 720 calendar days from the measurement date |
| `implied_volatility_call_90` | MATRIX | Implied volatility of the at-the-money call for the stock with an expiration 90 calendar days from the measurement date |
| `implied_volatility_mean_10` | MATRIX | The average of IvCall10 and IvPut10 |
| `implied_volatility_mean_1080` | MATRIX | The average of IvCall1080 and IvPut1080 |
| `implied_volatility_mean_120` | MATRIX | The average of IvCall120 and IvPut120 |
| `implied_volatility_mean_150` | MATRIX | The average of IvCall150 and IvPut150 |
| `implied_volatility_mean_180` | MATRIX | The average of IvCall180 and IvPut180 |
| `implied_volatility_mean_20` | MATRIX | The average of IvCall20 and IvPut20 |
| `implied_volatility_mean_270` | MATRIX | The average of IvCall270 and IvPut270 |
| `implied_volatility_mean_30` | MATRIX | The average of IvCall30 and IvPut30 |
| `implied_volatility_mean_360` | MATRIX | The average of IvCall360 and IvPut360 |
| `implied_volatility_mean_60` | MATRIX | The average of IvCall60 and IvPut60 |
| `implied_volatility_mean_720` | MATRIX | The average of IvCall720 and IvPut720 |
| `implied_volatility_mean_90` | MATRIX | The average of IvCall90 and IvPut90 |
| `implied_volatility_mean_skew_10` | MATRIX | Skew steepness for the implied volatility duration of 10 calendar days by subtracting the mean implied volatility of … |
| `implied_volatility_mean_skew_1080` | MATRIX | Skew steepness for the implied volatility duration of 1080 calendar days by subtracting the mean implied volatility o… |
| `implied_volatility_mean_skew_120` | MATRIX | Skew steepness for the implied volatility duration of 120 calendar days by subtracting the mean implied volatility of… |
| `implied_volatility_mean_skew_150` | MATRIX | Skew steepness for the implied volatility duration of 150 calendar days by subtracting the mean implied volatility of… |
| `implied_volatility_mean_skew_180` | MATRIX | Skew steepness for the implied volatility duration of 180 calendar days by subtracting the mean implied volatility of… |
| `implied_volatility_mean_skew_20` | MATRIX | Skew steepness for the implied volatility duration of 20 calendar days by subtracting the mean implied volatility of … |
| `implied_volatility_mean_skew_270` | MATRIX | Skew steepness for the implied volatility duration of 270 calendar days by subtracting the mean implied volatility of… |
| `implied_volatility_mean_skew_30` | MATRIX | Skew steepness for the implied volatility duration of 30 calendar days by subtracting the mean implied volatility of … |
| `implied_volatility_mean_skew_360` | MATRIX | Skew steepness for the implied volatility duration of 360 calendar days by subtracting the mean implied volatility of… |
| `implied_volatility_mean_skew_60` | MATRIX | Skew steepness for the implied volatility duration of 60 calendar days by subtracting the mean implied volatility of … |
| `implied_volatility_mean_skew_720` | MATRIX | Skew steepness for the implied volatility duration of 720 calendar days by subtracting the mean implied volatility of… |
| `implied_volatility_mean_skew_90` | MATRIX | Skew steepness for the implied volatility duration of 90 calendar days by subtracting the mean implied volatility of … |
| `implied_volatility_put_10` | MATRIX | At-the-money implied volatility of put options with 10 calendar days to expiration, annualized decimal |
| `implied_volatility_put_1080` | MATRIX | At-the-money implied volatility of put options with 1080 calendar days to expiration, annualized decimal |
| `implied_volatility_put_120` | MATRIX | At-the-money implied volatility of put options with 120 calendar days to expiration, annualized decimal |
| `implied_volatility_put_150` | MATRIX | At-the-money implied volatility of put options with 150 calendar days to expiration, annualized decimal |
| `implied_volatility_put_180` | MATRIX | At-the-money implied volatility of put options with 180 calendar days to expiration, annualized decimal |
| `implied_volatility_put_20` | MATRIX | At-the-money implied volatility of put options with 20 calendar days to expiration, annualized decimal |
| `implied_volatility_put_270` | MATRIX | Implied volatility of the at-the-money put for the stock with an expiration 270 calendar days from the measurement date |
| `implied_volatility_put_30` | MATRIX | Implied volatility of the at-the-money put for the stock with an expiration 30 calendar days from the measurement date |
| `implied_volatility_put_360` | MATRIX | Implied volatility of the at-the-money put for the stock with an expiration 360 calendar days from the measurement date |
| `implied_volatility_put_60` | MATRIX | Implied volatility of the at-the-money put for the stock with an expiration 60 calendar days from the measurement date |
| `implied_volatility_put_720` | MATRIX | Implied volatility of the at-the-money put for the stock with an expiration 720 calendar days from the measurement date |
| `implied_volatility_put_90` | MATRIX | Implied volatility of the at-the-money put for the stock with an expiration 90 calendar days from the measurement date |
| `parkinson_volatility_10` | MATRIX | Historical Parkinson volatility for approximately 10 calendar days |
| `parkinson_volatility_120` | MATRIX | Historical Parkinson volatility for approximately 120 calendar days |
| `parkinson_volatility_150` | MATRIX | Historical Parkinson volatility for approximately 150 calendar days |
| `parkinson_volatility_180` | MATRIX | Historical Parkinson volatility for approximately 180 calendar days |
| `parkinson_volatility_20` | MATRIX | Historical volatility using the Parkinson high–low estimator over approximately the past 20 calendar days |
| `parkinson_volatility_30` | MATRIX | Historical volatility using the Parkinson high–low estimator over approximately the past 30 calendar days |
| `parkinson_volatility_60` | MATRIX | Historical volatility using the Parkinson high–low estimator over approximately the past 60 calendar days |
| `parkinson_volatility_90` | MATRIX | Historical volatility using the Parkinson high–low estimator over approximately the past 90 calendar days |

## 用法提示（人工补充）

- TODO：典型组合方式、相关的 concept 页面
