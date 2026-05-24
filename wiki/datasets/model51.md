---
title: model51 数据集
type: entity
tags:
- dataset
- model
- usa
sources:
- worldquantbrain-api
created: '2026-05-24'
dataset_id: model51
category: model
delay: 1
region: USA
universe: TOP3000
---

<!-- managed by wq-agent wiki import-wq; manual edits below -->

# Systematic Risk Metrics

**ID**：`model51`　**Category**：model　**Region**：USA　**Universe**：TOP3000　**Delay**：1

## 描述

This dataset provides a comprehensive suite of risk metrics for optionable US equities, including measures such as beta, correlation, systematic and unsystematic risk, and implied volatility across multiple future time horizons. By quantifying both market-wide and company-specific risks, the dataset enables investors and analysts to assess the sensitivity of individual stocks to broader market movements and to identify potential sources of volatility. These metrics are particularly valuable for constructing risk-aware portfolios, evaluating hedging strategies, and forecasting price movements based on changes in risk profiles. The daily updates and granular coverage make it a powerful tool for dynamic risk management and predictive modeling in equity markets.

**字段数**：16

**已用 alpha 数**：28990

## 字段清单（16 项）

| id | type | description |
| --- | --- | --- |
| `beta_last_30_days_spy` | MATRIX | The rolling beta value of the security relative to SPY, calculated via regression over the last 30 calendar days, rep… |
| `beta_last_360_days_spy` | MATRIX | The rolling beta value of the security relative to SPY, calculated via regression over the last 360 calendar days, re… |
| `beta_last_60_days_spy` | MATRIX | The rolling beta value of the security relative to SPY, calculated via regression over the last 60 calendar days, rep… |
| `beta_last_90_days_spy` | MATRIX | The rolling beta value of the security relative to SPY, calculated via regression over the last 90 calendar days, rep… |
| `correlation_last_30_days_spy` | MATRIX | The Pearson correlation coefficient of daily log returns between the security and SPY, calculated over the most recen… |
| `correlation_last_360_days_spy` | MATRIX | The Pearson correlation coefficient of daily log returns between the security and SPY, calculated over the most recen… |
| `correlation_last_60_days_spy` | MATRIX | The Pearson correlation coefficient of daily log returns between the security and SPY, calculated over the most recen… |
| `correlation_last_90_days_spy` | MATRIX | The Pearson correlation coefficient of daily log returns between the security and SPY, calculated over the most recen… |
| `systematic_risk_last_30_days` | MATRIX | The portion of the security’s return variance attributed to systematic (market) risk, quantified as R² from a regress… |
| `systematic_risk_last_360_days` | MATRIX | The portion of the security’s return variance attributed to systematic (market) risk, quantified as R² from a regress… |
| `systematic_risk_last_60_days` | MATRIX | The portion of the security’s return variance attributed to systematic (market) risk, quantified as R² from a regress… |
| `systematic_risk_last_90_days` | MATRIX | The portion of the security’s return variance attributed to systematic (market) risk, quantified as R² from a regress… |
| `unsystematic_risk_last_30_days` | MATRIX | The portion of return variance not explained by SPY (idiosyncratic risk), calculated as 1 minus R² over the last 30 c… |
| `unsystematic_risk_last_360_days` | MATRIX | The portion of return variance not explained by SPY (idiosyncratic risk), calculated as 1 minus R² over the last 360 … |
| `unsystematic_risk_last_60_days` | MATRIX | The portion of return variance not explained by SPY (idiosyncratic risk), calculated as 1 minus R² over the last 60 c… |
| `unsystematic_risk_last_90_days` | MATRIX | The portion of return variance not explained by SPY (idiosyncratic risk), calculated as 1 minus R² over the last 90 c… |

## 用法提示（人工补充）

- TODO：典型组合方式、相关的 concept 页面
