---
title: news18 数据集
type: entity
tags:
- dataset
- news
- usa
sources:
- worldquantbrain-api
created: '2026-05-24'
dataset_id: news18
category: news
delay: 1
region: USA
universe: TOP3000
---

<!-- managed by wq-agent wiki import-wq; manual edits below -->

# Ravenpack News Data

**ID**：`news18`　**Category**：news　**Region**：USA　**Universe**：TOP3000　**Delay**：1

## 描述

This dataset provides structured analytics derived from global news sources, focusing on sentiment, event detection, and entity relevance for financial markets. It includes granular sentiment scores for specific events and entities, measures of event novelty and relevance, and a comprehensive taxonomy for classifying news events. The data covers a wide range of entities such as companies, products, people, and macroeconomic factors, and is enriched with metadata like event timing, fact level, and source trustworthiness. By quantifying the tone and impact of news stories, this dataset enables investors and researchers to systematically monitor market sentiment, identify significant events, and generate predictive signals for price movements, making it a valuable tool for quantitative trading, risk management, and alpha generation.

**字段数**：121

**已用 alpha 数**：43967

## 字段清单（121 项）

| id | type | description |
| --- | --- | --- |
| `composite_sentiment_score_2` | VECTOR | A combined sentiment score for a news story using multiple analysis techniques. |
| `corporate_action_sentiment` | VECTOR | A sentiment score for news stories about corporate action announcements. |
| `earnings_evaluation_sentiment` | VECTOR | A sentiment score for news stories about earnings evaluations. |
| `editorial_commentary_sentiment_2` | VECTOR | A sentiment score for short commentary and editorials on equity markets. |
| `entity_country_iso_code_4` | VECTOR | The two-letter ISO code representing the country associated with the entity. |
| `equity_sentiment_score` | VECTOR | A sentiment score indicating the tone of news about global equities. |
| `event_end_date_utc` | VECTOR | The UTC date when the event concludes. |
| `event_end_date_utc_fast_d1` | VECTOR | The UTC date when the event concludes. |
| `event_end_time_utc` | VECTOR | The UTC timestamp when the event concludes. |
| `event_novelty_score_2` | VECTOR | A score indicating how new or unique a news event is within a 24-hour window. |
| `event_sentiment_score` | VECTOR | A granular score representing the sentiment of a news event. |
| `event_start_date_utc` | VECTOR | The UTC date when the event begins. |
| `event_start_time_utc` | VECTOR | The UTC timestamp when the event begins. |
| `event_start_time_utc_fast_d1` | VECTOR | The UTC timestamp when the event begins. |
| `global_event_novelty_score_2` | VECTOR | A score indicating how novel an event is across all news providers within a 24-hour window. |
| `global_novelty_chain_elapsed_ms` | VECTOR | Milliseconds elapsed between the first and current event in a global novelty chain. |
| `mean_composite_sentiment_score` | MATRIX | The average composite sentiment score for news stories. |
| `mean_corporate_action_sentiment` | MATRIX | The average sentiment score for news about corporate action announcements. |
| `mean_earnings_evaluation_sentiment` | MATRIX | The average sentiment score for earnings evaluation news stories. |
| `mean_editorial_commentary_sentiment` | MATRIX | The average sentiment score for editorials and commentary on equity markets. |
| `mean_entity_relevance_score` | MATRIX | The average relevance score indicating how central an entity is to news stories. |
| `mean_equity_sentiment_score` | MATRIX | The average sentiment score for news about global equities. |
| `mean_event_novelty_score` | MATRIX | The average novelty score for events over a specified period. |
| `mean_event_sentiment_score` | MATRIX | The average sentiment score for events over a specified period. |
| `mean_merger_acquisition_sentiment` | MATRIX | The average sentiment score for news about mergers, acquisitions, and takeovers. |
| `mean_news_impact_projection` | MATRIX | The average projected market impact score for news flashes. |
| `merger_acquisition_sentiment` | VECTOR | A sentiment score for news stories about mergers, acquisitions, and takeovers. |
| `news_impact_projection_score` | VECTOR | A score representing the projected market impact of a news flash. |
| `novelty_chain_elapsed_ms` | VECTOR | Milliseconds elapsed between the first and current event in a novelty chain. |
| `nws18_acb` | VECTOR | News sentiment specializing in corporate action announcements |
| `nws18_bam` | VECTOR | Mergers and acquisitions sentiment indicator (e.g., -1 negative, 0 neutral, +1 positive) |
| `nws18_bam_fast_d1` | VECTOR | Mergers and acquisitions sentiment indicator (e.g., -1 negative, 0 neutral, +1 positive) |
| `nws18_bee` | VECTOR | Earnings evaluation score indicating positive, neutral, or negative assessment (-1, 0, +1) |
| `nws18_bee_fast_d1` | VECTOR | Earnings evaluation score indicating positive, neutral, or negative assessment (-1, 0, +1) |
| `nws18_ber` | VECTOR | Earnings Release Indicator flag for earnings release events |
| `nws18_ber_fast_d1` | VECTOR | Earnings Release Indicator flag for earnings release events |
| `nws18_event_relevance` | VECTOR | Integer from 0 to 100 indicating the event’s relevance within the story |
| `nws18_event_relevance_fast_d1` | VECTOR | Integer from 0 to 100 indicating the event’s relevance within the story |
| `nws18_event_similarity_days` | VECTOR | Number of days since a similar event was last detected within the past 365 days, up to 5 decimals |
| `nws18_ghc_lna` | VECTOR | Change in analyst recommendation |
| `nws18_nip` | VECTOR | Narrative impact score in [-1, 1] estimating the news item’s short-term market impact (e.g., next two hours) |
| `nws18_qcm` | VECTOR | News sentiment of relevant news with high confidence |
| `nws18_qep` | VECTOR | Equities sentiment polarity score derived from positive/negative words in news (typically -1, 0, +1) |
| `nws18_qep_fast_d1` | VECTOR | Equities sentiment polarity score derived from positive/negative words in news (typically -1, 0, +1) |
| `nws18_qmb` | VECTOR | Editorials and commentary score indicating stance or sentiment (-1, 0, +1) |
| `nws18_qmb_fast_d1` | VECTOR | Editorials and commentary score indicating stance or sentiment (-1, 0, +1) |
| `nws18_relevance` | VECTOR | Score from 0 to 100 indicating how strongly the entity is related to the story higher is more relevant |
| `nws18_relevance_fast_d1` | VECTOR | Score from 0 to 100 indicating how strongly the entity is related to the story higher is more relevant |
| `nws18_ssc` | VECTOR | Granular sentiment score from -1.00 to +1.00 for the story, combining multiple sentiment analysis techniques |
| `nws18_ssc_fast_d1` | VECTOR | Granular sentiment score from -1.00 to +1.00 for the story, combining multiple sentiment analysis techniques |
| `nws18_sse` | VECTOR | Continuous sentiment score between -1.00 and +1.00 for the entity-event |
| `reporting_period_end_date_utc` | VECTOR | The UTC date marking the end of the reporting period for the event. |
| `reporting_period_end_date_utc_fast_d1` | VECTOR | The UTC date marking the end of the reporting period for the event. |
| `reporting_period_end_time_utc` | VECTOR | The UTC timestamp marking the end of the reporting period for the event. |
| `reporting_period_end_time_utc_fast_d1` | VECTOR | The UTC timestamp marking the end of the reporting period for the event. |
| `reporting_period_start_date_utc` | VECTOR | The UTC date marking the beginning of the reporting period for the event. |
| `reporting_period_start_time_utc` | VECTOR | The UTC timestamp marking the beginning of the reporting period for the event. |
| `reporting_period_start_time_utc_fast_d1` | VECTOR | The UTC timestamp marking the beginning of the reporting period for the event. |
| `rp_css_assets` | MATRIX | Composite sentiment score of assets news |
| `rp_css_business` | MATRIX | Composite sentiment score of business-related news |
| `rp_css_credit` | MATRIX | Composite sentiment score of credit news |
| `rp_css_credit_ratings` | MATRIX | Composite sentiment score of credit ratings news |
| `rp_css_dividends` | MATRIX | Composite sentiment score of dividends news |
| `rp_css_earnings` | MATRIX | Composite sentiment score of earnings news |
| `rp_css_equity` | MATRIX | Composite sentiment score of equity action news |
| `rp_css_insider` | MATRIX | Composite sentiment score of insider trading news |
| `rp_css_inverstor` | MATRIX | Composite sentiment score of investor relations news |
| `rp_css_labor` | MATRIX | Composite sentiment score of labor issues news |
| `rp_css_legal` | MATRIX | Composite sentiment score of legal news |
| `rp_css_marketing` | MATRIX | Composite sentiment score of marketing news |
| `rp_css_mna` | MATRIX | Composite sentiment score of mergers and acquisitions-related news |
| `rp_css_partner` | MATRIX | Composite sentiment score of partnership news |
| `rp_css_price` | MATRIX | Composite sentiment score of stock price news |
| `rp_css_product` | MATRIX | Composite sentiment score of product and service-related news |
| `rp_css_ptg` | MATRIX | Composite sentiment score of price target news |
| `rp_css_ratings` | MATRIX | Composite sentiment score of analyst ratings-related news |
| `rp_css_revenue` | MATRIX | Composite sentiment score of revenue news |
| `rp_css_society` | MATRIX | Composite sentiment score of society-related news |
| `rp_css_technical` | MATRIX | Composite sentiment score based on technical analysis |
| `rp_ess_assets` | MATRIX | Event sentiment score of assets news |
| `rp_ess_business` | MATRIX | Event sentiment score of business-related news |
| `rp_ess_credit` | MATRIX | Event sentiment score of credit news |
| `rp_ess_credit_ratings` | MATRIX | Event sentiment score of credit ratings news |
| `rp_ess_dividends` | MATRIX | Event sentiment score of dividends news |
| `rp_ess_earnings` | MATRIX | Event sentiment score of earnings news |
| `rp_ess_equity` | MATRIX | Event sentiment score of equity action news |
| `rp_ess_insider` | MATRIX | Event sentiment score of insider trading news |
| `rp_ess_labor` | MATRIX | Event sentiment score of labor issues news |
| `rp_ess_legal` | MATRIX | Event sentiment score of legal news |
| `rp_ess_mna` | MATRIX | Event sentiment score of mergers and acquisitions-related news |
| `rp_ess_partner` | MATRIX | Event sentiment score of partnership news |
| `rp_ess_price` | MATRIX | Event sentiment score of stock price news |
| `rp_ess_product` | MATRIX | Event sentiment score of product and service-related news |
| `rp_ess_ptg` | MATRIX | Event sentiment score of price target news |
| `rp_ess_ratings` | MATRIX | Event sentiment score of analyst ratings-related news |
| `rp_ess_revenue` | MATRIX | Event sentiment score of revenue news |
| `rp_ess_society` | MATRIX | Event sentiment score of society-related news |
| `rp_ess_technical` | MATRIX | Event sentiment score based on technical analysis |
| `rp_nip_assets` | MATRIX | News impact projection of assets news |
| `rp_nip_business` | MATRIX | News impact projection of business-related news |
| `rp_nip_credit` | MATRIX | News impact projection of credit news |
| `rp_nip_credit_ratings` | MATRIX | News impact projection of credit ratings news |
| `rp_nip_dividends` | MATRIX | News impact projection of dividends news |
| `rp_nip_earnings` | MATRIX | News impact projection of earnings news |
| `rp_nip_equity` | MATRIX | News impact projection of equity action news |
| `rp_nip_insider` | MATRIX | News impact projection of insider trading news |
| `rp_nip_inverstor` | MATRIX | News impact projection of investor relations news |
| `rp_nip_labor` | MATRIX | News impact projection of labor issues news |
| `rp_nip_legal` | MATRIX | News impact projection of legal news |
| `rp_nip_marketing` | MATRIX | News impact projection of marketing news |
| `rp_nip_mna` | MATRIX | News impact projection of mergers and acquisitions-related news |
| `rp_nip_partner` | MATRIX | News impact projection of partnership news |
| `rp_nip_price` | MATRIX | News impact projection of stock price news |
| `rp_nip_product` | MATRIX | News impact projection of product and service-related news |
| `rp_nip_ptg` | MATRIX | News impact projection of price target news |
| `rp_nip_ratings` | MATRIX | News impact projection of analyst ratings-related news |
| `rp_nip_revenue` | MATRIX | News impact projection of revenue news |
| `rp_nip_society` | MATRIX | News impact projection of society-related news |
| `rp_nip_technical` | MATRIX | News impact projection based on technical analysis |
| `story_event_record_count` | VECTOR | The total number of event records published for a news story. |
| `story_event_record_count_fast_d1` | VECTOR | The total number of event records published for a news story. |

## 用法提示（人工补充）

- TODO：典型组合方式、相关的 concept 页面
