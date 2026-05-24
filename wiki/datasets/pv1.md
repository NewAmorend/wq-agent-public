---
title: pv1 数据集
type: entity
tags:
- dataset
- pv
- usa
sources:
- worldquantbrain-api
created: '2026-05-24'
dataset_id: pv1
category: pv
delay: 1
region: USA
universe: TOP3000
---

<!-- managed by wq-agent wiki import-wq; manual edits below -->

# Price Volume Data for Equity

**ID**：`pv1`　**Category**：pv　**Region**：USA　**Universe**：TOP3000　**Delay**：1

## 描述

The dataset contains financial data related to equities, including metrics such as prices (open, high, low, close), trading volumes, market capitalization, returns, dividends, splits, and other key indicators that provide insights into stock performance and market activity.

**字段数**：24

**已用 alpha 数**：1634561

## 字段清单（24 项）

| id | type | description |
| --- | --- | --- |
| `adjfactor` | MATRIX | Adjustment factor applied to historical prices and dividends to account for splits and other corporate actions |
| `adv20` | MATRIX | Average daily volume in past 20 days |
| `cap` | MATRIX | Daily market capitalization (in millions) |
| `close` | MATRIX | Daily close price |
| `country` | GROUP | Country grouping |
| `currency` | GROUP | Currency |
| `cusip` | SYMBOL | CUSIP Value |
| `dividend` | MATRIX | Dividend |
| `exchange` | GROUP | Exchange grouping |
| `high` | MATRIX | Daily high price |
| `industry` | GROUP | Industry grouping |
| `isin` | SYMBOL | ISIN Value |
| `low` | MATRIX | Daily low price |
| `market` | GROUP | Market grouping |
| `open` | MATRIX | Daily open price |
| `returns` | MATRIX | Daily returns |
| `sector` | GROUP | Sector grouping |
| `sedol` | SYMBOL | Sedol |
| `sharesout` | MATRIX | Daily outstanding shares (in millions) |
| `split` | MATRIX | Stock split ratio |
| `subindustry` | GROUP | Subindustry grouping |
| `ticker` | SYMBOL | Ticker |
| `volume` | MATRIX | Daily volume |
| `vwap` | MATRIX | Daily volume weighted average price |

## 用法提示（人工补充）

- TODO：典型组合方式、相关的 concept 页面
