---
title: sentiment1 数据集
type: entity
tags:
- dataset
- sentiment
- usa
sources:
- worldquantbrain-api
created: '2026-05-24'
dataset_id: sentiment1
category: sentiment
delay: 1
region: USA
universe: TOP3000
---

<!-- managed by wq-agent wiki import-wq; manual edits below -->

# Research Sentiment Data

**ID**：`sentiment1`　**Category**：sentiment　**Region**：USA　**Universe**：TOP3000　**Delay**：1

## 描述

This dataset provides weekly sentiment scores for a broad range of assets including commodities, foreign exchange, indices, and equities. The sentiment scores are derived from a composite of 23 factors grouped into five categories: company, analyst, fundamental, price, and market sentiment. Covering the S&P 1500 and a multi-cap universe, the dataset offers both individual stock and aggregate market sentiment indicators. These measures can help identify overbought or oversold conditions, offering valuable insights for predicting potential price movements and market turning points.

**字段数**：19

**已用 alpha 数**：12597

## 字段清单（19 项）

| id | type | description |
| --- | --- | --- |
| `daily_equity_mood_indicator` | MATRIX | A daily composite value representing the sentiment level for an equity. |
| `snt1_cored1_score` | MATRIX | Proprietary composite analyst score; bearish if < 5, bullish if > 5, neutral if between -5 and 5 |
| `snt1_d1_analystcoverage` | MATRIX | Number of analysts providing an earnings estimate for the stock |
| `snt1_d1_buyrecpercent` | MATRIX | Percentage of analysts recommending a buy, calculated as (# of analysts recommending buy) / (# of all analysts) |
| `snt1_d1_downtargetpercent` | MATRIX | Percent of analysts who have lowered their price target recently, out of all analysts covering the stock |
| `snt1_d1_dtstsespe` | MATRIX | Standard deviation (dispersion) among analysts' earnings estimates for the next fiscal year |
| `snt1_d1_dynamicfocusrank` | MATRIX | Composite rank (0-100) emphasizing dynamic, short-term analyst sentiment signals; higher values indicate stronger buy… |
| `snt1_d1_earningsrevision` | MATRIX | One-month change in the mean (average) analyst earnings estimate divided by the stock price |
| `snt1_d1_earningssurprise` | MATRIX | Difference between actual reported earnings and expected earnings (consensus), divided by share price |
| `snt1_d1_earningstorpedo` | MATRIX | Difference between expected (FY1) earnings and previous four quarters' actual earnings divided by price; flags possib… |
| `snt1_d1_fundamentalfocusrank` | MATRIX | Rank (0-100) emphasizing longer-term, fundamental/value metrics; higher values for buy signal, lower for sell signal |
| `snt1_d1_longtermepsgrowthest` | MATRIX | Median expected long-term (3-5 years) growth rate in operating earnings as forecasted by analysts |
| `snt1_d1_netearningsrevision` | MATRIX | Net percentage of analysts raising minus lowering earnings estimates, out of total analysts covering the stock |
| `snt1_d1_netrecpercent` | MATRIX | Percentage difference between analysts recommending buy and those recommending sell, divided by total number of analysts |
| `snt1_d1_nettargetpercent` | MATRIX | Net percentage of analysts raising minus lowering price targets, divided by total number of analysts |
| `snt1_d1_sellrecpercent` | MATRIX | Percentage of analysts recommending a sell, calculated as (# of analysts recommending sell) / (# of all analysts) |
| `snt1_d1_stockrank` | MATRIX | Rank (0-100) based on equity-style factors, where higher values reflect a stronger buy signal and lower values a sell… |
| `snt1_d1_uptargetpercent` | MATRIX | Percent of analysts who have increased their price target recently, out of all analysts covering the stock |
| `weekly_equity_mood_index` | MATRIX | A weekly composite score reflecting market mood for individual equities. |

## 用法提示（人工补充）

- TODO：典型组合方式、相关的 concept 页面
