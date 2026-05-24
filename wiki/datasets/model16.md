---
title: model16 数据集
type: entity
tags:
- dataset
- model
- usa
sources:
- worldquantbrain-api
created: '2026-05-24'
dataset_id: model16
category: model
delay: 1
region: USA
universe: TOP3000
---

<!-- managed by wq-agent wiki import-wq; manual edits below -->

# Fundamental Scores

**ID**：`model16`　**Category**：model　**Region**：USA　**Universe**：TOP3000　**Delay**：1

## 描述

This dataset provides a comprehensive mapping between Bloomberg IDs (BBID) and Reuters Instrument Codes (RIC), facilitating cross-referencing of securities across two major financial data platforms. By enabling seamless integration of data from Bloomberg and Refinitiv, it helps analysts and portfolio managers ensure accurate security identification, streamline data aggregation, and reduce errors in multi-source research workflows. While not directly predictive of price movements, this mapping is essential for robust data management, enabling more reliable analysis and backtesting when combining datasets that use different security identifiers.

**字段数**：24

**已用 alpha 数**：5265

## 字段清单（24 项）

| id | type | description |
| --- | --- | --- |
| `analyst_revision_rank_derivative` | MATRIX | Daily-indicator variant of momentum capturing recent price moves and analyst estimate revisions |
| `cashflow_efficiency_rank_derivative` | MATRIX | Ranks stocks by their ability to generate cash flows and operational profitability |
| `composite_factor_score_derivative` | MATRIX | Momentum score based on analyst revisions; intraday variant |
| `earnings_certainty_rank_derivative` | MATRIX | Measures the sustainability and certainty of earnings quality |
| `fscore_bfl_growth` | MATRIX | Growth composite estimating expected medium-term growth potential (e.g., revenues, earnings); higher is better (0–100) |
| `fscore_bfl_momentum` | MATRIX | Composite momentum measure reflecting recent price dynamics and analyst estimate revisions to identify improving or d… |
| `fscore_bfl_profitability` | MATRIX | Profitability composite ranking firms by ability to generate cash flows and operational efficiency; higher is better … |
| `fscore_bfl_quality` | MATRIX | Composite measuring earnings quality, stability, and balance-sheet resilience |
| `fscore_bfl_surface` | MATRIX | Static composite “style surface” score aggregating the five primary style scores; larger surface implies higher rank |
| `fscore_bfl_surface_accel` | MATRIX | Acceleration (derivative) of the pentagon surface score relative to the previous month |
| `fscore_bfl_total` | MATRIX | Blended composite M-Score combining the static pentagon surface score and its acceleration into an overarching rating |
| `fscore_bfl_value` | MATRIX | Valuation composite indicating how under- or overpriced a stock is versus common valuation measures; higher is better… |
| `fscore_growth` | MATRIX | Composite measuring the stock’s expected medium-term growth potential |
| `fscore_momentum` | MATRIX | Composite momentum metric focused on recent analyst estimate revisions to identify stocks experiencing upward or down… |
| `fscore_profitability` | MATRIX | Composite ranking stocks by their ability to generate cash flows and operational profitability |
| `fscore_quality` | MATRIX | Composite measuring the sustainability and certainty of earnings |
| `fscore_surface` | MATRIX | Static overall “style surface” score combining Value, Growth, Profitability, Momentum, and Quality; larger surface im… |
| `fscore_surface_accel` | MATRIX | Acceleration (derivative) of the pentagon surface score, indicating whether the overall style surface is rising or fa… |
| `fscore_total` | MATRIX | Final blended score that combines the static pentagon surface score with its acceleration |
| `fscore_value` | MATRIX | Composite assessing whether the stock is under- or overpriced using standard valuation measures (e.g., multiples) |
| `growth_potential_rank_derivative` | MATRIX | Composite growth score qualifying the stock’s expected medium‑term growth potential |
| `multi_factor_acceleration_score_derivative` | MATRIX | Change in the acceleration of multi-factor score compared to previous period. |
| `multi_factor_static_score_derivative` | MATRIX | Change in static multi-factor score compared to previous period. |
| `relative_valuation_rank_derivative` | MATRIX | Assesses whether the stock is under or overpriced based on standard valuation multiples indicator variant |

## 用法提示（人工补充）

- TODO：典型组合方式、相关的 concept 页面
