---
title: option9 数据集
type: entity
tags:
- dataset
- option
- usa
sources:
- worldquantbrain-api
created: '2026-05-24'
dataset_id: option9
category: option
delay: 1
region: USA
universe: TOP3000
---

<!-- managed by wq-agent wiki import-wq; manual edits below -->

# Options Analytics

**ID**：`option9`　**Category**：option　**Region**：USA　**Universe**：TOP3000　**Delay**：1

## 描述

This dataset provides comprehensive option-driven metrics for over 2,500 US equities, updated daily using end-of-day market data. It includes put/call ratios based on both trading volume and open interest across multiple future time horizons, forward prices, and breakeven levels for all, call, and put options. These metrics are calculated for constant terms ranging from 10 to 1,080 calendar days, offering granular insights into market sentiment, positioning, and expected price levels. By analyzing shifts in put/call ratios, forward prices, and breakeven points, traders and analysts can gauge investor sentiment, identify potential price inflection points, and enhance predictive models for equity price movements.

**字段数**：74

**已用 alpha 数**：51243

## 字段清单（74 项）

| id | type | description |
| --- | --- | --- |
| `call_breakeven_10` | MATRIX | Price at which a stock's call options with expiration 10 days in the future break even based on its recent bid/ask me… |
| `call_breakeven_1080` | MATRIX | Price at which a stock's call options with expiration 1080 days in the future break even based on its recent bid/ask … |
| `call_breakeven_120` | MATRIX | Price at which a stock's call options with expiration 120 days in the future break even based on its recent bid/ask m… |
| `call_breakeven_150` | MATRIX | Price at which a stock's call options with expiration 150 days in the future break even based on its recent bid/ask m… |
| `call_breakeven_180` | MATRIX | Open-interest-weighted mean breakeven price at which buyers of call options break even for options expiring in 180 days |
| `call_breakeven_20` | MATRIX | Open-interest-weighted average breakeven price of call options expiring in 20 days, representing the price at which c… |
| `call_breakeven_270` | MATRIX | Price at which a stock's call options with expiration 270 days in the future break even based on its recent bid/ask mean |
| `call_breakeven_30` | MATRIX | Open-interest-weighted average breakeven price of call options expiring in 30 days, representing the price at which c… |
| `call_breakeven_360` | MATRIX | Weighted mean break-even price of call options expiring in 360 days, based on recent bid/ask prices |
| `call_breakeven_60` | MATRIX | Open interest-weighted mean breakeven price for call options expiring in 60 days, showing average price at which call… |
| `call_breakeven_720` | MATRIX | Weighted mean breakeven price of call options expiring in 720 days indicating the price at which call buyers break even |
| `call_breakeven_90` | MATRIX | Price at which a stock's call options with expiration 90 days in the future break even based on its recent bid/ask mean |
| `forward_price_10` | MATRIX | Synthetic forward price for the underlying at 10 days derived from put-call parity using ATM options and adjusted for… |
| `forward_price_1080` | MATRIX | Synthetic forward price at 1080 days derived from at-the-money call and put option prices, reflecting market consensu… |
| `forward_price_120` | MATRIX | Synthetic forward price at 120 days derived from at-the-money call and put options reflecting the market's forward ex… |
| `forward_price_150` | MATRIX | Synthetic forward price at 150 days derived from at-the-money call and put options reflecting the market's forward ex… |
| `forward_price_180` | MATRIX | Synthetic forward price at 180 days derived from put-call parity using at-the-money calls and puts reflecting market … |
| `forward_price_20` | MATRIX | Synthetic forward price for the underlying at 20 days derived from put-call parity using ATM options and adjusted for… |
| `forward_price_270` | MATRIX | Synthetic forward price at 270 days expiry derived from ATM calls and puts reflecting the market-consensus forward ex… |
| `forward_price_30` | MATRIX | Synthetic forward price at 30 days expiry, derived from at-the-money call and put options, reflecting market consensu… |
| `forward_price_360` | MATRIX | Synthetic forward price at 360 days derived from put-call parity using ATM call and put prices, reflecting the market… |
| `forward_price_60` | MATRIX | Synthetic forward price at 60 days derived from at-the-money call and put options reflecting the market's forward exp… |
| `forward_price_720` | MATRIX | Synthetic forward price at 720 days derived from at-the-money call and put options reflecting the market's forward ex… |
| `forward_price_90` | MATRIX | Synthetic forward price at 90 days derived from put-call parity using ATM call and put prices, reflecting the market-… |
| `option_breakeven_10` | MATRIX | Open-interest-weighted mean breakeven price at which buyers of calls and puts combined break even for options expirin… |
| `option_breakeven_1080` | MATRIX | Open-interest-weighted mean breakeven price at which buyers of calls and puts combined break even for options expirin… |
| `option_breakeven_120` | MATRIX | Weighted mean breakeven price for combined call and put options with expiration 120 days in the future, based on rece… |
| `option_breakeven_150` | MATRIX | Price at which a stock's options with expiration 150 days in the future break even based on its recent bid/ask mean |
| `option_breakeven_180` | MATRIX | Weighted mean break-even price for combined call and put options expiring in 180 days, based on recent bid/ask prices |
| `option_breakeven_20` | MATRIX | Price at which a stock's options with expiration 20 days in the future break even based on its recent bid/ask mean |
| `option_breakeven_270` | MATRIX | The weighted mean price at which buyers of call and put options combined break even at 270 days to expiry based on re… |
| `option_breakeven_30` | MATRIX | Open-interest-weighted average breakeven price of all call and put options expiring in 30 days, representing the pric… |
| `option_breakeven_360` | MATRIX | Open-interest-weighted average breakeven price of all call and put options expiring in 360 days, representing the pri… |
| `option_breakeven_60` | MATRIX | The weighted mean price at which buyers of call and put options combined break even at 60 days to expiry based on rec… |
| `option_breakeven_720` | MATRIX | Price at which a stock's options with expiration 720 days in the future break even based on its recent bid/ask mean |
| `option_breakeven_90` | MATRIX | Open-interest-weighted mean breakeven price at which buyers of calls and puts combined break even for options expirin… |
| `pcr_oi_10` | MATRIX | Ratio of put open interest to call open interest for options expiring in 10 days, indicating short-term positioning |
| `pcr_oi_1080` | MATRIX | Ratio of put option open interest to call option open interest for stock options expiring in 1080 days, representing … |
| `pcr_oi_120` | MATRIX | Ratio of total put option open interest to total call option open interest for options expiring in 120 days, indicati… |
| `pcr_oi_150` | MATRIX | Ratio of total put option open interest to total call option open interest for options expiring in 150 days, indicati… |
| `pcr_oi_180` | MATRIX | Ratio of total put option open interest to call option open interest for options expiring in 180 days, representing l… |
| `pcr_oi_20` | MATRIX | Ratio of put open interest to call open interest on a stock's options with expiration 20 days in the future |
| `pcr_oi_270` | MATRIX | Ratio of put open interest to call open interest for options expiring in 270 days, indicating longer-term position skew |
| `pcr_oi_30` | MATRIX | Ratio of put open interest to call open interest for options expiring in 30 days, reflecting medium-term option posit… |
| `pcr_oi_360` | MATRIX | Ratio of total put option open interest to call option open interest for options expiring in 360 days |
| `pcr_oi_60` | MATRIX | Ratio of put open interest to call open interest for options expiring in 60 days, reflecting medium-to-long term opti… |
| `pcr_oi_720` | MATRIX | Ratio of put open interest to call open interest for options expiring in 720 days, indicating very long-term option s… |
| `pcr_oi_90` | MATRIX | Ratio of put open interest to call open interest for options expiring in 90 days, reflecting longer-term positioning |
| `pcr_oi_all` | MATRIX | Ratio of total put option open interest to call option open interest aggregated across all option maturities for the … |
| `pcr_vol_10` | MATRIX | Ratio of total put option volume to call option volume for options expiring in 10 days, reflecting very short-term se… |
| `pcr_vol_1080` | MATRIX | Ratio of put volume to call volume on a stock's options with expiration 1080 days in the future. |
| `pcr_vol_120` | MATRIX | Ratio of put options volume to call options volume for contracts expiring in 120 days on a stock's options |
| `pcr_vol_150` | MATRIX | Ratio of total put options volume to call options volume for options expiring in 150 days, reflecting short-term opti… |
| `pcr_vol_180` | MATRIX | Ratio of total put option volume to call option volume for options expiring in 180 days, capturing short-term options… |
| `pcr_vol_20` | MATRIX | Ratio of put option volume to call option volume for options expiring in 20 days, signaling short-term options flow s… |
| `pcr_vol_270` | MATRIX | Ratio of total put options volume to call options volume for contracts expiring 270 days in the future, indicating sh… |
| `pcr_vol_30` | MATRIX | Ratio of put volume to call volume on a stock's options with expiration 30 days in the future |
| `pcr_vol_360` | MATRIX | Ratio of put volume to call volume on a stock's options with expiration 360 days in the future |
| `pcr_vol_60` | MATRIX | Ratio of total put options volume to call options volume for contracts expiring 60 days in the future, indicating sho… |
| `pcr_vol_720` | MATRIX | Ratio of put options volume to call options volume for contracts expiring in 720 days on a stock's options |
| `pcr_vol_90` | MATRIX | Ratio of put options volume to call options volume for stock options expiring in 90 days, indicating short-term optio… |
| `pcr_vol_all` | MATRIX | Ratio of total put option volume to call option volume aggregated across all maturities, measuring short-term options… |
| `put_breakeven_10` | MATRIX | Open interest-weighted mean breakeven price for put options expiring in 10 days, average price at which put buyers br… |
| `put_breakeven_1080` | MATRIX | Price at which a stock's put options with expiration 1080 days in the future break even based on its recent bid/ask mean |
| `put_breakeven_120` | MATRIX | Price at which a stock's put options with expiration 120 days in the future break even based on its recent bid/ask mean |
| `put_breakeven_150` | MATRIX | Open-interest-weighted mean breakeven price at which buyers of put options break even for options expiring in 150 days |
| `put_breakeven_180` | MATRIX | Weighted mean breakeven price of put options expiring in 180 days derived from open interest or volume, indicating th… |
| `put_breakeven_20` | MATRIX | Price at which a stock's put options with expiration 20 days in the future break even based on its recent bid/ask mea… |
| `put_breakeven_270` | MATRIX | Weighted mean breakeven price of put options expiring in 270 days indicating the break even price for put buyers base… |
| `put_breakeven_30` | MATRIX | The weighted mean break-even price of put options expiring in 30 days based on recent bid/ask prices |
| `put_breakeven_360` | MATRIX | Open-interest-weighted mean breakeven price at which buyers of put options break even for options expiring in 360 days |
| `put_breakeven_60` | MATRIX | Price at which a stock's put options with expiration 60 days in the future break even based on its recent bid/ask mea… |
| `put_breakeven_720` | MATRIX | Weighted mean breakeven price of put options expiring in 720 days indicating the put buyers break-even price based on… |
| `put_breakeven_90` | MATRIX | Open-interest-weighted mean breakeven price at which buyers of put options break even for options expiring in 90 days |

## 用法提示（人工补充）

- TODO：典型组合方式、相关的 concept 页面
