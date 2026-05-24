---
title: analyst4 数据集
type: entity
tags:
- analyst
- dataset
- usa
sources:
- worldquantbrain-api
created: '2026-05-24'
dataset_id: analyst4
category: analyst
delay: 1
region: USA
universe: TOP3000
---

<!-- managed by wq-agent wiki import-wq; manual edits below -->

# Analyst Estimate Data for Equity

**ID**：`analyst4`　**Category**：analyst　**Region**：USA　**Universe**：TOP3000　**Delay**：1

## 描述

This dataset provides intraday updates of consensus financial estimates, actuals, and company guidance for over 16,000 global companies, sourced from more than 800 contributing brokers. It includes multiple daily delta files per region, allowing users to track real-time changes in analyst expectations for key financial metrics such as EPS, sales, dividends, cash flow, and industry-specific items. The dataset also offers daily historical consensus timelines, enabling analysis of estimate revisions, surprises, and trends. By capturing the latest market sentiment and analyst forecasts, this data is highly valuable for predicting price movements, identifying earnings momentum, and responding to market-moving events as they unfold.

**字段数**：1324

**已用 alpha 数**：593140

## 字段清单（1324 项）

| id | type | description |
| --- | --- | --- |
| `actual_cashflow_per_share_value_quarterly` | MATRIX | Cash Flow Per Share - actual value for the quarter |
| `actual_dividend_value_quarterly` | MATRIX | Dividend - Actual value for the quarter |
| `actual_eps_value_quarterly` | MATRIX | Earnings Per Share (Income Statement/Per Share) (Actual) |
| `actual_sales_value_annual` | MATRIX | Sales - Actual Value |
| `actual_sales_value_quarterly` | MATRIX | Sales - Value in financial services income statement (in millions) |
| `actuals_reporting_currency` | VECTOR | Home currency of instrument |
| `actuals_value_currency_code` | MATRIX | Pricing Currency where the security trades |
| `adj_net_income_avg` | MATRIX | Average adjusted net profit, excluding non-recurring items, for the period. |
| `adj_net_income_median` | MATRIX | Median adjusted net profit, excluding non-recurring items, for the period. |
| `adj_net_income_stddev` | MATRIX | Standard deviation of adjusted net profit estimates, excluding non-recurring items. |
| `anl4_adjusted_netincome_ft` | MATRIX | Adjusted net income - forecast type (revision/new/...) |
| `anl4_ads1detailafv110_bk` | VECTOR | Broker name (int) |
| `anl4_ads1detailafv110_estvalue` | VECTOR | Estimation value |
| `anl4_ads1detailafv110_person` | VECTOR | Broker Id |
| `anl4_ads1detailafv110_prevval` | VECTOR | The Previous Estimation of Financial Item |
| `anl4_ads1detailqfv110_bk` | VECTOR | Broker name (int) |
| `anl4_ads1detailqfv110_estvalue` | VECTOR | Estimation value |
| `anl4_ads1detailqfv110_person` | VECTOR | Broker Id |
| `anl4_ads1detailqfv110_prevval` | VECTOR | The previous estimation of financial item |
| `anl4_adxqfv110_down` | VECTOR | Number of lower estimations |
| `anl4_adxqfv110_high` | VECTOR | The highest estimation |
| `anl4_adxqfv110_low` | VECTOR | The lowest estimation |
| `anl4_adxqfv110_mean` | VECTOR | Mean of estimations |
| `anl4_adxqfv110_median` | VECTOR | Median of estimations |
| `anl4_adxqfv110_numest` | VECTOR | The number of forecasts counted in aggregation |
| `anl4_adxqfv110_pu` | VECTOR | The number of upper estimations |
| `anl4_ady_down` | VECTOR | Number of lower estimations |
| `anl4_ady_high` | VECTOR | The highest estimation |
| `anl4_ady_low` | VECTOR | The lowest estimation |
| `anl4_ady_mean` | VECTOR | Mean of estimations |
| `anl4_ady_median` | VECTOR | Median of estimations |
| `anl4_ady_numest` | VECTOR | The number of forecasts counted in aggregation |
| `anl4_ady_pu` | VECTOR | The number of upper estimations |
| `anl4_af_cfps_value` | MATRIX | Cash Flow Per Share - Actual Value |
| `anl4_af_div_value` | MATRIX | Dividend - Actual value |
| `anl4_af_eps_value` | MATRIX | Earnings Per Share - Actual Value |
| `anl4_afv4_actual` | VECTOR | Announced financial data |
| `anl4_afv4_cfps_high` | MATRIX | Cash Flow Per Share - The highest estimation for the annual forecast |
| `anl4_afv4_cfps_low` | MATRIX | Cash Flow Per Share - The lowest estimation for the upcoming fiscal year |
| `anl4_afv4_cfps_mean` | MATRIX | Cash Flow Per Share - average of estimations for the annual frequency |
| `anl4_afv4_cfps_median` | MATRIX | Cash Flow Per Share - Median value among forecasts for the annual frequency |
| `anl4_afv4_cfps_number` | MATRIX | Cash Flow Per Share - number of estimations for annual frequency |
| `anl4_afv4_div_high` | MATRIX | Dividend per share - The highest estimation for the annual forecast. |
| `anl4_afv4_div_low` | MATRIX | Dividend - The lowest estimation for the annual forecast |
| `anl4_afv4_div_mean` | MATRIX | Dividend per share - average of estimations for annual frequency |
| `anl4_afv4_div_median` | MATRIX | Dividend per share - Median value among forecasts |
| `anl4_afv4_div_number` | MATRIX | Number of estimations for Dividend per share - annually |
| `anl4_afv4_div_std` | MATRIX | Dividend per share - standard deviation of estimations |
| `anl4_afv4_dts_spe` | MATRIX | Earnings per share - standard deviation of estimations |
| `anl4_afv4_eps_high` | MATRIX | Earnings per share - The highest estimation |
| `anl4_afv4_eps_low` | MATRIX | Earnings per share - The lowest estimation for annual frequency |
| `anl4_afv4_eps_mean` | MATRIX | Earnings per share - mean of estimations for annual frequency |
| `anl4_afv4_eps_number` | MATRIX | Earnings per share - number of estimations for annual frequency |
| `anl4_afv4_maxguidance` | VECTOR | Max guidance value |
| `anl4_afv4_median_eps` | MATRIX | Earnings per share - median of estimations |
| `anl4_afv4_minguidance` | VECTOR | Min guidance value |
| `anl4_bac1actualqfv110_actual` | VECTOR | Announced financial data |
| `anl4_bac1actualqfv110_item` | VECTOR | Financial item |
| `anl4_bac1conafv110_item` | VECTOR | Financial item |
| `anl4_bac1conltv110_item` | VECTOR | Financial item |
| `anl4_bac1conqfv110_item` | VECTOR | Financial item |
| `anl4_bac1conrecv110_item` | VECTOR | Financial item |
| `anl4_bac1detailafv110_item` | VECTOR | Financial item |
| `anl4_bac1detaillt_item` | VECTOR | Financial item |
| `anl4_bac1detailqfv110_item` | VECTOR | Financial item |
| `anl4_bac1detailrec_item` | VECTOR | Financial item |
| `anl4_basicafv4_actual` | VECTOR | Announced financial data for the annual period. |
| `anl4_basicconafv110_down` | VECTOR | Number of lower estimations |
| `anl4_basicconafv110_high` | VECTOR | The highest estimation |
| `anl4_basicconafv110_low` | VECTOR | The lowest estimation |
| `anl4_basicconafv110_mean` | VECTOR | Mean of estimations |
| `anl4_basicconafv110_median` | VECTOR | Median of estimations |
| `anl4_basicconafv110_numest` | VECTOR | The number of forecasts counted in aggregation |
| `anl4_basicconafv110_pu` | VECTOR | The number of upper estimations |
| `anl4_basicconltv110_down` | VECTOR | Number of lower estimations |
| `anl4_basicconltv110_high` | VECTOR | The highest estimation |
| `anl4_basicconltv110_low` | VECTOR | The lowest estimation |
| `anl4_basicconltv110_mean` | VECTOR | Mean of estimations |
| `anl4_basicconltv110_median` | VECTOR | Median of estimations |
| `anl4_basicconltv110_numest` | VECTOR | The number of forecasts counted in aggregation |
| `anl4_basicconltv110_pu` | VECTOR | The number of upper estimations |
| `anl4_basicconqfv110_down` | VECTOR | Number of lower estimations |
| `anl4_basicconqfv110_high` | VECTOR | The highest estimation |
| `anl4_basicconqfv110_low` | VECTOR | The lowest estimation |
| `anl4_basicconqfv110_mean` | VECTOR | Mean of estimations |
| `anl4_basicconqfv110_median` | VECTOR | Median of estimations |
| `anl4_basicconqfv110_numest` | VECTOR | The number of forecasts counted in aggregation |
| `anl4_basicconqfv110_pu` | VECTOR | The number of upper estimations |
| `anl4_basicdetaillt_bk` | VECTOR | Broker name (int) |
| `anl4_basicdetaillt_estvalue` | VECTOR | Estimation value |
| `anl4_basicdetaillt_person` | VECTOR | Broker Id |
| `anl4_basicdetaillt_prevval` | VECTOR | The Previous Estimation of Financial Item |
| `anl4_basicdetailqfv110_bk` | VECTOR | Broker name (int) |
| `anl4_basicdetailqfv110_estvalue` | VECTOR | Estimation value |
| `anl4_basicdetailqfv110_person` | VECTOR | Broker Id |
| `anl4_basicdetailqfv110_prevval` | VECTOR | The previous estimation of financial item |
| `anl4_basicdetailrec_bk` | VECTOR | Broker name (int) |
| `anl4_basicdetailrec_person` | VECTOR | Broker Id |
| `anl4_basicdetailrec_ratingvalue` | VECTOR | Score on the given instrument |
| `anl4_basicqfv4_actual` | VECTOR | Announced financial data |
| `anl4_basicqfv4_maxguidance` | VECTOR | Max guidance value |
| `anl4_basicqfv4_minguidance` | VECTOR | Min guidance value |
| `anl4_baz1v110_bk` | VECTOR | Broker name (int) |
| `anl4_baz1v110_estvalue` | VECTOR | Estimation value |
| `anl4_baz1v110_person` | VECTOR | Broker Id |
| `anl4_baz1v110_prevval` | VECTOR | The previous estimation of financial item |
| `anl4_buy` | VECTOR | The number of recommendations to long the instrument |
| `anl4_bvps_flag` | MATRIX | Book value per share - forecast type (revision/new/...) |
| `anl4_bvps_high` | MATRIX | Book value - the highest estimation, per share |
| `anl4_bvps_low` | MATRIX | Book value - the lowest estimation, per share |
| `anl4_bvps_mean` | MATRIX | Book value per share - average of estimations |
| `anl4_bvps_median` | MATRIX | Book value per share - Median value among forecasts |
| `anl4_bvps_number` | MATRIX | Book value per share - number of estimations |
| `anl4_bvps_value` | MATRIX | Book value per share - announced financial value |
| `anl4_capex_flag` | MATRIX | Capital Expenditures - forecast type (revision/new/...) |
| `anl4_capex_high` | MATRIX | Capital Expenditures - The highest estimation |
| `anl4_capex_low` | MATRIX | Capital Expenditures - The lowest estimation |
| `anl4_capex_mean` | MATRIX | Capital Expenditures - mean of estimations |
| `anl4_capex_number` | MATRIX | Capital Expenditures - number of estimations |
| `anl4_capex_std` | MATRIX | Capital Expenditures - standard deviation of estimations |
| `anl4_capex_value` | MATRIX | Capital Expenditures - announced financial value |
| `anl4_cff_flag` | MATRIX | Cash Flow From Financing Activities - forecast type (revision/new/...) |
| `anl4_cff_high` | MATRIX | Cash Flow From Financing - The highest of forecasted values |
| `anl4_cff_low` | MATRIX | Cash Flow From Financing - The lowest estimation |
| `anl4_cff_mean` | MATRIX | Cash Flow From Financing - mean of estimations |
| `anl4_cff_median` | MATRIX | Cash Flow From Financing Activities - Median value among forecasts |
| `anl4_cff_number` | MATRIX | Cash Flow From Financing - number of estimations |
| `anl4_cff_value` | MATRIX | Cash Flow From Financing - announced financial value |
| `anl4_cfi_flag` | MATRIX | Cash Flow From Investing - forecast type (revision/new/...) |
| `anl4_cfi_high` | MATRIX | Cash Flow From Investing - The highest estimation |
| `anl4_cfi_low` | MATRIX | Cash Flow From Investing - The lowest estimation |
| `anl4_cfi_mean` | MATRIX | Cash Flow From Investing - mean of estimations |
| `anl4_cfi_median` | MATRIX | Cash Flow From Investing - median of estimations |
| `anl4_cfi_number` | MATRIX | Cash Flow From Investing - number of estimations |
| `anl4_cfi_value` | MATRIX | Cash Flow From Investing - announced financial value |
| `anl4_cfo_flag` | MATRIX | Cash Flow From Operations - forecast type (revision/new/...) |
| `anl4_cfo_high` | MATRIX | Cash Flow From Operations - The highest value among forecasts |
| `anl4_cfo_low` | MATRIX | Cash Flow From Operations - The lowest estimation |
| `anl4_cfo_mean` | MATRIX | Cash Flow From Operations - mean of estimations |
| `anl4_cfo_median` | MATRIX | Cash Flow From Operations - median of estimations |
| `anl4_cfo_number` | MATRIX | Cash Flow From Operations - number of estimations |
| `anl4_cfo_value` | MATRIX | Cash Flow From Operations - announced financial value |
| `anl4_cuo1actualqfv110_actual` | VECTOR | Announced financial data |
| `anl4_cuo1actualqfv110_item` | VECTOR | Financial item |
| `anl4_cuo1conafv110_item` | VECTOR | Financial item |
| `anl4_cuo1conqfv110_item` | VECTOR | Financial item |
| `anl4_cuo1detailafv110_item` | VECTOR | Financial item |
| `anl4_cuo1detailqfv110_item` | VECTOR | Financial item |
| `anl4_cuo1guidaf_item` | VECTOR | Financial item |
| `anl4_cuo1guidaf_maxguidance` | VECTOR | Max guidance value |
| `anl4_cuo1guidaf_minguidance` | VECTOR | Minimum guidance value |
| `anl4_dei2laf_item` | VECTOR | Financial item |
| `anl4_dei2lqfv110_item` | VECTOR | Financial item |
| `anl4_dei3lafv110_item` | VECTOR | Financial item |
| `anl4_dei3lltv110_item` | VECTOR | Financial item |
| `anl4_dei3lqfv110_item` | VECTOR | Financial item |
| `anl4_dei3lrec_item` | VECTOR | Financial item |
| `anl4_detailltv4_est` | VECTOR | Long term estimation value |
| `anl4_detailltv4_preest` | VECTOR | The previous estimation of financial item |
| `anl4_detailltv4v104_est` | VECTOR | Estimation value |
| `anl4_detailltv4v104_preest` | VECTOR | The previous estimation of financial item |
| `anl4_detailrecv4_est` | VECTOR | Estimation value for recommendation detail |
| `anl4_detailrecv4v104_est` | VECTOR | Estimation value |
| `anl4_dez1afv4_est` | VECTOR | Estimation value |
| `anl4_dez1afv4_preest` | VECTOR | The previous estimation of finanicial item |
| `anl4_dez1basicafv4_est` | VECTOR | Estimation value |
| `anl4_dez1basicafv4_preest` | VECTOR | The previous estimation of finanicial item |
| `anl4_dez1basicafv4v104_est` | VECTOR | Estimation value |
| `anl4_dez1basicafv4v104_preest` | VECTOR | The previous estimation of financial item |
| `anl4_dez1basicqfv4_est` | VECTOR | Estimation value |
| `anl4_dez1basicqfv4_preest` | VECTOR | The previous estimation of finanicial item |
| `anl4_dez1basicqfv4v104_est` | VECTOR | Estimation value |
| `anl4_dez1basicqfv4v104_preest` | VECTOR | The previous estimation of financial item |
| `anl4_dez1qfv4_est` | VECTOR | Estimation value |
| `anl4_dez1qfv4_preest` | VECTOR | The previous estimation of finanicial item |
| `anl4_dez1safv4_est` | VECTOR | Estimation value |
| `anl4_dez1safv4_preest` | VECTOR | The previous estimation of finanicial item |
| `anl4_dts_ptp` | MATRIX | Pretax income - std of estimations |
| `anl4_dts_rspe` | MATRIX | Reported Earnings per share - standard deviation of estimations |
| `anl4_eaz1laf_bk` | VECTOR | Broker name (int) |
| `anl4_eaz1laf_estvalue` | VECTOR | Estimation value |
| `anl4_eaz1laf_person` | VECTOR | Broker Id |
| `anl4_eaz1laf_prevval` | VECTOR | The previous estimation of financial item |
| `anl4_eaz1lqfv110_bk` | VECTOR | Broker name (int) |
| `anl4_eaz1lqfv110_estvalue` | VECTOR | Estimation value |
| `anl4_eaz1lqfv110_person` | VECTOR | Broker Id |
| `anl4_eaz1lqfv110_prevval` | VECTOR | The previous estimation of financial item |
| `anl4_eaz2lafv110_bk` | VECTOR | Broker name (int) |
| `anl4_eaz2lafv110_estvalue` | VECTOR | Estimation value |
| `anl4_eaz2lafv110_person` | VECTOR | Broker Id |
| `anl4_eaz2lafv110_prevval` | VECTOR | The previous estimation of financial item |
| `anl4_eaz2lltv110_bk` | VECTOR | Broker name (int) |
| `anl4_eaz2lltv110_estvalue` | VECTOR | Estimation value |
| `anl4_eaz2lltv110_person` | VECTOR | Broker Id |
| `anl4_eaz2lltv110_prevval` | VECTOR | The previous estimation of financial item |
| `anl4_eaz2lqfv110_bk` | VECTOR | Broker name (int) |
| `anl4_eaz2lqfv110_estvalue` | VECTOR | Estimation value |
| `anl4_eaz2lqfv110_person` | VECTOR | Broker Id |
| `anl4_eaz2lqfv110_prevval` | VECTOR | The previous estimation of financial item |
| `anl4_eaz2lrec_bk` | VECTOR | Broker name (int) |
| `anl4_eaz2lrec_person` | VECTOR | Broker Id |
| `anl4_eaz2lrec_ratingvalue` | VECTOR | Score on the given instrument |
| `anl4_ebit_high` | MATRIX | Earnings before interest and taxes - The highest estimation |
| `anl4_ebit_low` | MATRIX | Earnings before interest and taxes - The lowest estimation |
| `anl4_ebit_mean` | MATRIX | Earnings before interest and taxes - mean of estimations |
| `anl4_ebit_median` | MATRIX | Earnings before interest and taxes - median of estimations |
| `anl4_ebit_number` | MATRIX | Earnings before interest and taxes - number of estimations |
| `anl4_ebit_std` | MATRIX | Earnings before interest and taxes - standard deviation of estimations |
| `anl4_ebit_value` | MATRIX | Earnings before interest and taxes - announced financial value |
| `anl4_ebitda_flag` | MATRIX | Earnings before interest, taxes, depreciation and amortization - forecast type (revision/new/...) |
| `anl4_ebitda_high` | MATRIX | Earnings before interest, taxes, depreciation, and amortization - the highest estimation |
| `anl4_ebitda_low` | MATRIX | Earnings before interest, taxes, depreciation and amortization - The lowest estimation |
| `anl4_ebitda_mean` | MATRIX | Earnings before interest, taxes, depreciation and amortization - mean of estimations |
| `anl4_ebitda_number` | MATRIX | Earnings before interest, taxes, depreciation and amortization - number of estimations |
| `anl4_ebitda_std` | MATRIX | Earnings before interest, taxes, depreciation, and amortization - standard deviation of estimations |
| `anl4_ebitda_value` | MATRIX | Earnings before interest, taxes, depreciation and amortization - announced financial value |
| `anl4_epsa_flag` | MATRIX | Earnings per share adjusted by excluding extraordinary items and stock option expenses - forecast type (revision/new/… |
| `anl4_epsr_flag` | MATRIX | GAAP Earnings - estimation type (revision/new/...), per share |
| `anl4_epsr_high` | MATRIX | GAAP Earnings per share - The highest estimation |
| `anl4_epsr_low` | MATRIX | GAAP Earnings per share - The lowest estimation |
| `anl4_epsr_mean` | MATRIX | GAAP Earnings per share - mean of estimations |
| `anl4_epsr_number` | MATRIX | GAAP Earnings per share - number of estimations |
| `anl4_epsr_value` | MATRIX | GAAP Earnings per share - announced financial value |
| `anl4_fcf_flag` | MATRIX | Free cash flow - forecast type (revision/new/...) |
| `anl4_fcf_high` | MATRIX | Free cash flow - aggregation on estimations, max |
| `anl4_fcf_low` | MATRIX | Free Cash Flow - The lowest estimation |
| `anl4_fcf_mean` | MATRIX | Free Cash Flow - mean of estimations |
| `anl4_fcf_median` | MATRIX | Free cash flow - aggregation on estimations, 50th percentile |
| `anl4_fcf_number` | MATRIX | Free Cash Flow - number of estimations |
| `anl4_fcf_value` | MATRIX | Free cash flow- announced financial value |
| `anl4_fcfps_flag` | MATRIX | Free cash flow per share - forecast type (revision/new/...) |
| `anl4_fcfps_high` | MATRIX | Free Cash Flow Per Share - the highest estimation |
| `anl4_fcfps_low` | MATRIX | Free Cash Flow Per Share - the lowest estimation |
| `anl4_fcfps_mean` | MATRIX | Free cash flow per share - mean of estimations |
| `anl4_fcfps_median` | MATRIX | Free cash flow - summary on estimations, 50th-percentile, per share |
| `anl4_fcfps_number` | MATRIX | Free Cash Flow per Share - number of estimations |
| `anl4_ffo_flag` | MATRIX | Funds from Operation - forecast type (revision/new/...) |
| `anl4_flag_erbfintax` | MATRIX | Earnings before interest and taxes - forecast type (revision/new/...) |
| `anl4_fs_actual_1qf_v4_nd_bvps_value` | MATRIX | Announced book value per share |
| `anl4_fs_actual_1qf_v4_nd_capex_value` | MATRIX | Announced value of capital expenditures |
| `anl4_fs_actual_1qf_v4_nd_cff_value` | MATRIX | Announced value of cash flow from financing |
| `anl4_fs_actual_1qf_v4_nd_cfi_value` | MATRIX | Cash Flow From Investing - announced financial value |
| `anl4_fs_actual_1qf_v4_nd_cfo_value` | MATRIX | Announced cash flow from operations |
| `anl4_fs_actual_1qf_v4_nd_ebit_value` | MATRIX | Announced value of earnings before interest and taxes (EBIT) |
| `anl4_fs_actual_1qf_v4_nd_ebitda_value` | MATRIX | Announced earnings before interest, taxes, depreciation, and amortization |
| `anl4_fs_actual_1qf_v4_nd_epsr_value` | MATRIX | GAAP Earnings per share - announced financial value |
| `anl4_fs_actual_1qf_v4_nd_fcf_value` | MATRIX | Announced value of free cash flow |
| `anl4_fs_actual_1qf_v4_nd_fcfps_value` | MATRIX | Free cash flow per share - announced financial value |
| `anl4_fs_actual_1qf_v4_nd_grossincome_value` | MATRIX | Announced value of gross income |
| `anl4_fs_actual_1qf_v4_nd_netdebt_value` | MATRIX | Announced value of net debt |
| `anl4_fs_actual_1qf_v4_nd_netprofit_value` | MATRIX | Announced net profit |
| `anl4_fs_actual_1qf_v4_nd_netprofita_value` | MATRIX | Announced value of adjusted net income |
| `anl4_fs_actual_1qf_v4_nd_ptp_value` | MATRIX | Announced value of pretax income |
| `anl4_fs_actual_1qf_v4_nd_ptpr_value` | MATRIX | Announced value of reported pretax income |
| `anl4_fs_actual_1qf_v4_nd_rd_exp_value` | MATRIX | Announced value of research and development expense |
| `anl4_fs_actual_1qf_v4_nd_sga_value` | MATRIX | Actual value for selling, general and administrative expense |
| `anl4_fs_actual_1qf_v4_nd_sh_equity_value` | MATRIX | Announced value of shareholders' equity |
| `anl4_fs_actual_1qf_v4_nd_totassets_value` | MATRIX | Actual value for total assets |
| `anl4_fs_actual_1qf_v4_nd_totgw_value` | MATRIX | Announced financial value for total goodwill |
| `anl4_fs_actual_af_v4_nd_actual` | VECTOR | Reported actual value for the financial item |
| `anl4_fs_actual_af_v4_nd_currency` | VECTOR | Home currency of the instrument in which the actual value is reported |
| `anl4_fs_actual_basic_af_v4_nd_actual` | VECTOR | Reported actual value of the financial item for the annual period |
| `anl4_fs_actual_basic_qf_v4_nd_actual` | VECTOR | Reported actual value for the item |
| `anl4_fs_actual_qf_v4_nd_actual` | VECTOR | Reported actual value for the specified item |
| `anl4_fs_actuals_advanced_af_nd_bvps_value` | MATRIX | Book value per share actual value |
| `anl4_fs_actuals_advanced_af_nd_capex_value` | MATRIX | Capital expenditures total value |
| `anl4_fs_actuals_advanced_af_nd_cff_value` | MATRIX | Cash flow from financing value |
| `anl4_fs_actuals_advanced_af_nd_cfi_value` | MATRIX | Cash flow from investing value |
| `anl4_fs_actuals_advanced_af_nd_cfo_value` | MATRIX | Cash flow from operations value for the annual period |
| `anl4_fs_actuals_advanced_af_nd_currency` | MATRIX | Pricing currency in which the security trades |
| `anl4_fs_actuals_advanced_af_nd_ebit_value` | MATRIX | Earnings before interest and taxes (EBIT) actual value |
| `anl4_fs_actuals_advanced_af_nd_ebitda_value` | MATRIX | EBITDA actual value for the annual period |
| `anl4_fs_actuals_advanced_af_nd_epsr_value` | MATRIX | Reported earnings per share actual value |
| `anl4_fs_actuals_advanced_af_nd_fcf_value` | MATRIX | Free cash flow actual value for the annual period |
| `anl4_fs_actuals_advanced_af_nd_fcfps_value` | MATRIX | Free cash flow per share actual value for the annual period |
| `anl4_fs_actuals_advanced_af_nd_grossincome_value` | MATRIX | Gross income actual value on an annual basis |
| `anl4_fs_actuals_advanced_af_nd_netdebt_value` | MATRIX | Net debt actual value for the annual period |
| `anl4_fs_actuals_advanced_af_nd_netprofit_value` | MATRIX | Net profit announced financial value for annual data |
| `anl4_fs_actuals_advanced_af_nd_netprofita_value` | MATRIX | Adjusted net income announced actual value for annual frequency |
| `anl4_fs_actuals_advanced_af_nd_ptp_value` | MATRIX | Pretax profit actual value for the annual period |
| `anl4_fs_actuals_advanced_af_nd_ptpr_value` | MATRIX | Reported pretax income (PTPR) actual value for the annual fiscal period |
| `anl4_fs_actuals_advanced_af_nd_rd_exp_value` | MATRIX | Research and Development expense actual value for the annual period |
| `anl4_fs_actuals_advanced_af_nd_sga_value` | MATRIX | Selling, General and Administrative expense actual value |
| `anl4_fs_actuals_advanced_af_nd_sh_equity_value` | MATRIX | Shareholders' equity total actual value |
| `anl4_fs_actuals_advanced_af_nd_totassets_value` | MATRIX | Total assets actual value |
| `anl4_fs_actuals_advanced_af_nd_totgw_value` | MATRIX | Total goodwill value |
| `anl4_fs_actuals_advanced_qf_nd_bvps_value` | MATRIX | Book value per share, actual value |
| `anl4_fs_actuals_advanced_qf_nd_capex_value` | MATRIX | Total capital expenditures from cash flow/investing, in millions |
| `anl4_fs_actuals_advanced_qf_nd_cff_value` | MATRIX | Cash flow from financing value |
| `anl4_fs_actuals_advanced_qf_nd_cfi_value` | MATRIX | Cash flow from investing value |
| `anl4_fs_actuals_advanced_qf_nd_cfo_value` | MATRIX | Cash flow from operations value |
| `anl4_fs_actuals_advanced_qf_nd_ebit_value` | MATRIX | Earnings before interest and taxes actual value for the quarter |
| `anl4_fs_actuals_advanced_qf_nd_ebitda_value` | MATRIX | Actual EBITDA for the quarter |
| `anl4_fs_actuals_advanced_qf_nd_eps_nongaap_value` | MATRIX | Non-GAAP earnings per share actual value |
| `anl4_fs_actuals_advanced_qf_nd_epsr_value` | MATRIX | Reported earnings per share, actual value |
| `anl4_fs_actuals_advanced_qf_nd_fcf_value` | MATRIX | Actual free cash flow for the quarter |
| `anl4_fs_actuals_advanced_qf_nd_fcfps_value` | MATRIX | Free cash flow per share announced financial value |
| `anl4_fs_actuals_advanced_qf_nd_grossincome_value` | MATRIX | Gross income actual value for the quarter |
| `anl4_fs_actuals_advanced_qf_nd_netdebt_value` | MATRIX | Net debt value for the quarter |
| `anl4_fs_actuals_advanced_qf_nd_netprofit_value` | MATRIX | Net profit, actual value for the quarter |
| `anl4_fs_actuals_advanced_qf_nd_netprofita_value` | MATRIX | Adjusted net income announced financial value |
| `anl4_fs_actuals_advanced_qf_nd_ptp_value` | MATRIX | Pretax profit actual value for the quarter |
| `anl4_fs_actuals_advanced_qf_nd_ptpr_value` | MATRIX | Actual reported pretax income for the quarter |
| `anl4_fs_actuals_advanced_qf_nd_rd_exp_value` | MATRIX | Research and development expense (income statement) value in millions |
| `anl4_fs_actuals_advanced_qf_nd_sga_value` | MATRIX | Selling, general and administrative expense value |
| `anl4_fs_actuals_advanced_qf_nd_sh_equity_value` | MATRIX | Total shareholders' equity, actual value |
| `anl4_fs_actuals_advanced_qf_nd_totassets_value` | MATRIX | Actual total assets for the quarter |
| `anl4_fs_actuals_advanced_qf_nd_totgw_value` | MATRIX | Actual total goodwill value in millions |
| `anl4_fs_actuals_basic_af_nd_cfps_value` | MATRIX | Cash Flow Per Share actual value for the annual period |
| `anl4_fs_actuals_basic_af_nd_div_value` | MATRIX | Dividend actual value for the annual period |
| `anl4_fs_actuals_basic_af_nd_eps_value` | MATRIX | Earnings Per Share actual value for the annual period |
| `anl4_fs_actuals_basic_af_nd_sales_value` | MATRIX | Sales/Revenue actual value for the annual period |
| `anl4_fs_actuals_basic_qf_nd_cfps_value` | MATRIX | Actual cash flow per share for the quarter |
| `anl4_fs_actuals_basic_qf_nd_div_value` | MATRIX | Dividend per share - announced financial value |
| `anl4_fs_actuals_basic_qf_nd_eps_value` | MATRIX | Actual earnings per share for the quarter |
| `anl4_fs_actuals_basic_qf_nd_sales_value` | MATRIX | Actual sales/revenue for the quarter, expressed in millions of the stated currency |
| `anl4_fs_basic_splt_v4_nd_div_estimate` | VECTOR | Analyst’s estimated dividend per share for the specified fiscal period |
| `anl4_fs_basic_splt_v4_nd_div_previosestimate` | VECTOR | Previous dividend per share estimate value prior to the latest revision |
| `anl4_fs_basic_splt_v4_nd_eps_estimate` | VECTOR | Analyst’s estimated earnings per share for the specified fiscal period |
| `anl4_fs_basic_splt_v4_nd_eps_previosestimate` | VECTOR | Previous earnings per share estimate value prior to the latest revision |
| `anl4_fs_basic_splt_v4_nd_sales_estimate` | VECTOR | Analyst’s estimated sales/revenue for the specified fiscal period |
| `anl4_fs_basic_splt_v4_nd_sales_previosestimate` | VECTOR | Previous sales estimate value prior to the latest revision |
| `anl4_fs_detail_estimate_1qf_v4_nd_bvps_high` | MATRIX | Book Value Per Share High Estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_bvps_low` | MATRIX | Book Value Per Share Low Estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_bvps_mean` | MATRIX | Book Value Per Share Mean Estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_bvps_median` | MATRIX | Book Value Per Share Median Estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_bvps_number` | MATRIX | Number of Book Value Per Share Estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_capex_high` | MATRIX | Capital Expenditure High Estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_capex_low` | MATRIX | Capital Expenditure Low Estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_capex_mean` | MATRIX | Capital Expenditure Mean Estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_capex_median` | MATRIX | Capital Expenditure Median Estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_capex_number` | MATRIX | Number of Capital Expenditure Estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_cff_high` | MATRIX | Cash Flow from Financing High Estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_cff_low` | MATRIX | Cash Flow from Financing Low Estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_cff_mean` | MATRIX | Cash Flow from Financing Mean Estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_cff_median` | MATRIX | Cash Flow from Financing Median Estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_cff_number` | MATRIX | Number of Cash Flow from Financing Estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_cfi_high` | MATRIX | Cash Flow from Investing High Estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_cfi_low` | MATRIX | Cash Flow from Investing Low Estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_cfi_mean` | MATRIX | Cash Flow from Investing Mean Estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_cfi_median` | MATRIX | Cash Flow from Investing Median Estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_cfi_number` | MATRIX | Number of Cash Flow from Investing Estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_cfo_high` | MATRIX | Cash Flow from Operations High Estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_cfo_low` | MATRIX | Cash Flow from Operations Low Estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_cfo_mean` | MATRIX | Cash Flow from Operations Mean Estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_cfo_median` | MATRIX | Cash Flow from Operations Median Estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_cfo_number` | MATRIX | Number of Cash Flow from Operations Estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_cfo_std` | MATRIX | Standard Deviation of Cash Flow from Operations Estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_ebit_high` | MATRIX | High EBIT estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_ebit_low` | MATRIX | Low EBIT estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_ebit_mean` | MATRIX | Mean of analyst estimates for EBIT |
| `anl4_fs_detail_estimate_1qf_v4_nd_ebit_median` | MATRIX | Median of EBIT (earnings before interest and taxes) estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_ebit_number` | MATRIX | Number of EBIT estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_ebit_std` | MATRIX | Standard deviation of analyst estimates for EBIT |
| `anl4_fs_detail_estimate_1qf_v4_nd_ebitda_high` | MATRIX | High EBITDA estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_ebitda_low` | MATRIX | Lowest estimate of EBITDA |
| `anl4_fs_detail_estimate_1qf_v4_nd_ebitda_mean` | MATRIX | Mean of analyst estimates for EBITDA |
| `anl4_fs_detail_estimate_1qf_v4_nd_ebitda_median` | MATRIX | Median of EBITDA estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_ebitda_number` | MATRIX | Number of analyst estimates for EBITDA |
| `anl4_fs_detail_estimate_1qf_v4_nd_ebitda_std` | MATRIX | Standard deviation of analyst estimates for EBITDA |
| `anl4_fs_detail_estimate_1qf_v4_nd_epsr_high` | MATRIX | High estimated EPS growth rate |
| `anl4_fs_detail_estimate_1qf_v4_nd_epsr_low` | MATRIX | Lowest analyst estimate for GAAP EPS (reported EPS) |
| `anl4_fs_detail_estimate_1qf_v4_nd_epsr_mean` | MATRIX | Mean estimated EPS growth rate |
| `anl4_fs_detail_estimate_1qf_v4_nd_epsr_median` | MATRIX | Median of analyst estimates for GAAP EPS (reported EPS) |
| `anl4_fs_detail_estimate_1qf_v4_nd_epsr_number` | MATRIX | Number of EPS growth rate estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_fcf_high` | MATRIX | Highest analyst estimate for free cash flow |
| `anl4_fs_detail_estimate_1qf_v4_nd_fcf_low` | MATRIX | Free Cash Flow - lowest estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_fcf_mean` | MATRIX | Mean of analyst estimates for free cash flow |
| `anl4_fs_detail_estimate_1qf_v4_nd_fcf_median` | MATRIX | Free Cash Flow - median (50th percentile) estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_fcf_number` | MATRIX | Number of analyst estimates for free cash flow |
| `anl4_fs_detail_estimate_1qf_v4_nd_fcfps_high` | MATRIX | Highest analyst estimate for free cash flow per share |
| `anl4_fs_detail_estimate_1qf_v4_nd_fcfps_low` | MATRIX | Free Cash Flow per Share - lowest estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_fcfps_mean` | MATRIX | Mean of analyst estimates for free cash flow per share |
| `anl4_fs_detail_estimate_1qf_v4_nd_fcfps_median` | MATRIX | Median (50th percentile) of analyst estimates for free cash flow per share |
| `anl4_fs_detail_estimate_1qf_v4_nd_fcfps_number` | MATRIX | Number of analyst estimates for free cash flow per share |
| `anl4_fs_detail_estimate_1qf_v4_nd_grossincome_high` | MATRIX | Gross Income - highest estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_grossincome_low` | MATRIX | Lowest analyst estimate for gross income |
| `anl4_fs_detail_estimate_1qf_v4_nd_grossincome_mean` | MATRIX | Mean of analyst estimates for gross income |
| `anl4_fs_detail_estimate_1qf_v4_nd_grossincome_median` | MATRIX | Median (50th percentile) of analyst estimates for gross income |
| `anl4_fs_detail_estimate_1qf_v4_nd_grossincome_number` | MATRIX | Number of analyst estimates for gross income |
| `anl4_fs_detail_estimate_1qf_v4_nd_grossincome_std` | MATRIX | Standard deviation of analyst estimates for gross income |
| `anl4_fs_detail_estimate_1qf_v4_nd_netdebt_high` | MATRIX | Net debt highest analyst estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_netdebt_low` | MATRIX | Lowest estimate of net debt |
| `anl4_fs_detail_estimate_1qf_v4_nd_netdebt_mean` | MATRIX | Mean of analyst estimates for Net Debt |
| `anl4_fs_detail_estimate_1qf_v4_nd_netdebt_median` | MATRIX | Median of Net Debt estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_netdebt_number` | MATRIX | Net debt - number of contributing analyst estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_netprofit_high` | MATRIX | Net Profit — highest estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_netprofit_low` | MATRIX | Net profit - lowest analyst estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_netprofit_mean` | MATRIX | Net profit mean of analyst estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_netprofit_median` | MATRIX | Median of analyst estimates for net profit |
| `anl4_fs_detail_estimate_1qf_v4_nd_netprofit_number` | MATRIX | Net Profit - number of analyst estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_netprofit_std` | MATRIX | Net Profit - standard deviation of estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_netprofita_high` | MATRIX | Highest estimate of Adjusted Net Income (Net Profit, Adjusted) |
| `anl4_fs_detail_estimate_1qf_v4_nd_netprofita_low` | MATRIX | Adjusted net income – lowest analyst estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_netprofita_mean` | MATRIX | Mean of analyst estimates for adjusted net income |
| `anl4_fs_detail_estimate_1qf_v4_nd_netprofita_median` | MATRIX | Median of Adjusted Net Income (Net Profit, Adjusted) estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_netprofita_number` | MATRIX | Number of adjusted net income (Net Profit Attributable) estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_netprofita_std` | MATRIX | Standard deviation of analyst estimates for adjusted net income |
| `anl4_fs_detail_estimate_1qf_v4_nd_ptp_high` | MATRIX | Highest analyst estimate for pretax income |
| `anl4_fs_detail_estimate_1qf_v4_nd_ptp_low` | MATRIX | Lowest estimate of pretax income |
| `anl4_fs_detail_estimate_1qf_v4_nd_ptp_mean` | MATRIX | Mean of Pre-tax Income estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_ptp_median` | MATRIX | Median of Pre-tax Income estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_ptp_number` | MATRIX | Pre-tax income number of contributing estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_ptp_std` | MATRIX | Pre-tax income standard deviation of estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_ptpr_high` | MATRIX | Highest estimate of Reported Pretax Income |
| `anl4_fs_detail_estimate_1qf_v4_nd_ptpr_low` | MATRIX | Lowest estimate of reported pretax income |
| `anl4_fs_detail_estimate_1qf_v4_nd_ptpr_mean` | MATRIX | Reported pretax income - mean of estimations |
| `anl4_fs_detail_estimate_1qf_v4_nd_ptpr_median` | MATRIX | Median estimate of Reported Pretax Income |
| `anl4_fs_detail_estimate_1qf_v4_nd_ptpr_number` | MATRIX | Number of analyst estimates for reported pretax income |
| `anl4_fs_detail_estimate_1qf_v4_nd_rd_exp_high` | MATRIX | Research and Development Expense — highest estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_rd_exp_low` | MATRIX | Lowest analyst estimate for Research and Development expenditure |
| `anl4_fs_detail_estimate_1qf_v4_nd_rd_exp_mean` | MATRIX | Mean of research and development expense estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_rd_exp_median` | MATRIX | Median of Research and Development Expense estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_rd_exp_number` | MATRIX | Number of analyst estimates for research and development expense |
| `anl4_fs_detail_estimate_1qf_v4_nd_sga_high` | MATRIX | Highest analyst estimate for Selling, General and Administrative expenses |
| `anl4_fs_detail_estimate_1qf_v4_nd_sga_low` | MATRIX | Lowest analyst estimate for Selling, General and Administrative expenses |
| `anl4_fs_detail_estimate_1qf_v4_nd_sga_mean` | MATRIX | Mean of analysts' estimates for Selling, General and Administrative expenses |
| `anl4_fs_detail_estimate_1qf_v4_nd_sga_median` | MATRIX | Median of analyst estimates for selling, general and administrative expense |
| `anl4_fs_detail_estimate_1qf_v4_nd_sga_number` | MATRIX | Number of Selling, General and Administrative Expense estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_sh_equity_high` | MATRIX | Shareholders' Equity highest analyst estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_sh_equity_low` | MATRIX | Shareholders' Equity lowest analyst estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_sh_equity_mean` | MATRIX | Mean of analyst estimates for shareholders' equity |
| `anl4_fs_detail_estimate_1qf_v4_nd_sh_equity_median` | MATRIX | Shareholders' Equity - median estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_sh_equity_number` | MATRIX | Number of Shareholders' Equity estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_totassets_high` | MATRIX | Total Assets - The highest estimation |
| `anl4_fs_detail_estimate_1qf_v4_nd_totassets_low` | MATRIX | Total Assets - lowest estimate |
| `anl4_fs_detail_estimate_1qf_v4_nd_totassets_mean` | MATRIX | Mean (average) of total assets estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_totassets_median` | MATRIX | Median of total assets estimates |
| `anl4_fs_detail_estimate_1qf_v4_nd_totassets_number` | MATRIX | Total Assets - number of estimations |
| `anl4_fs_detail_estimate_1qf_v4_nd_totgw_high` | MATRIX | Total Goodwill - The highest estimation |
| `anl4_fs_detail_estimate_1qf_v4_nd_totgw_low` | MATRIX | Lowest estimate of total goodwill |
| `anl4_fs_detail_estimate_1qf_v4_nd_totgw_mean` | MATRIX | Mean of analyst estimates for total goodwill |
| `anl4_fs_detail_estimate_1qf_v4_nd_totgw_median` | MATRIX | Total Goodwill - median of estimations |
| `anl4_fs_detail_estimate_1qf_v4_nd_totgw_number` | MATRIX | Number of contributing estimates for total goodwill |
| `anl4_fs_detail_estimate_basic_af_v4_nd_currency` | VECTOR | Currency code in which the estimate is reported |
| `anl4_fs_detail_estimate_basic_af_v4_nd_estimate` | VECTOR | Current estimate value reported by the broker/analyst for the item and period |
| `anl4_fs_detail_estimate_basic_af_v4_nd_previosestimate` | VECTOR | Previous estimate value from the same broker/analyst prior to this revision |
| `anl4_fs_detail_estimate_basic_qf_v4_nd_currency` | VECTOR | Currency code in which the estimate is reported |
| `anl4_fs_detail_estimate_basic_qf_v4_nd_estimate` | VECTOR | Estimated value |
| `anl4_fs_detail_estimate_basic_qf_v4_nd_previosestimate` | VECTOR | Previous estimate value before the current revision |
| `anl4_fs_detail_estimate_saf_v4_nd_estimate` | VECTOR | Estimated value for the financial item |
| `anl4_fs_detail_estimate_saf_v4_nd_previosestimate` | VECTOR | Previous estimate value for the same item |
| `anl4_fs_detail_estimates_advanced_af_nd_bvps_high` | MATRIX | Highest analyst estimate of book value per share for the annual period |
| `anl4_fs_detail_estimates_advanced_af_nd_bvps_low` | MATRIX | Lowest analyst estimate of book value per share for the annual period |
| `anl4_fs_detail_estimates_advanced_af_nd_bvps_mean` | MATRIX | Mean of analyst estimates of book value per share for the annual period |
| `anl4_fs_detail_estimates_advanced_af_nd_bvps_median` | MATRIX | Median of analyst estimates of book value per share for the annual period |
| `anl4_fs_detail_estimates_advanced_af_nd_bvps_number` | MATRIX | Number of analyst estimates of book value per share for the annual period |
| `anl4_fs_detail_estimates_advanced_af_nd_bvps_std` | MATRIX | Standard deviation of analyst estimates of book value per share for the annual period |
| `anl4_fs_detail_estimates_advanced_af_nd_capex_high` | MATRIX | Highest analyst estimate of Capital Expenditures for the upcoming fiscal year |
| `anl4_fs_detail_estimates_advanced_af_nd_capex_low` | MATRIX | Lowest analyst estimate of Capital Expenditures for the upcoming annual fiscal period |
| `anl4_fs_detail_estimates_advanced_af_nd_capex_mean` | MATRIX | Mean of analyst estimates for Capital Expenditures for the annual forecast |
| `anl4_fs_detail_estimates_advanced_af_nd_capex_median` | MATRIX | Median of analyst estimates for Capital Expenditures for the annual forecast |
| `anl4_fs_detail_estimates_advanced_af_nd_capex_number` | MATRIX | Number of analyst estimates for Capital Expenditures on an annual basis |
| `anl4_fs_detail_estimates_advanced_af_nd_capex_std` | MATRIX | Standard deviation of analyst estimates for Capital Expenditures on an annual basis |
| `anl4_fs_detail_estimates_advanced_af_nd_cff_high` | MATRIX | Highest analyst forecast for annual cash flow from financing |
| `anl4_fs_detail_estimates_advanced_af_nd_cff_low` | MATRIX | Lowest analyst forecast for annual cash flow from financing |
| `anl4_fs_detail_estimates_advanced_af_nd_cff_mean` | MATRIX | Mean of analyst estimates for annual cash flow from financing |
| `anl4_fs_detail_estimates_advanced_af_nd_cff_median` | MATRIX | Median of analyst forecasts for annual cash flow from financing |
| `anl4_fs_detail_estimates_advanced_af_nd_cff_number` | MATRIX | Number of analyst estimates for annual cash flow from financing |
| `anl4_fs_detail_estimates_advanced_af_nd_cff_std` | MATRIX | Standard deviation of analyst estimates for annual cash flow from financing |
| `anl4_fs_detail_estimates_advanced_af_nd_cfi_high` | MATRIX | Highest analyst forecast for annual cash flow from investing |
| `anl4_fs_detail_estimates_advanced_af_nd_cfi_low` | MATRIX | Lowest analyst forecast for annual cash flow from investing |
| `anl4_fs_detail_estimates_advanced_af_nd_cfi_mean` | MATRIX | Mean of analyst estimates for annual cash flow from investing |
| `anl4_fs_detail_estimates_advanced_af_nd_cfi_median` | MATRIX | Median of analyst forecasts for annual cash flow from investing |
| `anl4_fs_detail_estimates_advanced_af_nd_cfi_number` | MATRIX | Number of analyst estimates for annual cash flow from investing |
| `anl4_fs_detail_estimates_advanced_af_nd_cfi_std` | MATRIX | Standard deviation of analyst estimates for annual cash flow from investing |
| `anl4_fs_detail_estimates_advanced_af_nd_cfo_high` | MATRIX | Cash Flow from Operations, highest estimate |
| `anl4_fs_detail_estimates_advanced_af_nd_cfo_low` | MATRIX | Cash Flow from Operations, lowest estimate |
| `anl4_fs_detail_estimates_advanced_af_nd_cfo_mean` | MATRIX | Cash Flow from Operations, mean estimate |
| `anl4_fs_detail_estimates_advanced_af_nd_cfo_median` | MATRIX | Cash Flow from Operations, median estimate |
| `anl4_fs_detail_estimates_advanced_af_nd_cfo_number` | MATRIX | Cash Flow from Operations, number of estimates |
| `anl4_fs_detail_estimates_advanced_af_nd_cfo_std` | MATRIX | Cash Flow from Operations, standard deviation of estimates |
| `anl4_fs_detail_estimates_advanced_af_nd_ebit_high` | MATRIX | Highest analyst annual estimate for EBIT |
| `anl4_fs_detail_estimates_advanced_af_nd_ebit_low` | MATRIX | Lowest analyst annual estimate for EBIT |
| `anl4_fs_detail_estimates_advanced_af_nd_ebit_mean` | MATRIX | Consensus mean of analyst annual estimates for EBIT |
| `anl4_fs_detail_estimates_advanced_af_nd_ebit_median` | MATRIX | Median of analyst annual estimates for EBIT |
| `anl4_fs_detail_estimates_advanced_af_nd_ebit_number` | MATRIX | Number of contributing analyst annual estimates for EBIT |
| `anl4_fs_detail_estimates_advanced_af_nd_ebit_std` | MATRIX | Standard deviation of analyst annual estimates for EBIT |
| `anl4_fs_detail_estimates_advanced_af_nd_ebitda_high` | MATRIX | Highest analyst annual estimate for EBITDA |
| `anl4_fs_detail_estimates_advanced_af_nd_ebitda_low` | MATRIX | Lowest analyst annual estimate for EBITDA |
| `anl4_fs_detail_estimates_advanced_af_nd_ebitda_mean` | MATRIX | Consensus mean of analyst annual estimates for EBITDA |
| `anl4_fs_detail_estimates_advanced_af_nd_ebitda_median` | MATRIX | Median of analyst annual estimates for EBITDA |
| `anl4_fs_detail_estimates_advanced_af_nd_ebitda_number` | MATRIX | Number of contributing analyst annual estimates for EBITDA |
| `anl4_fs_detail_estimates_advanced_af_nd_ebitda_std` | MATRIX | Standard deviation of analyst annual estimates for EBITDA |
| `anl4_fs_detail_estimates_advanced_af_nd_epsr_high` | MATRIX | Highest analyst estimate of reported (GAAP) earnings per share for the annual period |
| `anl4_fs_detail_estimates_advanced_af_nd_epsr_low` | MATRIX | Lowest analyst estimate of reported (GAAP) earnings per share for the annual period |
| `anl4_fs_detail_estimates_advanced_af_nd_epsr_mean` | MATRIX | Mean of analyst estimates of reported (GAAP) earnings per share for the annual period |
| `anl4_fs_detail_estimates_advanced_af_nd_epsr_median` | MATRIX | Median of analyst estimates of reported (GAAP) earnings per share for the annual period |
| `anl4_fs_detail_estimates_advanced_af_nd_epsr_number` | MATRIX | Number of analyst estimates of reported (GAAP) earnings per share for the annual period |
| `anl4_fs_detail_estimates_advanced_af_nd_epsr_std` | MATRIX | Standard deviation of analyst estimates of reported (GAAP) earnings per share for the annual period |
| `anl4_fs_detail_estimates_advanced_af_nd_fcf_high` | MATRIX | Highest analyst forecast for annual free cash flow |
| `anl4_fs_detail_estimates_advanced_af_nd_fcf_low` | MATRIX | Lowest analyst forecast for annual free cash flow |
| `anl4_fs_detail_estimates_advanced_af_nd_fcf_mean` | MATRIX | Mean of analyst estimates for annual free cash flow |
| `anl4_fs_detail_estimates_advanced_af_nd_fcf_median` | MATRIX | Median of analyst forecasts for annual free cash flow |
| `anl4_fs_detail_estimates_advanced_af_nd_fcf_number` | MATRIX | Number of analyst estimates for annual free cash flow |
| `anl4_fs_detail_estimates_advanced_af_nd_fcf_std` | MATRIX | Standard deviation of analyst estimates for annual free cash flow |
| `anl4_fs_detail_estimates_advanced_af_nd_fcfps_high` | MATRIX | Highest analyst forecast for annual free cash flow per share |
| `anl4_fs_detail_estimates_advanced_af_nd_fcfps_low` | MATRIX | Lowest analyst forecast for annual free cash flow per share |
| `anl4_fs_detail_estimates_advanced_af_nd_fcfps_mean` | MATRIX | Mean of analyst estimates for annual free cash flow per share |
| `anl4_fs_detail_estimates_advanced_af_nd_fcfps_median` | MATRIX | Median of analyst forecasts for annual free cash flow per share |
| `anl4_fs_detail_estimates_advanced_af_nd_fcfps_number` | MATRIX | Number of analyst estimates for annual free cash flow per share |
| `anl4_fs_detail_estimates_advanced_af_nd_grossincome_high` | MATRIX | Highest analyst annual estimate for Gross Income |
| `anl4_fs_detail_estimates_advanced_af_nd_grossincome_low` | MATRIX | Lowest analyst annual estimate for Gross Income |
| `anl4_fs_detail_estimates_advanced_af_nd_grossincome_mean` | MATRIX | Consensus mean of analyst annual estimates for Gross Income |
| `anl4_fs_detail_estimates_advanced_af_nd_grossincome_median` | MATRIX | Median of analyst annual estimates for Gross Income |
| `anl4_fs_detail_estimates_advanced_af_nd_grossincome_number` | MATRIX | Number of contributing analyst annual estimates for Gross Income |
| `anl4_fs_detail_estimates_advanced_af_nd_grossincome_std` | MATRIX | Standard deviation of analyst annual estimates for Gross Income |
| `anl4_fs_detail_estimates_advanced_af_nd_netdebt_high` | MATRIX | Highest analyst annual estimate for Net Debt |
| `anl4_fs_detail_estimates_advanced_af_nd_netdebt_low` | MATRIX | Lowest analyst annual estimate for Net Debt |
| `anl4_fs_detail_estimates_advanced_af_nd_netdebt_mean` | MATRIX | Consensus mean of analyst annual estimates for Net Debt |
| `anl4_fs_detail_estimates_advanced_af_nd_netdebt_median` | MATRIX | Median of analyst annual estimates for Net Debt |
| `anl4_fs_detail_estimates_advanced_af_nd_netdebt_number` | MATRIX | Number of contributing analyst annual estimates for Net Debt |
| `anl4_fs_detail_estimates_advanced_af_nd_netprofit_high` | MATRIX | Net Profit, highest estimate |
| `anl4_fs_detail_estimates_advanced_af_nd_netprofit_low` | MATRIX | Net Profit, lowest estimate |
| `anl4_fs_detail_estimates_advanced_af_nd_netprofit_mean` | MATRIX | Net Profit, mean estimate |
| `anl4_fs_detail_estimates_advanced_af_nd_netprofit_median` | MATRIX | Net Profit, median estimate |
| `anl4_fs_detail_estimates_advanced_af_nd_netprofit_number` | MATRIX | Net Profit, number of estimates |
| `anl4_fs_detail_estimates_advanced_af_nd_netprofit_std` | MATRIX | Net Profit, standard deviation of estimates |
| `anl4_fs_detail_estimates_advanced_af_nd_netprofita_high` | MATRIX | Net Profit Attributable, highest estimate |
| `anl4_fs_detail_estimates_advanced_af_nd_netprofita_low` | MATRIX | Net Profit Attributable, lowest estimate |
| `anl4_fs_detail_estimates_advanced_af_nd_netprofita_mean` | MATRIX | Net Profit Attributable, mean estimate |
| `anl4_fs_detail_estimates_advanced_af_nd_netprofita_median` | MATRIX | Net Profit Attributable, median estimate |
| `anl4_fs_detail_estimates_advanced_af_nd_netprofita_number` | MATRIX | Net Profit Attributable, number of estimates |
| `anl4_fs_detail_estimates_advanced_af_nd_netprofita_std` | MATRIX | Net Profit Attributable, standard deviation of estimates |
| `anl4_fs_detail_estimates_advanced_af_nd_ptp_high` | MATRIX | Pretax income, highest analyst estimate |
| `anl4_fs_detail_estimates_advanced_af_nd_ptp_low` | MATRIX | Pretax income, lowest analyst estimate |
| `anl4_fs_detail_estimates_advanced_af_nd_ptp_mean` | MATRIX | Pretax income, mean of analyst estimates |
| `anl4_fs_detail_estimates_advanced_af_nd_ptp_median` | MATRIX | Pretax income, median of analyst estimates |
| `anl4_fs_detail_estimates_advanced_af_nd_ptp_number` | MATRIX | Pretax income, number of analyst estimates |
| `anl4_fs_detail_estimates_advanced_af_nd_ptp_std` | MATRIX | Pretax income, standard deviation of analyst estimates |
| `anl4_fs_detail_estimates_advanced_af_nd_ptpr_high` | MATRIX | Highest analyst estimate for annual reported pretax income |
| `anl4_fs_detail_estimates_advanced_af_nd_ptpr_low` | MATRIX | Lowest analyst estimate for annual reported pretax income |
| `anl4_fs_detail_estimates_advanced_af_nd_ptpr_mean` | MATRIX | Consensus mean of analysts’ annual reported pretax income forecasts |
| `anl4_fs_detail_estimates_advanced_af_nd_ptpr_median` | MATRIX | Median of analysts’ annual reported pretax income forecasts |
| `anl4_fs_detail_estimates_advanced_af_nd_ptpr_number` | MATRIX | Number of contributing analyst estimates for annual reported pretax income |
| `anl4_fs_detail_estimates_advanced_af_nd_rd_exp_high` | MATRIX | Highest individual analyst estimate for Research and Development expense for the annual forecast period |
| `anl4_fs_detail_estimates_advanced_af_nd_rd_exp_low` | MATRIX | Lowest individual analyst estimate for Research and Development expense for the annual forecast period |
| `anl4_fs_detail_estimates_advanced_af_nd_rd_exp_mean` | MATRIX | Mean of analyst estimates for Research and Development expense for the annual forecast period |
| `anl4_fs_detail_estimates_advanced_af_nd_rd_exp_median` | MATRIX | Median of analyst estimates for Research and Development expense for the annual forecast period |
| `anl4_fs_detail_estimates_advanced_af_nd_rd_exp_number` | MATRIX | Number of contributing analyst estimates for Research and Development expense for the annual forecast period |
| `anl4_fs_detail_estimates_advanced_af_nd_sga_high` | MATRIX | Highest individual analyst estimate for Selling, General and Administrative expenses for the annual forecast period |
| `anl4_fs_detail_estimates_advanced_af_nd_sga_low` | MATRIX | Lowest individual analyst estimate for Selling, General and Administrative expenses for the annual forecast period |
| `anl4_fs_detail_estimates_advanced_af_nd_sga_mean` | MATRIX | Mean of analyst estimates for Selling, General and Administrative expenses for the annual forecast period |
| `anl4_fs_detail_estimates_advanced_af_nd_sga_median` | MATRIX | Median of analyst estimates for Selling, General and Administrative expenses for the annual forecast period |
| `anl4_fs_detail_estimates_advanced_af_nd_sga_number` | MATRIX | Number of contributing analyst estimates for Selling, General and Administrative expenses for the annual forecast period |
| `anl4_fs_detail_estimates_advanced_af_nd_sh_equity_high` | MATRIX | Highest analyst annual estimate for Shareholders' Equity |
| `anl4_fs_detail_estimates_advanced_af_nd_sh_equity_low` | MATRIX | Lowest analyst annual estimate for Shareholders' Equity |
| `anl4_fs_detail_estimates_advanced_af_nd_sh_equity_mean` | MATRIX | Consensus mean of analyst annual estimates for Shareholders' Equity |
| `anl4_fs_detail_estimates_advanced_af_nd_sh_equity_median` | MATRIX | Median of analyst annual estimates for Shareholders' Equity |
| `anl4_fs_detail_estimates_advanced_af_nd_sh_equity_number` | MATRIX | Number of contributing analyst annual estimates for Shareholders' Equity |
| `anl4_fs_detail_estimates_advanced_af_nd_sh_equity_std` | MATRIX | Standard deviation of analyst annual estimates for Shareholders' Equity |
| `anl4_fs_detail_estimates_advanced_af_nd_tbvps_high` | MATRIX | Highest analyst estimate of tangible book value per share for the annual period |
| `anl4_fs_detail_estimates_advanced_af_nd_tbvps_low` | MATRIX | Lowest analyst estimate of tangible book value per share for the annual period |
| `anl4_fs_detail_estimates_advanced_af_nd_tbvps_mean` | MATRIX | Mean of analyst estimates of tangible book value per share for the annual period |
| `anl4_fs_detail_estimates_advanced_af_nd_tbvps_median` | MATRIX | Median of analyst estimates of tangible book value per share for the annual period |
| `anl4_fs_detail_estimates_advanced_af_nd_tbvps_number` | MATRIX | Number of analyst estimates of tangible book value per share for the annual period |
| `anl4_fs_detail_estimates_advanced_af_nd_totassets_high` | MATRIX | Highest individual analyst estimate for Total Assets for the annual forecast period |
| `anl4_fs_detail_estimates_advanced_af_nd_totassets_low` | MATRIX | Lowest individual analyst estimate for Total Assets for the annual forecast period |
| `anl4_fs_detail_estimates_advanced_af_nd_totassets_mean` | MATRIX | Mean of analyst estimates for Total Assets for the annual forecast period |
| `anl4_fs_detail_estimates_advanced_af_nd_totassets_median` | MATRIX | Median of analyst estimates for Total Assets for the annual forecast period |
| `anl4_fs_detail_estimates_advanced_af_nd_totassets_number` | MATRIX | Number of contributing analyst estimates for Total Assets for the annual forecast period |
| `anl4_fs_detail_estimates_advanced_af_nd_totassets_std` | MATRIX | Standard deviation of analyst estimates for Total Assets for the annual forecast period |
| `anl4_fs_detail_estimates_advanced_af_nd_totgw_high` | MATRIX | Highest analyst estimate for Total Goodwill for the annual forecast period |
| `anl4_fs_detail_estimates_advanced_af_nd_totgw_low` | MATRIX | Lowest analyst estimate for Total Goodwill for the annual forecast period |
| `anl4_fs_detail_estimates_advanced_af_nd_totgw_mean` | MATRIX | Mean of analyst estimates for Total Goodwill for the annual forecast period |
| `anl4_fs_detail_estimates_advanced_af_nd_totgw_median` | MATRIX | Median of analyst estimates for Total Goodwill for the annual forecast period |
| `anl4_fs_detail_estimates_advanced_af_nd_totgw_number` | MATRIX | Number of analyst estimates for Total Goodwill for the annual forecast period |
| `anl4_fs_detail_estimates_basic_af_v4_nd_cfps_high` | MATRIX | Cash Flow Per Share (CFPS) highest analyst estimate for the annual forecast |
| `anl4_fs_detail_estimates_basic_af_v4_nd_cfps_low` | MATRIX | Cash Flow Per Share (CFPS) lowest analyst estimate for the upcoming fiscal year |
| `anl4_fs_detail_estimates_basic_af_v4_nd_cfps_mean` | MATRIX | Cash Flow Per Share (CFPS) consensus mean of analyst estimates for the annual period |
| `anl4_fs_detail_estimates_basic_af_v4_nd_cfps_median` | MATRIX | Cash Flow Per Share (CFPS) median of analyst estimates for the annual period |
| `anl4_fs_detail_estimates_basic_af_v4_nd_cfps_number` | MATRIX | Cash Flow Per Share (CFPS) number of contributing analyst estimates for the annual period |
| `anl4_fs_detail_estimates_basic_af_v4_nd_currency` | MATRIX | Home currency of the instrument |
| `anl4_fs_detail_estimates_basic_af_v4_nd_div_high` | MATRIX | Dividend per share highest analyst estimate for the annual forecast |
| `anl4_fs_detail_estimates_basic_af_v4_nd_div_low` | MATRIX | Dividend per share lowest analyst estimate for the annual forecast |
| `anl4_fs_detail_estimates_basic_af_v4_nd_div_mean` | MATRIX | Dividend per share consensus mean of analyst estimates for the annual period |
| `anl4_fs_detail_estimates_basic_af_v4_nd_div_median` | MATRIX | Dividend per share median of analyst estimates for the annual period |
| `anl4_fs_detail_estimates_basic_af_v4_nd_div_number` | MATRIX | Dividend per share number of contributing analyst estimates for the annual period |
| `anl4_fs_detail_estimates_basic_af_v4_nd_div_std` | MATRIX | Dividend per share standard deviation of analyst estimates |
| `anl4_fs_detail_estimates_basic_af_v4_nd_eps_high` | MATRIX | Earnings per share (EPS) highest analyst estimate for the annual period |
| `anl4_fs_detail_estimates_basic_af_v4_nd_eps_low` | MATRIX | Earnings per share (EPS) lowest analyst estimate for the annual period |
| `anl4_fs_detail_estimates_basic_af_v4_nd_eps_mean` | MATRIX | Earnings per share (EPS) consensus mean of analyst estimates for the annual period |
| `anl4_fs_detail_estimates_basic_af_v4_nd_eps_median` | MATRIX | Earnings per share (EPS) median of analyst estimates for the annual period |
| `anl4_fs_detail_estimates_basic_af_v4_nd_eps_number` | MATRIX | Earnings per share (EPS) number of contributing analyst estimates for the annual period |
| `anl4_fs_detail_estimates_basic_af_v4_nd_eps_std` | MATRIX | Earnings per share (EPS) standard deviation of analyst estimates |
| `anl4_fs_detail_estimates_basic_af_v4_nd_sales_high` | MATRIX | Sales/Revenue highest analyst estimate for the annual period |
| `anl4_fs_detail_estimates_basic_af_v4_nd_sales_low` | MATRIX | Sales/Revenue lowest analyst estimate for the annual period |
| `anl4_fs_detail_estimates_basic_af_v4_nd_sales_mean` | MATRIX | Sales/Revenue consensus mean of analyst estimates for the annual period |
| `anl4_fs_detail_estimates_basic_af_v4_nd_sales_median` | MATRIX | Sales/Revenue median of analyst estimates for the annual period |
| `anl4_fs_detail_estimates_basic_af_v4_nd_sales_number` | MATRIX | Sales/Revenue number of contributing analyst estimates for the annual period |
| `anl4_fs_detail_estimates_basic_af_v4_nd_sales_std` | MATRIX | Sales/Revenue standard deviation of analyst estimates |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_cfps_high` | MATRIX | Highest Cash Flow Per Share estimate (delay 1 quarter) |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_cfps_low` | MATRIX | Lowest Cash Flow Per Share estimate (delay 1 quarter) |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_cfps_mean` | MATRIX | Average of Cash Flow Per Share estimates (delay 1 quarter) |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_cfps_median` | MATRIX | Median Cash Flow Per Share estimate |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_cfps_number` | MATRIX | Number of Cash Flow Per Share estimates (delay 1 quarter) |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_div_high` | MATRIX | Highest Dividend per share estimate (delay 1 quarter) |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_div_low` | MATRIX | Lowest Dividend per share estimate (delay 1 quarter) |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_div_mean` | MATRIX | Average Dividend per share estimate (delay 1 quarter) |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_div_median` | MATRIX | Median Dividend per share estimate |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_div_number` | MATRIX | Number of Dividend per share estimates (delay 1 quarter) |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_div_std` | MATRIX | Standard deviation of Dividend per share estimates |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_eps_high` | MATRIX | Highest Earnings Per Share estimate |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_eps_low` | MATRIX | Lowest Earnings Per Share estimate |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_eps_mean` | MATRIX | Mean Earnings Per Share estimate |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_eps_median` | MATRIX | Median Earnings Per Share estimate |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_eps_number` | MATRIX | Number of Earnings Per Share estimates |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_eps_std` | MATRIX | Standard deviation of Earnings Per Share estimates |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_sales_high` | MATRIX | Highest Sales estimate |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_sales_low` | MATRIX | Lowest Sales estimate |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_sales_mean` | MATRIX | Mean Sales estimate (delay 1 quarter) |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_sales_median` | MATRIX | Median Sales estimate |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_sales_number` | MATRIX | Number of Sales estimates |
| `anl4_fs_detail_estimates_basic_qf_delay1_v4_nd_sales_std` | MATRIX | Standard deviation of Sales estimates |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_cfps_high` | MATRIX | Cash Flow Per Share - highest estimation |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_cfps_low` | MATRIX | Cash Flow Per Share - lowest estimation |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_cfps_mean` | MATRIX | Cash Flow Per Share - average of estimations |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_cfps_median` | MATRIX | Cash Flow Per Share - median of estimations |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_cfps_number` | MATRIX | Cash Flow Per Share - number of estimations |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_div_high` | MATRIX | Dividend per share - highest estimation |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_div_low` | MATRIX | Dividend per share - lowest estimation |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_div_mean` | MATRIX | Dividend per share - average of estimations |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_div_median` | MATRIX | Dividend per share - median of estimations |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_div_number` | MATRIX | Dividend per share - number of estimations |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_div_std` | MATRIX | Dividend per share - standard deviation of estimations |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_eps_high` | MATRIX | Earnings per share - highest estimation |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_eps_low` | MATRIX | Earnings per share - lowest estimation |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_eps_mean` | MATRIX | Earnings per share - mean of estimations |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_eps_median` | MATRIX | Earnings per share - 50th percentile (median) of estimations |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_eps_number` | MATRIX | Earnings per share - number of estimations |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_eps_std` | MATRIX | Earnings per share - standard deviation of estimations |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_sales_high` | MATRIX | Sales - the highest estimation |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_sales_low` | MATRIX | Sales - the lowest estimation |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_sales_mean` | MATRIX | Sales - mean of estimations |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_sales_median` | MATRIX | Sales - median of estimations |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_sales_number` | MATRIX | Sales - number of estimations |
| `anl4_fs_detail_estimates_basic_qf_v4_nd_sales_std` | MATRIX | Standard deviation of Sales estimations |
| `anl4_fs_detail_lt_v4_nd_estimate` | VECTOR | Current estimate value reported by the analyst |
| `anl4_fs_detail_lt_v4_nd_previosestimate` | VECTOR | Previous estimate value prior to the latest revision |
| `anl4_fs_detail_rec_v4_nd_estimate` | VECTOR | Recommendation value/rating provided by the broker/analyst |
| `anl4_fs_guidance_af_v4_nd_estimate` | VECTOR | Point guidance estimate value for the item |
| `anl4_fs_guidance_af_v4_nd_maxguidance` | VECTOR | Maximum value of the company’s annual guidance range for the item |
| `anl4_fs_guidance_af_v4_nd_minguidance` | VECTOR | Minimum value of the company’s annual guidance range for the item |
| `anl4_fs_guidance_basic_af_v4_nd_estimate` | VECTOR | Point estimate for the company’s basic annual financial guidance |
| `anl4_fs_guidance_basic_af_v4_nd_maxguidance` | VECTOR | Maximum value of the company’s annual guidance range for the item |
| `anl4_fs_guidance_basic_af_v4_nd_minguidance` | VECTOR | Minimum value of the company’s annual guidance range for the item |
| `anl4_fs_guidance_basic_qf_v4_nd_estimate` | VECTOR | Point estimate value for the guidance item |
| `anl4_fs_guidance_basic_qf_v4_nd_maxguidance` | VECTOR | Maximum guidance value for the item |
| `anl4_fs_guidance_basic_qf_v4_nd_minguidance` | VECTOR | Minimum guidance value for the item |
| `anl4_fs_guidance_qf_v4_nd_currency` | VECTOR | Currency code in which the guidance is reported |
| `anl4_fs_guidance_qf_v4_nd_estimate` | VECTOR | Point guidance estimate value |
| `anl4_fs_guidance_qf_v4_nd_maxguidance` | VECTOR | Maximum value of the guidance range for the item |
| `anl4_fs_guidance_qf_v4_nd_minguidance` | VECTOR | Minimum value of the guidance range for the item |
| `anl4_fs_guidances_advanced_af_nd_bvps_maxguidance` | MATRIX | Book value per share - maximum guidance value for the annual period |
| `anl4_fs_guidances_advanced_af_nd_bvps_minguidance` | MATRIX | Minimum annual guidance value for Book Value Per Share |
| `anl4_fs_guidances_advanced_af_nd_capex_maxguidance` | MATRIX | Maximum guidance value for capital expenditures on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_capex_minguidance` | MATRIX | Minimum guidance value for capital expenditures on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_capex_value` | MATRIX | Capital expenditures - total guidance value for the annual period |
| `anl4_fs_guidances_advanced_af_nd_cff_maxguidance` | MATRIX | Maximum annual guidance value for Cash Flow From Financing |
| `anl4_fs_guidances_advanced_af_nd_cff_minguidance` | MATRIX | Minimum annual guidance value for Cash Flow From Financing |
| `anl4_fs_guidances_advanced_af_nd_cfi_maxguidance` | MATRIX | Maximum annual guidance value for Cash Flow from Investing |
| `anl4_fs_guidances_advanced_af_nd_cfi_minguidance` | MATRIX | Minimum annual guidance value for Cash Flow From Investing |
| `anl4_fs_guidances_advanced_af_nd_cfo_maxguidance` | MATRIX | Maximum guidance value for Cash Flow from Operations on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_cfo_minguidance` | MATRIX | Minimum guidance value for cash flow from operations on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_currency` | MATRIX | Pricing currency where the security trades for the annual period |
| `anl4_fs_guidances_advanced_af_nd_custom_eps_maxguidance` | MATRIX | Maximum guidance value for custom earnings per share on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_custom_eps_minguidance` | MATRIX | Customized earnings per share - minimum guidance value for the annual period |
| `anl4_fs_guidances_advanced_af_nd_ebit_maxguidance` | MATRIX | Maximum annual guidance value for Earnings Before Interest and Taxes (EBIT) |
| `anl4_fs_guidances_advanced_af_nd_ebit_minguidance` | MATRIX | Minimum guidance value for Earnings Before Interest and Taxes (EBIT) on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_ebitda_maxguidance` | MATRIX | Maximum guidance value for EBITDA on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_ebitda_minguidance` | MATRIX | Minimum annual guidance value for EBITDA |
| `anl4_fs_guidances_advanced_af_nd_epsa_maxguidance` | MATRIX | The maximum guidance value for adjusted earnings per share on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_epsa_minguidance` | MATRIX | Minimum guidance value for adjusted earnings per share excluding extraordinary items and stock option expenses on an … |
| `anl4_fs_guidances_advanced_af_nd_epsr_maxguidance` | MATRIX | Maximum guidance value for reported earnings per share (EPSR) for the annual period |
| `anl4_fs_guidances_advanced_af_nd_epsr_minguidance` | MATRIX | Reported Earnings per Share minimum guidance value for the annual period |
| `anl4_fs_guidances_advanced_af_nd_fcf_maxguidance` | MATRIX | The maximum guidance value for Free Cash Flow on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_fcf_minguidance` | MATRIX | Minimum annual guidance value for Free Cash Flow |
| `anl4_fs_guidances_advanced_af_nd_fcfps_maxguidance` | MATRIX | Maximum annual guidance value for Free Cash Flow per Share (FCFPS) |
| `anl4_fs_guidances_advanced_af_nd_fcfps_minguidance` | MATRIX | Minimum annual guidance value for Free Cash Flow per Share |
| `anl4_fs_guidances_advanced_af_nd_ffo_maxguidance` | MATRIX | Maximum guidance value for Funds from Operations on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_ffo_minguidance` | MATRIX | Minimum annual guidance value for Funds From Operations |
| `anl4_fs_guidances_advanced_af_nd_ffoa_maxguidance` | MATRIX | Adjusted funds from operations - maximum guidance value for the annual period |
| `anl4_fs_guidances_advanced_af_nd_ffoa_minguidance` | MATRIX | Adjusted funds from operation - minimum guidance for the annual period |
| `anl4_fs_guidances_advanced_af_nd_grossincome_maxguidance` | MATRIX | Maximum guidance value for gross income on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_grossincome_minguidance` | MATRIX | Minimum guidance value for Gross Income on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_netdebt_maxguidance` | MATRIX | Maximum annual guidance value for Net Debt on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_netdebt_minguidance` | MATRIX | Minimum annual guidance value for Net Debt |
| `anl4_fs_guidances_advanced_af_nd_netprofit_maxguidance` | MATRIX | The maximum guidance value for net profit on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_netprofit_minguidance` | MATRIX | Minimum guidance value for Net Profit on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_netprofita_maxguidance` | MATRIX | Maximum annual guidance value for adjusted net profit |
| `anl4_fs_guidances_advanced_af_nd_netprofita_minguidance` | MATRIX | Minimum annual guidance value for adjusted net profit |
| `anl4_fs_guidances_advanced_af_nd_ptp_maxguidance` | MATRIX | Maximum annual guidance value for Pretax income |
| `anl4_fs_guidances_advanced_af_nd_ptp_minguidance` | MATRIX | Minimum guidance value for pretax income on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_ptpr_maxguidance` | MATRIX | Maximum annual guidance value for reported pretax income (PTPR) |
| `anl4_fs_guidances_advanced_af_nd_ptpr_minguidance` | MATRIX | Reported Pretax income - minimum guidance value |
| `anl4_fs_guidances_advanced_af_nd_rd_exp_maxguidance` | MATRIX | Maximum guidance value for Research and Development Expense on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_rd_exp_minguidance` | MATRIX | Minimum guidance value for Research & Development Expense on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_sga_maxguidance` | MATRIX | The maximum guidance value for Selling, General & Administrative Expense |
| `anl4_fs_guidances_advanced_af_nd_sga_minguidance` | MATRIX | Minimum guidance value for Selling, General & Administrative Expense on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_sh_equity_maxguidance` | MATRIX | Maximum annual guidance value for Shareholder's Equity |
| `anl4_fs_guidances_advanced_af_nd_sh_equity_minguidance` | MATRIX | Minimum guidance value for Shareholder’s Equity |
| `anl4_fs_guidances_advanced_af_nd_shr_maxguidance` | MATRIX | Maximum guidance value for Shares |
| `anl4_fs_guidances_advanced_af_nd_shr_minguidance` | MATRIX | Minimum guidance for shares on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_shrb_maxguidance` | MATRIX | Maximum guidance value for Shares Basic for the annual period |
| `anl4_fs_guidances_advanced_af_nd_shrb_minguidance` | MATRIX | Minimum annual guidance value for Basic Shares (SHRB) |
| `anl4_fs_guidances_advanced_af_nd_soe_maxguidance` | MATRIX | Stock option expense - maximum guidance value for the annual period |
| `anl4_fs_guidances_advanced_af_nd_soe_minguidance` | MATRIX | Minimum guidance value for stock option expense on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_tbvps_maxguidance` | MATRIX | Maximum annual guidance value for Tangible Book Value per Share |
| `anl4_fs_guidances_advanced_af_nd_tbvps_minguidance` | MATRIX | Minimum annual guidance value for Tangible Book Value per Share |
| `anl4_fs_guidances_advanced_af_nd_totassets_maxguidance` | MATRIX | Maximum guidance value for total assets on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_totassets_minguidance` | MATRIX | Minimum annual guidance value for Total Assets |
| `anl4_fs_guidances_advanced_af_nd_totgw_maxguidance` | MATRIX | Maximum guidance value for total goodwill on an annual basis |
| `anl4_fs_guidances_advanced_af_nd_totgw_minguidance` | MATRIX | Minimum guidance value for Total Goodwill |
| `anl4_fs_guidances_advanced_qf_nd_bvps_maxguidance` | MATRIX | Book Value Per Share – maximum guidance value among forecasts |
| `anl4_fs_guidances_advanced_qf_nd_bvps_minguidance` | MATRIX | Minimum guidance value for Book Value per Share (BVPS) |
| `anl4_fs_guidances_advanced_qf_nd_capex_maxguidance` | MATRIX | Maximum guidance value for capital expenditures (CAPEX) |
| `anl4_fs_guidances_advanced_qf_nd_capex_minguidance` | MATRIX | Minimum guidance value for Capital Expenditures |
| `anl4_fs_guidances_advanced_qf_nd_cff_maxguidance` | MATRIX | Cash Flow from Financing maximum guidance value |
| `anl4_fs_guidances_advanced_qf_nd_cff_minguidance` | MATRIX | Minimum guidance value for Cash Flow From Financing |
| `anl4_fs_guidances_advanced_qf_nd_cfi_maxguidance` | MATRIX | Maximum guidance value for Cash Flow from Investing |
| `anl4_fs_guidances_advanced_qf_nd_cfi_minguidance` | MATRIX | Cash Flow from Investing minimum guidance value |
| `anl4_fs_guidances_advanced_qf_nd_cfo_maxguidance` | MATRIX | Maximum guidance value for Cash Flow from Operations |
| `anl4_fs_guidances_advanced_qf_nd_cfo_minguidance` | MATRIX | Minimum guidance value for Cash Flow from Operations |
| `anl4_fs_guidances_advanced_qf_nd_custom_eps_maxguidance` | MATRIX | Custom Earnings per share - the highest guidance value |
| `anl4_fs_guidances_advanced_qf_nd_custom_eps_minguidance` | MATRIX | Custom Earnings per share - Minimum guidance value |
| `anl4_fs_guidances_advanced_qf_nd_ebit_maxguidance` | MATRIX | Maximum guidance value for EBIT |
| `anl4_fs_guidances_advanced_qf_nd_ebit_minguidance` | MATRIX | Minimum guidance value for Earnings Before Interest and Taxes (EBIT) |
| `anl4_fs_guidances_advanced_qf_nd_ebitda_maxguidance` | MATRIX | Maximum guidance value for EBITDA |
| `anl4_fs_guidances_advanced_qf_nd_ebitda_minguidance` | MATRIX | Minimum guidance value for EBITDA (Earnings before interest, taxes, depreciation and amortization) |
| `anl4_fs_guidances_advanced_qf_nd_epsa_maxguidance` | MATRIX | The maximum guidance value for adjusted earnings per share |
| `anl4_fs_guidances_advanced_qf_nd_epsa_minguidance` | MATRIX | Minimum guidance value for adjusted EPS (excluding extraordinary items and stock option expenses) |
| `anl4_fs_guidances_advanced_qf_nd_epsr_maxguidance` | MATRIX | Maximum guidance value for reported EPS |
| `anl4_fs_guidances_advanced_qf_nd_epsr_minguidance` | MATRIX | Minimum guidance value for reported EPS |
| `anl4_fs_guidances_advanced_qf_nd_fcf_maxguidance` | MATRIX | Maximum guidance value for Free Cash Flow |
| `anl4_fs_guidances_advanced_qf_nd_fcf_minguidance` | MATRIX | Minimum guidance value for Free Cash Flow |
| `anl4_fs_guidances_advanced_qf_nd_fcfps_maxguidance` | MATRIX | The maximum guidance value for free cash flow per share |
| `anl4_fs_guidances_advanced_qf_nd_fcfps_minguidance` | MATRIX | Free cash flow per share minimum guidance value |
| `anl4_fs_guidances_advanced_qf_nd_ffo_maxguidance` | MATRIX | Maximum guidance value for Funds from Operation |
| `anl4_fs_guidances_advanced_qf_nd_ffo_minguidance` | MATRIX | Funds from operation - minimum guidance value |
| `anl4_fs_guidances_advanced_qf_nd_ffoa_maxguidance` | MATRIX | Adjusted funds from operation - maximum guidance value |
| `anl4_fs_guidances_advanced_qf_nd_ffoa_minguidance` | MATRIX | Minimum guidance value for Adjusted funds from operation |
| `anl4_fs_guidances_advanced_qf_nd_grossincome_maxguidance` | MATRIX | Maximum guidance value for Gross Income |
| `anl4_fs_guidances_advanced_qf_nd_grossincome_minguidance` | MATRIX | Minimum guidance value for Gross Income |
| `anl4_fs_guidances_advanced_qf_nd_netdebt_maxguidance` | MATRIX | Maximum guidance value for Net Debt |
| `anl4_fs_guidances_advanced_qf_nd_netdebt_minguidance` | MATRIX | Minimum guidance value for Net Debt |
| `anl4_fs_guidances_advanced_qf_nd_netprofit_maxguidance` | MATRIX | Maximum guidance value for Net Profit |
| `anl4_fs_guidances_advanced_qf_nd_netprofit_minguidance` | MATRIX | Net profit minimum guidance value |
| `anl4_fs_guidances_advanced_qf_nd_netprofita_maxguidance` | MATRIX | Maximum guidance value for Adjusted net income |
| `anl4_fs_guidances_advanced_qf_nd_netprofita_minguidance` | MATRIX | Minimum guidance value for adjusted net income |
| `anl4_fs_guidances_advanced_qf_nd_ptp_maxguidance` | MATRIX | Maximum guidance value for pretax income (PTP) |
| `anl4_fs_guidances_advanced_qf_nd_ptp_minguidance` | MATRIX | Minimum guidance value for Pretax income |
| `anl4_fs_guidances_advanced_qf_nd_ptpr_maxguidance` | MATRIX | Maximum guidance value for Reported Pretax Income |
| `anl4_fs_guidances_advanced_qf_nd_ptpr_minguidance` | MATRIX | Minimum guidance value for reported pretax income (PTPR) |
| `anl4_fs_guidances_advanced_qf_nd_rd_exp_maxguidance` | MATRIX | Maximum guidance value for Research and Development expense |
| `anl4_fs_guidances_advanced_qf_nd_rd_exp_minguidance` | MATRIX | Minimum guidance value for Research and Development Expense |
| `anl4_fs_guidances_advanced_qf_nd_sga_maxguidance` | MATRIX | Maximum guidance value for SG&A expenses |
| `anl4_fs_guidances_advanced_qf_nd_sga_minguidance` | MATRIX | Selling, General and Administrative Expense - minimum guidance value |
| `anl4_fs_guidances_advanced_qf_nd_sh_equity_maxguidance` | MATRIX | Maximum guidance value for Total Shareholders’ Equity |
| `anl4_fs_guidances_advanced_qf_nd_sh_equity_minguidance` | MATRIX | Minimum guidance value for Shareholders' Equity |
| `anl4_fs_guidances_advanced_qf_nd_shr_maxguidance` | MATRIX | The maximum guidance for Shares |
| `anl4_fs_guidances_advanced_qf_nd_shr_minguidance` | MATRIX | Minimum guidance value for Shares |
| `anl4_fs_guidances_advanced_qf_nd_shrb_maxguidance` | MATRIX | Maximum guidance value for basic shares (SHRB) |
| `anl4_fs_guidances_advanced_qf_nd_shrb_minguidance` | MATRIX | Minimum guidance value for Shares Basic |
| `anl4_fs_guidances_advanced_qf_nd_soe_maxguidance` | MATRIX | Maximum guidance value for stock option expense (SOE) |
| `anl4_fs_guidances_advanced_qf_nd_soe_minguidance` | MATRIX | Stock option expense - minimum guidance value |
| `anl4_fs_guidances_advanced_qf_nd_tbvps_maxguidance` | MATRIX | Tangible Book Value per Share maximum guidance value |
| `anl4_fs_guidances_advanced_qf_nd_tbvps_minguidance` | MATRIX | Tangible Book Value per Share - minimum guidance value |
| `anl4_fs_guidances_advanced_qf_nd_totassets_maxguidance` | MATRIX | Maximum guidance value for Total Assets |
| `anl4_fs_guidances_advanced_qf_nd_totassets_minguidance` | MATRIX | Minimum guidance value for Total Assets |
| `anl4_fs_guidances_advanced_qf_nd_totgw_maxguidance` | MATRIX | Maximum guidance value for Total Goodwill, i.e., the upper bound of the provided guidance range |
| `anl4_fs_guidances_advanced_qf_nd_totgw_minguidance` | MATRIX | Minimum guidance value for Total Goodwill |
| `anl4_fs_guidances_basic_af_nd_cfps_maxguidance` | MATRIX | Maximum guidance value for Cash Flow Per Share on an annual basis |
| `anl4_fs_guidances_basic_af_nd_cfps_minguidance` | MATRIX | Minimum guidance value for Cash Flow Per Share on an annual basis |
| `anl4_fs_guidances_basic_af_nd_div_maxguidance` | MATRIX | Maximum guidance value for Dividend per share on an annual basis |
| `anl4_fs_guidances_basic_af_nd_div_minguidance` | MATRIX | Minimum guidance value for Dividend per share on an annual basis |
| `anl4_fs_guidances_basic_af_nd_eps_maxguidance` | MATRIX | Maximum guidance value for Earnings Per Share on an annual basis |
| `anl4_fs_guidances_basic_af_nd_eps_minguidance` | MATRIX | Minimum guidance value for Earnings Per Share on an annual basis |
| `anl4_fs_guidances_basic_af_nd_eps_value` | MATRIX | Earnings Per Share — guidance value for annual frequency |
| `anl4_fs_guidances_basic_af_nd_sales_maxguidance` | MATRIX | Maximum guidance value for annual sales |
| `anl4_fs_guidances_basic_af_nd_sales_minguidance` | MATRIX | Minimum sales guidance for the annual period |
| `anl4_fs_guidances_basic_af_nd_sales_value` | MATRIX | Sales — guidance value for the annual period |
| `anl4_fs_guidances_basic_qf_nd_cfps_maxguidance` | MATRIX | Upper bound of the company’s Cash Flow Per Share guidance range |
| `anl4_fs_guidances_basic_qf_nd_cfps_minguidance` | MATRIX | Lower bound of the company’s Cash Flow Per Share guidance range |
| `anl4_fs_guidances_basic_qf_nd_div_maxguidance` | MATRIX | Upper bound of the company’s Dividend per share guidance range |
| `anl4_fs_guidances_basic_qf_nd_div_minguidance` | MATRIX | Lower bound of the company’s Dividend per share guidance range |
| `anl4_fs_guidances_basic_qf_nd_eps_maxguidance` | MATRIX | Upper bound of the company’s EPS guidance range |
| `anl4_fs_guidances_basic_qf_nd_eps_minguidance` | MATRIX | Lower bound of the company’s EPS guidance range |
| `anl4_fs_guidances_basic_qf_nd_eps_value` | MATRIX | Current EPS guidance value |
| `anl4_fs_guidances_basic_qf_nd_sales_maxguidance` | MATRIX | Upper bound of the company’s Sales guidance range |
| `anl4_fs_guidances_basic_qf_nd_sales_minguidance` | MATRIX | Lower bound of the company’s Sales guidance range |
| `anl4_fs_guidances_basic_qf_nd_sales_value` | MATRIX | Current Sales guidance value |
| `anl4_fsactualafv4_actual` | VECTOR | Announced financial data |
| `anl4_fsactualafv4_item` | VECTOR | Financial item |
| `anl4_fsactualqfv4_actual` | VECTOR | Announced financial data |
| `anl4_fsactualqfv4_item` | VECTOR | Financial item |
| `anl4_fsdetailltv4v104_item` | VECTOR | Financial item |
| `anl4_fsdetailrecv4v104_item` | VECTOR | Financial item |
| `anl4_fsdtlestmtafv4_item` | VECTOR | Financial item |
| `anl4_fsdtlestmtbscqv104_item` | VECTOR | Financial item |
| `anl4_fsdtlestmtbscv104_item` | VECTOR | Financial item |
| `anl4_fsdtlestmtqfv4_item` | VECTOR | Financial item |
| `anl4_fsdtlestmtsafv4_item` | VECTOR | Financial item |
| `anl4_fsgdncbscv4_maxguidance` | VECTOR | Max guidance value |
| `anl4_fsgdncbscv4_minguidance` | VECTOR | Minimum guidance value |
| `anl4_fsguidanceafv4_item` | VECTOR | Financial item |
| `anl4_fsguidanceafv4_maxguidance` | VECTOR | Maximum guidance value |
| `anl4_fsguidanceafv4_minguidance` | VECTOR | Min guidance value |
| `anl4_fsguidancebasicqfv4_item` | VECTOR | Financial item |
| `anl4_fsguidanceqfv4_item` | VECTOR | Financial item |
| `anl4_fsguidanceqfv4_maxguidance` | VECTOR | Max guidance value |
| `anl4_fsguidanceqfv4_minguidance` | VECTOR | Min guidance value |
| `anl4_gric_flag` | MATRIX | Gross income - forecast type (revision/new/...) |
| `anl4_gric_high` | MATRIX | Gross income - The highest estimation |
| `anl4_gric_low` | MATRIX | Gross income - The lowest estimation |
| `anl4_gric_mean` | MATRIX | Gross income - mean of estimations |
| `anl4_gric_median` | MATRIX | Gross income - median of estimations |
| `anl4_gric_number` | MATRIX | Gross income - number of estimations |
| `anl4_gric_std` | MATRIX | Gross income - std of estimations |
| `anl4_gric_value` | MATRIX | Gross income- announced financial value |
| `anl4_guiafv4_est` | VECTOR | Estimation value |
| `anl4_guibasicqfv4_est` | VECTOR | Estimation value |
| `anl4_guiqfv4_est` | VECTOR | Estimation value |
| `anl4_hold` | VECTOR | The number of recommendations not clear about short or long the instrument |
| `anl4_mark` | VECTOR | Recommendation consensus score |
| `anl4_median_capexp` | MATRIX | Capital Expenditures - median of estimations |
| `anl4_median_epsreported` | MATRIX | GAAP Earnings per share - median of estimations |
| `anl4_medianepsbfam` | MATRIX | Earnings before interest, taxes, depreciation and amortization - median of estimations |
| `anl4_netdebt_flag` | MATRIX | Net debt - forecast type (revision/new/...) |
| `anl4_netdebt_high` | MATRIX | Net debt - the highest estimation |
| `anl4_netdebt_low` | MATRIX | Net debt - the lowest estimation |
| `anl4_netdebt_mean` | MATRIX | Net debt - mean of estimations |
| `anl4_netdebt_median` | MATRIX | Net Debt - median of estimations |
| `anl4_netdebt_number` | MATRIX | Net debt - Number of estimations |
| `anl4_netprofit_flag` | MATRIX | Net profit - forecast type (revision/new/...) |
| `anl4_netprofit_high` | MATRIX | Net Profit - The highest estimation |
| `anl4_netprofit_low` | MATRIX | Net Profit - The Lowest Estimation |
| `anl4_netprofit_mean` | MATRIX | Net profit - mean of estimations |
| `anl4_netprofit_median` | MATRIX | Net profit - Median of estimations |
| `anl4_netprofit_number` | MATRIX | Net profit - number of estimations |
| `anl4_netprofit_std` | MATRIX | Net profit - standard deviation of estimations |
| `anl4_netprofit_value` | MATRIX | Net profit- announced financial value |
| `anl4_netprofita_high` | MATRIX | Adjusted Net Income - the highest estimation |
| `anl4_netprofita_low` | MATRIX | Adjusted net income - the lowest estimation |
| `anl4_netprofita_mean` | MATRIX | Adjusted net income - mean of estimations |
| `anl4_netprofita_median` | MATRIX | Adjusted net income - median of estimations |
| `anl4_netprofita_number` | MATRIX | Adjusted net income - number of estimations |
| `anl4_netprofita_std` | MATRIX | Adjusted net income - std of estimations |
| `anl4_netprofita_value` | MATRIX | Adjusted net income- announced financial value |
| `anl4_norec` | VECTOR | The number of brokers with no recommendation |
| `anl4_ptp_flag` | MATRIX | Pretax income - forecast type (revision/new/...) |
| `anl4_ptp_high` | MATRIX | Pretax income - the highest estimation |
| `anl4_ptp_low` | MATRIX | Pretax income - the lowest estimation |
| `anl4_ptp_mean` | MATRIX | Pretax income - mean of estimations |
| `anl4_ptp_median` | MATRIX | Pretax income - median of estimations |
| `anl4_ptp_number` | MATRIX | Pretax Income - number of estimations |
| `anl4_ptp_value` | MATRIX | Pretax income- announced financial value |
| `anl4_ptpr_flag` | MATRIX | Reported Pretax income - forecast type (revision/new/...) |
| `anl4_ptpr_high` | MATRIX | Reported pretax income - the highest estimation |
| `anl4_ptpr_low` | MATRIX | Reported Pretax Income - The Lowest Estimation |
| `anl4_ptpr_mean` | MATRIX | Reported Pretax income - mean of estimations |
| `anl4_ptpr_median` | MATRIX | Reported pretax income - Median of estimations |
| `anl4_ptpr_number` | MATRIX | Reported Pretax Income - number of estimations |
| `anl4_qf_az_cfps_mean` | MATRIX | Cash Flow Per Share - average of estimations |
| `anl4_qf_az_cfps_median` | MATRIX | Cash Flow Per Share - Median value among forecasts |
| `anl4_qf_az_cfps_number` | MATRIX | Cash Flow Per Share - number of estimations |
| `anl4_qf_az_div_mean` | MATRIX | Dividend per share - average of estimations |
| `anl4_qf_az_div_median` | MATRIX | Dividend per share - median of estimations |
| `anl4_qf_az_div_number` | MATRIX | Dividend per share - number of estimations |
| `anl4_qf_az_dts_spe` | MATRIX | Earnings per share - std of estimations |
| `anl4_qf_az_eps` | MATRIX | EPS - aggregation on estimations, 50th percentile |
| `anl4_qf_az_eps_mean` | MATRIX | Earnings per share - mean of estimations |
| `anl4_qf_az_eps_number` | MATRIX | Earnings per share - number of estimations |
| `anl4_qf_az_hgih_spe` | MATRIX | Earnings per share - The highest estimation |
| `anl4_qf_az_hgih_spfc` | MATRIX | Cash Flow - The highest estimation, per share |
| `anl4_qf_az_hgih_vid` | MATRIX | Dividend per share - The highest estimation |
| `anl4_qf_az_wol_spe` | MATRIX | Earnings per share - The lowest estimation |
| `anl4_qf_az_wol_spfc` | MATRIX | Cash Flow Per Share - The lowest estimation |
| `anl4_qf_az_wol_vid` | MATRIX | Dividend per share - The lowest value among forecasts |
| `anl4_qfd1_az_cfps_median` | MATRIX | Cash Flow Per Share - Median value among forecasts |
| `anl4_qfd1_az_cfps_number` | MATRIX | Cash Flow Per Share - number of estimations |
| `anl4_qfd1_az_div_median` | MATRIX | Dividend per share - median of estimations |
| `anl4_qfd1_az_div_number` | MATRIX | Dividend per share - number of estimations |
| `anl4_qfd1_az_dts_spe` | MATRIX | Earnings per share - std of estimations |
| `anl4_qfd1_az_eps_number` | MATRIX | Earnings per share - number of estimations |
| `anl4_qfd1_az_hgih_spe` | MATRIX | Earnings per share - The highest estimation |
| `anl4_qfd1_az_hgih_spfc` | MATRIX | Cash Flow - The highest estimation, per share |
| `anl4_qfd1_az_hgih_vid` | MATRIX | Dividend per share - The highest estimation |
| `anl4_qfd1_az_wol_spe` | MATRIX | Earnings per share - The lowest estimation |
| `anl4_qfd1_az_wol_spfc` | MATRIX | Cash Flow Per Share - The lowest estimation |
| `anl4_qfd1_az_wol_vid` | MATRIX | Dividend per share - The lowest value among forecasts |
| `anl4_qfd1_azeps` | MATRIX | EPS - aggregation on estimations, 50th percentile |
| `anl4_qfv4_actual` | VECTOR | Announced financial data |
| `anl4_qfv4_cfps_high` | MATRIX | Cash Flow Per Share - The highest estimation for the quarter |
| `anl4_qfv4_cfps_low` | MATRIX | Cash Flow Per Share - The lowest estimation |
| `anl4_qfv4_cfps_mean` | MATRIX | Cash Flow Per Share - average of estimations |
| `anl4_qfv4_cfps_median` | MATRIX | Cash Flow Per Share - Median value among forecasts |
| `anl4_qfv4_cfps_number` | MATRIX | Cash Flow Per Share - number of estimations |
| `anl4_qfv4_div_high` | MATRIX | Dividend per share - The highest estimation |
| `anl4_qfv4_div_low` | MATRIX | Dividend per share - The lowest estimation |
| `anl4_qfv4_div_mean` | MATRIX | Dividend per share - mean of estimations |
| `anl4_qfv4_div_median` | MATRIX | Dividend per share - median of estimations |
| `anl4_qfv4_div_number` | MATRIX | Dividend - number of estimations |
| `anl4_qfv4_dts_spe` | MATRIX | Earnings per share - standard deviation of estimations |
| `anl4_qfv4_eps_high` | MATRIX | Earnings per share - The highest estimation |
| `anl4_qfv4_eps_low` | MATRIX | Earnings per share - The lowest estimation |
| `anl4_qfv4_eps_mean` | MATRIX | Earnings per share - mean of estimations |
| `anl4_qfv4_eps_number` | MATRIX | Earnings per share - number of estimations |
| `anl4_qfv4_maxguidance` | VECTOR | Max guidance value |
| `anl4_qfv4_median_eps` | MATRIX | Earnings per share - median of estimations |
| `anl4_qfv4_minguidance` | VECTOR | Min guidance value |
| `anl4_rd_exp_flag` | MATRIX | Research and Development Expense - forecast type (revision/new/...) |
| `anl4_rd_exp_high` | MATRIX | Research and Development Expense - the highest estimation |
| `anl4_rd_exp_low` | MATRIX | Research and Development Expense - the lowest estimation |
| `anl4_rd_exp_mean` | MATRIX | Research and Development Expense - mean of estimations |
| `anl4_rd_exp_median` | MATRIX | Research and Development Expense - Median of estimations |
| `anl4_rd_exp_number` | MATRIX | Research and Development Expense - Number of Estimations |
| `anl4_tbve_ft` | MATRIX | Tangible Book Value per Share - forecast type (revision/new/...) |
| `anl4_tbvps_high` | MATRIX | Tangible Book Value per Share - The highest estimation |
| `anl4_tbvps_low` | MATRIX | Tangible Book Value per Share - The lowest estimation |
| `anl4_tbvps_mean` | MATRIX | Tangible Book Value per Share - mean of estimations |
| `anl4_tbvps_median` | MATRIX | Tangible Book Value per Share - median of estimations |
| `anl4_tbvps_number` | MATRIX | Tangible Book Value per Share - number of estimations |
| `anl4_tot_gw_ft` | MATRIX | Total Goodwill - forecast type (revision/new/...) |
| `anl4_total_rec` | VECTOR | The total number of recommendations |
| `anl4_totassets_flag` | MATRIX | Total Assets - forecast type (revision/new/...) |
| `anl4_totassets_high` | MATRIX | Total Assets - The highest estimation |
| `anl4_totassets_low` | MATRIX | Total Assets - The lowest estimation |
| `anl4_totassets_mean` | MATRIX | Total Assets - mean of estimations |
| `anl4_totassets_median` | MATRIX | Total Assets - median of estimations |
| `anl4_totassets_number` | MATRIX | Total Assets - number of estimations |
| `anl4_totassets_std` | MATRIX | Total Assets - standard deviation of estimations |
| `anl4_totassets_value` | MATRIX | Total Assets - actual value |
| `anl4_totgw_high` | MATRIX | Total Goodwill - The highest estimation |
| `anl4_totgw_low` | MATRIX | Total Goodwill - The lowest estimation |
| `anl4_totgw_mean` | MATRIX | Total Goodwill - mean of estimations |
| `anl4_totgw_median` | MATRIX | Total Goodwill - median of estimations |
| `anl4_totgw_number` | MATRIX | Total Goodwill - number of estimations |
| `anl4_under` | VECTOR | The number of Underweight recommendations |
| `avg_capex_quarterly_estimate` | MATRIX | The arithmetic average of broker estimates for capital expenditures in the current quarter. |
| `avg_ebitda_quarterly_estimate` | MATRIX | The arithmetic average of quarterly broker estimates for earnings before interest, taxes, depreciation, and amortizat… |
| `avg_pretax_profit_quarterly_estimate` | MATRIX | The arithmetic average of broker estimates for pretax profit in the current quarter. |
| `avg_total_assets_quarterly_estimate` | MATRIX | The arithmetic average of broker estimates for total assets in the current quarter. |
| `basic_shares_max_guidance_qtr` | MATRIX | The maximum guidance value for Basic Shares. |
| `book_value_per_share_2` | MATRIX | Book Value Per Share - Actual Value |
| `book_value_per_share_avg` | MATRIX | Average book value per share. |
| `book_value_per_share_max` | MATRIX | Highest estimate of book value per share. |
| `book_value_per_share_median` | MATRIX | Median value of book value per share. |
| `book_value_per_share_min` | MATRIX | Lowest estimate of book value per share. |
| `book_value_per_share_min_guidance_qtr` | MATRIX | Book value per share - minimum guidance value |
| `book_value_per_share_reported_value` | MATRIX | Book Value Per Share - Actual Value |
| `capital_expenditure_amount` | MATRIX | Capital Expenditures - Total value |
| `capital_expenditure_guidance_value` | MATRIX | Capital Expenditures - Total value for the annual guidance |
| `capital_expenditure_max` | MATRIX | Highest estimate of capital expenditures for the period. |
| `capital_expenditure_max_guidance_qtr` | MATRIX | The maximum guidance value for Capital Expenditures |
| `capital_expenditure_median` | MATRIX | Median value of capital expenditures for the period. |
| `capital_expenditure_min` | MATRIX | Minimum projected spending on fixed assets for the period. |
| `capital_expenditure_reported_value` | MATRIX | Capital Expenditures - Total (Cash Flow/Investing) (Millions) |
| `capital_expenditure_stddev` | MATRIX | Standard deviation of capital expenditure estimates. |
| `cash_flow_financing_max_guidance` | MATRIX | Cash Flow From Financing - Maximum guidance value provided annually |
| `cash_flow_from_financing` | MATRIX | Cash Flow From Financing - Value |
| `cash_flow_from_investing` | MATRIX | Cash Flow from Investing - Value |
| `cash_flow_from_operations` | MATRIX | Cash Flow from Operations - Value for the annual period |
| `cash_flow_operations_min_guidance` | MATRIX | Minimum guidance value for Cash Flow from Operations on an annual basis. |
| `cashflow_financing_avg` | MATRIX | Average cash flows from financing activities. |
| `cashflow_financing_max` | MATRIX | Highest estimate of cash flows from financing activities. |
| `cashflow_financing_median` | MATRIX | Median value of cash flows from financing activities. |
| `cashflow_financing_min` | MATRIX | Lowest estimate of cash flows from financing activities. |
| `cashflow_investing_avg` | MATRIX | Average cash flows from investing activities. |
| `cashflow_investing_max` | MATRIX | Highest estimate of cash flows from investing activities. |
| `cashflow_investing_median` | MATRIX | Median value of cash flows from investing activities. |
| `cashflow_investing_min` | MATRIX | Lowest estimate of cash flows from investing activities. |
| `cashflow_per_share_average` | MATRIX | Cash Flow Per Share - average of estimations with a delay of 1 quarter |
| `cashflow_per_share_estimate_count` | MATRIX | Cash Flow Per Share - number of estimations - delay1 |
| `cashflow_per_share_max_guidance` | MATRIX | The maximum guidance value for Cash Flow Per Share on an annual basis. |
| `cashflow_per_share_max_guidance_quarterly` | MATRIX | The maximum guidance value for Cash Flow Per Share. |
| `cashflow_per_share_maximum` | MATRIX | Cash Flow - The highest estimation, per share, with a delay of 1 quarter |
| `cashflow_per_share_median_value` | MATRIX | Cash Flow Per Share - Median value among forecasts |
| `cashflow_per_share_min_guidance` | MATRIX | Cash Flow Per Share - Minimum guidance value for the annual period |
| `cashflow_per_share_min_guidance_quarterly` | MATRIX | Minimum guidance value for Cash Flow Per Share |
| `cashflow_per_share_minimum` | MATRIX | Cash Flow Per Share - The lowest estimation, delay 1 quarter |
| `dividend_estimate_average` | MATRIX | Dividend per share - average of estimations - delay 1 |
| `dividend_estimate_count` | MATRIX | Dividend per share - number of estimations with a delay of 1 quarter |
| `dividend_estimate_maximum` | MATRIX | Dividend per share - The highest value among forecasts with a delay of 1 quarter |
| `dividend_estimate_median_value` | MATRIX | Dividend per share - median of estimations |
| `dividend_estimate_minimum` | MATRIX | Dividend per share - The lowest value among forecasts - D1 |
| `dividend_estimate_standard_deviation` | MATRIX | Dividend per share - standard deviation of estimations |
| `dividend_estimate_stddev_quarterly` | MATRIX | Dividend per share - standard deviation of estimations |
| `dividend_estimate_value` | VECTOR | Dividend per share - estimated value |
| `dividend_max_guidance_quarterly` | MATRIX | Maximum guidance value for Dividend per share |
| `dividend_max_guidance_value` | MATRIX | The maximum guidance value for Dividend per share on an annual basis. |
| `dividend_min_guidance_quarterly` | MATRIX | Minimum guidance value for Dividend per share |
| `dividend_min_guidance_value` | MATRIX | Minimum guidance value for Dividend per share on an annual basis |
| `dividend_previous_estimate_value` | VECTOR | The previous estimation of dividend |
| `earnings_per_share_average` | MATRIX | Earnings per share - mean of estimations |
| `earnings_per_share_estimate_count` | MATRIX | Earnings per share - number of estimations |
| `earnings_per_share_guidance_value` | MATRIX | Earnings Per Share - guidance value for annual frequency |
| `earnings_per_share_max_guidance` | MATRIX | The maximum guidance value for Earnings Per Share on an annual basis. |
| `earnings_per_share_maximum` | MATRIX | Earnings per share - The highest estimation |
| `earnings_per_share_median_value` | MATRIX | Earnings per share - median of estimations |
| `earnings_per_share_min_guidance` | MATRIX | Minimum guidance value for Earnings Per Share on an annual basis. |
| `earnings_per_share_minimum` | MATRIX | Earnings per share - The lowest estimation |
| `earnings_per_share_nongaap_value` | MATRIX | Non-GAAP Earnings Per Share - Actual Value |
| `earnings_per_share_reported` | MATRIX | Reported Earnings Per Share - Actual Value |
| `earnings_per_share_reported_value` | MATRIX | Reported Earnings Per Share - Actual Value |
| `earnings_per_share_standard_deviation` | MATRIX | Earnings per share - standard deviation of estimations |
| `ebit_avg` | MATRIX | Average operating profit before interest and taxes. |
| `ebit_max` | MATRIX | Highest estimate of operating profit before interest and taxes. |
| `ebit_median` | MATRIX | Median value of operating profit before interest and taxes. |
| `ebit_min` | MATRIX | Lowest estimate of operating profit before interest and taxes. |
| `ebit_reported_value` | MATRIX | Earnings Before Interest & Taxes - actual value for the quarter |
| `ebit_stddev` | MATRIX | Standard deviation of operating profit before interest and taxes. |
| `ebitda_max` | MATRIX | Highest estimate of EBITDA for the period. |
| `ebitda_median` | MATRIX | Median value of EBITDA for the period. |
| `ebitda_min` | MATRIX | Lowest estimate of EBITDA for the period. |
| `ebitda_reported_value` | MATRIX | EBITDA value for the quarter. |
| `ebitda_stddev` | MATRIX | Standard deviation of EBITDA estimates, indicating variability. |
| `eps_adjusted_min_guidance_qtr` | MATRIX | Minimum guidance value for adjusted Earnings per share excluding extraordinary items and stock option expenses. |
| `eps_adjusted_min_guidance_value` | MATRIX | The minimum guidance value for adjusted earnings per share excluding extraordinary items and stock option expenses on… |
| `eps_estimate_value` | VECTOR | Earnings per share - estimation value |
| `eps_guidance_value_quarterly` | MATRIX | Earnings Per Share - Basic value |
| `eps_max_guidance_quarterly` | MATRIX | The maximum guidance value for Earnings Per Share. |
| `eps_min_guidance_quarterly` | MATRIX | Minimum guidance value for Earnings per Share |
| `eps_previous_estimate_value` | VECTOR | The previous estimation of Earnings Per Share |
| `eps_reported_avg` | MATRIX | Average reported earnings per share. |
| `eps_reported_max` | MATRIX | Highest estimate of reported earnings per share. |
| `eps_reported_median` | MATRIX | Median value of reported earnings per share. |
| `eps_reported_min_guidance_qtr` | MATRIX | Reported Earnings Per Share - Minimum guidance value |
| `est_bookvalue_ps` | MATRIX | Book value per share - average of estimations |
| `est_capex` | MATRIX | Capital Expenditures - mean of estimations |
| `est_cashflow_fin` | MATRIX | Cash Flow From Financing - mean of estimations |
| `est_cashflow_invst` | MATRIX | Cash Flow From Investing - mean of estimations |
| `est_cashflow_op` | MATRIX | Cash Flow From Operations - mean of estimations |
| `est_cashflow_ps` | MATRIX | Cash Flow Per Share - average of estimations |
| `est_dividend_ps` | MATRIX | Dividend per share - average of estimations |
| `est_ebit` | MATRIX | Earnings before interest and taxes - mean of estimations |
| `est_ebitda` | MATRIX | Earnings before interest, taxes, depreciation, and amortization - mean of estimations |
| `est_eps` | MATRIX | Earnings per share - mean of estimations |
| `est_epsa` | MATRIX | Earnings per share adjusted by excluding extraordinary items and stock option expenses - average of estimations |
| `est_epsr` | MATRIX | GAAP Earnings per share - mean of estimations |
| `est_fcf` | MATRIX | Free Cash Flow - Mean of Estimations |
| `est_fcf_ps` | MATRIX | Free Cash Flow Per Share - Mean of Estimations |
| `est_ffo` | MATRIX | Funds From Operation - Summary on Estimations, Mean |
| `est_grossincome` | MATRIX | Gross income - Mean of estimations |
| `est_netdebt` | MATRIX | Net debt - mean of estimations |
| `est_netprofit` | MATRIX | Net profit - mean of estimations |
| `est_netprofit_adj` | MATRIX | Adjusted net income - Mean of estimations |
| `est_ptp` | MATRIX | Pretax income - mean of estimations |
| `est_ptpr` | MATRIX | Reported pretax income - mean of estimations |
| `est_rd_expense` | MATRIX | Research and Development Expense - mean of estimations |
| `est_sales` | MATRIX | Sales - mean of estimations |
| `est_sga` | MATRIX | SGA - mean of estimations |
| `est_shequity` | MATRIX | Mean of SH Equity segment - mean of estimations |
| `est_tbv_ps` | MATRIX | Tangible Book Value per Share - mean of estimations |
| `est_tot_assets` | MATRIX | Total Assets - mean of estimations |
| `est_tot_goodwill` | MATRIX | Total Goodwill - mean of estimations |
| `estimate_value_currency_code` | VECTOR | Home currency of instrument |
| `estimate_value_currency_code_detail_qtr` | VECTOR | Home currency of instrument |
| `estimate_value_currency_code_qtr` | VECTOR | Home currency of instrument |
| `financing_cashflow_reported_value` | MATRIX | Cash Flow From Financing - Value |
| `free_cash_flow_per_share` | MATRIX | Free cash flow per share - actual financial value for the annual period |
| `free_cash_flow_per_share_actual_value` | MATRIX | Free cash flow per share- announced financial value |
| `free_cash_flow_per_share_max_guidance` | MATRIX | The maximum guidance value for Free Cash Flow Per Share on an annual basis. |
| `free_cash_flow_per_share_reported_value` | MATRIX | Free cash flow per share- announced financial value |
| `free_cash_flow_reported_value` | MATRIX | Free cash flow value for the quarter. |
| `free_cash_flow_total` | MATRIX | Free Cash Flow value - Annual |
| `free_cashflow_avg` | MATRIX | Average free cash flow for the period. |
| `free_cashflow_max` | MATRIX | Highest estimate of free cash flow for the period. |
| `free_cashflow_min` | MATRIX | Lowest estimate of free cash flow for the period. |
| `free_cashflow_per_share_avg` | MATRIX | Average free cash flow per share. |
| `free_cashflow_per_share_max` | MATRIX | Highest estimate of free cash flow per share. |
| `free_cashflow_per_share_median` | MATRIX | Median value of free cash flow per share. |
| `funds_from_operations_max_guidance` | MATRIX | The maximum guidance value for Funds from operation - annual |
| `goodwill_min_guidance_qtr` | MATRIX | Minimum guidance value for Total Goodwill |
| `gross_income_avg` | MATRIX | Average gross income for the period. |
| `gross_income_max` | MATRIX | Highest estimate of gross income for the period. |
| `gross_income_median` | MATRIX | Median value of gross income for the period. |
| `gross_income_reported_value` | MATRIX | Gross Income value for the quarter |
| `gross_income_total` | MATRIX | Gross Income value on an annual basis |
| `guidance_estimate_value` | VECTOR | Estimated value for basic annual financial guidance |
| `guidance_previous_estimate_value_qtr` | VECTOR | The previous estimation of finanicial item |
| `guidance_reporting_currency` | MATRIX | Pricing Currency where the security trades - Annual |
| `guidance_value_currency_code_qtr` | VECTOR | Home currency of instrument |
| `highest_sales_estimate` | MATRIX | Sales - The highest estimation for the annual period |
| `investing_cashflow_reported_value` | MATRIX | Cash Flow from Investing - Value |
| `lowest_sales_estimate` | MATRIX | Sales - The lowest estimation for the annual period |
| `max_adj_net_income_quarterly_estimate` | MATRIX | The highest broker estimate for adjusted net profit in the current quarter. |
| `max_adjusted_eps_guidance` | MATRIX | The maximum guidance value for adjusted earnings per share. |
| `max_adjusted_eps_guidance_2` | MATRIX | The maximum guidance value for adjusted earnings per share on an annual basis. |
| `max_adjusted_funds_from_operations_adj_guidance` | MATRIX | Adjusted funds from operation - Maximum guidance value |
| `max_adjusted_funds_from_operations_guidance` | MATRIX | Max guidance value for Funds from operation |
| `max_adjusted_funds_from_operations_guidance_2` | MATRIX | Adjusted funds from operation - maximum guidance value for the annual period |
| `max_adjusted_net_income_guidance` | MATRIX | The maximum guidance value for Adjusted net income. |
| `max_adjusted_net_profit_guidance` | MATRIX | The maximum guidance value for adjusted net profit on an annual basis. |
| `max_book_value_per_share_guidance` | MATRIX | Book value per share - Maximum value among forecasts |
| `max_book_value_per_share_guidance_2` | MATRIX | Book value per share - Maximum guidance value for the annual period |
| `max_capital_expenditure_guidance` | MATRIX | The maximum guidance value for Capital Expenditures on an annual basis. |
| `max_custom_eps_guidance` | MATRIX | Custom Earnings per share - The highest guidance value |
| `max_customized_eps_guidance` | MATRIX | The maximum guidance value for custom earnings per share on an annual basis. |
| `max_ebit_guidance` | MATRIX | The maximum guidance value for Earnings Before Interest and Taxes (EBIT) on an annual basis. |
| `max_ebitda_guidance` | MATRIX | The maximum guidance value for Earnings Before Interest, Taxes, Depreciation, and Amortization (EBITDA) on an annual … |
| `max_financing_cashflow_guidance` | MATRIX | Cash Flow From Financing - Maximum guidance value |
| `max_free_cash_flow_guidance` | MATRIX | The maximum guidance value for Free Cash Flow on an annual basis. |
| `max_free_cashflow_guidance` | MATRIX | The maximum guidance value for Free Cash Flow. |
| `max_free_cashflow_per_share_guidance` | MATRIX | The maximum guidance value for free cash flow per share. |
| `max_gross_income_guidance` | MATRIX | The maximum guidance value for Gross Income. |
| `max_gross_income_guidance_2` | MATRIX | The maximum guidance for Gross Income on an annual basis. |
| `max_investing_cashflow_guidance` | MATRIX | The maximum guidance value for Cash Flow from Investing. |
| `max_investing_cashflow_guidance_2` | MATRIX | The maximum guidance value for Cash Flow from Investing activities on an annual basis. |
| `max_net_debt_guidance` | MATRIX | The maximum guidance value for Net Debt on an annual basis. |
| `max_net_income_guidance` | MATRIX | The maximum guidance value for net profit. |
| `max_net_profit_guidance` | MATRIX | The maximum guidance value for net profit on an annual basis. |
| `max_net_profit_quarterly_estimate` | MATRIX | The highest broker estimate for net profit in the current quarter. |
| `max_operating_cashflow_guidance` | MATRIX | The maximum guidance value for Cash Flow from Operations. |
| `max_operating_cashflow_guidance_2` | MATRIX | The maximum guidance value for Cash Flow from Operations on an annual basis. |
| `max_pretax_profit_guidance` | MATRIX | The maximum guidance value for Pretax income on an annual basis. |
| `max_reported_eps_guidance` | MATRIX | Reported Earnings Per Share - Maximum guidance value |
| `max_reported_eps_guidance_2` | MATRIX | Reported Earnings Per Share - Maximum guidance value for the annual period |
| `max_reported_pretax_income_guidance` | MATRIX | Reported Pretax income- maximum guidance value |
| `max_reported_pretax_income_guidance_2` | MATRIX | Reported Pretax income- maximum guidance value |
| `max_reported_pretax_profit_quarterly_estimate` | MATRIX | The highest broker estimate for reported pretax profit in the current quarter. |
| `max_research_development_expense_guidance` | MATRIX | The maximum guidance value for Research and Development Expense. |
| `max_selling_general_admin_guidance` | MATRIX | The maximum guidance value for Selling, General & Administrative Expense |
| `max_share_buyback_guidance` | MATRIX | Maximum guidance value for Shares Basic - Annual |
| `max_shareholders_equity_guidance` | MATRIX | The maximum guidance value for Total Shareholders' Equity. |
| `max_shares_outstanding_guidance` | MATRIX | The maximum guidance for Shares |
| `max_stock_option_expense_guidance` | MATRIX | Stock option expense - Maximum guidance value for the annual period |
| `max_tangible_book_value_per_share_guidance` | MATRIX | Tangible Book Value per Share - maximum guidance value |
| `max_total_assets_guidance` | MATRIX | The maximum guidance value for Total Assets. |
| `max_total_assets_guidance_2` | MATRIX | The maximum guidance value for Total Assets |
| `max_total_assets_quarterly_estimate` | MATRIX | The highest broker estimate for total assets in the current quarter. |
| `max_total_goodwill_guidance` | MATRIX | The maximum guidance value for Total Goodwill. |
| `max_total_goodwill_guidance_2` | MATRIX | The maximum guidance value for Total Goodwill on an annual basis. |
| `maximum_guidance_value` | VECTOR | Maximum guidance value for basic annual financials |
| `median_free_cash_flow_quarterly_estimate` | MATRIX | The median broker estimate for free cash flow in the current quarter. |
| `median_sales_estimate` | MATRIX | Sales - median of estimations |
| `min_adj_net_income_quarterly_estimate` | MATRIX | The lowest broker estimate for adjusted net profit in the current quarter. |
| `min_adjusted_funds_from_operations_adj_guidance` | MATRIX | Minimum guidance value for Adjusted funds from operation |
| `min_adjusted_funds_from_operations_guidance` | MATRIX | Funds from operation - minimum guidance value |
| `min_adjusted_funds_from_operations_guidance_2` | MATRIX | Adjusted funds from operation - minimum guidance for the annual period |
| `min_adjusted_net_income_guidance` | MATRIX | Adjusted net income - minimum guidance value |
| `min_basic_shares_guidance` | MATRIX | Shares Basic - Minimum guidance value |
| `min_book_value_per_share_guidance` | MATRIX | Book value per share - minimum guidance value for the annual period |
| `min_capex_guidance` | MATRIX | Minimum guidance value for Capital Expenditures |
| `min_capital_expenditure_guidance` | MATRIX | Minimum guidance value for Capital Expenditures |
| `min_custom_eps_guidance` | MATRIX | Custom Earnings per share - Minimum guidance value |
| `min_customized_eps_guidance` | MATRIX | Customized Earnings per share - Minimum guidance value for the annual period |
| `min_ebit_guidance` | MATRIX | Minimum guidance value for Earnings Before Interest and Taxes (EBIT) |
| `min_ebit_guidance_2` | MATRIX | Minimum guidance value for Earnings Before Interest and Taxes (EBIT) on an annual basis. |
| `min_ebitda_guidance` | MATRIX | Minimum guidance value for Earnings Before Interest, Taxes, Depreciation, and Amortization (EBITDA) - Annual |
| `min_financing_cashflow_guidance` | MATRIX | Minimum guidance value for Cash Flow From Financing |
| `min_financing_cashflow_guidance_2` | MATRIX | Minimum guidance value for Cash Flow From Financing on an annual basis |
| `min_free_cash_flow_guidance` | MATRIX | The minimum guidance value for Free Cash Flow on an annual basis. |
| `min_free_cash_flow_per_share_guidance` | MATRIX | Free cash flow per share - minimum guidance value for the annual period |
| `min_free_cash_flow_per_share_quarterly_estimate` | MATRIX | The lowest broker estimate for free cash flow per share in the current quarter. |
| `min_free_cashflow_guidance` | MATRIX | Minimum guidance value for Free Cash Flow |
| `min_free_cashflow_per_share_guidance` | MATRIX | Free cash flow per share - minimum guidance value |
| `min_funds_from_operations_guidance` | MATRIX | Funds from operation - minimum guidance value for annual period |
| `min_gross_income_guidance` | MATRIX | The minimum guidance value for Gross Income. |
| `min_gross_income_guidance_2` | MATRIX | The minimum guidance for Gross Income on an annual basis. |
| `min_gross_income_quarterly_estimate` | MATRIX | The lowest broker estimate for gross income in the current quarter. |
| `min_investing_cashflow_guidance` | MATRIX | Cash Flow From Investing - Minimum guidance value |
| `min_investing_cashflow_guidance_2` | MATRIX | Cash Flow From Investing - Minimum guidance value for the annual period |
| `min_net_debt_guidance` | MATRIX | The minimum guidance value for Net Debt on an annual basis. |
| `min_net_income_guidance` | MATRIX | Net profit - minimum guidance value |
| `min_net_profit_guidance` | MATRIX | Minimum guidance value for Net Profit on an annual basis |
| `min_operating_cashflow_guidance` | MATRIX | Minimum guidance value for Cash Flow from Operations |
| `min_pretax_profit_guidance` | MATRIX | Minimum guidance value for Pretax income |
| `min_pretax_profit_guidance_2` | MATRIX | The minimum guidance value for Pretax income on an annual basis. |
| `min_reported_eps_guidance` | MATRIX | Reported Earnings Per Share - Minimum guidance value for the annual period |
| `min_reported_eps_quarterly_estimate` | MATRIX | The lowest broker estimate for reported earnings per share in the current quarter. |
| `min_research_development_expense_guidance` | MATRIX | Minimum guidance value for Research & Development Expense |
| `min_research_development_expense_guidance_2` | MATRIX | Minimum guidance value for Research & Development Expense on an annual basis |
| `min_sg_and_a_expense_guidance` | MATRIX | Selling, General & Administrative Expense - Minimum guidance value |
| `min_share_buyback_guidance` | MATRIX | Shares Basic - Minimum guidance value for the annual period |
| `min_share_count_guidance` | MATRIX | Minimum guidance for shares on an annual basis |
| `min_shareholders_equity_guidance` | MATRIX | Minimum guidance value for Shareholders' Equity |
| `min_shares_outstanding_guidance` | MATRIX | Minimum guidance value for Shares |
| `min_stock_option_expense_guidance` | MATRIX | Stock option expense - minimum guidance value |
| `min_stock_option_expense_guidance_2` | MATRIX | Minimum guidance value for stock option expense on an annual basis |
| `min_tangible_book_value_per_share_guidance` | MATRIX | Tangible Book Value per Share - minimum guidance value |
| `min_tangible_book_value_per_share_guidance_2` | MATRIX | Tangible Book Value per Share - Minimum guidance value |
| `min_total_assets_guidance` | MATRIX | Minimum guidance value for Total Assets |
| `min_total_assets_guidance_2` | MATRIX | Minimum guidance value for Total Assets on an annual basis |
| `min_total_goodwill_guidance` | MATRIX | Total Goodwill - The lowest guidance value |
| `minimum_guidance_value` | VECTOR | Minimum guidance value for basic annual financials |
| `net_debt_actual_value` | MATRIX | Net debt- announced financial value |
| `net_debt_amount` | MATRIX | Net debt - actual value for the annual period |
| `net_debt_avg` | MATRIX | Average net debt, calculated as total debt minus cash. |
| `net_debt_max` | MATRIX | Highest estimate of net debt, calculated as total debt minus cash. |
| `net_debt_max_guidance_qtr` | MATRIX | Maximum guidance value for Net Debt |
| `net_debt_median` | MATRIX | Median value of net debt, calculated as total debt minus cash. |
| `net_debt_min` | MATRIX | Lowest estimate of net debt, calculated as total debt minus cash. |
| `net_debt_min_guidance_qtr` | MATRIX | Minimum guidance value for Net Debt |
| `net_debt_reported_value` | MATRIX | Net Debt value for the quarter |
| `net_income_adjusted` | MATRIX | Adjusted net income- announced financial value for annual frequency |
| `net_income_avg` | MATRIX | Average net profit after all expenses and taxes. |
| `net_income_median` | MATRIX | Median value of net profit after all expenses and taxes. |
| `net_income_min` | MATRIX | Lowest estimate of net profit after all expenses and taxes. |
| `net_income_stddev` | MATRIX | Standard deviation of net profit estimates. |
| `net_income_total_2` | MATRIX | Net profit- announced financial value for annual data |
| `net_profit_adjusted_min_guidance` | MATRIX | The minimum guidance value for adjusted net profit on an annual basis. |
| `net_profit_adjusted_value` | MATRIX | Adjusted net income- announced financial value |
| `net_profit_reported_value` | MATRIX | Net profit- announced financial value |
| `num_adj_net_income_est` | MATRIX | Number of estimates for adjusted net profit, excluding non-recurring items. |
| `num_book_value_per_share_est` | MATRIX | Number of estimates for book value per share. |
| `num_capex_est` | MATRIX | Number of estimates for capital expenditures. |
| `num_cashflow_financing_est` | MATRIX | Number of estimates for cash flows from financing activities. |
| `num_cashflow_investing_est` | MATRIX | Number of estimates for cash flows from investing activities. |
| `num_ebit_est` | MATRIX | Number of estimates for operating profit before interest and taxes. |
| `num_ebitda_estimates_quarter` | MATRIX | The count of broker estimates for EBITDA in the current quarter. |
| `num_eps_reported_est` | MATRIX | Number of estimates for reported earnings per share. |
| `num_free_cashflow_est` | MATRIX | Number of estimates for free cash flow. |
| `num_free_cashflow_per_share_est` | MATRIX | Number of estimates for free cash flow per share. |
| `num_gross_income_est` | MATRIX | Number of estimates for gross income. |
| `num_net_debt_est` | MATRIX | Number of estimates for net debt. |
| `num_net_income_est` | MATRIX | Number of estimates for net profit after all expenses and taxes. |
| `num_op_cash_flow_est` | MATRIX | Number of estimates for cash flow from operations. |
| `num_pretax_income_est` | MATRIX | Number of estimates for profit before taxes. |
| `num_pretax_income_reported_est` | MATRIX | Number of estimates for reported profit before taxes, including exceptional items. |
| `num_rnd_expense_est` | MATRIX | Number of estimates for research and development expenses. |
| `num_sga_estimates_quarter` | MATRIX | The count of broker estimates for selling, general, and administrative expenses in the current quarter. |
| `num_shareholders_equity_est` | MATRIX | Number of estimates for owners’ equity after liabilities. |
| `num_total_assets_est` | MATRIX | Number of estimates for total assets. |
| `num_total_goodwill_estimates_quarter` | MATRIX | The count of broker estimates for total goodwill in the current quarter. |
| `op_cash_flow_avg` | MATRIX | Average cash generated from core business operations. |
| `op_cash_flow_max` | MATRIX | Highest estimate of cash generated from core business operations. |
| `op_cash_flow_median` | MATRIX | Median value of cash generated from core business operations. |
| `op_cash_flow_min` | MATRIX | Lowest estimate of cash generated from core business operations. |
| `op_cash_flow_stddev` | MATRIX | Standard deviation of operating cash flow estimates. |
| `operating_cashflow_reported_value` | MATRIX | Cash Flow from Operations - Value |
| `operating_profit_before_depr_amort` | MATRIX | EBITDA value - Annual |
| `operating_profit_before_depr_amort_max_guidance_qtr` | MATRIX | Max guidance value for Earnings before interest, taxes, depreciation and amortization |
| `operating_profit_before_depr_amort_min_guidance_qtr` | MATRIX | Minimum guidance value for Earnings before interest, taxes, depreciation and amortization |
| `operating_profit_before_interest_tax` | MATRIX | Earnings Before Interest and Taxes (EBIT) - Actual Value |
| `operating_profit_max_guidance_qtr` | MATRIX | The maximum guidance value for Earnings Before Interest and Taxes. |
| `pretax_income_actual_reported_value` | MATRIX | Reported Pretax income- announced financial value |
| `pretax_income_max` | MATRIX | Highest estimate of profit before taxes. |
| `pretax_income_max_guidance_qtr` | MATRIX | The maximum guidance value for Pretax income. |
| `pretax_income_median` | MATRIX | Median value of profit before taxes. |
| `pretax_income_min` | MATRIX | Lowest estimate of profit before taxes. |
| `pretax_income_reported` | MATRIX | Reported Pretax income - actual value for the annual fiscal period |
| `pretax_income_reported_avg` | MATRIX | Average reported profit before taxes, including exceptional items. |
| `pretax_income_reported_median` | MATRIX | Median reported profit before taxes, including exceptional items. |
| `pretax_income_reported_min` | MATRIX | Lowest estimate of reported profit before taxes, including exceptional items. |
| `pretax_income_reported_min_guidance` | MATRIX | Reported Pretax income - minimum guidance value |
| `pretax_income_reported_min_guidance_qtr` | MATRIX | Reported Pretax income- minimum guidance value |
| `pretax_income_reported_value` | MATRIX | Reported Pretax income - actual value for the quarter |
| `pretax_income_standalone_value` | MATRIX | Pretax Profit - actual value for the quarter |
| `pretax_income_stddev` | MATRIX | Standard deviation of profit before taxes, showing estimate dispersion. |
| `pretax_income_total` | MATRIX | Pretax Profit - Value for the annual period |
| `previous_guidance_estimate` | VECTOR | The previous estimation of financial item - annual frequency |
| `previous_guidance_value_annual` | VECTOR | The previous estimation of finanicial item |
| `previous_quarterly_guidance_estimate` | VECTOR | The previous estimation of finanicial item |
| `previous_recommendation_value` | VECTOR | The previous estimation of financial item for recommendation |
| `reporting_currency_code_9` | MATRIX | Home currency of instrument |
| `research_development_expense` | MATRIX | Research & Development Expense - Actual Value (Annual) |
| `research_development_expense_actual_value` | MATRIX | Research and Development Expense- announced financial value |
| `research_development_expense_reported_value` | MATRIX | Research & Development (Income Statement) Value in Millions |
| `research_development_max_guidance` | MATRIX | The maximum guidance value for Research and Development Expense on an annual basis. |
| `rnd_expense_avg` | MATRIX | Average research and development expenses. |
| `rnd_expense_max` | MATRIX | Highest estimate of research and development expenses. |
| `rnd_expense_median` | MATRIX | Median value of research and development expenses. |
| `rnd_expense_min` | MATRIX | Lowest estimate of research and development expenses. |
| `sales_estimate_average` | MATRIX | Sales - mean of estimations with a delay of 1 quarter |
| `sales_estimate_average_annual` | MATRIX | Sales - mean of estimations |
| `sales_estimate_average_quarterly` | MATRIX | Sales - mean of estimations |
| `sales_estimate_count` | MATRIX | Sales - number of estimations |
| `sales_estimate_count_2` | MATRIX | Number of Sales estimates |
| `sales_estimate_count_quarterly` | MATRIX | Sales - number of estimations |
| `sales_estimate_dispersion` | MATRIX | Standard deviation of Sales estimations for the annual period. |
| `sales_estimate_maximum` | MATRIX | Sales - The highest estimation |
| `sales_estimate_maximum_quarterly` | MATRIX | Sales - The highest estimation |
| `sales_estimate_median_quarterly` | MATRIX | Sales - median of estimations |
| `sales_estimate_median_value` | MATRIX | Sales - Median value among forecasts |
| `sales_estimate_minimum` | MATRIX | Sales - The lowest estimation |
| `sales_estimate_minimum_quarterly` | MATRIX | Sales - The lowest estimation |
| `sales_estimate_standard_deviation` | MATRIX | Sales - standard deviation of estimations |
| `sales_estimate_stddev_quarterly` | MATRIX | Standard deviation of Sales estimations |
| `sales_estimate_value` | VECTOR | Sales - Estimated value |
| `sales_guidance_value` | MATRIX | Sales - Guidance value for the annual period |
| `sales_guidance_value_quarterly` | MATRIX | Sales - guidance value |
| `sales_max_guidance_quarterly` | MATRIX | The maximum guidance value for sales. |
| `sales_max_guidance_value` | MATRIX | Maximum guidance value for annual sales |
| `sales_min_guidance_quarterly` | MATRIX | Minimum guidance value for Sales |
| `sales_min_guidance_value` | MATRIX | Minimum sales guidance for the annual period. |
| `sales_previous_estimate_value` | VECTOR | The previous estimation of Sales |
| `selling_general_admin_expense` | MATRIX | Selling, General & Administrative Expense Value |
| `selling_general_admin_expense_actual_value` | MATRIX | Selling, General & Administrative Expense - actual value |
| `selling_general_admin_expense_max_guidance_qtr` | MATRIX | Selling, General & Admin Expenses - Maximum guidance value |
| `selling_general_admin_expense_reported_value` | MATRIX | Selling, General & Administrative Expense value |
| `sg_and_a_expense_avg` | MATRIX | Average selling, general, and administrative expenses. |
| `sg_and_a_expense_max` | MATRIX | Highest estimate of selling, general, and administrative expenses. |
| `sg_and_a_expense_median` | MATRIX | Median value of selling, general, and administrative expenses. |
| `sg_and_a_expense_min` | MATRIX | Lowest estimate of selling, general, and administrative expenses. |
| `sg_and_admin_min_guidance_value` | MATRIX | Minimum guidance value for Selling, General & Administrative Expense on an annual basis. |
| `shareholders_equity_actual_value` | MATRIX | Shareholders' Equity - Total Value |
| `shareholders_equity_avg` | MATRIX | Average owners’ equity after liabilities. |
| `shareholders_equity_max` | MATRIX | Highest estimate of owners’ equity after liabilities. |
| `shareholders_equity_max_guidance` | MATRIX | The maximum guidance value for Shareholder's Equity on an annual basis. |
| `shareholders_equity_median` | MATRIX | Median value of owners’ equity after liabilities for the period. |
| `shareholders_equity_min` | MATRIX | Lowest estimate of owners’ equity after liabilities for the period. |
| `shareholders_equity_min_guidance` | MATRIX | Minimum guidance value for Share Equity |
| `shareholders_equity_reported_value` | MATRIX | Shareholders' Equity - Total Value |
| `shareholders_equity_stddev` | MATRIX | Standard deviation of owners’ equity estimates. |
| `shareholders_equity_total_2` | MATRIX | Shareholder's Equity - Total Value |
| `shares_outstanding_max_guidance` | MATRIX | Maximum guidance value for Shares |
| `stddev_gross_income_quarterly_estimate` | MATRIX | The standard deviation of broker estimates for gross income in the current quarter. |
| `stddev_rd_expense_quarterly_estimate` | MATRIX | The standard deviation of broker estimates for research and development expense in the current quarter. |
| `stddev_reported_eps_quarterly_estimate` | MATRIX | The standard deviation of broker estimates for reported earnings per share in the current quarter. |
| `stddev_sga_expense_quarterly_estimate` | MATRIX | The standard deviation of broker estimates for selling, general, and administrative expenses in the current quarter. |
| `stock_option_expense_max_guidance_qtr` | MATRIX | Stock option expense - maximum guidance value |
| `tangible_book_value_per_share_max_guidance` | MATRIX | Tangible Book Value per Share - Maximum guidance value |
| `total_assets_amount` | MATRIX | Total Assets - actual value |
| `total_assets_median` | MATRIX | Median value of total assets owned by the company. |
| `total_assets_min` | MATRIX | Lowest estimate of total assets owned by the company. |
| `total_assets_reported_value` | MATRIX | Total Assets - actual value |
| `total_assets_stddev` | MATRIX | Standard deviation of total assets estimates. |
| `total_goodwill_actual_value` | MATRIX | Total Goodwill - announced financial value |
| `total_goodwill_amount` | MATRIX | Total Goodwill - Value |
| `total_goodwill_avg` | MATRIX | Average value of goodwill assets for the period. |
| `total_goodwill_max` | MATRIX | Highest estimate of goodwill assets for the period. |
| `total_goodwill_median` | MATRIX | Median value of goodwill assets for the period. |
| `total_goodwill_min` | MATRIX | Lowest estimate of goodwill assets for the period. |
| `total_goodwill_reported_value` | MATRIX | Total Goodwill - Actual Value in Millions |

## 用法提示（人工补充）

- TODO：典型组合方式、相关的 concept 页面
