---
title: model77 数据集
type: entity
tags:
- dataset
- model
- usa
sources:
- worldquantbrain-api
created: '2026-05-24'
dataset_id: model77
category: model
delay: 1
region: USA
universe: TOP3000
---

<!-- managed by wq-agent wiki import-wq; manual edits below -->

# Analysts' Factor Model

**ID**：`model77`　**Category**：model　**Region**：USA　**Universe**：TOP3000　**Delay**：1

## 描述

This dataset is a comprehensive library of quantitative alpha factors and multi-factor models designed to predict equity price movements across global markets. It includes over 350 stock selection signals spanning value, momentum, quality, growth, risk, liquidity, sentiment, and industry-specific factors, with coverage across developed, emerging, and frontier markets. The dataset provides factor definitions, cross-sectional rankings, and performance analytics, enabling users to identify key drivers of returns and construct robust, diversified investment models. By systematically evaluating fundamental, technical, and specialty signals, the dataset helps investors uncover persistent sources of excess return and improve portfolio performance through data-driven stock selection and risk management.

**字段数**：3256

**已用 alpha 数**：88716

## 字段清单（3256 项）

| id | type | description |
| --- | --- | --- |
| `abnormal_return_earnings_release` | MATRIX | Abnormal stock return around quarterly earnings release event |
| `asia_pacific_sales_exposure` | MATRIX | Proportion of company sales from the Asia-Pacific region |
| `asset_growth_rate` | MATRIX | Aggregate Gamma |
| `asset_growth_rate_sensitivityfactor` | MATRIX | Aggregate gamma from the options market; measures overall options positioning impact on returns |
| `book_leverage_ratio_3` | MATRIX | Book leverage ratio; total assets divided by book equity |
| `capex_to_depreciation_linkage` | MATRIX | Linkage or ratio between capital expenditures and depreciation expense; may indicate asset reinvestment |
| `capex_to_total_assets` | MATRIX | TTM capital expenditure divided by total assets; measure of investment intensity |
| `cash_burn_rate` | MATRIX | Cash Burn Rate |
| `cash_burn_rate_v1` | MATRIX | Rate at which a company uses up its cash resources; lower value indicates better cash generation ability |
| `cash_earnings_return_on_equity` | MATRIX | Cash Earnings Return On Equity: a profitability metric measuring cash earnings as a proportion of shareholder equity |
| `cash_flow_return_on_invested_capital` | MATRIX | Cash Flow Return on Invested Capital; trailing 12-month cash flow divided by average invested capital |
| `change_in_eps_surprise` | MATRIX | Change in earnings per share (EPS) surprise compared to the previous earnings period |
| `coefficient_variation_fy1_eps` | MATRIX | Coefficient of variation (dispersion) of EPS estimates for fiscal year 1; analyst disagreement |
| `coefficient_variation_fy2_eps` | MATRIX | Dispersion of FY2 EPS analyst forecasts, calculated as standard deviation divided by the mean of FY2 estimates |
| `consensus_analyst_rating` | MATRIX | Street Consensus Rating |
| `credit_risk_premium_indicator` | MATRIX | Sensitivity of the company’s stock to changes in the credit risk premium (spread between BAA and AAA bond yields) |
| `current_liabilities_to_price` | MATRIX | Current Liabilities-to-Price |
| `current_liabilities_to_price_v1` | MATRIX | Current liabilities divided by price; indicator of short-term balance sheet risk |
| `current_ratio_2` | MATRIX | Current Ratio; current assets divided by current liabilities |
| `distress_risk_measure` | MATRIX | Distress measure score (quantifies financial distress or bankruptcy risk) |
| `dividends_to_gross_profit` | MATRIX | Total dividends paid divided by gross profit. |
| `earnings_expectation_module_score` | MATRIX | Earnings Expectations (submodule of Momentum Analyst II) |
| `earnings_momentum_analyst_score` | MATRIX | Reported Earnings Momentum (submodule of Momentum Analyst II) |
| `earnings_momentum_composite_score` | MATRIX | Composite score reflecting overall earnings momentum, calculated from related earnings momentum signals |
| `earnings_momentum_composite_score_2` | MATRIX | Composite score summarizing multiple earnings momentum signals into a single metric |
| `earnings_revision_magnitude` | MATRIX | Magnitude of analyst EPS forecast revisions; three-month change in median FY1 estimate, scaled |
| `earnings_shortfall_metric` | MATRIX | Measure of earnings shortfall (actual earnings below consensus expectations) |
| `earnings_torpedo_indicator` | MATRIX | Next four quarter EPS estimate plus trailing twelve-month real earnings surprise divided by trailing EPS. |
| `emea_sales_exposure` | MATRIX | Proportion of company’s sales coming from the Europe, Middle East, and Africa (EMEA) region |
| `enterprise_value_weighted_value_score` | MATRIX | Earnings Valuation (submodule of Value Analyst II) |
| `equity_value_score` | MATRIX | Earnings Quality (submodule of Value Analyst II) |
| `fcf_yield_multiplied_forward_roe` | MATRIX | Product of trailing twelve-month free cash flow yield and forward return on equity (ROE), typically calculated by mul… |
| `fcf_yield_times_forward_roe` | MATRIX | Product of trailing twelve-month free cash flow yield and next four-quarter forward return on equity |
| `fcf_yield_times_forward_roe_2` | MATRIX | Product of trailing twelve-month free cash flow yield and forward one-year return on equity, scaled by price |
| `fifteen_to_thirtysix_week_price_ratio` | MATRIX | Stock price ratio measured over past 15-36 weeks; price momentum indicator |
| `fifty_to_two_hundred_day_price_ratio` | MATRIX | 50-day moving average price divided by 200-day moving average price; medium-term momentum indicator |
| `financial_statement_value_score` | MATRIX | Financial Statement Valuation (submodule of Value Analyst II) |
| `five_year_dividend_growth_rate_2` | MATRIX | Five-year dividend growth rate |
| `five_year_eps_stability` | MATRIX | Standard deviation of last five years’ trailing twelve-month EPS divided by their mean. |
| `five_year_eps_trend_r_squared_2` | MATRIX | R-squared of the five-year trailing twelve-month EPS trend line, indicating earnings trend fit. |
| `five_year_eps_trend_slope_2` | MATRIX | Slope coefficient of the five-year trailing twelve-month EPS trend line. |
| `fixed_cash_to_current_liabilities_ratio` | MATRIX | Ratio of cash and equivalents to current liabilities, using a fixed calculation method. |
| `forward_book_value_to_price` | MATRIX | Forward-looking book value per share divided by closing price. |
| `forward_cash_flow_to_price` | MATRIX | Forward-looking cash flows per share divided by price. |
| `forward_ebitda_to_enterprise_value_2` | MATRIX | Forward-looking EBITDA divided by enterprise value. |
| `forward_median_earnings_yield` | MATRIX | Leading 12-Month Median Earnings Yield |
| `forward_median_earnings_yield_globaldividend` | MATRIX | Leading 12-Month Median Earnings Yield; estimated future earnings divided by price |
| `forward_sales_to_price` | MATRIX | Forward-looking sales per share divided by trading price. |
| `forward_two_year_eps_growth` | MATRIX | 2-Year Ahead EPS Growth; forecasted EPS for fiscal year 2 minus year 1, scaled by price |
| `forward_two_year_eps_growth_rate` | MATRIX | Projected two-year-ahead EPS growth, defined as the difference between FY2 and FY1 forecasted earnings scaled by price |
| `fundamental_growth_module_score` | MATRIX | Fundamental Growth (submodule of Momentum Analyst II) |
| `fy1_eps_estimate_dispersion_2` | MATRIX | FY1 EPS Estimates Dispersion |
| `fy1_eps_estimate_dispersion_globaldividend` | MATRIX | Dispersion of FY1 EPS estimates (e.g., coefficient of variation across analysts) |
| `fy2_eps_estimate_dispersion` | MATRIX | Dispersion of FY2 EPS analyst estimates, calculated as standard deviation divided by the mean of forecasts |
| `global_dividend_model_composite_score` | MATRIX | Composite Global Dividend factor for the stock |
| `gross_profit_margin_ttm_2` | MATRIX | Trailing twelve-month gross profit margin. |
| `gross_profit_to_assets_ratio` | MATRIX | Trailing twelve-month gross profit to assets ratio. |
| `high_low_eps_revision_sum` | MATRIX | Street revision confidence: sum of changes in highest and lowest FY1 EPS estimates over three months |
| `housing_starts_indicator` | MATRIX | Housing Starts Sensitivity |
| `implied_minus_realized_volatility_2` | MATRIX | Volatility Spread |
| `implied_option_volatility` | MATRIX | Implied volatility derived from options prices, indicating expected future stock volatility |
| `income_statement_value_score` | MATRIX | Investor Sentiment (submodule of Value Analyst II) |
| `industrial_production_indicator` | MATRIX | Industrial Production Sensitivity: measures the sensitivity of a stock’s performance to changes in industrial product… |
| `industry_adjusted_doubtful_receivables` | MATRIX | Industry-adjusted annual doubtful accounts receivable; asset-scaled minus industry mean |
| `industry_rel_ttm_sales_to_ev` | MATRIX | Industry-relative ratio of trailing twelve month sales to enterprise value, used for valuation comparison |
| `industry_relative_book_to_market` | MATRIX | Book-to-market ratio compared to industry average; valuation measure relative to industry |
| `industry_relative_ebitda_to_price` | MATRIX | TTM EBITDA-to-Price ratio compared to industry average; valuation metric relative to industry |
| `industry_relative_eps_to_price` | MATRIX | TTM EPS-to-Price ratio compared to industry average; valuation measure relative to industry |
| `industry_relative_fcf_to_price` | MATRIX | TTM Free Cash Flow-to-Price ratio compared to industry average; valuation metric relative to industry |
| `industry_relative_return_4w` | MATRIX | 4-week stock return relative to industry average, normalized by industry standard deviation |
| `industry_relative_return_5d` | MATRIX | 5-day stock return relative to industry average, normalized by industry standard deviation |
| `industry_relative_sales_to_price` | MATRIX | Sales-to-price ratio less industry average, deflated by industry standard deviation. |
| `industry_relative_sales_to_price_v1` | MATRIX | TTM Sales-to-Price ratio compared to industry average; measure of valuation relative to industry |
| `inflation_rate_indicator` | MATRIX | Sensitivity of the company’s stock to changes in the inflation rate |
| `interest_coverage_ratio_5` | MATRIX | Interest Coverage |
| `interest_coverage_ratio_globaldividend` | MATRIX | Interest Coverage Ratio; ratio of operating income to interest expense |
| `inventory_change_avg_assets` | MATRIX | Change in inventory relative to average total assets, often used to assess operational or financial efficiency |
| `inverse_peg_earnings_growth` | MATRIX | Inverse of PEG ratio: next four-quarters’ earnings estimate times long-term growth rate, scaled by price |
| `inverse_peg_ratio` | MATRIX | Inverse of PEG Ratio |
| `inverse_peg_ratio_2` | MATRIX | Inverse of PEG Ratio |
| `inverse_peg_ratio_2_emmodel` | MATRIX | Inverse of PEG ratio, calculated as next four-quarter earnings estimate times long-term growth rate scaled by price |
| `inverse_peg_ratio_emmodel` | MATRIX | Inverse of the PEG ratio, computed as next four-quarters’ earnings estimate times long-term growth rate, scaled by price |
| `lagged_inverse_peg_ratio` | MATRIX | Lagged Inverse of PEG Ratio |
| `latin_america_sales_exposure` | MATRIX | Proportion of company sales from Latin America |
| `liquidity_cash_to_liabilities_ratio` | MATRIX | Liquidity ratio calculated as cash and equivalents divided by current liabilities, using a fixed formula. |
| `long_term_earnings_growth_forecast` | MATRIX | Long-term earnings growth rate estimate, typically from consensus analysts such as I/B/E/S |
| `long_term_growth_estimate` | MATRIX | Long-term growth rate estimate for the company, typically sourced from analyst consensus |
| `long_term_growth_estimate_2` | MATRIX | Long-term growth rate forecast (I/B/E/S or First Call) |
| `long_term_growth_forecast_2` | MATRIX | Long-term earnings growth rate forecast (typically I/B/E/S consensus) |
| `market_volatility_index` | MATRIX | Sensitivity of stock or portfolio to market volatility as measured by the VIX index |
| `mdl177_2_5yearrelativevaluefactor_rel5ybp` | MATRIX | 5-year Relative Book-to-Market: current book-to-market minus the 60-month average, scaled by standard deviation |
| `mdl177_2_5yearrelativevaluefactor_rel5ycfp` | MATRIX | 5-year Relative Trailing 12-Month Cash Flow-to-Price: current TTM cash flow-to-price minus the 60-month average, scal… |
| `mdl177_2_5yearrelativevaluefactor_rel5ycoreepsp` | MATRIX | 5-year Relative Trailing 12-Month Core Earnings-to-Price: current TTM core earnings-to-price minus the 60-month avera… |
| `mdl177_2_5yearrelativevaluefactor_rel5ydivp` | MATRIX | 5-year Relative Trailing 12-Month Dividend Yield: current dividend yield minus the 60-month average, scaled by standa… |
| `mdl177_2_5yearrelativevaluefactor_rel5yebitdap` | MATRIX | 5-year Relative Trailing 12-Month EBITDA-to-Price: current TTM EBITDA per share-to-price minus the 60-month average, … |
| `mdl177_2_5yearrelativevaluefactor_rel5yep` | MATRIX | 5-year Relative Trailing 12-Month Earnings-to-Price: current TTM EPS before extra items-to-price minus the 60-month a… |
| `mdl177_2_5yearrelativevaluefactor_rel5yfcfp` | MATRIX | 5-year Relative Trailing 12-Month Free Cash Flow-to-Price: current TTM free cash flow-to-price minus the 60-month ave… |
| `mdl177_2_5yearrelativevaluefactor_rel5yfwdep` | MATRIX | 5-year Relative Leading 12-Month Earnings Yield: next 4-quarter consensus analyst earnings-to-price ratio minus the 6… |
| `mdl177_2_5yearrelativevaluefactor_rel5yocfp` | MATRIX | 5-year Relative Trailing 12-Month Operating Cash Flow-to-Price: current TTM operating cash flow-to-price minus the 60… |
| `mdl177_2_5yearrelativevaluefactor_rel5ysp` | MATRIX | 5-year Relative Trailing 12-Month Sales-to-Price: current TTM sales-to-price minus the 60-month average, scaled by st… |
| `mdl177_2_deepvaluefactor_acqmul` | MATRIX | Most recent invested capital divided by trailing 12-month EBITDA |
| `mdl177_2_deepvaluefactor_bp` | MATRIX | Book value per share divided by month-end trading price (book-to-market ratio) |
| `mdl177_2_deepvaluefactor_cashp` | MATRIX | Most recently reported cash and equivalents per share divided by trading price |
| `mdl177_2_deepvaluefactor_cashsev` | MATRIX | Cash and equivalents divided by enterprise value |
| `mdl177_2_deepvaluefactor_coreepsp` | MATRIX | Trailing 12-month core earnings per share from operations (excludes special items) divided by trading price |
| `mdl177_2_deepvaluefactor_curep` | MATRIX | Current Earnings Yield (sum of recent 3 quarters EPS and analyst estimates, divided by price) |
| `mdl177_2_deepvaluefactor_divyield` | MATRIX | Trailing 12-month dividends per share divided by month-end trading price (dividend yield) |
| `mdl177_2_deepvaluefactor_ebitdaev` | MATRIX | Trailing 12-month EBITDA divided by enterprise value |
| `mdl177_2_deepvaluefactor_ebitdap` | MATRIX | Trailing 12-month EBITDA per share divided by month-end trading price |
| `mdl177_2_deepvaluefactor_ebop` | MATRIX | Edwards–Bell–Ohlson value-to-price ratio |
| `mdl177_2_deepvaluefactor_estep` | MATRIX | Forward 12-month median earnings-to-price (earnings yield) |
| `mdl177_2_deepvaluefactor_f12mepssev` | MATRIX | Forward 12-month earnings per share divided by enterprise value |
| `mdl177_2_deepvaluefactor_fcfp` | MATRIX | Leading 12-Month Median Earnings Yield |
| `mdl177_2_deepvaluefactor_fwdep` | MATRIX | Forward 12-month earnings-to-price ratio (mean consensus EPS divided by trading price) |
| `mdl177_2_deepvaluefactor_indidivy` | MATRIX | Indicated dividend yield |
| `mdl177_2_deepvaluefactor_navp` | MATRIX | Most recent net asset value per share divided by price |
| `mdl177_2_deepvaluefactor_nnastp` | MATRIX | Net current assets per share (current assets minus total liabilities) divided by trading price |
| `mdl177_2_deepvaluefactor_past` | MATRIX | Price-to-total assets ratio (month-end trading price divided by total assets per share) |
| `mdl177_2_deepvaluefactor_pdy` | MATRIX | Indicated dividend yield |
| `mdl177_2_deepvaluefactor_proformaep` | MATRIX | Trailing 12-month pro forma earnings-to-price (excludes special items) |
| `mdl177_2_deepvaluefactor_ttmcapexp` | MATRIX | Trailing 12-month capital expenditures per share divided by trading price |
| `mdl177_2_deepvaluefactor_ttmcfp` | MATRIX | Trailing 12-month cash flow (net income plus depreciation) per share divided by trading price |
| `mdl177_2_deepvaluefactor_ttmepa` | MATRIX | Trailing 12-month earnings per share after special items divided by trading price |
| `mdl177_2_deepvaluefactor_ttmepb` | MATRIX | Trailing 12-month earnings per share before non-recurring items divided by trading price |
| `mdl177_2_deepvaluefactor_ttmfcfev` | MATRIX | Trailing 12-month free cash flow divided by enterprise value |
| `mdl177_2_deepvaluefactor_ttmfcfp` | MATRIX | Trailing 12-month free cash flow per share divided by month-end trading price (operating cash flow minus capital expe… |
| `mdl177_2_deepvaluefactor_ttmgfp` | MATRIX | Trailing 12-month growth flow-to-price (GAAP earnings plus R&D) per share divided by trading price |
| `mdl177_2_deepvaluefactor_ttmocfp` | MATRIX | Trailing 12-month operating cash flow per share divided by trading price |
| `mdl177_2_deepvaluefactor_ttmpiqp` | MATRIX | Trailing 12-month pretax income per share (operating plus nonoperating) divided by trading price |
| `mdl177_2_deepvaluefactor_ttmsaleev` | MATRIX | Trailing 12-month sales divided by enterprise value |
| `mdl177_2_deepvaluefactor_ttmsp` | MATRIX | Trailing 12-month sales per share divided by month-end trading price |
| `mdl177_2_deepvaluemodel2_dv_currroe` | MATRIX | Current return on equity for the stock, computed as net income divided by shareholders’ equity for the most recent re… |
| `mdl177_2_deepvaluemodel_chgshare` | MATRIX | Percent change in a company's shares outstanding compared to one year ago |
| `mdl177_2_deepvaluemodel_dv_yoychgat` | MATRIX | Year-over-year change in asset turnover; measures the difference in a company's asset turnover ratio compared to one … |
| `mdl177_2_deepvaluemodel_dvm_composite` | MATRIX | Composite deep value score for the stock; an integrated model-based measure aggregating multiple deep value signals |
| `mdl177_2_deepvaluemodel_indidivy` | MATRIX | Indicated dividend yield; the projected annual dividend divided by current stock price |
| `mdl177_2_deepvaluemodel_ttmfcfev` | MATRIX | Trailing twelve month free cash flow to enterprise value ratio; reflects free cash flow over the past year relative t… |
| `mdl177_2_earningmomentumfactor400_chg6mltg` | MATRIX | Percent change in consensus long-term earnings growth forecast compared to 6 months ago |
| `mdl177_2_earningmomentumfactor400_cvfy1eps` | MATRIX | Coefficient of variance (dispersion) in FY1 EPS consensus estimates |
| `mdl177_2_earningmomentumfactor400_cvfy2eps` | MATRIX | Dispersion of fiscal year 2 EPS analyst forecasts, measured as the standard deviation divided by the mean |
| `mdl177_2_earningmomentumfactor400_dypeg` | MATRIX | Reciprocal of the dividend yield–adjusted PEG ratio, a valuation metric |
| `mdl177_2_earningmomentumfactor400_egp` | MATRIX | Inverse of PEG Ratio, calculated as next 4-quarter's earnings estimate times long-term growth rate scaled by price |
| `mdl177_2_earningmomentumfactor400_epsrm` | MATRIX | Magnitude of the 3-month change in median FY1 consensus EPS estimate, scaled |
| `mdl177_2_earningmomentumfactor400_fcfroey1p` | MATRIX | Product of trailing 12-month free cash flow yield and forward return on equity |
| `mdl177_2_earningmomentumfactor400_fqsurstd` | MATRIX | Most recent standardized earnings surprise |
| `mdl177_2_earningmomentumfactor400_fy1epsskew` | MATRIX | Skewness of the distribution of leading 12-month EPS consensus estimates |
| `mdl177_2_earningmomentumfactor400_hlep` | MATRIX | Street revision confidence: sum of changes in highest and lowest FY1 earnings estimates over 3 months, scaled |
| `mdl177_2_earningmomentumfactor400_lagegp` | MATRIX | Lagged Inverse of PEG Ratio : It is defined as the trailing 12-month earnings per share before extraordinary items ti… |
| `mdl177_2_earningmomentumfactor400_ltg` | MATRIX | Consensus long-term expected annual earnings growth rate |
| `mdl177_2_earningmomentumfactor400_numrevq1` | MATRIX | Net number of upward minus downward revisions for fiscal quarter 1 EPS forecasts |
| `mdl177_2_earningmomentumfactor400_numrevy1` | MATRIX | Net number of upward minus downward revisions in FY1 EPS forecasts |
| `mdl177_2_earningmomentumfactor400_perg` | MATRIX | Risk-adjusted PEG ratio: price divided by next year’s EPS forecast, scaled by average long-term growth and multiplied… |
| `mdl177_2_earningmomentumfactor400_q1aepsg` | MATRIX | EPS growth estimate for next fiscal quarter |
| `mdl177_2_earningmomentumfactor400_qepsferr` | MATRIX | Forecast error for the prior fiscal quarter’s EPS estimates |
| `mdl177_2_earningmomentumfactor400_ratrev6m` | MATRIX | Average change in analyst recommendation (street rating) over previous 6 months |
| `mdl177_2_earningmomentumfactor400_rev1q1` | MATRIX | Change in fiscal quarter 1 EPS forecast compared to the prior period |
| `mdl177_2_earningmomentumfactor400_rev3y1` | MATRIX | 3-month change in FY1 EPS forecast |
| `mdl177_2_earningmomentumfactor400_rev3y2` | MATRIX | 3-month change in FY2 EPS forecast |
| `mdl177_2_earningmomentumfactor400_rev6` | MATRIX | Averaged revision in consensus FY1 EPS estimates over the last 6 months |
| `mdl177_2_earningmomentumfactor400_salesurp` | MATRIX | Sales Surprise, indicating the difference between reported and expected sales |
| `mdl177_2_earningmomentumfactor400_stdevfy1epsp` | MATRIX | Standard deviation of FY1 EPS estimates scaled by price |
| `mdl177_2_earningmomentumfactor400_stdevfy2epsp` | MATRIX | Standard deviation of FY2 EPS estimates scaled by price |
| `mdl177_2_earningmomentumfactor400_stockrating` | MATRIX | Consensus analyst recommendation for the company |
| `mdl177_2_earningmomentumfactor400_sucf` | MATRIX | Standardized Unexpected Cash Flow |
| `mdl177_2_earningmomentumfactor400_sue` | MATRIX | Standardized Unexpected Earnings, representing the earnings surprise relative to analyst expectations in standardized… |
| `mdl177_2_earningmomentumfactor400_surp` | MATRIX | Earnings surprise: actual EPS minus forecast, scaled by price at quarter end |
| `mdl177_2_earningmomentumfactor400_y1aepsg` | MATRIX | EPS growth estimate for next fiscal year |
| `mdl177_2_earningmomentumfactor400_y2aepsg` | MATRIX | EPS growth estimate for two years ahead |
| `mdl177_2_earningmomentumfactor400_y2repsg` | MATRIX | Projected EPS growth over two years |
| `mdl177_2_earningmomentumfactor400_y3sur` | MATRIX | Volatility-adjusted projected EPS growth over the next 3 years |
| `mdl177_2_earningsqualityfactor_chgsgasale` | MATRIX | Difference between the yearly change in quarterly SG&A expenses and the yearly change in quarterly sales |
| `mdl177_2_earningsqualityfactor_chgshare` | MATRIX | Percent change in number of outstanding shares compared to one year ago |
| `mdl177_2_earningsqualityfactor_cogsinvt` | MATRIX | Absolute value of the difference between yearly percent change in trailing 12-month cost of goods sold and yearly per… |
| `mdl177_2_earningsqualityfactor_dpcapex` | MATRIX | Absolute value of the difference between yearly percent change in trailing 12-month depreciation expense and yearly p… |
| `mdl177_2_earningsqualityfactor_epschgetr` | MATRIX | Trailing 12-month pre-tax income per share times the difference between current and prior year effective tax rates (t… |
| `mdl177_2_earningsqualityfactor_erc` | MATRIX | Earnings Response Coefficient |
| `mdl177_2_earningsqualityfactor_indrelrecd_` | MATRIX | A stock’s asset-adjusted annual doubtful receivables minus the industry average, deflated by standard deviation of in… |
| `mdl177_2_earningsqualityfactor_ncfeps` | MATRIX | Absolute value of the difference between the yearly percent change in trailing 12-month operating cash flow per share… |
| `mdl177_2_earningsqualityfactor_opincltd` | MATRIX | Difference between the yearly percent change in operating income and the yearly percent change in long-term debt |
| `mdl177_2_earningsqualityfactor_saleeps` | MATRIX | Absolute value of the difference between the yearly percent change in trailing 12-month sales per share and the yearl… |
| `mdl177_2_earningsqualityfactor_salegpm` | MATRIX | Difference between the yearly change in the most recent reported quarterly sales and the yearly change in quarterly g… |
| `mdl177_2_earningsqualityfactor_salerec` | MATRIX | Difference between the yearly percent change in trailing 12-month sales and the yearly percent change in accounts rec… |
| `mdl177_2_earningsqualityfactor_ttmaccu` | MATRIX | Difference between trailing 12-month net income and trailing 12-month operating cash flow, scaled by beginning total … |
| `mdl177_2_earningsqualityfactor_uaccl` | MATRIX | Difference between current accrued liabilities and expected levels, scaled by total assets |
| `mdl177_2_earningsqualityfactor_uap` | MATRIX | Difference between current accounts payable and expected level (prior year's balance multiplied by COGS growth in tra… |
| `mdl177_2_earningsqualityfactor_uar` | MATRIX | Difference between current accounts receivable and expected level (prior year's balance multiplied by sales growth in… |
| `mdl177_2_earningsqualityfactor_udep` | MATRIX | Difference between trailing 12-month depreciation expenses and expected depreciation expenses (prior year’s balance m… |
| `mdl177_2_earningsqualityfactor_uinv` | MATRIX | Difference between current inventory level and expected inventory level, likely scaled by assets |
| `mdl177_2_earningsqualityfactor_wcacc` | MATRIX | Sum of changes in receivables, inventory, payables, taxes, assets, and liabilities to measure working capital accruals |
| `mdl177_2_earningsqualityfactor_yoychgaa` | MATRIX | Trailing 12-month income before extra items less trailing 12-month operating cash flow, scaled by average total asset… |
| `mdl177_2_garpanalystmodel_qgp_alert` | MATRIX | Ranking indicator highlighting stocks that trigger specific GARP alert signals, possibly for rapid reassessment or at… |
| `mdl177_2_garpanalystmodel_qgp_avgrating` | MATRIX | Average of analyst ratings for the stock, reflecting consensus analyst opinion |
| `mdl177_2_garpanalystmodel_qgp_capeff` | MATRIX | Measurement of how efficiently a company utilizes its capital/resources, ranked relative to peers |
| `mdl177_2_garpanalystmodel_qgp_chgvaluation` | MATRIX | Three-month change in valuation metrics, tracking how a stock's valuation measures have evolved over the past quarter |
| `mdl177_2_garpanalystmodel_qgp_composite` | MATRIX | Composite score aggregating multiple GARP-specific metrics to represent overall attractiveness based on GARP principles |
| `mdl177_2_garpanalystmodel_qgp_growthval` | MATRIX | Valuation of a stock adjusted for its growth metrics, used within a GARP (Growth at a Reasonable Price) analyst frame… |
| `mdl177_2_garpanalystmodel_qgp_relgrowth` | MATRIX | Rank comparing a stock’s growth metrics to its peers, emphasizing relative growth within its universe |
| `mdl177_2_garpanalystmodel_qgp_relpegy` | MATRIX | A rolling ranking of stocks combining their PEGY (Price/Earnings-to-Growth-and-Yield) ratio over a set period, repres… |
| `mdl177_2_garpanalystmodel_qgp_roefcf` | MATRIX | Combined rank measuring both Return on Equity and Free Cash Flow to capture quality and profitability |
| `mdl177_2_garpanalystmodel_qgp_valuation` | MATRIX | Ranking of a stock's valuation according to GARP analyst metrics, possibly considering price-to-earnings, price-to-bo… |
| `mdl177_2_garpanalystmodel_qgp_vfpriceratio` | MATRIX | Ranking based on the ratio of intrinsic (fundamental, value-based) valuation to market price, indicating relative und… |
| `mdl177_2_garpanalystmodel_qgp_wratingchg` | MATRIX | Six-month weighted change in analyst ratings, capturing recent shifts in analyst opinion |
| `mdl177_2_garpmodel_gpm_composite` | MATRIX | GPM Composite Model |
| `mdl177_2_globaldevnorthamerica_v502_aci` | MATRIX | Abnormal Capital Investment: measures the change in a firm's recent 12-month capital investment intensity compared to… |
| `mdl177_2_globaldevnorthamerica_v502_acp` | MATRIX | Average Collection Period: average of trailing 12-month accounts receivable times 365 divided by trailing 12-month sa… |
| `mdl177_2_globaldevnorthamerica_v502_acqmul` | MATRIX | Acquisition Multiple: most recent invested capital divided by trailing 12-month EBITDA, showing acquisition valuation |
| `mdl177_2_globaldevnorthamerica_v502_actrtn12m` | MATRIX | 12-Month Active Return with 1-month Lag: percent change in stock price from month t-13 to t-1 |
| `mdl177_2_globaldevnorthamerica_v502_actrtn18m` | MATRIX | 18-Month Active Return with 1-Month Lag: percent change in stock price from month t-19 to t-1 |
| `mdl177_2_globaldevnorthamerica_v502_actrtn1m` | MATRIX | 1-Month Active Return: percent change in stock price from month t-1 to t |
| `mdl177_2_globaldevnorthamerica_v502_actrtn24m` | MATRIX | 24-Month Active Return with 1-Month Lag: percent change in stock price from month t-25 to t-1 |
| `mdl177_2_globaldevnorthamerica_v502_actrtn2m` | MATRIX | 2-Month Active Return: percent change in stock price from month t-2 to t |
| `mdl177_2_globaldevnorthamerica_v502_actrtn36m` | MATRIX | 36-Month Active Return with 1-Month Lag: percent change in stock price from month t-37 to t-1 |
| `mdl177_2_globaldevnorthamerica_v502_actrtn3m` | MATRIX | 3-Month Active Return: percent change in stock price from month t-3 to t |
| `mdl177_2_globaldevnorthamerica_v502_actrtn60m` | MATRIX | 60-Month Active Return with 1-Month Lag: percent change in stock price from month t-61 to t-1 |
| `mdl177_2_globaldevnorthamerica_v502_actrtn6m` | MATRIX | 6-Month Active Return with 1-Month Lag: percent change in stock price from month t-7 to t-1 |
| `mdl177_2_globaldevnorthamerica_v502_actrtn9m` | MATRIX | 9-Month Active Return with 1-Month Lag: percent change in stock price from month t-10 to t-1 |
| `mdl177_2_globaldevnorthamerica_v502_alpha60m` | MATRIX | 60-Month Alpha: intercept from regression of stock's monthly return versus S&P 500 monthly return for the past 60 mon… |
| `mdl177_2_globaldevnorthamerica_v502_app` | MATRIX | Average Payable Period: average of trailing 12-month accounts payable times 365 divided by trailing 12-month cost of … |
| `mdl177_2_globaldevnorthamerica_v502_aqi` | MATRIX | Asset Quality Index: year-over-year change of 1 minus the ratio of current assets plus PP&E to total assets, reflecti… |
| `mdl177_2_globaldevnorthamerica_v502_aspanratio` | MATRIX | Operating assets minus operating liabilities for the quarter, divided by lagged total assets, a balance sheet efficie… |
| `mdl177_2_globaldevnorthamerica_v502_astcomp` | MATRIX | Asset Composition: total current assets from the most recent quarter divided by total assets from the same quarter, i… |
| `mdl177_2_globaldevnorthamerica_v502_astto` | MATRIX | Assets Turnover Ratio: trailing 12-month sales divided by most recent quarterly assets, measuring efficiency of asset… |
| `mdl177_2_globaldevnorthamerica_v502_bdi` | MATRIX | Basic Defensive Interval: number of days a company can cover daily operating expenses solely from its cash and receiv… |
| `mdl177_2_globaldevnorthamerica_v502_beta` | MATRIX | 60-Month Beta: measure of stock's sensitivity to market movements, calculated as a weighted average (0.67 × 60-month … |
| `mdl177_2_globaldevnorthamerica_v502_betasigma` | MATRIX | Product of Beta and Sigma: product of 60-month adjusted beta and 60-month standard deviation of monthly returns, a ri… |
| `mdl177_2_globaldevnorthamerica_v502_booklev` | MATRIX | Book Leverage: most recent quarterly total assets divided by book equity, a leverage ratio |
| `mdl177_2_globaldevnorthamerica_v502_bp` | MATRIX | Book-to-Market: most recent book value per share divided by month-end trading price, a value investing measure |
| `mdl177_2_globaldevnorthamerica_v502_capacq` | MATRIX | Capital Acquisition Ratio: trailing 12-month operating cash flow less cash dividends, divided by total expenditures i… |
| `mdl177_2_globaldevnorthamerica_v502_capexast` | MATRIX | Capital Expenditure-to-Total Assets: trailing 12-month capital expenditures divided by most recent quarter's total as… |
| `mdl177_2_globaldevnorthamerica_v502_capexsale` | MATRIX | TTM Capital Expenditures-to-Sales: trailing 12-month capital expenditures divided by trailing 12-month sales, indicat… |
| `mdl177_2_globaldevnorthamerica_v502_cashburnrate` | MATRIX | Rate at which a company burns cash; computed as negative (operating cash flow plus investing cash flow) divided by ca… |
| `mdl177_2_globaldevnorthamerica_v502_cashc` | MATRIX | Cash conversion cycle in days: inventory days plus receivables days minus payables days |
| `mdl177_2_globaldevnorthamerica_v502_cashp` | MATRIX | Cash and equivalents per share divided by trading price (cash-to-price ratio) |
| `mdl177_2_globaldevnorthamerica_v502_cashratio` | MATRIX | Cash and equivalents divided by current liabilities (cash ratio) |
| `mdl177_2_globaldevnorthamerica_v502_cashsale` | MATRIX | Cash-to-sales ratio: trailing 12-month average cash and equivalents divided by trailing 12-month sales |
| `mdl177_2_globaldevnorthamerica_v502_cashsev` | MATRIX | Total cash and equivalents divided by enterprise value |
| `mdl177_2_globaldevnorthamerica_v502_ccd` | MATRIX | Current cash flow debt coverage: (cash flow from operations minus dividends) divided by current interest-bearing debt |
| `mdl177_2_globaldevnorthamerica_v502_cfita` | MATRIX | Trailing 12-month investing cash flow divided by average total assets over the last four quarters |
| `mdl177_2_globaldevnorthamerica_v502_cfleverage` | MATRIX | Total liabilities divided by trailing 12-month operating cash flow (cash flow leverage) |
| `mdl177_2_globaldevnorthamerica_v502_cfroi` | MATRIX | Trailing 12-month cash flow divided by average invested capital (equity, long-term debt, minority interest, and prefe… |
| `mdl177_2_globaldevnorthamerica_v502_cg3ysales` | MATRIX | Geometric growth rate of trailing 12-month sales per share over the last 12 quarters (3-year compound annual growth) |
| `mdl177_2_globaldevnorthamerica_v502_chg3ycfast` | MATRIX | Three-year change in assets-adjusted trailing 12-month operating cash flow: current minus 12 quarters ago, scaled by … |
| `mdl177_2_globaldevnorthamerica_v502_chg3ycfp` | MATRIX | Three-year change in price-adjusted trailing 12-month cash flow per share: current minus 12 quarters ago, divided by … |
| `mdl177_2_globaldevnorthamerica_v502_chg3yepsast` | MATRIX | Three-year change in assets-adjusted trailing 12-month EPS (before extra items): current minus 12 quarters ago, scale… |
| `mdl177_2_globaldevnorthamerica_v502_chg3yepsp` | MATRIX | Three-year change in price-adjusted trailing 12-month EPS: current minus 12 quarters ago, divided by month-end tradin… |
| `mdl177_2_globaldevnorthamerica_v502_chg3yfcfast` | MATRIX | Three-year change in assets-adjusted trailing 12-month free cash flow: current minus 12 quarters ago, divided by aver… |
| `mdl177_2_globaldevnorthamerica_v502_chg3yfcfp` | MATRIX | Three-year change in price-adjusted trailing 12-month free cash flow per share: current minus 12 quarters ago, divide… |
| `mdl177_2_globaldevnorthamerica_v502_chg3yocfast` | MATRIX | Three-year change in assets-adjusted trailing 12-month operating cash flow: current minus 12 quarters ago, divided by… |
| `mdl177_2_globaldevnorthamerica_v502_chg3yocfp` | MATRIX | Three-year change in price-adjusted trailing 12-month operating cash flow per share: current minus 12 quarters ago di… |
| `mdl177_2_globaldevnorthamerica_v502_chg6malpha18m` | MATRIX | Six-month nominal change in 18-month alpha; alpha is the intercept from regressing monthly returns on the S&P 500 ove… |
| `mdl177_2_globaldevnorthamerica_v502_chg6mltg` | MATRIX | Percent change in mean consensus long-term growth forecast compared to six months ago |
| `mdl177_2_globaldevnorthamerica_v502_chgalpha12m` | MATRIX | Six-month nominal change in 12-month alpha; alpha is the regression intercept of monthly returns versus the S&P 500 |
| `mdl177_2_globaldevnorthamerica_v502_chgalpha36m` | MATRIX | Six-month nominal change in 36-month alpha; alpha is the regression intercept of monthly returns versus the S&P 500 o… |
| `mdl177_2_globaldevnorthamerica_v502_chgars` | MATRIX | One-year change in accounts receivable as a percentage of trailing 12-month sales; current minus four quarters ago |
| `mdl177_2_globaldevnorthamerica_v502_chgcf` | MATRIX | One-year change in assets-adjusted trailing 12-month cash flow; current minus four quarters ago scaled by average tot… |
| `mdl177_2_globaldevnorthamerica_v502_chgcfp` | MATRIX | One-year change in price-adjusted trailing 12-month cash flow per share; current minus four quarters ago divided by t… |
| `mdl177_2_globaldevnorthamerica_v502_chgeps` | MATRIX | One-year change in assets-adjusted trailing 12-month EPS (before extra items); current minus four quarters ago deflat… |
| `mdl177_2_globaldevnorthamerica_v502_chgepsp` | MATRIX | One-year change in price-adjusted trailing 12-month EPS; current minus four quarters ago divided by month-end trading… |
| `mdl177_2_globaldevnorthamerica_v502_chgfcf` | MATRIX | One-year change in assets-adjusted trailing 12-month free cash flow; current minus four quarters ago divided by avera… |
| `mdl177_2_globaldevnorthamerica_v502_chgfcfp` | MATRIX | One-year change in price-adjusted trailing 12-month free cash flow per share; current minus four quarters ago divided… |
| `mdl177_2_globaldevnorthamerica_v502_chgis` | MATRIX | Change in inventory as a percentage of sales over one year; calculated as latest reported inventory/sales minus same … |
| `mdl177_2_globaldevnorthamerica_v502_chgnoa` | MATRIX | Year-over-year change in net operating assets to total assets; net operating assets = short-term debt + long-term deb… |
| `mdl177_2_globaldevnorthamerica_v502_chgnpm` | MATRIX | Change in net profit margin over one year; calculated as latest quarterly net profit margin minus net profit margin f… |
| `mdl177_2_globaldevnorthamerica_v502_chgocf` | MATRIX | Change in trailing twelve-month operating cash flow, asset-adjusted, over one year; calculated as the latest TTM oper… |
| `mdl177_2_globaldevnorthamerica_v502_chgocfp` | MATRIX | Change in trailing twelve-month operating cash flow per share over one year, divided by trading price |
| `mdl177_2_globaldevnorthamerica_v502_chgollev` | MATRIX | Change in operating liability leverage over one year; operating liability leverage = 1 - (short-term debt + long-term… |
| `mdl177_2_globaldevnorthamerica_v502_chgopm` | MATRIX | Change in operating profit margin over one year; most recent quarterly operating profit margin minus operating profit… |
| `mdl177_2_globaldevnorthamerica_v502_chgreccast` | MATRIX | Percent change in accounts receivable to current assets ratio over one year; most recent quarterly ratio minus ratio … |
| `mdl177_2_globaldevnorthamerica_v502_chgsgasale` | MATRIX | Difference between yearly change in quarterly SG&A expenses and yearly change in quarterly sales |
| `mdl177_2_globaldevnorthamerica_v502_chgshare` | MATRIX | Percent change in shares outstanding over one year; current vs. one year ago |
| `mdl177_2_globaldevnorthamerica_v502_chgvolpre4y` | MATRIX | Change in average trading volume over four years; difference in the most recent 6-month moving average of monthly tur… |
| `mdl177_2_globaldevnorthamerica_v502_cogsinvt` | MATRIX | Absolute difference between yearly percent change in trailing twelve-month cost of goods sold and yearly percent chan… |
| `mdl177_2_globaldevnorthamerica_v502_covol` | MATRIX | Sixty-month trading volume trend; slope of regression line of last 60 months' monthly trading volume against time |
| `mdl177_2_globaldevnorthamerica_v502_curindbp_` | MATRIX | Stock's current book-to-price ratio minus industry average, deflated by industry standard deviation |
| `mdl177_2_globaldevnorthamerica_v502_curindcfp_` | MATRIX | Stock’s TTM cash flow-to-price ratio minus industry average, deflated by industry standard deviation |
| `mdl177_2_globaldevnorthamerica_v502_curinddivp_` | MATRIX | Stock’s TTM dividend yield minus industry average, deflated by industry standard deviation |
| `mdl177_2_globaldevnorthamerica_v502_curindebitdap_` | MATRIX | Stock’s TTM EBITDA-to-price ratio minus industry average, deflated by industry standard deviation |
| `mdl177_2_globaldevnorthamerica_v502_curindep_` | MATRIX | Trailing twelve-month EPS-to-price ratio minus industry average, deflated by industry standard deviation |
| `mdl177_2_globaldevnorthamerica_v502_curindfcfp_` | MATRIX | Stock’s TTM free cash flow-to-price ratio minus industry average, deflated by industry standard deviation |
| `mdl177_2_globaldevnorthamerica_v502_curindocfp_` | MATRIX | Stock’s TTM operating cash flow-to-price ratio minus industry average, deflated by industry standard deviation |
| `mdl177_2_globaldevnorthamerica_v502_curindocfta_` | MATRIX | Stock’s TTM operating cash flow-to-total assets ratio minus industry average, deflated by industry standard deviation |
| `mdl177_2_globaldevnorthamerica_v502_curindsp_` | MATRIX | Stock’s TTM sales-to-price ratio minus industry average, deflated by industry standard deviation |
| `mdl177_2_globaldevnorthamerica_v502_curratio` | MATRIX | Current assets divided by current liabilities from most recent quarter; a measure of liquidity |
| `mdl177_2_globaldevnorthamerica_v502_cusip_sedol` | MATRIX | Security identifier, typically CUSIP or SEDOL code used to uniquely identify a stock or financial instrument |
| `mdl177_2_globaldevnorthamerica_v502_cvpre90dp` | MATRIX | Coefficient of variation of prior 90 days closing prices; last 90 days' price standard deviation divided by mean |
| `mdl177_2_globaldevnorthamerica_v502_cvvolp20d` | MATRIX | Ratio of 20-day price volatility to 20-day volume volatility; coefficient of variation of closing prices divided by c… |
| `mdl177_2_globaldevnorthamerica_v502_de` | MATRIX | Long-term debt divided by book equity from most recent quarter |
| `mdl177_2_globaldevnorthamerica_v502_debtcf` | MATRIX | Sum of long-term debt and short-term interest-bearing debt divided by trailing twelve-month cash flow |
| `mdl177_2_globaldevnorthamerica_v502_dfl` | MATRIX | Sum of trailing 12-month pretax income and interest expense divided by trailing 12-month pretax income |
| `mdl177_2_globaldevnorthamerica_v502_divcf` | MATRIX | Trailing 12-month cash dividends divided by trailing 12-month cash flow |
| `mdl177_2_globaldevnorthamerica_v502_divcov` | MATRIX | Dividend Coverage Ratio: Company's trailing twelve-month profit from operations divided by its annual dividend payments |
| `mdl177_2_globaldevnorthamerica_v502_divyield` | MATRIX | TTM Dividend Yield: Trailing twelve-month dividends per share divided by month-end trading price |
| `mdl177_2_globaldevnorthamerica_v502_dpcapex` | MATRIX | Change in TTM Depreciation vs. CapEx: Absolute difference between yearly percent change in depreciation expense and t… |
| `mdl177_2_globaldevnorthamerica_v502_ebitdaev` | MATRIX | TTM EBITDA-to-Enterprise Value: Trailing twelve-month earnings before interest, taxes, depreciation, and amortization… |
| `mdl177_2_globaldevnorthamerica_v502_ebitdap` | MATRIX | TTM EBITDA-to-Price: Trailing twelve-month earnings before interest, taxes, depreciation, and amortization divided by… |
| `mdl177_2_globaldevnorthamerica_v502_epschgetr` | MATRIX | EPS from Change in Effective Tax Rate: Trailing twelve-month pre-tax income per share multiplied by the change in eff… |
| `mdl177_2_globaldevnorthamerica_v502_equityto` | MATRIX | Equity Turnover Ratio: Trailing twelve-month sales divided by average trailing twelve-month reported book equity |
| `mdl177_2_globaldevnorthamerica_v502_fc_curindfwdep_` | MATRIX | Industry Relative Leading 4-QTRs EPS to Price: Stock's next four quarters' consensus EPS-to-price ratio minus industr… |
| `mdl177_2_globaldevnorthamerica_v502_fc_cvfy1eps` | MATRIX | FY1 EPS Estimates Dispersion: Standard deviation of analyst earnings estimates for fiscal year one divided by mean co… |
| `mdl177_2_globaldevnorthamerica_v502_fc_cvfy2eps` | MATRIX | FY2 EPS Forecast Dispersion: Standard deviation of analyst earnings estimates for fiscal year two divided by mean con… |
| `mdl177_2_globaldevnorthamerica_v502_fc_dypeg` | MATRIX | Reciprocal of Dividend Yield-adjusted PEG: Reciprocal of forward twelve-month price/earnings ratio divided by sum of … |
| `mdl177_2_globaldevnorthamerica_v502_fc_ebop` | MATRIX | Edwards-Bell-Ohlson Value-to-Price: Firm's intrinsic valuation from EBO model divided by month-end trading price, com… |
| `mdl177_2_globaldevnorthamerica_v502_fc_egp` | MATRIX | Inverse PEG Ratio: Next one year average forecasted earnings multiplied by long-term growth rate and scaled by stock … |
| `mdl177_2_globaldevnorthamerica_v502_fc_epsrm` | MATRIX | Street Revision Magnitude: Three-month change in analysts' median forecast for fiscal year one scaled by current mean… |
| `mdl177_2_globaldevnorthamerica_v502_fc_estep` | MATRIX | Leading 12-Month Median Earnings Yield: Next fiscal year's median consensus earnings estimate divided by current trad… |
| `mdl177_2_globaldevnorthamerica_v502_fc_f12mepssev` | MATRIX | Forward 12-M EPS-to-Enterprise Value: Consensus forward twelve-month earnings per share forecast divided by sum of ma… |
| `mdl177_2_globaldevnorthamerica_v502_fc_fcfp` | MATRIX | Forward Free Cash Flow-to-Price: Next four quarters' mean consensus earnings estimate plus trailing twelve-month depr… |
| `mdl177_2_globaldevnorthamerica_v502_fc_fcfroey1p` | MATRIX | Product of TTM FCF Yield and Forward ROE: Trailing twelve-month free cash flow per share times next four quarters' co… |
| `mdl177_2_globaldevnorthamerica_v502_fc_fwdep` | MATRIX | Leading 12-Month Mean Earnings Yield: Next four quarters' mean consensus earnings estimate divided by trading price |
| `mdl177_2_globaldevnorthamerica_v502_fc_fwdroe` | MATRIX | Forward Return on Equity: Analysts' earnings estimate for next four quarters divided by most recent reported common e… |
| `mdl177_2_globaldevnorthamerica_v502_fc_hlep` | MATRIX | Street Revision Confidence: Sum of three-month change in highest and lowest fiscal year one earnings estimates, scale… |
| `mdl177_2_globaldevnorthamerica_v502_fc_numest` | MATRIX | Number of Analyst Coverage: Count of analysts making earnings estimates for fiscal year one |
| `mdl177_2_globaldevnorthamerica_v502_fc_numrevy1` | MATRIX | Net Number of Revisions for Fiscal Year One: Weighted average of analyst increases minus decreases in FY1 forecasts, … |
| `mdl177_2_globaldevnorthamerica_v502_fc_pdy` | MATRIX | Predicted Dividend Yield: Assumed payout ratio times next four quarters' consensus earnings estimate divided by tradi… |
| `mdl177_2_globaldevnorthamerica_v502_fc_rel5yfwdep` | MATRIX | Five-Year Relative Leading 12-M Earnings Yield: Stock's current next four quarters' consensus earnings-to-price ratio… |
| `mdl177_2_globaldevnorthamerica_v502_fc_rev3y1` | MATRIX | Three-Month Revision in FY1 EPS Forecasts: Change in current mean consensus forecast for fiscal year one minus three … |
| `mdl177_2_globaldevnorthamerica_v502_fc_rev3y2` | MATRIX | Three-Month Revision in FY2 EPS Forecasts: Change in current mean consensus earnings estimate for fiscal year two min… |
| `mdl177_2_globaldevnorthamerica_v502_fc_rev6` | MATRIX | Six-Month Average Revision for FY1 EPS: Average of prior six months' monthly changes in consensus analyst forecasts f… |
| `mdl177_2_globaldevnorthamerica_v502_fc_stdevfy1epsp` | MATRIX | Std Dev of FY1 EPS Estimates-to-Price: Standard deviation of analyst forecasts for fiscal year one scaled by closing … |
| `mdl177_2_globaldevnorthamerica_v502_fc_stdevfy2epsp` | MATRIX | Std Dev of FY2 EPS Estimates-to-Price: Standard deviation of analyst forecasts for fiscal year two scaled by closing … |
| `mdl177_2_globaldevnorthamerica_v502_fc_y2aepsg` | MATRIX | Forecasted EPS growth for 2 years ahead: most recent consensus earnings estimate for year 2 minus year 1, divided by … |
| `mdl177_2_globaldevnorthamerica_v502_fcfequity` | MATRIX | Trailing 12-month free cash flow divided by average book equity over the same period |
| `mdl177_2_globaldevnorthamerica_v502_fcfroi` | MATRIX | Trailing 12-month free cash flow divided by average invested capital (sum of common equity, long-term debt, minority … |
| `mdl177_2_globaldevnorthamerica_v502_fcfsale` | MATRIX | Trailing 12-month free cash flow divided by trailing 12-month sales |
| `mdl177_2_globaldevnorthamerica_v502_ff10mrtn` | MATRIX | Percent change in stock price from 12 months ago to 2 months ago (momentum) |
| `mdl177_2_globaldevnorthamerica_v502_fixastto` | MATRIX | Trailing 12-month sales divided by average total fixed assets for the same period |
| `mdl177_2_globaldevnorthamerica_v502_flowratio` | MATRIX | (Current assets minus cash/equivalents) divided by (current liabilities minus short-term debt), using most recent qua… |
| `mdl177_2_globaldevnorthamerica_v502_gear` | MATRIX | Long-term debt divided by (total assets minus current liabilities) |
| `mdl177_2_globaldevnorthamerica_v502_high52w` | MATRIX | Month-end price divided by highest monthly closing price in the past 12 months |
| `mdl177_2_globaldevnorthamerica_v502_indrelcroe_` | MATRIX | Stock's lagged quarterly ROE minus industry average ROE, deflated by industry ROE standard deviation |
| `mdl177_2_globaldevnorthamerica_v502_indrelrecd_` | MATRIX | Stock's asset-adjusted annual doubtful receivables minus industry average, deflated by industry standard deviation |
| `mdl177_2_globaldevnorthamerica_v502_indrelrtn4w_` | MATRIX | Stock’s 4-week return minus industry average 4-week return, deflated by industry standard deviation |
| `mdl177_2_globaldevnorthamerica_v502_indrelrtn5d_` | MATRIX | Stock’s 5-day return minus industry average 5-day return, deflated by industry standard deviation |
| `mdl177_2_globaldevnorthamerica_v502_intcov` | MATRIX | Quarterly operating income before depreciation divided by quarterly long-term debt interest expenses |
| `mdl177_2_globaldevnorthamerica_v502_invast` | MATRIX | Current inventory level divided by total assets from most recent quarter |
| `mdl177_2_globaldevnorthamerica_v502_invto` | MATRIX | Trailing 12-month cost of goods sold divided by average inventory in the same period |
| `mdl177_2_globaldevnorthamerica_v502_lagegp` | MATRIX | Trailing 12-month EPS before extraordinary items multiplied by change in yearly sales per share growth rate, divided … |
| `mdl177_2_globaldevnorthamerica_v502_liqcoeff` | MATRIX | Slope of regression between monthly stock trading turnover ratio and monthly stock price returns |
| `mdl177_2_globaldevnorthamerica_v502_ltg` | MATRIX | Consensus long-term growth forecast, typically expected annual operating earnings increase over next business cycle |
| `mdl177_2_globaldevnorthamerica_v502_milliq` | MATRIX | Monthly average of daily absolute return to daily dollar trading volume ratio (illiquidity measure) |
| `mdl177_2_globaldevnorthamerica_v502_mktcappera` | MATRIX | Current market capitalization divided by number of analysts providing Fiscal Year 1 EPS estimates |
| `mdl177_2_globaldevnorthamerica_v502_mktlev` | MATRIX | Total market value plus latest reported book debt divided by market value |
| `mdl177_2_globaldevnorthamerica_v502_navp` | MATRIX | Book value of net assets per share minus intangibles and liabilities, divided by closing price |
| `mdl177_2_globaldevnorthamerica_v502_ncfeps` | MATRIX | Absolute difference between yearly percent change in operating cash flow per share and yearly percent change in dilut… |
| `mdl177_2_globaldevnorthamerica_v502_netcashp` | MATRIX | Quarterly cash & equivalents minus long- and short-term debt, divided by current market value |
| `mdl177_2_globaldevnorthamerica_v502_netdebt` | MATRIX | Net debt (long- plus short-term debt minus cash & equivalents) divided by the sum of net debt, preferred stock, and c… |
| `mdl177_2_globaldevnorthamerica_v502_nfaldebt` | MATRIX | Quarterly reported net fixed assets divided by long-term debt |
| `mdl177_2_globaldevnorthamerica_v502_niper` | MATRIX | Net income after taxes for trailing 12 months divided by number of employees at last fiscal year end |
| `mdl177_2_globaldevnorthamerica_v502_nlassets` | MATRIX | Natural logarithm of most recent quarterly reported total assets |
| `mdl177_2_globaldevnorthamerica_v502_nlmktcap` | MATRIX | Natural logarithm of the cubic of stock’s total market value |
| `mdl177_2_globaldevnorthamerica_v502_nlprice` | MATRIX | Natural logarithm of the cubic of a stock's unadjusted closing price |
| `mdl177_2_globaldevnorthamerica_v502_nlsales` | MATRIX | Natural logarithm of the cubic of a company's trailing 12-month sales |
| `mdl177_2_globaldevnorthamerica_v502_nlvolcap` | MATRIX | Natural logarithm of the ratio of trailing 1-year average monthly volume to trailing 1-year average monthly market va… |
| `mdl177_2_globaldevnorthamerica_v502_nnastp` | MATRIX | Net current assets per share minus total liabilities per share, divided by price |
| `mdl177_2_globaldevnorthamerica_v502_noato` | MATRIX | Trailing 12-month sales divided by 4-quarter average net operating assets (net operating assets = short-term debt + l… |
| `mdl177_2_globaldevnorthamerica_v502_nopatmargin` | MATRIX | Trailing 12-month NOPAT margin: (Net Income + Interest Expense × (1-Effective Tax Rate)) divided by Net Sales |
| `mdl177_2_globaldevnorthamerica_v502_npm` | MATRIX | Most recently reported quarterly net income after tax divided by quarterly sales |
| `mdl177_2_globaldevnorthamerica_v502_ocfast` | MATRIX | Trailing 12-month net cash flow from operations divided by average total assets |
| `mdl177_2_globaldevnorthamerica_v502_ocfmargin` | MATRIX | Trailing 12-month cash flow from operations divided by trailing 12-month sales |
| `mdl177_2_globaldevnorthamerica_v502_ocfratio` | MATRIX | Most recently reported quarterly cash flow from operations divided by current liabilities |
| `mdl177_2_globaldevnorthamerica_v502_ocfroi` | MATRIX | Trailing 12-month operating cash flow divided by average invested capital (invested capital = common equity + long-te… |
| `mdl177_2_globaldevnorthamerica_v502_ollev` | MATRIX | 1 minus the ratio of (short-term debt + long-term debt + common equity + preferred equity - cash) to (total assets - … |
| `mdl177_2_globaldevnorthamerica_v502_opincltd` | MATRIX | Difference between yearly percent change in operating income and the yearly percent change in long-term debt |
| `mdl177_2_globaldevnorthamerica_v502_oplev` | MATRIX | Percent change in trailing 12-month operating income (from previous quarter) divided by percent change in trailing 12… |
| `mdl177_2_globaldevnorthamerica_v502_opmb` | MATRIX | Most recently reported quarterly operating income divided by quarterly sales |
| `mdl177_2_globaldevnorthamerica_v502_p50_200ratio` | MATRIX | Moving average of last 50 days stock prices divided by moving average of last 200 days stock prices |
| `mdl177_2_globaldevnorthamerica_v502_past` | MATRIX | Month-end trading price divided by most recent quarterly reported total assets per share |
| `mdl177_2_globaldevnorthamerica_v502_pctabv260low` | MATRIX | Current closing price divided by lowest daily low price in last 260 trading days |
| `mdl177_2_globaldevnorthamerica_v502_pctchg3ycf` | MATRIX | Percent change in most recent trailing 12-month cash flow per share compared to 12 quarters ago |
| `mdl177_2_globaldevnorthamerica_v502_pctchg3yeps` | MATRIX | Percent change in most recent trailing 12-month earnings per share compared to 12 quarters ago |
| `mdl177_2_globaldevnorthamerica_v502_pctchg3yfcf` | MATRIX | Percent change in most recent trailing 12-month free cash flow per share compared to 12 quarters ago |
| `mdl177_2_globaldevnorthamerica_v502_pctchg3yocf` | MATRIX | Percent change in most recent trailing 12-month operating cash flow per share compared to 12 quarters ago |
| `mdl177_2_globaldevnorthamerica_v502_pctchgastto` | MATRIX | Percent change in most recent asset turnover ratio compared to 4 quarters ago; asset turnover ratio = trailing 12-mon… |
| `mdl177_2_globaldevnorthamerica_v502_pctchgcf` | MATRIX | Percent change in most recent trailing 12-month cash flow per share compared to 4 quarters ago |
| `mdl177_2_globaldevnorthamerica_v502_pctchgeps` | MATRIX | Percent change in most recent trailing 12-month earnings per share before extra items compared to 4 quarters ago |
| `mdl177_2_globaldevnorthamerica_v502_pctchgfcf` | MATRIX | Percent change in most recent trailing 12-month free cash flow per share compared to 4 quarters ago |
| `mdl177_2_globaldevnorthamerica_v502_pctchgocf` | MATRIX | Percent change in most recent trailing 12-month operating cash flow per share compared to 4 quarters ago |
| `mdl177_2_globaldevnorthamerica_v502_pctchgqtrast` | MATRIX | Growth in most recent reported quarterly total assets per share compared to four quarters ago |
| `mdl177_2_globaldevnorthamerica_v502_pctchgqtrsales` | MATRIX | Growth in most recent reported quarterly sales per share compared to 4 quarters ago |
| `mdl177_2_globaldevnorthamerica_v502_pcurlia` | MATRIX | Most recently reported quarterly current liabilities per share divided by closing price |
| `mdl177_2_globaldevnorthamerica_v502_perg` | MATRIX | Risk-adjusted PEG Ratio: Stock price divided by forward 12-month consensus earnings, scaled by average long-term grow… |
| `mdl177_2_globaldevnorthamerica_v502_pinoa` | MATRIX | Pretax Return on Net Operating Assets: Trailing 12-month operating income after depreciation divided by average net o… |
| `mdl177_2_globaldevnorthamerica_v502_pr_1536` | MATRIX | 15/36 Week Stock Price Ratio: Moving average of last 15 weeks' prices divided by moving average of last 36 weeks' prices |
| `mdl177_2_globaldevnorthamerica_v502_pr_30w75w` | MATRIX | 30-75 Week Stock Price Ratio: Moving average of last 30 weeks' prices divided by moving average of last 75 weeks' prices |
| `mdl177_2_globaldevnorthamerica_v502_qr` | MATRIX | Quick Ratio: (Current assets minus inventories) divided by total current liabilities from the most recent quarter |
| `mdl177_2_globaldevnorthamerica_v502_rationalalpha` | MATRIX | Rational Decay Alpha: Historical 12-month market (S&P 500) adjusted excess return using proprietary decay function (Y… |
| `mdl177_2_globaldevnorthamerica_v502_ratrev6m` | MATRIX | Street Rating Revision: 6-month average change in analyst recommendations |
| `mdl177_2_globaldevnorthamerica_v502_rdsale` | MATRIX | R&D Intensity: Average trailing 12-month R&D expenses divided by total sales in the same period |
| `mdl177_2_globaldevnorthamerica_v502_reinrate` | MATRIX | Reinvestment Rate: (TTM earnings per share before extra items minus TTM dividends per share) divided by average book … |
| `mdl177_2_globaldevnorthamerica_v502_rel5ybp` | MATRIX | 5-year Relative Book-to-Market: Current book-to-market ratio minus 60-month average BTM, scaled by 60-month standard … |
| `mdl177_2_globaldevnorthamerica_v502_rel5ycfp` | MATRIX | 5-year Relative TTM Cash Flow-to-Price: Current TTM cash flow-to-price ratio minus 60-month average, scaled by 60-mon… |
| `mdl177_2_globaldevnorthamerica_v502_rel5ydivp` | MATRIX | 5-year Relative TTM Dividend Yield: Current dividend yield minus 60-month average, scaled by 60-month standard deviation |
| `mdl177_2_globaldevnorthamerica_v502_rel5yebitdap` | MATRIX | 5-year Relative TTM EBITDA-to-Price: Current TTM EBITDA per share-to-price minus 60-month average, scaled by 60-month… |
| `mdl177_2_globaldevnorthamerica_v502_rel5yep` | MATRIX | 5-year Relative TTM Earnings-to-Price: Current TTM EPS before extra items-to-price ratio minus 60-month average, scal… |
| `mdl177_2_globaldevnorthamerica_v502_rel5yfcfp` | MATRIX | 5-year Relative TTM Free Cash Flow-to-Price: Current TTM free cash flow-to-price minus 60-month average, scaled by 60… |
| `mdl177_2_globaldevnorthamerica_v502_rel5yocfp` | MATRIX | 5-year Relative TTM Operating Cash Flow-to-Price: Current TTM operating cash flow-to-price minus 60-month average, sc… |
| `mdl177_2_globaldevnorthamerica_v502_rel5ysp` | MATRIX | 5-year Relative TTM Sales-to-Price: Current TTM sales-to-price ratio minus 60-month average, scaled by 60-month stand… |
| `mdl177_2_globaldevnorthamerica_v502_relpricestrength_` | MATRIX | Industry-adjusted 12-month Relative Price Strength: Stock's 12-month price strength minus industry average, deflated … |
| `mdl177_2_globaldevnorthamerica_v502_reoa` | MATRIX | Retained Earnings-to-Total Assets: Cumulative retained earnings from most recent quarter divided by total assets in s… |
| `mdl177_2_globaldevnorthamerica_v502_rerror60m` | MATRIX | Regression Error of 60-Month CAPM: Standard error of regression slope for stock's last 60-month returns against S&P 5… |
| `mdl177_2_globaldevnorthamerica_v502_revper` | MATRIX | Revenue per Employee: Trailing 12-month total sales divided by number of employees at last reported fiscal year end |
| `mdl177_2_globaldevnorthamerica_v502_roa` | MATRIX | Return on Assets: TTM income before extra items divided by average total assets in same period |
| `mdl177_2_globaldevnorthamerica_v502_roe` | MATRIX | Return on Equity: TTM income before extra items divided by average common equity in same period |
| `mdl177_2_globaldevnorthamerica_v502_roic` | MATRIX | Return on Invested Capital: TTM net income plus interest expenses divided by average invested capital (common equity,… |
| `mdl177_2_globaldevnorthamerica_v502_rsi26w` | MATRIX | 26-Week Relative Price Strength: Most recent weekly closing price divided by weekly closing price 26 weeks ago |
| `mdl177_2_globaldevnorthamerica_v502_rtn2nd6m` | MATRIX | Second Preceding 6-month Return: Percent price change from month t-12 to t-7 |
| `mdl177_2_globaldevnorthamerica_v502_rtn39w` | MATRIX | 39-Week Return with 4-week Lag: Price change from week t-43 to week t-4 |
| `mdl177_2_globaldevnorthamerica_v502_saleeps` | MATRIX | Change in TTM Sales vs EPS: Absolute value of difference between yearly percent change in TTM sales per share and TTM… |
| `mdl177_2_globaldevnorthamerica_v502_saleg5y` | MATRIX | 5-year Sales Growth: Difference between TTM sales per share and those 20 quarters ago, deflated by average prior 20 q… |
| `mdl177_2_globaldevnorthamerica_v502_salegpm` | MATRIX | Change in Quarterly Sales vs Gross Margin: Difference between yearly change in most recent reported quarterly sales a… |
| `mdl177_2_globaldevnorthamerica_v502_salerec` | MATRIX | Difference between the yearly percent change in trailing 12-month sales and the yearly percent change in accounts rec… |
| `mdl177_2_globaldevnorthamerica_v502_sga` | MATRIX | Trailing 12-month selling, general and administrative expenses divided by trailing 12-month sales |
| `mdl177_2_globaldevnorthamerica_v502_sigma` | MATRIX | Standard deviation of a stock’s monthly returns over the prior 60 months |
| `mdl177_2_globaldevnorthamerica_v502_skew90cortn` | MATRIX | Skewness of the distribution of a stock's daily excess returns (relative to S&P 500) over the last 90 days, using 3*(… |
| `mdl177_2_globaldevnorthamerica_v502_skew90drtn` | MATRIX | Skewness of the distribution of a stock's daily price returns over the last 90 days, measuring lack of symmetry, calc… |
| `mdl177_2_globaldevnorthamerica_v502_slope52wp` | MATRIX | 4-week lagged slope coefficient from least squares regression of last 52 weeks’ weekly closing price against weekly d… |
| `mdl177_2_globaldevnorthamerica_v502_slope66wp` | MATRIX | 4-week lagged slope coefficient from least squares regression of last 66 weeks’ weekly closing price against weekly d… |
| `mdl177_2_globaldevnorthamerica_v502_stockrating` | MATRIX | Consensus recommendation for a company (“Street Consensus Rating”) |
| `mdl177_2_globaldevnorthamerica_v502_surp` | MATRIX | Difference between actual earnings per share and consensus forecasts prior to announcement, scaled by quarter-end price |
| `mdl177_2_globaldevnorthamerica_v502_susgrowth` | MATRIX | Maximum growth rate a firm can sustain without increasing financial leverage |
| `mdl177_2_globaldevnorthamerica_v502_swc` | MATRIX | Average working capital over trailing 12 months divided by total sales in that period; working capital = inventory + … |
| `mdl177_2_globaldevnorthamerica_v502_tobinq` | MATRIX | Market value of equity plus debt, divided by assets; (E+D)/A, with debt measured at book value |
| `mdl177_2_globaldevnorthamerica_v502_totalcov` | MATRIX | (Cash Flow from Operations + Interest Paid + Tax Paid) divided by (Interest + Principal Paid) |
| `mdl177_2_globaldevnorthamerica_v502_totalsaleg` | MATRIX | Percent change in company’s trailing 12-month total sales versus total sales one year ago |
| `mdl177_2_globaldevnorthamerica_v502_tstalp` | MATRIX | (CORREL*(260-2)^.5)/(1-CORREL^2)^.5, where CORREL is the correlation coefficient between log daily stock price and da… |
| `mdl177_2_globaldevnorthamerica_v502_ttmaccu` | MATRIX | Difference between trailing 12-month net income and trailing 12-month operating cash flow, scaled by beginning total … |
| `mdl177_2_globaldevnorthamerica_v502_ttmcapexp` | MATRIX | Trailing 12-month capital expenditures per share divided by trading price |
| `mdl177_2_globaldevnorthamerica_v502_ttmcfp` | MATRIX | Trailing 12-month cash flow per share (net income plus depreciation) scaled by trading price |
| `mdl177_2_globaldevnorthamerica_v502_ttmepa` | MATRIX | An indicator that standardizes and compares relative share price between time periods and among companies. |
| `mdl177_2_globaldevnorthamerica_v502_ttmepb` | MATRIX | The company's performance in trailing 1-year before taking into account of non-recurring gain or loss.stock divided b… |
| `mdl177_2_globaldevnorthamerica_v502_ttmfcfev` | MATRIX | Trailing 12-month free cash flow for a stock divided by its enterprise value (EV = equity market value + long/short-t… |
| `mdl177_2_globaldevnorthamerica_v502_ttmfcfp` | MATRIX | Trailing 12-month free cash flow per share divided by month-end price; FCF = operating cash flow minus capital expend… |
| `mdl177_2_globaldevnorthamerica_v502_ttmgfp` | MATRIX | Sum of trailing 12-month growth flow value per share (R&D expenses plus reported net income) divided by month-end tra… |
| `mdl177_2_globaldevnorthamerica_v502_ttmocfp` | MATRIX | Trailing 12-month operating cash flow per share divided by trading price |
| `mdl177_2_globaldevnorthamerica_v502_ttmpiqp` | MATRIX | Most recent trailing 12-month operating and non-operating income per share before income taxes and minority interest … |
| `mdl177_2_globaldevnorthamerica_v502_ttmsaleev` | MATRIX | Trailing 12-month sales for a stock divided by most recent enterprise value |
| `mdl177_2_globaldevnorthamerica_v502_ttmsp` | MATRIX | Most recently reported trailing 12-month sales per share divided by month-end trading price |
| `mdl177_2_globaldevnorthamerica_v502_tw_ep` | MATRIX | Twelve-month forward earnings yield using time-weighted combination of FY1 and FY2 earnings estimates |
| `mdl177_2_globaldevnorthamerica_v502_uap` | MATRIX | Difference between current accounts payable and expected accounts payable (prior year closing balance grown by traili… |
| `mdl177_2_globaldevnorthamerica_v502_uar` | MATRIX | Difference between current accounts receivable and expected accounts receivable (prior year closing balance grown by … |
| `mdl177_2_globaldevnorthamerica_v502_udep` | MATRIX | Unexpected Change in Depreciation: the difference between trailing 12-month depreciation expense and the expected lev… |
| `mdl177_2_globaldevnorthamerica_v502_uinv` | MATRIX | Unexpected Change in Inventory: the difference between a company’s actual inventory level and its expected inventory … |
| `mdl177_2_globaldevnorthamerica_v502_var24m` | MATRIX | 24-Month Value at Risk: the minimum monthly price return over the last 20 months, representing the extreme negative r… |
| `mdl177_2_globaldevnorthamerica_v502_varresirtn` | MATRIX | 24-month residual return variance: the variance of monthly residual returns over the last 24 months, where residual r… |
| `mdl177_2_globaldevnorthamerica_v502_visiratio` | MATRIX | Visibility Ratio: most recent daily trading volume divided by the average daily trading volume over the previous 50 t… |
| `mdl177_2_globaldevnorthamerica_v502_volpre6m` | MATRIX | 6-month moving average of the monthly trading turnover ratio, representing average trading activity over the last 6 m… |
| `mdl177_2_globaldevnorthamerica_v502_volto` | MATRIX | Trading Turnover Ratio: monthly total trading volume divided by the most recently reported total outstanding shares |
| `mdl177_2_globaldevnorthamerica_v502_wcacc` | MATRIX | Working Capital Accruals: accrual component of earnings based on changes such as increases in accounts receivable and… |
| `mdl177_2_globaldevnorthamerica_v502_wcast` | MATRIX | Working Capital-to-Total Assets: average working capital over the trailing 12 months divided by average total assets … |
| `mdl177_2_globaldevnorthamerica_v502_wcinv` | MATRIX | Working Capital to Inventory: most recent quarterly working capital divided by inventory, indicating liquidity covera… |
| `mdl177_2_globaldevnorthamerica_v502_yoychgaa` | MATRIX | Year-over-year change in accruals-to-assets: the difference between scaled accruals (income before extraordinary item… |
| `mdl177_2_globaldevnorthamerica_v502_yoychgcr` | MATRIX | Year-over-year change in current ratio: the change in current assets divided by current liabilities from the most rec… |
| `mdl177_2_globaldevnorthamerica_v502_yoychgda` | MATRIX | Year-over-year change in leverage: the change in total liabilities as a percentage of total assets from the most rece… |
| `mdl177_2_globaldevnorthamerica_v502_yoychggpm` | MATRIX | Year-over-year change in gross profit margin: the change in (sales minus cost of goods sold) divided by sales from th… |
| `mdl177_2_globaldevnorthamerica_v502_yoychgroa` | MATRIX | Year-over-year change in return on assets: the change in trailing 12-month income before extraordinary items as a per… |
| `mdl177_2_globaldevnorthamericasensitivityfactor_apsales` | MATRIX | Company sales exposure or proportion of total sales attributable to Asia-Pacific region |
| `mdl177_2_globaldevnorthamericasensitivityfactor_ceroe` | MATRIX | Cash Earnings Return On Equity, a measure of profitability calculated as cash earnings divided by equity |
| `mdl177_2_globaldevnorthamericasensitivityfactor_crp` | MATRIX | Sensitivity or beta/exposure of the company's returns or fundamentals to changes in Credit Risk Premium (spread betwe… |
| `mdl177_2_globaldevnorthamericasensitivityfactor_da` | MATRIX | Debt to Assets ratio, measures leverage as total debt divided by total assets |
| `mdl177_2_globaldevnorthamericasensitivityfactor_emeasales` | MATRIX | Company sales exposure or proportion of total sales attributable to Europe, Middle East, and Africa (EMEA) region |
| `mdl177_2_globaldevnorthamericasensitivityfactor_hs` | MATRIX | Sensitivity or beta/exposure of the company's returns or fundamentals to changes in Housing Starts |
| `mdl177_2_globaldevnorthamericasensitivityfactor_inflation` | MATRIX | Sensitivity or beta/exposure of the company's returns or fundamentals to changes in the inflation rate |
| `mdl177_2_globaldevnorthamericasensitivityfactor_ip` | MATRIX | Sensitivity or beta/exposure of the company's returns or fundamentals to changes in industrial production |
| `mdl177_2_globaldevnorthamericasensitivityfactor_lasales` | MATRIX | Company sales exposure or proportion of total sales attributable to Latin America region |
| `mdl177_2_globaldevnorthamericasensitivityfactor_nasales` | MATRIX | Company sales exposure or proportion of total sales attributable to North America region |
| `mdl177_2_globaldevnorthamericasensitivityfactor_oilprice` | MATRIX | Sensitivity or beta/exposure of the company's returns or fundamentals to changes in oil prices |
| `mdl177_2_globaldevnorthamericasensitivityfactor_usd` | MATRIX | Sensitivity or beta/exposure of the company's returns or fundamentals to changes in US Dollar value |
| `mdl177_2_globaldevnorthamericasensitivityfactor_vix` | MATRIX | Sensitivity or beta/exposure of the company's returns or fundamentals to changes in overall market volatility as meas… |
| `mdl177_2_globaldevnorthamericasensitivityfactor_yieldsprd` | MATRIX | Sensitivity or beta/exposure of the company's returns or fundamentals to changes in the yield curve slope |
| `mdl177_2_growthanalystmodel2_qga_ltepssurprise` | MATRIX | Long Term EPS Surprise |
| `mdl177_2_growthanalystmodel_qga_composite` | MATRIX | Composite score combining multiple Growth Analyst signals into a single metric |
| `mdl177_2_growthanalystmodel_qga_epscapex` | MATRIX | EPS Growth to CapEx Link |
| `mdl177_2_growthanalystmodel_qga_epstrend` | MATRIX | Trend indicator for earnings per share (direction and persistence of recent EPS changes) |
| `mdl177_2_growthanalystmodel_qga_fcfroe` | MATRIX | Return on equity computed using free cash flow (Free Cash Flow / Shareholders' Equity) |
| `mdl177_2_growthanalystmodel_qga_iarsales` | MATRIX | Inv Acc Rec to Sales Link |
| `mdl177_2_growthanalystmodel_qga_niroe` | MATRIX | Return on equity computed using net income (Net Income / Shareholders' Equity) |
| `mdl177_2_growthanalystmodel_qga_opmarginsales` | MATRIX | Measure of linkage between operating margin and sales (strength of margins relative to revenue growth) |
| `mdl177_2_historicalgrowthfactor_chg3ycfast` | MATRIX | Absolute change in trailing twelve-month operating cash flow over three years, scaled by average total assets |
| `mdl177_2_historicalgrowthfactor_chg3ycfp` | MATRIX | Change in trailing 12-month cash flow per share over 3 years divided by trading price |
| `mdl177_2_historicalgrowthfactor_chg3yepsast` | MATRIX | Change in trailing 12-month EPS (before extra items) from 12 quarters ago, divided by average total assets per share |
| `mdl177_2_historicalgrowthfactor_chg3yepsp` | MATRIX | Change in trailing twelve-month earnings per share from 12 quarters ago, divided by month-end trading price |
| `mdl177_2_historicalgrowthfactor_chg3yfcfast` | MATRIX | Absolute change in trailing twelve-month free cash flow over three years, scaled by average total assets |
| `mdl177_2_historicalgrowthfactor_chg3yfcfp` | MATRIX | Change in trailing 12-month free cash flow per share over 3 years, divided by month-end trading price |
| `mdl177_2_historicalgrowthfactor_chg3yocfast` | MATRIX | Change in trailing 12-month operating cash flow from 12 quarters ago, divided by average total assets |
| `mdl177_2_historicalgrowthfactor_chg3yocfp` | MATRIX | Change in trailing twelve-month operating cash flow per share from 12 quarters ago, divided by trading price |
| `mdl177_2_historicalgrowthfactor_chgars` | MATRIX | Change in accounts receivable to sales ratio over the past year (quarterly) |
| `mdl177_2_historicalgrowthfactor_chgcf` | MATRIX | Change in trailing twelve-month cash flow over the past year (four quarters), scaled by average total assets |
| `mdl177_2_historicalgrowthfactor_chgcfp` | MATRIX | Change in trailing 12-month cash flow per share over the past year divided by trading price |
| `mdl177_2_historicalgrowthfactor_chgeps` | MATRIX | Change in trailing twelve-month earnings per share (before extra items) from 4 quarters ago, scaled by average total … |
| `mdl177_2_historicalgrowthfactor_chgepsp` | MATRIX | Change in trailing 12-month earnings per share over the past year, scaled by month-end trading price |
| `mdl177_2_historicalgrowthfactor_chgfcf` | MATRIX | Change in trailing 12-month free cash flow over the past year divided by average total assets |
| `mdl177_2_historicalgrowthfactor_chgfcfp` | MATRIX | Change in trailing 12-month free cash flow per share over the past year divided by trading price |
| `mdl177_2_historicalgrowthfactor_chgis` | MATRIX | Change in the ratio of inventory to sales over the past year (quarterly) |
| `mdl177_2_historicalgrowthfactor_chgnpm` | MATRIX | Change in net profit margin from one year ago (quarterly), calculated as the difference between most recent and year-… |
| `mdl177_2_historicalgrowthfactor_chgocf` | MATRIX | Change in trailing twelve-month operating cash flow from 4 quarters ago, divided by average total assets |
| `mdl177_2_historicalgrowthfactor_chgocfp` | MATRIX | Change in trailing twelve-month operating cash flow per share from 4 quarters ago, divided by the trading price |
| `mdl177_2_historicalgrowthfactor_chgopm` | MATRIX | Change in quarterly operating profit margin over the past year |
| `mdl177_2_historicalgrowthfactor_cv4qcf3y` | MATRIX | Coefficient of variation (stability or volatility) of trailing twelve-month cash flow over the past 3 years |
| `mdl177_2_historicalgrowthfactor_cv4qeps3y` | MATRIX | Coefficient of variation (a measure of stability or volatility) of trailing twelve-month earnings per share over a 3-… |
| `mdl177_2_historicalgrowthfactor_cv4qfcf3y` | MATRIX | Coefficient of variation (stability or volatility) of trailing twelve-month free cash flow over a 3-year period |
| `mdl177_2_historicalgrowthfactor_cv4qocf3y` | MATRIX | Coefficient of variation (stability or volatility) of trailing twelve-month operating cash flow over a 3-year period |
| `mdl177_2_historicalgrowthfactor_cv4qsales3y` | MATRIX | Coefficient of variation (stability or volatility) of trailing twelve-month sales over a 3-year period |
| `mdl177_2_historicalgrowthfactor_cvopinc` | MATRIX | Coefficient of variation (standard deviation divided by mean) of operating income per share during last 12 quarters |
| `mdl177_2_historicalgrowthfactor_div5yg` | MATRIX | 5-year growth rate of dividends |
| `mdl177_2_historicalgrowthfactor_fcfequity` | MATRIX | TTM free cash flow divided by average book equity in the same 12-month period |
| `mdl177_2_historicalgrowthfactor_pctchg3ycf` | MATRIX | Percent change in trailing twelve-month cash flow per share over a 3-year period |
| `mdl177_2_historicalgrowthfactor_pctchg3yeps` | MATRIX | Percent change in trailing 12-month earnings per share compared to 12 quarters ago |
| `mdl177_2_historicalgrowthfactor_pctchg3yfcf` | MATRIX | Percent change in trailing twelve-month free cash flow per share over a 3-year period |
| `mdl177_2_historicalgrowthfactor_pctchg3yocf` | MATRIX | Percent change in trailing twelve-month operating cash flow per share over a 3-year (12-quarter) period |
| `mdl177_2_historicalgrowthfactor_pctchgastto` | MATRIX | Percent change in asset turnover ratio over the past year (TTM sales divided by average total assets compared to 4 qu… |
| `mdl177_2_historicalgrowthfactor_pctchgcf` | MATRIX | Percent change in trailing 12-month cash flow per share compared to 4 quarters ago |
| `mdl177_2_historicalgrowthfactor_pctchgeps` | MATRIX | Percent change in trailing 12-month EPS before extra items compared to 4 quarters ago |
| `mdl177_2_historicalgrowthfactor_pctchgfcf` | MATRIX | Percent change in trailing 12-month free cash flow per share compared to 4 quarters ago |
| `mdl177_2_historicalgrowthfactor_pctchgocf` | MATRIX | Percent change in trailing 12-month operating cash flow per share compared to 4 quarters ago |
| `mdl177_2_historicalgrowthfactor_pctchgqtrast` | MATRIX | Percent change in most recent reported quarterly total assets per share compared to four quarters ago |
| `mdl177_2_historicalgrowthfactor_pctchgqtrsales` | MATRIX | Growth in most recent quarterly sales per share compared to 4 quarters ago |
| `mdl177_2_historicalgrowthfactor_reinrate` | MATRIX | Reinvestment rate: trailing 12-month EPS before extra items minus dividends per share, divided by average book equity… |
| `mdl177_2_historicalgrowthfactor_rsqr4qcf3y` | MATRIX | R-squared of the regression trend line for trailing twelve-month cash flow per share over the prior 12 quarters (3 ye… |
| `mdl177_2_historicalgrowthfactor_rsqr4qeps3y` | MATRIX | R-squared of the 3-year trend line for TTM EPS (regression fit quality) |
| `mdl177_2_historicalgrowthfactor_rsqr4qfcf3y` | MATRIX | R-squared of the 3-year trend line for TTM free cash flow (regression fit quality) |
| `mdl177_2_historicalgrowthfactor_rsqr4qocf3y` | MATRIX | R-squared of the 3-year trend line for TTM operating cash flow (regression fit quality) |
| `mdl177_2_historicalgrowthfactor_rsqr4qsales3y` | MATRIX | R-squared of the regression trend line for trailing twelve-month sales per share over the prior 12 quarters (3 years) |
| `mdl177_2_historicalgrowthfactor_saleg5y` | MATRIX | 5-year growth in sales per share, difference from 20 quarters ago, deflated by average sales in the prior 20 quarters |
| `mdl177_2_historicalgrowthfactor_salegstdev` | MATRIX | Standard deviation of year-over-year quarterly sales growth rate during last 12 quarters |
| `mdl177_2_historicalgrowthfactor_salesaccel4q` | MATRIX | Measure of acceleration in quarterly sales growth over the last 4 quarters |
| `mdl177_2_historicalgrowthfactor_se5yepsg` | MATRIX | Mean long-term EPS growth rate minus 5-year EPS growth, divided by the stability (variation) of 5-year EPS growth |
| `mdl177_2_historicalgrowthfactor_slope4qcf3y` | MATRIX | Slope of the 3-year trend line for quarterly cash flow (using 4-quarter data) |
| `mdl177_2_historicalgrowthfactor_slope4qeps3y` | MATRIX | Slope of trend line for TTM EPS over the past 3 years (using 4-quarter data) |
| `mdl177_2_historicalgrowthfactor_slope4qfcf3y` | MATRIX | Slope of the 3-year trend line for trailing twelve-month free cash flow per share, indicating long-term growth rate |
| `mdl177_2_historicalgrowthfactor_slope4qocf3y` | MATRIX | Slope of the 3-year trend line for trailing twelve-month operating cash flow per share, indicating long-term growth rate |
| `mdl177_2_historicalgrowthfactor_slope4qsales3y` | MATRIX | Slope of the 3-year trend line for trailing twelve-month sales per share, indicating long-term growth rate |
| `mdl177_2_historicalgrowthfactor_susgrowth` | MATRIX | Maximum sustainable growth rate for the firm without increasing leverage |
| `mdl177_2_historicalgrowthfactor_totalsaleg` | MATRIX | Percent change in trailing 12-month total sales compared to one year ago |
| `mdl177_2_industryrrelativevaluefactor_curindbp_` | MATRIX | Industry Relative Book-to-Market: Stock's current book-to-price ratio minus industry average, scaled by industry stan… |
| `mdl177_2_industryrrelativevaluefactor_curindcfp_` | MATRIX | Industry Relative TTM Cash Flow-to-Price: Stock's trailing 12-month cash flow-to-price ratio minus industry average, … |
| `mdl177_2_industryrrelativevaluefactor_curindcoreepsp_` | MATRIX | Industry Relative TTM Core Earnings-to-Price: Stock's trailing 12-month core earnings-to-price ratio minus industry a… |
| `mdl177_2_industryrrelativevaluefactor_curinddivp_` | MATRIX | Industry Relative TTM Dividend Yield: Stock's trailing 12-month dividend yield minus industry average, scaled by indu… |
| `mdl177_2_industryrrelativevaluefactor_curindebitdap_` | MATRIX | Industry Relative TTM EBITDA-to-Price: Stock's trailing 12-month EBITDA-to-price ratio minus industry average, scaled… |
| `mdl177_2_industryrrelativevaluefactor_curindep_` | MATRIX | Industry Relative TTM EPS-to-Price: Stock's trailing 12-month earnings per share-to-price ratio minus industry averag… |
| `mdl177_2_industryrrelativevaluefactor_curindfcfp_` | MATRIX | Industry Relative TTM Free Cash Flow-to-Price: Stock's trailing 12-month free cash flow-to-price ratio minus industry… |
| `mdl177_2_industryrrelativevaluefactor_curindfwdep_` | MATRIX | Industry Relative Leading 4-QTRs EPS to Price: Stock's next 4-quarter analyst EPS estimate-to-price ratio minus indus… |
| `mdl177_2_industryrrelativevaluefactor_curindocfp_` | MATRIX | Industry Relative TTM Operating Cash Flow-to-Price: Stock's trailing 12-month operating cash flow-to-price ratio minu… |
| `mdl177_2_industryrrelativevaluefactor_curindocfta_` | MATRIX | Industry Relative TTM Operating Cash Flow-to-Total Assets: Stock's trailing 12-month operating cash flow-to-total ass… |
| `mdl177_2_industryrrelativevaluefactor_curindsp_` | MATRIX | Industry Relative TTM Sales-to-Price: Stock's trailing 12-month sales-to-price ratio minus industry average, scaled b… |
| `mdl177_2_liquidityriskfactor_altmanz` | MATRIX | Altman Z score; linear combination of five financial ratios to evaluate bankruptcy risk |
| `mdl177_2_liquidityriskfactor_aqi` | MATRIX | Asset Quality Index; year-over-year change of 1 minus the ratio of (current assets + property, plant & equipment) div… |
| `mdl177_2_liquidityriskfactor_astcomp` | MATRIX | Asset composition; current assets from most recent quarter divided by total assets from same quarter |
| `mdl177_2_liquidityriskfactor_atmcallvol` | MATRIX | Implied volatility of the company’s nearest at-the-money call options |
| `mdl177_2_liquidityriskfactor_atmputvol` | MATRIX | Implied volatility of nearest at-the-money put options for the company |
| `mdl177_2_liquidityriskfactor_bap20d` | MATRIX | 20-day average of bid-ask spread divided by price, proxy for short-term liquidity |
| `mdl177_2_liquidityriskfactor_bdi` | MATRIX | Number of days company can pay its daily operating expenses using only cash and receivables, i.e. basic defensive int… |
| `mdl177_2_liquidityriskfactor_beta` | MATRIX | 60-month beta coefficient: 0.67 times 60-month beta plus 0.33, measuring stock sensitivity to market (S&P 500) moveme… |
| `mdl177_2_liquidityriskfactor_betasigma` | MATRIX | Product of 60-month market beta and standard deviation of monthly returns, indicating combined systematic and total risk |
| `mdl177_2_liquidityriskfactor_booklev` | MATRIX | Book leverage ratio; reported quarterly total assets divided by book equity |
| `mdl177_2_liquidityriskfactor_cashratio` | MATRIX | Most recent quarter’s cash and equivalents divided by current liabilities, indicating liquidity position |
| `mdl177_2_liquidityriskfactor_ccd` | MATRIX | Current cash flow debt coverage ratio: most recent quarterly cash flow from operations less cash dividends, divided b… |
| `mdl177_2_liquidityriskfactor_cfleverage` | MATRIX | Cash flow leverage; total liabilities divided by trailing 12-month operating cash flow |
| `mdl177_2_liquidityriskfactor_covol` | MATRIX | Slope of the regression line across 60 months of trading volume against time; indicates trend in trading activity |
| `mdl177_2_liquidityriskfactor_curratio` | MATRIX | Current ratio; most recent quarter’s current assets divided by current liabilities |
| `mdl177_2_liquidityriskfactor_cvvolp20d` | MATRIX | Ratio of coefficient of variation of last 20 days’ closing prices to coefficient of variation of daily trading volume… |
| `mdl177_2_liquidityriskfactor_de` | MATRIX | Long-term debt-to-equity; latest long-term debt divided by book equity |
| `mdl177_2_liquidityriskfactor_debtcf` | MATRIX | Sum of latest reported long-term debt and short-term interest-bearing debt divided by TTM cash flow |
| `mdl177_2_liquidityriskfactor_dfl` | MATRIX | Degree of financial leverage; sum of TTM pretax income and TTM interest expense divided by TTM pretax income |
| `mdl177_2_liquidityriskfactor_divcov` | MATRIX | Ratio of trailing 1-year profits to annual dividends, representing coverage of dividends by earnings |
| `mdl177_2_liquidityriskfactor_flowratio` | MATRIX | Flow ratio; (current assets minus cash & equivalents) divided by (current liabilities minus short-term debt), using l… |
| `mdl177_2_liquidityriskfactor_gear` | MATRIX | Capital gearing ratio; long-term debt divided by (total assets minus current liabilities) |
| `mdl177_2_liquidityriskfactor_growdura` | MATRIX | Growth Duration |
| `mdl177_2_liquidityriskfactor_impduration` | MATRIX | Implied Equity Duration |
| `mdl177_2_liquidityriskfactor_intcov` | MATRIX | Interest coverage; latest quarterly operating income before depreciation divided by long-term debt interest expenses |
| `mdl177_2_liquidityriskfactor_liqcoeff` | MATRIX | Liquidity coefficient; slope from regression between monthly trading turnover ratio and monthly price returns |
| `mdl177_2_liquidityriskfactor_mad3yttmni` | MATRIX | Three-year mean absolute deviation of trailing twelve month net income, measuring income variability over the past th… |
| `mdl177_2_liquidityriskfactor_mad3yttmsale` | MATRIX | Three-year mean absolute deviation of trailing twelve month sales, measuring revenue variability over three years |
| `mdl177_2_liquidityriskfactor_milliq` | MATRIX | Stock illiquidity; monthly average of daily absolute return divided by daily dollar trading volume |
| `mdl177_2_liquidityriskfactor_mktcappera` | MATRIX | Current market capitalization divided by the number of analysts providing fiscal year 1 earnings estimates |
| `mdl177_2_liquidityriskfactor_mktlev` | MATRIX | Sum of total market capitalization and most recent quarterly book debt divided by market capitalization; represents m… |
| `mdl177_2_liquidityriskfactor_monchgsip` | MATRIX | Month-to-month change in short interest position (ratio), measures change in the amount of stock sold short |
| `mdl177_2_liquidityriskfactor_netcashp` | MATRIX | Net cash to equity; (quarterly cash & equivalents minus long-term and current debt) divided by current market value |
| `mdl177_2_liquidityriskfactor_nfaldebt` | MATRIX | Most recent quarterly net fixed assets divided by total long-term debt; gauges asset coverage of long-term debt |
| `mdl177_2_liquidityriskfactor_nlassets` | MATRIX | Natural logarithm of most recent quarterly total assets |
| `mdl177_2_liquidityriskfactor_nlmktcap` | MATRIX | Natural logarithm of the cube of a company’s total market capitalization, as a size factor |
| `mdl177_2_liquidityriskfactor_nlprice` | MATRIX | Natural logarithm of the cubic of a stock's unadjusted closing price |
| `mdl177_2_liquidityriskfactor_nlsales` | MATRIX | Natural logarithm of the cube of a company’s trailing twelve-month sales, used as a size proxy |
| `mdl177_2_liquidityriskfactor_nlvolcap` | MATRIX | Logarithm of the ratio of trailing one-year average monthly trading volume to trailing one-year average monthly marke… |
| `mdl177_2_liquidityriskfactor_numest` | MATRIX | Number of financial analysts providing earnings estimates for the company for the current fiscal year |
| `mdl177_2_liquidityriskfactor_ocfratio` | MATRIX | Operating cash flow ratio; latest quarterly operating cash flow divided by current liabilities |
| `mdl177_2_liquidityriskfactor_ohlsonscore` | MATRIX | Ohlson bankruptcy score; statistical model assessing bankruptcy probability based on size, leverage, performance, liq… |
| `mdl177_2_liquidityriskfactor_oplev` | MATRIX | Operating leverage; percent change in TTM operating income from previous quarter divided by percent change in TTM sal… |
| `mdl177_2_liquidityriskfactor_pcurlia` | MATRIX | Current liabilities per share (from latest report) divided by the company’s closing share price, indicating balance s… |
| `mdl177_2_liquidityriskfactor_qr` | MATRIX | Quick ratio: (current assets minus inventories) divided by current liabilities for most recent quarter, measures shor… |
| `mdl177_2_liquidityriskfactor_rerror60m` | MATRIX | Standard error of the slope of the regression line relating 60 months of a stock’s monthly returns to S&P 500 Index r… |
| `mdl177_2_liquidityriskfactor_si_ratio` | MATRIX | Ratio of shares sold short to average daily trading volume over the last 30 days |
| `mdl177_2_liquidityriskfactor_sigma` | MATRIX | Standard deviation of a stock’s monthly returns over prior 60 months; a volatility measure |
| `mdl177_2_liquidityriskfactor_sip` | MATRIX | Total shares of the company sold short, as reported by the exchange |
| `mdl177_2_liquidityriskfactor_tobinq` | MATRIX | Tobin’s q ratio; market value of equity plus debt divided by total assets, debt measured at book value |
| `mdl177_2_liquidityriskfactor_totalcov` | MATRIX | Ratio of (cash flow from operations + interest paid + tax paid) to (interest and principal paid); assesses ability to… |
| `mdl177_2_liquidityriskfactor_voldiff_pc` | MATRIX | Implied volatility difference between at-the-money put and call options, capturing liquidity risk or sentiment skew |
| `mdl177_2_liquidityriskfactor_volto` | MATRIX | Trading turnover ratio; monthly total trading volume divided by current outstanding shares |
| `mdl177_2_liquidityriskfactor_yoychgcr` | MATRIX | Year-over-year change in current ratio, comparing the most recent quarterly current ratio to that of the same quarter… |
| `mdl177_2_liquidityriskfactor_yoychgda` | MATRIX | Year-over-year quarterly change in leverage, expressed as difference in total liabilities to total assets percentage … |
| `mdl177_2_managementqualityfactor_aci` | MATRIX | Abnormal Capital Investment: change in firm’s recent trailing 12-month capital investment intensity compared to the a… |
| `mdl177_2_managementqualityfactor_acp` | MATRIX | Average collection period: average trailing 12-month accounts receivable times 365 divided by trailing 12-month sales |
| `mdl177_2_managementqualityfactor_adverint` | MATRIX | Advertising Intensity |
| `mdl177_2_managementqualityfactor_app` | MATRIX | Average payable period: average trailing 12-month accounts payable times 365 divided by trailing 12-month cost of goo… |
| `mdl177_2_managementqualityfactor_aspanratio` | MATRIX | Quarterly operating assets minus operating liabilities, divided by lagged total assets |
| `mdl177_2_managementqualityfactor_astto` | MATRIX | Assets Turnover Ratio: trailing 12-month sales divided by most recently reported quarterly assets |
| `mdl177_2_managementqualityfactor_capacq` | MATRIX | Capital acquisition ratio, a measure relevant to sector or industry valuation and financial health |
| `mdl177_2_managementqualityfactor_capdistp` | MATRIX | Total Capital Distribution |
| `mdl177_2_managementqualityfactor_capexast` | MATRIX | Capital Expenditure-to-Total Assets: trailing 12-month capital expenditures divided by total assets from most recent … |
| `mdl177_2_managementqualityfactor_capexsale` | MATRIX | Capital expenditures divided by sales over the trailing 12 months |
| `mdl177_2_managementqualityfactor_cashburnrate` | MATRIX | Negative of (cash from operations + cash from investments) divided by (cash + short-term investments) |
| `mdl177_2_managementqualityfactor_cashc` | MATRIX | Cash cycle: average inventory days plus average collection days minus average payable days |
| `mdl177_2_managementqualityfactor_cashsale` | MATRIX | Cash-to-sales: average cash & equivalents in trailing 12 months divided by trailing 12-month sales |
| `mdl177_2_managementqualityfactor_cfita` | MATRIX | TTM Cash Flow from Investment to Total Assets: trailing 12-month cash flow from investing divided by last 4 quarters’… |
| `mdl177_2_managementqualityfactor_cfroi` | MATRIX | Cash Flow Return on Invested Capital: trailing 12-month cash flow divided by average invested capital (common equity,… |
| `mdl177_2_managementqualityfactor_chgnoa` | MATRIX | Year-over-year change of net operating assets to total assets, where net operating assets equal short-term debt plus … |
| `mdl177_2_managementqualityfactor_chgollev` | MATRIX | Change in Operating Liability Leverage: current quarter operating liability leverage less operating liability leverag… |
| `mdl177_2_managementqualityfactor_chgreccast` | MATRIX | Year-over-year change in accounts receivable to current assets |
| `mdl177_2_managementqualityfactor_divcf` | MATRIX | Dividends to cash flow: trailing 12-month cash dividends divided by trailing 12-month cash flow |
| `mdl177_2_managementqualityfactor_equityto` | MATRIX | Equity Turnover: trailing 12-month sales divided by average trailing 12-month reported book equity |
| `mdl177_2_managementqualityfactor_exdisspi` | MATRIX | 24-Month Unusual Items to Sales |
| `mdl177_2_managementqualityfactor_fcfroi` | MATRIX | Free Cash Flow Return on Invested Capital: trailing 12-month free cash flow divided by average invested capital |
| `mdl177_2_managementqualityfactor_fcfsale` | MATRIX | Free cash flow to sales ratio over the trailing 12 months |
| `mdl177_2_managementqualityfactor_fixastto` | MATRIX | Fixed Assets Turnover: trailing 12-month sales divided by average total fixed assets over the same period |
| `mdl177_2_managementqualityfactor_fwdroe` | MATRIX | Forward (projected) return on equity |
| `mdl177_2_managementqualityfactor_indrelcroe_` | MATRIX | Stock’s lagged quarterly return on equity minus the industry average ROE, normalized by industry ROE standard deviation |
| `mdl177_2_managementqualityfactor_invast` | MATRIX | Current inventory level divided by total assets from most recent quarter |
| `mdl177_2_managementqualityfactor_invto` | MATRIX | Inventory Turnover Ratio: trailing 12-month cost of goods sold divided by average inventory over the same period |
| `mdl177_2_managementqualityfactor_min1ygrossmargin` | MATRIX | Lowest gross margin over the last 1 year |
| `mdl177_2_managementqualityfactor_min1yopmargin` | MATRIX | Minimum (trough) operating margin in the last year |
| `mdl177_2_managementqualityfactor_min2ygrossmargin` | MATRIX | Lowest gross margin over the last 2 years |
| `mdl177_2_managementqualityfactor_min2yopmargin` | MATRIX | Minimum (trough) operating margin in the last 2 years |
| `mdl177_2_managementqualityfactor_min3ygrossmargin` | MATRIX | Lowest gross margin over the last 3 years |
| `mdl177_2_managementqualityfactor_min3yopmargin` | MATRIX | Lowest operating profit margin over the last 3 years |
| `mdl177_2_managementqualityfactor_nef` | MATRIX | Net External Financing |
| `mdl177_2_managementqualityfactor_netdebt` | MATRIX | Net Debt Ratio: net debt divided by sum of net debt, preferred stock, and common stock, with net debt as long-term pl… |
| `mdl177_2_managementqualityfactor_niper` | MATRIX | Net income per employee: income after taxes for trailing 12 months divided by number of employees at last reported fi… |
| `mdl177_2_managementqualityfactor_noato` | MATRIX | Net operating asset turnover: trailing 12-month sales divided by 4-quarters average net operating assets (short-term … |
| `mdl177_2_managementqualityfactor_nopatmargin` | MATRIX | Net operating profit after tax (NOPAT) margin: (Net Income + Interest Expense*(1-Effective Tax Rate)) divided by net … |
| `mdl177_2_managementqualityfactor_npm` | MATRIX | Net profit margin: most recent quarterly net income after tax divided by corresponding quarterly sales |
| `mdl177_2_managementqualityfactor_ocfast` | MATRIX | Operating cash flow to assets: trailing 12-month net cash flow from operations divided by average total assets |
| `mdl177_2_managementqualityfactor_ocfmargin` | MATRIX | Operating Cash Flow Profit Margin: trailing 12-month operating cash flow divided by trailing 12-month sales |
| `mdl177_2_managementqualityfactor_ocfroi` | MATRIX | Operating cash flow return on invested capital: trailing 12-month operating cash flow divided by average invested cap… |
| `mdl177_2_managementqualityfactor_ollev` | MATRIX | Operating liability leverage: 1 minus the ratio of (short-term debt + long-term debt + common equity + preferred equi… |
| `mdl177_2_managementqualityfactor_opmb` | MATRIX | Operating Profit Margin: quarterly operating income divided by quarterly sales |
| `mdl177_2_managementqualityfactor_over` | MATRIX | Overhead expenses divided by sales |
| `mdl177_2_managementqualityfactor_pinoa` | MATRIX | Pretax return on net operating assets: trailing 12-month operating income after depreciation divided by average net o… |
| `mdl177_2_managementqualityfactor_rdsale` | MATRIX | R&D intensity: average trailing 12-month research & development expenses divided by total sales in the same period |
| `mdl177_2_managementqualityfactor_reoa` | MATRIX | Retained Earnings-to-Total Assets: cumulative retained earnings from most recent quarter divided by total assets from… |
| `mdl177_2_managementqualityfactor_revper` | MATRIX | Total sales for the trailing 12 months divided by number of employees at last fiscal year end |
| `mdl177_2_managementqualityfactor_roa` | MATRIX | Return on assets: trailing 12-month income before extra items divided by average total assets in the same period |
| `mdl177_2_managementqualityfactor_roe` | MATRIX | Return on equity: trailing 12-month income before extra items divided by average common equity in the same period |
| `mdl177_2_managementqualityfactor_roic` | MATRIX | Return on Invested Capital: trailing 12-month net income and interest expenses divided by average invested capital (c… |
| `mdl177_2_managementqualityfactor_saleicap` | MATRIX | Trailing 12-month sales divided by invested capital |
| `mdl177_2_managementqualityfactor_sga` | MATRIX | SG&A Expenses-to-Sales: trailing 12-month selling, general & admin expenses divided by trailing 12-month sales |
| `mdl177_2_managementqualityfactor_swc` | MATRIX | Working capital to sales: average working capital for trailing 12 months divided by total sales in the same period |
| `mdl177_2_managementqualityfactor_wcast` | MATRIX | Working Capital-to-Total Assets: average working capital in the trailing 12-months divided by average total assets in… |
| `mdl177_2_managementqualityfactor_wcinv` | MATRIX | Working Capital to Inventory: most recent quarterly working capital divided by inventory |
| `mdl177_2_managementqualityfactor_yoychggpm` | MATRIX | Yearly Change In Gross Profit Margin: most recent quarterly gross profit margin minus margin for same quarter one yea… |
| `mdl177_2_managementqualityfactor_yoychgroa` | MATRIX | Yearly Change in Return on Assets: most recent trailing 12-month net income before extra items as % of total assets, … |
| `mdl177_2_momemtumanalystmodel_qma_alpha6m` | MATRIX | Rank of the six-month change in alpha (risk-adjusted outperformance) relative to peers |
| `mdl177_2_momemtumanalystmodel_qma_chgnowc` | MATRIX | Rank of change in net working capital (current assets minus current liabilities), indicating how working capital shif… |
| `mdl177_2_momemtumanalystmodel_qma_composite` | MATRIX | Rank representing composite momentum signal derived from analyst-related factors |
| `mdl177_2_momemtumanalystmodel_qma_condsurp` | MATRIX | Rank of the conditional earnings or revenue surprise, likely adjusted for market or analyst expectations |
| `mdl177_2_momemtumanalystmodel_qma_earnexp` | MATRIX | Rank for analyst expectations, calculated as equal-weighted average of earnings revisions and ratings change ranks |
| `mdl177_2_momemtumanalystmodel_qma_eplinkage` | MATRIX | Rank indicating the strength of linkage between earnings-related changes and stock price movement, considering factor… |
| `mdl177_2_momemtumanalystmodel_qma_epsgrwth` | MATRIX | Rank representing change in trailing twelve month EPS growth, scaled by recent stock price (earnings yield based) |
| `mdl177_2_momemtumanalystmodel_qma_estrev` | MATRIX | Rank based on analyst estimate revisions, reflecting recent up and down changes to future EPS forecasts relative to t… |
| `mdl177_2_momemtumanalystmodel_qma_indrelrtn3m` | MATRIX | Rank based on difference between a stock’s 3-month return and the industry average 3-month return |
| `mdl177_2_momemtumanalystmodel_qma_lagpricemo` | MATRIX | Rank of lagged price momentum, comparing prior 12-month to recent 1-month returns and adjusting for volatility |
| `mdl177_2_momemtumanalystmodel_qma_mktresponse` | MATRIX | Rank based on the market's price response following recent earnings announcements, typically measured over a short wi… |
| `mdl177_2_momemtumanalystmodel_qma_ratingchg` | MATRIX | Rank reflecting analyst ratings changes, indicating the trend in upgrades and downgrades over recent months |
| `mdl177_2_momemtumanalystmodel_qma_relpricemo` | MATRIX | Rank of the stock's price momentum relative to market or peer group, combining various momentum measures |
| `mdl177_2_momemtumanalystmodel_qma_repearnmom` | MATRIX | Rank representing average of earnings growth and earnings surprise, measuring earnings momentum |
| `mdl177_2_momemtumanalystmodel_qma_rskadj` | MATRIX | Rank aggregating risk adjustments, incorporating volatility and growth, penalizing excessive volatility or return dev… |
| `mdl177_2_momemtumanalystmodel_qma_ttmfcfchg` | MATRIX | Rank for change in trailing twelve month free cash flow over two quarters, scaled by previous value |
| `mdl177_2_priceanalystmodel2_qpa_composite` | MATRIX | Composite signal from the QSG Price Analyst model for US equities, combining multiple analyst-driven price-related fa… |
| `mdl177_2_priceanalystmodel_qpa_compsn` | MATRIX | Sector-neutral price analyst model signal, designed to remove sector biases from the stock’s price signal |
| `mdl177_2_priceanalystmodel_qpa_indrs` | MATRIX | Industry relative strength signal for a stock, measuring its price performance versus its industry peers |
| `mdl177_2_priceanalystmodel_qpa_rskadjrs` | MATRIX | Risk Adj Relative Strength |
| `mdl177_2_pricemomemtummodel2_indrelrtn5d_` | MATRIX | 5-day industry-relative return: the stock’s 5-day return minus its industry average, standardized by the industry’s r… |
| `mdl177_2_pricemomemtummodel_pmm_composite` | MATRIX | A combined price momentum signal aggregating multiple price momentum metrics for a stock, used as an overall momentum… |
| `mdl177_2_pricemomemtummodel_rationalalpha` | MATRIX | The excess 12-month return of a stock versus the market (S&P 500), adjusted using a proprietary rational decay functi… |
| `mdl177_2_pricemomemtummodel_relpricestrength_` | MATRIX | The stock's industry-adjusted 12-month relative price strength: its 12-month price strength minus the average price s… |
| `mdl177_2_pricemomemtummodel_visiratio` | MATRIX | Ratio of a stock's latest daily trading volume to its average daily trading volume over the previous 50 days, reflect… |
| `mdl177_2_pricemomemtummodel_voldiff_pc` | MATRIX | Difference between at-the-money put option volatility and at-the-money call option volatility for the stock, measurin… |
| `mdl177_2_pricemomentumfactor_abr` | MATRIX | Abnormal return observed around the quarterly earnings release event for the stock |
| `mdl177_2_pricemomentumfactor_actrtn12m` | MATRIX | Percent change in stock price from 13 months ago to 1 month ago (12-month active return with 1-month lag) |
| `mdl177_2_pricemomentumfactor_actrtn18m` | MATRIX | Percent change in stock price from 19 months ago to 1 month ago (18-month active return with 1-month lag) |
| `mdl177_2_pricemomentumfactor_actrtn1m` | MATRIX | Percent change in stock price from last month to this month (1-month active return) |
| `mdl177_2_pricemomentumfactor_actrtn24m` | MATRIX | Percent change in stock price from 25 months ago to 1 month ago (24-month active return with 1-month lag) |
| `mdl177_2_pricemomentumfactor_actrtn2m` | MATRIX | Percent change in the stock's price over the last 2 months |
| `mdl177_2_pricemomentumfactor_actrtn36m` | MATRIX | Percent price change for the stock from 37 months prior to 1 month prior; a measure of 36-month active return |
| `mdl177_2_pricemomentumfactor_actrtn3m` | MATRIX | Percent change in price over the last three months |
| `mdl177_2_pricemomentumfactor_actrtn60m` | MATRIX | Percent change in stock price from 61 months ago to 1 month ago (60-month active return with 1-month lag) |
| `mdl177_2_pricemomentumfactor_actrtn6m` | MATRIX | Percent price change for the stock from 7 months prior to 1 month prior; a measure of 6-month active return |
| `mdl177_2_pricemomentumfactor_alpha60m` | MATRIX | Intercept from regression of stock's monthly returns against S&P 500 monthly returns over last 60 months (five-year a… |
| `mdl177_2_pricemomentumfactor_chg6malpha18m` | MATRIX | Change in stock's 18-month alpha over previous 6 months; alpha is regression intercept (monthly returns vs S&P 500) o… |
| `mdl177_2_pricemomentumfactor_chgalpha12m` | MATRIX | Change in the stock's 12-month alpha over the last 6 months, where alpha is the regression intercept of the stock's m… |
| `mdl177_2_pricemomentumfactor_chgalpha36m` | MATRIX | Change in stock's 36-month alpha over the past 6 months, where alpha is regression intercept (monthly returns vs S&P … |
| `mdl177_2_pricemomentumfactor_chgvolpre4y` | MATRIX | Difference between recent 6-month average monthly trading volume (as turnover ratio) and the 12-month average monthly… |
| `mdl177_2_pricemomentumfactor_cvpre90dp` | MATRIX | Coefficient of variation (standard deviation divided by mean) of the stock's closing prices over the last 90 days, re… |
| `mdl177_2_pricemomentumfactor_ff10mrtn` | MATRIX | Percent price change representing Fama-French momentum from 12 months prior to 2 months prior for the stock |
| `mdl177_2_pricemomentumfactor_high52w` | MATRIX | Ratio of the stock's month-end price to the highest monthly closing price in the past 12 months, measuring proximity … |
| `mdl177_2_pricemomentumfactor_indrelrtn4w_` | MATRIX | Stock's 4-week return minus industry average 4-week return, scaled by industry standard deviation, indicating industr… |
| `mdl177_2_pricemomentumfactor_indrelrtn5d_` | MATRIX | Stock's 5-day return minus industry average 5-day return, scaled by industry standard deviation, reflecting industry-… |
| `mdl177_2_pricemomentumfactor_normalmf60d` | MATRIX | Money Flow signal normalized over the last 60 days |
| `mdl177_2_pricemomentumfactor_p50_200ratio` | MATRIX | Moving average of a stock's last 50 days prices divided by the moving average over the last 200 days; a technical ind… |
| `mdl177_2_pricemomentumfactor_pc_ratio` | MATRIX | Put/Call ratio (ratio of traded put options to call options), an indicator of market sentiment or positioning |
| `mdl177_2_pricemomentumfactor_pctabv260low` | MATRIX | Ratio of the current closing price to the lowest daily price in the last 260 trading days, measuring how far price ha… |
| `mdl177_2_pricemomentumfactor_po4_52` | MATRIX | Difference or oscillator between the stock's price measured over a 4-week versus 52-week period, typically used to ga… |
| `mdl177_2_pricemomentumfactor_pr_1536` | MATRIX | Ratio of moving average of the stock's prices in the last 15 weeks to the moving average in the last 36 weeks, indica… |
| `mdl177_2_pricemomentumfactor_pr_30w75w` | MATRIX | Moving average of last 30 weeks' prices divided by moving average of last 75 weeks' prices, indicating medium/long-te… |
| `mdl177_2_pricemomentumfactor_pvt51w` | MATRIX | 51-week volume price trend indicator with a 4-week lag |
| `mdl177_2_pricemomentumfactor_rationalalpha` | MATRIX | Proprietary measure of the stock's 12-month market-adjusted excess return (regression Y-intercept vs S&P 500) adjuste… |
| `mdl177_2_pricemomentumfactor_relpricestrength_` | MATRIX | Industry-adjusted 12-month relative price strength; stock's price strength relative to industry peers, standardized |
| `mdl177_2_pricemomentumfactor_rsi26w` | MATRIX | Ratio of most recent weekly closing price to the closing price 26 weeks ago; a 26-week relative price strength indicator |
| `mdl177_2_pricemomentumfactor_rtn2nd6m` | MATRIX | Percent price change from 12 months ago to 7 months ago (second preceding 6-month return), measuring earlier momentum |
| `mdl177_2_pricemomentumfactor_rtn39w` | MATRIX | Stock price change over a 39-week period with a 4-week lag (from week t-43 to t-4) |
| `mdl177_2_pricemomentumfactor_sharpe36m` | MATRIX | Sharpe Ratio for the past 36 months, which quantifies risk-adjusted return using total volatility |
| `mdl177_2_pricemomentumfactor_skew90cortn` | MATRIX | Skewness of daily stock excess returns (vs. S&P 500 index) over the previous 90 days |
| `mdl177_2_pricemomentumfactor_skew90drtn` | MATRIX | Skewness (asymmetry) of the distribution of daily stock returns over the most recent 90 days |
| `mdl177_2_pricemomentumfactor_slope52wp` | MATRIX | Lagged slope coefficient of the least squares regression line of weekly closing prices over the last 52 weeks |
| `mdl177_2_pricemomentumfactor_slope66wp` | MATRIX | Lagged slope coefficient from least squares regression of closing prices over the last 66 weeks, indicating the trend… |
| `mdl177_2_pricemomentumfactor_sortinoratio` | MATRIX | Sortino Ratio, which measures risk-adjusted return considering only downside (negative) volatility |
| `mdl177_2_pricemomentumfactor_tstalp` | MATRIX | One-year price momentum indicator based on the correlation of log daily prices over the last 260 trading days |
| `mdl177_2_pricemomentumfactor_var24m` | MATRIX | Minimum monthly price return for a stock over the last 24 months, used as a Value at Risk measure |
| `mdl177_2_pricemomentumfactor_varresirtn` | MATRIX | Variance of the monthly residual return (actual minus beta-adjusted S&P 500 return) over the last 24 months, measurin… |
| `mdl177_2_pricemomentumfactor_visiratio` | MATRIX | Stock's most recent daily volume divided by the average daily volume over prior 50 trading days, indicating current v… |
| `mdl177_2_pricemomentumfactor_volpre6m` | MATRIX | 6-month moving average of monthly turnover ratio (trading volume relative to shares outstanding) |
| `mdl177_2_put_put_capmod` | MATRIX | Capital Strength Module |
| `mdl177_2_put_put_cashburn` | MATRIX | Cash Burn Rate |
| `mdl177_2_put_put_chgalpha` | MATRIX | Six-Month Alpha Change Rank |
| `mdl177_2_put_put_chgoll` | MATRIX | Change in Operating Liability Leverage |
| `mdl177_2_put_put_chshrs` | MATRIX | Percent change in shares outstanding over a recent period, e.g. due to buybacks or issuance |
| `mdl177_2_put_put_dypeg` | MATRIX | Reciprocal of Dividend Yield-adjusted PEG |
| `mdl177_2_put_put_equality` | MATRIX | Earnings Quality Rank |
| `mdl177_2_put_put_indepsp` | MATRIX | Industry-relative ratio of core EPS to price |
| `mdl177_2_put_put_indestep` | MATRIX | Industry-relative ratio of expected (forward-looking, aggregate next 4 quarters) earnings per share to price |
| `mdl177_2_put_put_indfcfp` | MATRIX | Industry-relative ratio of free cash flow to price |
| `mdl177_2_put_put_indroe` | MATRIX | Industry-relative return on equity |
| `mdl177_2_put_put_momod` | MATRIX | Composite momentum module, combining multiple momentum signals |
| `mdl177_2_put_put_opincev` | MATRIX | Ratio of operating income to enterprise value |
| `mdl177_2_put_put_qualmod` | MATRIX | Quality Module |
| `mdl177_2_put_put_siratio` | MATRIX | Short-interest ratio (shares sold short divided by float or average daily volume) |
| `mdl177_2_put_put_strevconf` | MATRIX | Street Revision Confidence |
| `mdl177_2_put_put_sucf` | MATRIX | Standardized value of unexpected cash flow (actual minus expected, normalized across stocks) |
| `mdl177_2_put_put_totcov` | MATRIX | Total Coverage |
| `mdl177_2_put_put_valmod` | MATRIX | Valuation Module |
| `mdl177_2_relativevaluemodel_capacq` | MATRIX | Capital Acquisition Ratio; trailing 12-month operating cash flow less cash dividends, divided by total expenditures f… |
| `mdl177_2_relativevaluemodel_fc_estep` | MATRIX | Leading 12-Month Median Earnings Yield; median consensus earnings estimate for the next fiscal year divided by tradin… |
| `mdl177_2_relativevaluemodel_fmrelval` | MATRIX | Fielitz & Muller Relative Intrinsic Value |
| `mdl177_2_relativevaluemodel_roe` | MATRIX | Return on Equity; trailing 12-month income before extra items divided by average common equity for the same period |
| `mdl177_2_relativevaluemodel_rvm_composite` | MATRIX | Relative Value Model Composite; overall composite score aggregating various relative value signals within the model |
| `mdl177_2_relativevaluemodel_ttmfcfp` | MATRIX | TTM Free Cash Flow-to-Price; trailing 12-month free cash flow per share divided by month-end trading price. Free cash… |
| `mdl177_2_sensitivityfactor400_actrtn9m` | MATRIX | Percent change in the stock price over the past 9 months, with a 1-month lag (from month t-10 to t-1) |
| `mdl177_2_sensitivityfactor400_ag` | MATRIX | Aggregate Gamma |
| `mdl177_2_sensitivityfactor400_apsales` | MATRIX | Company’s sales revenue exposure to the Asia-Pacific region, expressed as a proportion of total sales |
| `mdl177_2_sensitivityfactor400_capexdeplink` | MATRIX | Capital Expenditures to Depreciation Linkage : It is defined as the absolute value of the difference between ranked (… |
| `mdl177_2_sensitivityfactor400_ceroe` | MATRIX | Cash Earnings Return On Equity |
| `mdl177_2_sensitivityfactor400_chg12msip` | MATRIX | Change in the short interest ratio (shares sold short / shares outstanding) over the previous 12 months |
| `mdl177_2_sensitivityfactor400_chg12mtotdebt` | MATRIX | Relative change in total debt (sum of long-term and short-term debt) over the past 12 months |
| `mdl177_2_sensitivityfactor400_chginvavgast` | MATRIX | 12-month change in quarterly total inventory, normalized by the average assets between the most recent quarter-end an… |
| `mdl177_2_sensitivityfactor400_chgqtrepssurp` | MATRIX | Change in Real Earnings Surprise : It is defined as the change in quarterly earnings surprise (Actual EPS - Consensus… |
| `mdl177_2_sensitivityfactor400_crp` | MATRIX | Credit Risk Premium Sensitivity |
| `mdl177_2_sensitivityfactor400_dm` | MATRIX | A score representing financial distress risk, calculated using the Campbell, Hilscher and Szilagyi model and/or Chen … |
| `mdl177_2_sensitivityfactor400_earnshortfall` | MATRIX | Earnings Shortfall : It is defined as the difference between reported accounting earnings and free cash flow, scaled … |
| `mdl177_2_sensitivityfactor400_emeasales` | MATRIX | Company’s sales revenue exposure to the Europe, Middle East, and Africa (EMEA) region, expressed as a proportion of t… |
| `mdl177_2_sensitivityfactor400_hs` | MATRIX | Housing Starts Sensitivity |
| `mdl177_2_sensitivityfactor400_impvol` | MATRIX | Implied volatility estimate derived from options markets for the stock, reflecting expected future market volatility |
| `mdl177_2_sensitivityfactor400_imr` | MATRIX | Volatility Spread |
| `mdl177_2_sensitivityfactor400_inflation` | MATRIX | Inflation Sensitivity |
| `mdl177_2_sensitivityfactor400_ip` | MATRIX | Industrial Production Sensitivity |
| `mdl177_2_sensitivityfactor400_irttmsalesev` | MATRIX | Stock's trailing 12 month sales-to-enterprise (SEV) value less the average of the SEVs of all stocks in the same indu… |
| `mdl177_2_sensitivityfactor400_lasales` | MATRIX | Company’s sales revenue exposure to Latin America, expressed as a proportion of total sales |
| `mdl177_2_sensitivityfactor400_nasales` | MATRIX | Company’s sales revenue exposure to North America, expressed as a proportion of total sales |
| `mdl177_2_sensitivityfactor400_ney` | MATRIX | Normalized Earnings Yield : It is defined as the average of three normalized earnings calculated by ROE, NPM and EPS … |
| `mdl177_2_sensitivityfactor400_oilprice` | MATRIX | Oil Prices Sensitivity |
| `mdl177_2_sensitivityfactor400_otmptc` | MATRIX | Out-of-the-Money Put-to-Call Ratio |
| `mdl177_2_sensitivityfactor400_pbroeresidual` | MATRIX | Adjusted price-to-book signal incorporating firm growth, based on Wilcox and Philips (2005), representing the residua… |
| `mdl177_2_sensitivityfactor400_rev3my1std` | MATRIX | The change in a stock's current analysts mean earnings estimate for fiscal year 1 less that of three months ago, scal… |
| `mdl177_2_sensitivityfactor400_rev3my2std` | MATRIX | 3-M Revision in FY2 EPS Forecasts: Dispersion Relative : It is defined as the change in a stock's current analysts me… |
| `mdl177_2_sensitivityfactor400_ttmocfev` | MATRIX | Trailing 12-month operating cash flow per share divided by enterprise value per share; a valuation and quality metric |
| `mdl177_2_sensitivityfactor400_ttmopincev` | MATRIX | Trailing 12-month operating income (before depreciation/amortization) divided by enterprise value, where EV = Equity … |
| `mdl177_2_sensitivityfactor400_usd` | MATRIX | US Dollar Value Sensitivity |
| `mdl177_2_sensitivityfactor400_vix` | MATRIX | Sensitivity of the stock or factor to changes in the CBOE Volatility Index (VIX), a market volatility measure |
| `mdl177_2_sensitivityfactor400_y2aepsgpc` | MATRIX | Percentage change in consensus analyst EPS forecast from fiscal year 1 to fiscal year 2, normalized by year 1 forecas… |
| `mdl177_2_sensitivityfactor400_yieldsprd` | MATRIX | Sensitivity of the stock or factor to changes in the slope of the yield curve, measured as the difference between lon… |
| `mdl177_2_surpriseanalystmodel_qsa_composite` | MATRIX | Aggregate rank that combines several surprise-related analyst metrics into a single composite score |
| `mdl177_2_surpriseanalystmodel_qsa_efficiency` | MATRIX | Fundamentals Rank |
| `mdl177_2_surpriseanalystmodel_qsa_estexpect` | MATRIX | Rank indicating the trend or direction of analyst estimate changes for a company (estimate trend rank) |
| `mdl177_2_surpriseanalystmodel_qsa_percent` | MATRIX | Estimated probability (in percent) that a company will deliver an earnings or revenue surprise |
| `mdl177_2_surpriseanalystmodel_qsa_surpsn` | MATRIX | Rank of a company's earnings or revenue surprise, normalized relative to its sector (sector-neutral surprise analyst … |
| `mdl177_2_valueanalystmodel_qva_alertrank` | MATRIX | Alert Rank |
| `mdl177_2_valueanalystmodel_qva_capexdep` | MATRIX | Rank based on the ratio of capital expenditures to depreciation, showing investment intensity or asset renewal |
| `mdl177_2_valueanalystmodel_qva_cashflow` | MATRIX | Rank of free cash flow relative to market capitalization |
| `mdl177_2_valueanalystmodel_qva_chgacc` | MATRIX | Rank based on change in net operating working capital, reflecting shifts in operational liquidity or efficiency |
| `mdl177_2_valueanalystmodel_qva_chgato` | MATRIX | Rank based on change in asset turnover ratio (sales/assets), indicating improvements or declines in efficiency |
| `mdl177_2_valueanalystmodel_qva_chginv` | MATRIX | Rank based on change in inventory levels, typically signaling operational efficiency or demand shifts |
| `mdl177_2_valueanalystmodel_qva_composite` | MATRIX | Composite rank combining multiple value analyst measures for overall scoring |
| `mdl177_2_valueanalystmodel_qva_earnquality` | MATRIX | Rank based on the quality and sustainability of earnings |
| `mdl177_2_valueanalystmodel_qva_earnval` | MATRIX | Rank based on valuation of earnings, such as P/E or related metrics |
| `mdl177_2_valueanalystmodel_qva_epmodule` | MATRIX | Rank based on cyclicality of company earnings, measuring how variable or stable earnings are |
| `mdl177_2_valueanalystmodel_qva_finstmt` | MATRIX | Composite rank based on multiple financial statement metrics |
| `mdl177_2_valueanalystmodel_qva_incstmt` | MATRIX | Rank of operating income in relation to enterprise value based on income statement data |
| `mdl177_2_valueanalystmodel_qva_invsentiment` | MATRIX | Investor Sentiment Rank |
| `mdl177_2_valueanalystmodel_qva_mgtsignaling` | MATRIX | Management Signaling Rank |
| `mdl177_2_valueanalystmodel_qva_pegy` | MATRIX | Rank based on PEGY ratio (Price/Earnings to Growth & Yield), assessing valuation adjusted for earnings growth and div… |
| `mdl177_2_valueanalystmodel_qva_shortfall` | MATRIX | Rank based on earnings shortfall, flagging how much reported earnings fell below expectations |
| `mdl177_2_valueanalystmodel_qva_valuation` | MATRIX | Overall valuation rank, likely reflecting various value measures |
| `mdl177_2_valueanalystmodel_qva_yoychgdebt` | MATRIX | Rank based on year-over-year change in debt issuance, indicating leverage dynamics |
| `mdl177_2_valueanalystmodel_qva_yoychgshares` | MATRIX | Rank based on year-over-year change in shares outstanding, reflecting dilution or buybacks |
| `mdl177_2_valuemomemtummodel_earningsexpectationmodule` | MATRIX | A module tracking market expectations regarding the company's future earnings, often based on analyst forecasts or co… |
| `mdl177_2_valuemomemtummodel_earningspricelinkmodule` | MATRIX | Earnings-Price Link Module |
| `mdl177_2_valuemomemtummodel_earningsqualitymodule` | MATRIX | Earnings Quality Module |
| `mdl177_2_valuemomemtummodel_earningsvaluationmodule` | MATRIX | Earnings Valuation Module |
| `mdl177_2_valuemomemtummodel_financialstatementmodule` | MATRIX | Financial Statement Module |
| `mdl177_2_valuemomemtummodel_investorsentimentmodule` | MATRIX | Investor Sentiment Module |
| `mdl177_2_valuemomemtummodel_managementsignalingmodule` | MATRIX | Management Signaling Module |
| `mdl177_2_valuemomemtummodel_pricemomentummodule` | MATRIX | A factor signal module measuring price momentum, i.e., recent upward or downward movement in the company’s stock price |
| `mdl177_2_valuemomemtummodel_reportedearningsmomentummodule` | MATRIX | Reported Earnings Momentum Module |
| `mdl177_2_valuemomemtummodel_vm_compositesn` | MATRIX | Value Momentum Composite SN |
| `mdl177_2_valuemomemtummodel_vma_composite` | MATRIX | Value Momentum Composite |
| `mdl177_2_vma2_vma2` | MATRIX | Value Momentum Analyst II overall composite score combining Value and Momentum components |
| `mdl177_2_vma2_vma2_ma` | MATRIX | Momentum Analyst II composite score aggregating price momentum, earnings momentum, expectations, and fundamental grow… |
| `mdl177_2_vma2_vma2_ma_ee` | MATRIX | Earnings Expectations subscore within the Momentum Analyst II component, reflecting analyst forecasts and revisions m… |
| `mdl177_2_vma2_vma2_ma_em` | MATRIX | Reported Earnings Momentum subscore within the Momentum Analyst II component, tracking momentum in realized earnings … |
| `mdl177_2_vma2_vma2_ma_fg` | MATRIX | Fundamental Growth subscore within the Momentum Analyst II component, measuring growth in fundamentals such as sales,… |
| `mdl177_2_vma2_vma2_ma_pm` | MATRIX | Price Momentum; measures price trend or momentum for the stock over a selected period |
| `mdl177_2_vma2_vma2_va` | MATRIX | Value Analyst II composite score aggregating valuation-oriented subscores (Earnings Quality, Earnings Valuation, Fina… |
| `mdl177_2_vma2_vma2_va_eq` | MATRIX | Earnings Quality subscore within the Value Analyst II component, capturing the reliability and sustainability of earn… |
| `mdl177_2_vma2_vma2_va_ev` | MATRIX | Earnings Valuation subscore within the Value Analyst II component, focused on earnings-based valuation ratios (e.g., … |
| `mdl177_2_vma2_vma2_va_fs` | MATRIX | Financial Statement Valuation subscore within the Value Analyst II component, based on ratios from financial statemen… |
| `mdl177_2_vma2_vma2_va_is` | MATRIX | Investor Sentiment subscore within the Value Analyst II component, capturing valuation-related sentiment and investor… |
| `mdl177_5shortsentimentfactor_act_util` | MATRIX | Actual Utilization Rate: the real observed proportion of shares lent out (actively used for short selling) versus ava… |
| `mdl177_5shortsentimentfactor_benchmark_fee` | MATRIX | Implied loan rate or benchmark borrowing fee in the securities lending market |
| `mdl177_5shortsentimentfactor_conc_ratio` | MATRIX | Short Concentration Ratio: measures the degree to which short interest is concentrated in a limited number of stocks,… |
| `mdl177_5shortsentimentfactor_days_to_cover` | MATRIX | Days to Cover: number of days it would take for all current short positions to be repurchased (covered), given averag… |
| `mdl177_5shortsentimentfactor_dmd_conc` | MATRIX | Demand value concentration: degree to which borrowing demand is concentrated among a few borrowers |
| `mdl177_5shortsentimentfactor_dmd_supply` | MATRIX | Demand-to-supply ratio in securities lending, indicating borrow demand relative to lendable supply |
| `mdl177_5shortsentimentfactor_inv_conc` | MATRIX | Inventory value concentration: degree to which lending inventory is concentrated among a few lenders |
| `mdl177_5shortsentimentfactor_lend_supply` | MATRIX | Lending Supply: the total quantity of shares available for lending in the market, reflecting liquidity for short sellers |
| `mdl177_5shortsentimentfactor_onloan_conc` | MATRIX | On Loan Concentration: degree to which stocks on loan (for short selling) are concentrated in a few names, signifying… |
| `mdl177_5shortsentimentfactor_sht_int` | MATRIX | Short Interest: the total number of shares currently sold short (but not yet covered), a key indicator of bearish sen… |
| `mdl177_deepvaluefactor_acqmul_alt` | MATRIX | Acquisition Multiple: most recent invested capital divided by trailing 12-month EBITDA |
| `mdl177_deepvaluefactor_bp_alt` | MATRIX | Book-to-Price: most recent book value per share divided by trading price |
| `mdl177_deepvaluefactor_cashp_alt` | MATRIX | Cash-to-Price: most recently reported cash and equivalents per share divided by trading price |
| `mdl177_deepvaluefactor_cashsev_alt` | MATRIX | Cash-to-Enterprise Value: total cash and equivalents divided by enterprise value |
| `mdl177_deepvaluefactor_coreepsp_alt` | MATRIX | TTM Core Earnings-to-Price: trailing 12-month operational/core EPS excluding special items divided by trading price |
| `mdl177_deepvaluefactor_curep_alt` | MATRIX | Cash-to-Price |
| `mdl177_deepvaluefactor_divyield_alt` | MATRIX | TTM Dividend Yield: trailing 12-month dividends per share divided by trading price |
| `mdl177_deepvaluefactor_ebitdaev_alt` | MATRIX | TTM EBITDA-to-Enterprise Value: trailing 12-month EBITDA divided by enterprise value |
| `mdl177_deepvaluefactor_ebitdap_alt` | MATRIX | TTM EBITDA-to-Price: trailing 12-month EBITDA divided by trading price |
| `mdl177_deepvaluefactor_ebop_alt` | MATRIX | Edwards-Bell-Ohlson Value-to-Price: valuation from the EBO model divided by market price |
| `mdl177_deepvaluefactor_estep_alt` | MATRIX | TTM EBITDA-to-Price |
| `mdl177_deepvaluefactor_f12mepssev_alt` | MATRIX | Cash to Enterprise Value |
| `mdl177_deepvaluefactor_fcfp_alt` | MATRIX | Leading 12-Month Median Earnings Yield |
| `mdl177_deepvaluefactor_fwdep_alt` | MATRIX | Forward 12-month Earnings-to-Price: next four quarters’ mean consensus EPS divided by price |
| `mdl177_deepvaluefactor_indidivy_alt` | MATRIX | Indicated Dividend Yield: expected annualized dividend divided by price |
| `mdl177_deepvaluefactor_navp_alt` | MATRIX | Ratio of a company’s net asset value per share (tangible book value) to its current share price, indicating how much … |
| `mdl177_deepvaluefactor_nnastp_alt` | MATRIX | Net Current Assets-to-Price: current assets minus total liabilities per share divided by price |
| `mdl177_deepvaluefactor_past_alt` | MATRIX | Price-to-Total Assets: trading price divided by most recent total assets per share |
| `mdl177_deepvaluefactor_pdy_alt` | MATRIX | Indicated Dividend Yield |
| `mdl177_deepvaluefactor_proformaep_alt` | MATRIX | TTM Pro Forma Earnings-to-Price: trailing 12-month adjusted/pro forma earnings per share divided by trading price |
| `mdl177_deepvaluefactor_ttmcapexp_alt` | MATRIX | TTM Capital Expenditures-to-Price: trailing 12-month capital expenditures per share divided by trading price |
| `mdl177_deepvaluefactor_ttmcfp_alt` | MATRIX | TTM Cash Flow-to-Price: trailing 12-month net income plus depreciation per share divided by trading price |
| `mdl177_deepvaluefactor_ttmepa_alt` | MATRIX | An indicator that standardizes and compares relative share price between time periods and among companies. |
| `mdl177_deepvaluefactor_ttmepb_alt` | MATRIX | The company's performance in trailing 1-year before taking into account of non-recurring gain or loss.stock divided b… |
| `mdl177_deepvaluefactor_ttmfcfev_alt` | MATRIX | TTM Free Cash Flow-to-Enterprise Value: trailing 12-month free cash flow divided by enterprise value |
| `mdl177_deepvaluefactor_ttmfcfp_alt` | MATRIX | TTM Free Cash Flow-to-Price: trailing 12-month free cash flow per share divided by trading price |
| `mdl177_deepvaluefactor_ttmgfp_alt` | MATRIX | TTM Growth Flow-to-Price: trailing four quarters GAAP earnings plus R&D expenses per share divided by trading price |
| `mdl177_deepvaluefactor_ttmocfp_alt` | MATRIX | TTM Operating Cash Flow-to-Price: trailing 12-month operating cash flow per share divided by trading price |
| `mdl177_deepvaluefactor_ttmpiqp_alt` | MATRIX | TTM Pretax Income-to-Price: trailing 12-month pretax income per share divided by trading price |
| `mdl177_deepvaluefactor_ttmsaleev_alt` | MATRIX | TTM Sales-to-Enterprise Value: trailing 12-month sales divided by enterprise value |
| `mdl177_deepvaluefactor_ttmsp_alt` | MATRIX | TTM Sales-to-Price: trailing 12-month sales per share divided by trading price |
| `mdl177_devnorthamericashortsentimentfactor_act_util` | MATRIX | Actual utilization rate of lendable inventory currently on loan |
| `mdl177_devnorthamericashortsentimentfactor_benchmark_fee` | MATRIX | Implied loan rate or benchmark borrowing fee for the stock in the securities lending market |
| `mdl177_devnorthamericashortsentimentfactor_conc_ratio` | MATRIX | Short concentration ratio, measuring how concentrated short positions or utilization are |
| `mdl177_devnorthamericashortsentimentfactor_days_to_cover` | MATRIX | Number of days required to cover current short interest based on average daily trading volume |
| `mdl177_devnorthamericashortsentimentfactor_dmd_conc` | MATRIX | Demand value concentration, indicating how borrow demand value is concentrated |
| `mdl177_devnorthamericashortsentimentfactor_dmd_supply` | MATRIX | Demand-to-supply ratio of borrow demand relative to available lending supply |
| `mdl177_devnorthamericashortsentimentfactor_inv_conc` | MATRIX | Concentration of lending inventory value, indicating how supply is concentrated among a few holders |
| `mdl177_devnorthamericashortsentimentfactor_lend_supply` | MATRIX | Total quantity of shares available to lend (lendable inventory) |
| `mdl177_devnorthamericashortsentimentfactor_onloan_conc` | MATRIX | Concentration of shares currently on loan, indicating how on-loan positions are concentrated |
| `mdl177_devnorthamericashortsentimentfactor_sht_int` | MATRIX | Short interest, the number of shares sold short and outstanding |
| `mdl177_devnorthamericashortsentimentfactor_util` | MATRIX | Utilization: proportion of lendable shares currently on loan |
| `mdl177_earningmomentumfactor_chg6mltg` | MATRIX | Percent change in consensus long-term growth forecast over past 6 months |
| `mdl177_earningmomentumfactor_chg6mltg_alt` | MATRIX | Percent change in consensus long-term growth estimate over previous six months |
| `mdl177_earningmomentumfactor_cvfy1eps` | MATRIX | Forecast dispersion for FY1 EPS; standard deviation of analyst estimates for fiscal year 1 divided by mean |
| `mdl177_earningmomentumfactor_cvfy1eps_alt` | MATRIX | Dispersion (coefficient of variation) of FY1 earnings per share forecasts among analysts |
| `mdl177_earningmomentumfactor_cvfy2eps` | MATRIX | Forecast dispersion for FY2 EPS; standard deviation of analyst estimates for fiscal year 2 earnings per share divided… |
| `mdl177_earningmomentumfactor_cvfy2eps_alt` | MATRIX | Dispersion (coefficient of variation) of FY2 EPS forecasts among analysts |
| `mdl177_earningmomentumfactor_dypeg` | MATRIX | Reciprocal of dividend yield-adjusted PEG ratio; valuation metric adjusting PEG by dividend yield |
| `mdl177_earningmomentumfactor_dypeg_alt` | MATRIX | Reciprocal of dividend yield-adjusted PEG ratio |
| `mdl177_earningmomentumfactor_egp` | MATRIX | Inverse of PEG Ratio; next 4-quarter earnings estimate times long-term growth rate forecast, scaled by price |
| `mdl177_earningmomentumfactor_egp_alt` | MATRIX | Inverse PEG ratio; EPS-to-price divided by growth rate |
| `mdl177_earningmomentumfactor_epsrm` | MATRIX | Magnitude of street revisions; 3-month change in median FY1 consensus earnings estimate, scaled by price |
| `mdl177_earningmomentumfactor_epsrm_alt` | MATRIX | Magnitude of 3-month revision in median consensus FY1 earnings forecast |
| `mdl177_earningmomentumfactor_fcfroey1p` | MATRIX | Product of trailing 12-month free cash flow yield and forward return on equity; combines FCF per share and next 4-qua… |
| `mdl177_earningmomentumfactor_fcfroey1p_alt` | MATRIX | Product of trailing twelve-month free cash flow yield per share and forward-looking return on equity (ROE), measuring… |
| `mdl177_earningmomentumfactor_fqsurstd` | MATRIX | Most recent earnings surprise; standardized value quantifying how actual earnings differed from consensus in latest r… |
| `mdl177_earningmomentumfactor_fqsurstd_alt` | MATRIX | Most recent earnings surprise standardized (actual minus expected EPS) |
| `mdl177_earningmomentumfactor_fy1epsskew` | MATRIX | Skewness statistic of the distribution of leading 12-month consensus EPS estimates, indicating asymmetry in earnings … |
| `mdl177_earningmomentumfactor_fy1epsskew_alt` | MATRIX | Skewness of leading 12-month analyst EPS estimates |
| `mdl177_earningmomentumfactor_hlep` | MATRIX | Street revision confidence; sum of 3-month change in highest and lowest FY1 earnings estimates, scaled by price |
| `mdl177_earningmomentumfactor_hlep_alt` | MATRIX | Sum of 3-month change in highest and lowest FY1 EPS estimate, scaled by price |
| `mdl177_earningmomentumfactor_lagegp` | MATRIX | Lagged inverse of PEG Ratio; trailing 12-month EPS before extraordinary items times change in yearly trailing sales p… |
| `mdl177_earningmomentumfactor_lagegp_alt` | MATRIX | Inverse PEG ratio calculated using trailing 12-month EPS and sales growth rate, divided by price |
| `mdl177_earningmomentumfactor_ltg` | MATRIX | Long-term growth rate estimate; consensus annual growth forecast for operating earnings over the next full business c… |
| `mdl177_earningmomentumfactor_ltg_alt` | MATRIX | Consensus long-term earnings growth rate estimate |
| `mdl177_earningmomentumfactor_numrevq1` | MATRIX | Net number of analyst revisions for fiscal quarter 1; weighted average of forecast increases minus decreases for Q1 |
| `mdl177_earningmomentumfactor_numrevq1_alt` | MATRIX | Net number of analyst revisions for fiscal quarter one EPS estimates |
| `mdl177_earningmomentumfactor_numrevy1` | MATRIX | Net # of Revisions for Fiscal Year 1 |
| `mdl177_earningmomentumfactor_numrevy1_alt` | MATRIX | Net number of upward and downward revisions in FY1 EPS forecasts |
| `mdl177_earningmomentumfactor_perg` | MATRIX | Risk-adjusted PEG ratio, calculated as stock price divided by leading 12-month consensus earnings forecast, scaled by… |
| `mdl177_earningmomentumfactor_perg_alt` | MATRIX | Risk-adjusted PEG ratio accounting for price, forecast EPS, growth rate, and 36-month beta |
| `mdl177_earningmomentumfactor_q1aepsg` | MATRIX | Estimated EPS growth for the next fiscal quarter |
| `mdl177_earningmomentumfactor_q1aepsg_alt` | MATRIX | Estimated growth in earnings per share for the upcoming fiscal quarter |
| `mdl177_earningmomentumfactor_qepsferr` | MATRIX | Prior fiscal quarter forecast error; difference between actual and estimated EPS for previous quarter |
| `mdl177_earningmomentumfactor_qepsferr_alt` | MATRIX | Forecast error for prior fiscal quarter’s earnings (actual EPS minus forecasted EPS) |
| `mdl177_earningmomentumfactor_ratrev6m` | MATRIX | 6-month average change in street analyst recommendations |
| `mdl177_earningmomentumfactor_ratrev6m_alt` | MATRIX | Six-month average change in analyst recommendation ratings, indicating shifts in analyst sentiment toward the stock |
| `mdl177_earningmomentumfactor_rev1q1` | MATRIX | Revision in fiscal Q1 EPS forecasts; change in current Q1 forecast minus previous Q1 forecast |
| `mdl177_earningmomentumfactor_rev1q1_alt` | MATRIX | Change in EPS forecast for fiscal quarter one |
| `mdl177_earningmomentumfactor_rev3y1` | MATRIX | 3-month revision in FY1 EPS forecasts; change in current FY1 estimate minus 3 months ago, scaled |
| `mdl177_earningmomentumfactor_rev3y1_alt` | MATRIX | Change in FY1 EPS forecasts over the past three months |
| `mdl177_earningmomentumfactor_rev3y2` | MATRIX | 3-month revision in FY2 EPS forecasts; difference in FY2 estimates from three months ago to now, scaled |
| `mdl177_earningmomentumfactor_rev3y2_alt` | MATRIX | Change in FY2 EPS forecasts over the past three months |
| `mdl177_earningmomentumfactor_rev6` | MATRIX | Averaged Last 6-M EPS Revisions for FY1 |
| `mdl177_earningmomentumfactor_rev6_alt` | MATRIX | Average of analyst earnings per share (EPS) estimate revisions for fiscal year 1 (FY1) over the past 6 months |
| `mdl177_earningmomentumfactor_salesurp` | MATRIX | Sales surprise; positive or negative deviation in actual sales versus consensus forecasts |
| `mdl177_earningmomentumfactor_salesurp_alt` | MATRIX | Magnitude of actual sales exceeding or missing consensus forecast |
| `mdl177_earningmomentumfactor_stdevfy1epsp` | MATRIX | Standard deviation of FY1 EPS estimates-to-price; dispersion of FY1 analyst EPS forecasts scaled by stock price |
| `mdl177_earningmomentumfactor_stdevfy1epsp_alt` | MATRIX | Standard deviation of FY1 EPS estimates expressed relative to price |
| `mdl177_earningmomentumfactor_stdevfy2epsp` | MATRIX | Standard deviation of FY2 EPS estimates-to-price; dispersion of FY2 analyst EPS forecasts scaled by stock price |
| `mdl177_earningmomentumfactor_stdevfy2epsp_alt` | MATRIX | Standard deviation of FY2 EPS estimates expressed relative to price |
| `mdl177_earningmomentumfactor_stockrating` | MATRIX | Consensus analyst recommendation for the stock |
| `mdl177_earningmomentumfactor_stockrating_alt` | MATRIX | Consensus recommendation for the stock (e.g., buy/hold/sell) |
| `mdl177_earningmomentumfactor_sucf` | MATRIX | Standardized measure of unexpected cash flow, quantifying the deviation of reported cash flow from expected values, a… |
| `mdl177_earningmomentumfactor_sucf_alt` | MATRIX | Standardized Unexpected Cash Flow |
| `mdl177_earningmomentumfactor_sue` | MATRIX | Standardized unexpected earnings; deviation of reported earnings from consensus, usually normalized |
| `mdl177_earningmomentumfactor_sue_alt` | MATRIX | Standardized measure of unexpected earnings, typically deviation from analyst expectations |
| `mdl177_earningmomentumfactor_surp` | MATRIX | Real earnings surprise; difference between actual and forecast EPS prior to announcement, scaled by price at quarter end |
| `mdl177_earningmomentumfactor_surp_alt` | MATRIX | Difference between actual EPS and consensus forecast, scaled by quarter-end price |
| `mdl177_earningmomentumfactor_y1aepsg` | MATRIX | 1-year ahead EPS growth; projected increase in earnings per share for next fiscal year |
| `mdl177_earningmomentumfactor_y1aepsg_alt` | MATRIX | Estimated earnings per share growth for fiscal year one compared to prior year |
| `mdl177_earningmomentumfactor_y2aepsg` | MATRIX | 2-year ahead EPS growth; projected increase in earnings per share for fiscal year 2 |
| `mdl177_earningmomentumfactor_y2aepsg_alt` | MATRIX | Estimated earnings per share growth for fiscal year two compared to year one |
| `mdl177_earningmomentumfactor_y2repsg` | MATRIX | 2-year projected EPS growth; forecasted earnings per share growth over 2 years, likely scaled by price |
| `mdl177_earningmomentumfactor_y2repsg_alt` | MATRIX | Forecasted 2-year ahead EPS growth |
| `mdl177_earningmomentumfactor_y3sur` | MATRIX | Volatility-adj 3-yr Projected EPS Growth |
| `mdl177_earningmomentumfactor_y3sur_alt` | MATRIX | Volatility-adjusted projected earnings per share growth over the next three years |
| `mdl177_earningsmomemtummodel_chgsup_alt` | MATRIX | Change in EPS Surprise |
| `mdl177_earningsmomemtummodel_emm_composite_alt` | MATRIX | Composite score measuring earnings momentum using multiple signals within the model |
| `mdl177_earningsmomemtummodel_fc_cvfy2eps_alt` | MATRIX | Dispersion of FY2 EPS forecasts: standard deviation of analyst estimates divided by mean consensus |
| `mdl177_earningsmomemtummodel_fc_egp_alt` | MATRIX | Next 1-year average earnings estimate scaled by expected long-term growth rate and stock price (inverse PEG-type meas… |
| `mdl177_earningsmomemtummodel_fc_fcfroey1p_alt` | MATRIX | Product of trailing 12-month free cash flow yield and forward return on equity, scaled by stock price |
| `mdl177_earningsmomemtummodel_fc_fqsurstd_alt` | MATRIX | Most recent quarterly earnings surprise (actual EPS minus consensus) standardized by the standard deviation of analys… |
| `mdl177_earningsmomemtummodel_fc_numrevy1_alt` | MATRIX | Weighted average net number of FY1 analyst forecast revisions in a month (raises minus lowers) divided by total forec… |
| `mdl177_earningsmomemtummodel_fc_rev3y2_alt` | MATRIX | 3-month change in FY2 EPS forecasts (FY2 estimate revision over 3 months) |
| `mdl177_earningsmomemtummodel_fc_y2repsg_alt` | MATRIX | Difference between FY2 consensus EPS forecast and last fiscal year's reported EPS, divided by month-end price (2-year… |
| `mdl177_earningsmomemtummodel_ltg_alt` | MATRIX | Consensus long-term operating earnings growth rate forecast over the next business cycle |
| `mdl177_earningsqualityfactor_chgsgasale` | MATRIX | Difference between yearly change in quarterly SG&A expenses and yearly change in quarterly sales |
| `mdl177_earningsqualityfactor_chgsgasale_alt` | MATRIX | Change in quarterly SG&A expenses versus sales; difference in SG&A-to-sales ratios |
| `mdl177_earningsqualityfactor_chgshare` | MATRIX | Percent change in company's number of shares outstanding over one year |
| `mdl177_earningsqualityfactor_chgshare_alt` | MATRIX | Change in shares outstanding |
| `mdl177_earningsqualityfactor_cogsinvt` | MATRIX | Absolute difference between yearly percent change in cost of goods sold and percent change in inventory level |
| `mdl177_earningsqualityfactor_cogsinvt_alt` | MATRIX | Change in TTM cost of goods sold versus inventory level; absolute difference between yearly percent changes |
| `mdl177_earningsqualityfactor_dpcapex` | MATRIX | Absolute difference between yearly percent change in depreciation expense and in capital expenditure (trailing 12 mon… |
| `mdl177_earningsqualityfactor_dpcapex_alt` | MATRIX | Change in TTM depreciation versus capital expenditures; absolute difference between percent changes |
| `mdl177_earningsqualityfactor_epschgetr` | MATRIX | EPS adjusted by change in trailing 12-month effective tax rate (pre-tax income per share times tax rate change over p… |
| `mdl177_earningsqualityfactor_epschgetr_alt` | MATRIX | EPS from change in effective tax rate; EPS times the change in ETR over the last four quarters |
| `mdl177_earningsqualityfactor_erc` | MATRIX | Earnings Response Coefficient; the sensitivity of a stock's return to its earnings announcement |
| `mdl177_earningsqualityfactor_erc_alt` | MATRIX | Earnings Response Coefficient, slope between market-adjusted returns and quarterly earnings changes |
| `mdl177_earningsqualityfactor_indrelrecd_` | MATRIX | Industry-adjusted doubtful account receivables; a stock's asset-adjusted annual doubtful receivables minus the indust… |
| `mdl177_earningsqualityfactor_indrelrecd__alt` | MATRIX | Industry-adjusted doubtful accounts receivable, asset-adjusted annual doubtful receivables minus the industry mean |
| `mdl177_earningsqualityfactor_ncfeps` | MATRIX | Absolute difference between yearly percent change in operating cash flow per share and yearly percent change in dilut… |
| `mdl177_earningsqualityfactor_ncfeps_alt` | MATRIX | Change in trailing twelve months earnings per share versus operating cash flows |
| `mdl177_earningsqualityfactor_opincltd` | MATRIX | Difference between yearly percent change in operating income and yearly percent change in long-term debt |
| `mdl177_earningsqualityfactor_opincltd_alt` | MATRIX | Change in trailing twelve months operating income versus long-term debt |
| `mdl177_earningsqualityfactor_saleeps` | MATRIX | Absolute difference between yearly percent change in sales per share and yearly percent change in diluted EPS |
| `mdl177_earningsqualityfactor_saleeps_alt` | MATRIX | Change in trailing twelve months sales versus earnings per share |
| `mdl177_earningsqualityfactor_salegpm` | MATRIX | Difference between yearly change in quarterly sales and yearly change in gross profit margin |
| `mdl177_earningsqualityfactor_salegpm_alt` | MATRIX | Change in quarterly sales versus gross margin |
| `mdl177_earningsqualityfactor_salerec` | MATRIX | Difference between yearly percent change in trailing 12-month sales and percent change in accounts receivable |
| `mdl177_earningsqualityfactor_salerec_alt` | MATRIX | Change in trailing twelve months sales versus accounts receivable |
| `mdl177_earningsqualityfactor_ttmaccu` | MATRIX | Accounting accruals; trailing 12-month net income minus trailing 12-month operating cash flow, scaled by beginning to… |
| `mdl177_earningsqualityfactor_ttmaccu_alt` | MATRIX | Trailing twelve months accruals (earnings quality measure based on accruals) |
| `mdl177_earningsqualityfactor_uaccl` | MATRIX | Unexpected change in accrued liabilities, difference between current and expected accrued liabilities scaled by total… |
| `mdl177_earningsqualityfactor_uaccl_alt` | MATRIX | Unexpected change in accrued liabilities, difference scaled by total assets |
| `mdl177_earningsqualityfactor_uap` | MATRIX | Unexpected change in accounts payable, difference between current and expected accounts payable scaled by total assets |
| `mdl177_earningsqualityfactor_uap_alt` | MATRIX | Unexpected change in accounts payable |
| `mdl177_earningsqualityfactor_uar` | MATRIX | Unexpected change in accounts receivable, the difference between current and expected accounts receivable scaled by t… |
| `mdl177_earningsqualityfactor_uar_alt` | MATRIX | Unexpected change in accounts receivable, difference from expected level scaled by total assets |
| `mdl177_earningsqualityfactor_udep` | MATRIX | Unexpected change in depreciation expense, difference between actual and expected depreciation scaled by total assets |
| `mdl177_earningsqualityfactor_udep_alt` | MATRIX | Unexpected change in depreciation |
| `mdl177_earningsqualityfactor_uinv` | MATRIX | Unexpected change in inventory, difference between actual and expected inventory level |
| `mdl177_earningsqualityfactor_uinv_alt` | MATRIX | Unexpected change in inventory level |
| `mdl177_earningsqualityfactor_wcacc` | MATRIX | Working capital accruals; sum of changes in receivables, inventory, payables, taxes, assets/liabilities |
| `mdl177_earningsqualityfactor_wcacc_alt` | MATRIX | Working capital accruals, sum of changes in receivables, inventory, payables, taxes, and other current assets/liabili… |
| `mdl177_earningsqualityfactor_yoychgaa` | MATRIX | Year-over-year change in accruals to assets; difference in scaled accruals this year vs. one year ago |
| `mdl177_earningsqualityfactor_yoychgaa_alt` | MATRIX | Year-over-year change in accruals-adjusted assets |
| `mdl177_emmcomposite_emm_composite` | MATRIX | Composite score measuring the earnings momentum of a US-listed stock, summarizing factors such as recent earnings gro… |
| `mdl177_fa_acqmul` | MATRIX | Acquisition Multiple: recent quarterly invested capital divided by trailing 12-month EBITDA |
| `mdl177_fa_actrtn1m` | MATRIX | 1-Month Active Return |
| `mdl177_fa_altmanz` | MATRIX | Altman Z Score: score indicating likelihood of bankruptcy |
| `mdl177_fa_app` | MATRIX | Average Payable Period: Average time (in days) taken to pay suppliers, calculated as trailing 12-month accounts payab… |
| `mdl177_fa_aspanratio` | MATRIX | Attention Span Ratio |
| `mdl177_fa_astcomp` | MATRIX | Total current assets divided by total assets from the most recent quarter |
| `mdl177_fa_astto` | MATRIX | Assets turnover ratio: trailing twelve month sales divided by average assets |
| `mdl177_fa_atmcallvol` | MATRIX | Implied volatility of at-the-money call options |
| `mdl177_fa_bp` | MATRIX | Book-to-Market: Most recent book value per share divided by month-end trading price |
| `mdl177_fa_capacq` | MATRIX | Capital Acquisition Ratio: Trailing 12-month operating cash flow minus trailing 12-month cash dividends, divided by t… |
| `mdl177_fa_cashsev` | MATRIX | Total cash & equivalents divided by enterprise value |
| `mdl177_fa_chg3yfcfp` | MATRIX | Change in trailing twelve month free cash flow per share over three years, divided by price |
| `mdl177_fa_chgis` | MATRIX | One-year change in quarterly inventory as a percentage of sales |
| `mdl177_fa_chgnoa` | MATRIX | Change in Net Operating Assets |
| `mdl177_fa_chgnpm` | MATRIX | One-year change in net profit margin (most recent quarterly NPM minus four quarters ago) |
| `mdl177_fa_chgocfp` | MATRIX | One-year change in price-adjusted trailing twelve month operating cash flow per share |
| `mdl177_fa_chgollev` | MATRIX | Change in Operating Liability Leverage: Absolute change in the OLLEV metric over the specified period |
| `mdl177_fa_chgsgasale` | MATRIX | Change in SG&A Expenses versus Sales: difference between annualized quarterly SG&A change and sales change |
| `mdl177_fa_curratio` | MATRIX | Ratio of current assets to current liabilities from most recent quarter |
| `mdl177_fa_cv4qcf3y` | MATRIX | Coefficient of Variation over 3 Years for Cash Flow: Stability of TTM cash flow over three years |
| `mdl177_fa_divcov` | MATRIX | Dividend coverage ratio (earnings or cash flow available to cover dividend payments) |
| `mdl177_fa_ebitdaev` | MATRIX | TTM EBITDA-to-Enterprise Value: Trailing twelve-month EBITDA divided by enterprise value |
| `mdl177_fa_equityto` | MATRIX | Equity Turnover Ratio |
| `mdl177_fa_fc_egp` | MATRIX | Inverse PEG ratio, calculated using next 4 quarters' earnings estimate times long-term growth rate, divided by price |
| `mdl177_fa_fc_f12mepssev` | MATRIX | Forward 12-Month EPS-to-Enterprise Value: Consensus forward 12-month EPS forecast divided by market value of equity p… |
| `mdl177_fa_fc_fcfp` | MATRIX | Forward Free Cash Flow-to-Price: Next 4-quarter mean consensus earnings estimate plus trailing 12-month depreciation … |
| `mdl177_fa_fc_fwdep` | MATRIX | Leading 12-Month Mean Earnings Yield: Next 4-quarter mean consensus earnings estimate divided by trading price |
| `mdl177_fa_fc_pdy` | MATRIX | Predicted Dividend Yield: Assumed payout ratio (function of last year's payout and long-term growth rate) multiplied … |
| `mdl177_fa_fc_y2aepsg` | MATRIX | Two-Year Ahead EPS Growth: Current year 2 earnings forecast minus year 1 forecast, divided by trading price |
| `mdl177_fa_fc_y2repsg` | MATRIX | Two-Year Projected EPS Growth: Year 2 forecast minus recent actual EPS, scaled by trading price |
| `mdl177_fa_fcfroi` | MATRIX | Free Cash Flow Return on Invested Capital: Trailing 12-month free cash flow divided by average invested capital over … |
| `mdl177_fa_fixastto` | MATRIX | Fixed Assets Turnover Ratio |
| `mdl177_fa_flowratio` | MATRIX | (Current assets minus cash and equivalents) divided by (current liabilities minus short-term debt) |
| `mdl177_fa_monchgsip` | MATRIX | Monthly change in the ratio of shares sold short over shares outstanding |
| `mdl177_fa_netcashp` | MATRIX | Net Cash to Equity: Recent cash and equivalents minus long-term and short-term debt, divided by market value |
| `mdl177_fa_nlvolcap` | MATRIX | Average Monthly Trading Volume-to-Market Cap: Log of trailing 12-month average monthly volume divided by trailing 12-… |
| `mdl177_fa_nnastp` | MATRIX | Ratio of net current assets per share (current assets minus total liabilities) to stock price |
| `mdl177_fa_ocfast` | MATRIX | Operating Cash Flow to Assets: Ratio of operating cash flow over the period to total assets; measures how effectively… |
| `mdl177_fa_ocfratio` | MATRIX | Operating Cash Flow Ratio: cash flow from operations divided by current liabilities |
| `mdl177_fa_ollev` | MATRIX | Operating Liability Leverage: 1 minus the ratio of (short-term debt + long-term debt + common equity + preferred equi… |
| `mdl177_fa_past` | MATRIX | Price-to-Total Assets: Month-end trading price divided by most recent total assets per share |
| `mdl177_fa_qr` | MATRIX | Quick ratio (recent current assets minus inventories, divided by current liabilities) |
| `mdl177_fa_ratrev6m` | MATRIX | Six-month average change in analyst recommendation (Street Rating Revision) |
| `mdl177_fa_rel5ycfp` | MATRIX | 5-year Relative Trailing Twelve Month Cash Flow-to-Price: TTM cash flow to price ratio versus industry or market over… |
| `mdl177_fa_rel5ycoreepsp` | MATRIX | Five-year average relative trailing twelve month core earnings per share to price, compared to industry or benchmark |
| `mdl177_fa_rel5yebitdap` | MATRIX | Five-year average relative ratio of trailing twelve month EBITDA to price, compared to industry or benchmark |
| `mdl177_fa_rel5yfcfp` | MATRIX | Five-year average relative trailing twelve month free cash flow to price, compared to industry or benchmark |
| `mdl177_fa_rel5yocfp` | MATRIX | 5-year Relative Trailing Twelve Month Operating Cash Flow-to-Price: TTM operating cash flow to price comparison versu… |
| `mdl177_fa_rerror60m` | MATRIX | Standard error of regression for past 60 monthly returns against the S&P 500 (CAPM); measures model fit error |
| `mdl177_fa_rsqr4qsales3y` | MATRIX | R-squared measure of three-year trailing twelve month sales per share trend line (goodness of fit to linear sales trend) |
| `mdl177_fa_saleicap` | MATRIX | Trailing 12-Month Sales to Invested Capital: Sales over the past 12 months divided by invested capital |
| `mdl177_fa_totalcov` | MATRIX | Total Coverage: Ratio that measures how well a company’s cash flows, interest paid, and taxes can cover its interest … |
| `mdl177_fa_ttmfcfev` | MATRIX | TTM Free Cash Flow-to-Enterprise Value: Trailing twelve-month free cash flow divided by enterprise value |
| `mdl177_fa_ttmfcfp` | MATRIX | Trailing Twelve-Month Free Cash Flow-to-Price: TTM free cash flow per share divided by month-end trading price |
| `mdl177_fa_voldiff_pc` | MATRIX | Difference between implied volatility of ATM put options and ATM call options |
| `mdl177_fa_wcacc` | MATRIX | Working capital accruals: increases in receivables/inventories minus increases in payables/taxes |
| `mdl177_fa_yoychggpm` | MATRIX | Yearly Change in Gross Profit Margin: Change in the company's gross profit margin relative to the prior year |
| `mdl177_fangma_dvf_usa_fangma_dvf22` | MATRIX | Deep value factors 22 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_dvm_usa_fangma_dvm1` | MATRIX | Deep value model 1 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_dvm_usa_fangma_dvm2` | MATRIX | Deep value model 2 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_dvm_usa_fangma_dvm3` | MATRIX | Deep value model 3 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_dvm_usa_fangma_dvm4` | MATRIX | Deep value model 4 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_dvm_usa_fangma_dvm5` | MATRIX | Deep value model 5 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_emf_usa_fangma_emf15` | MATRIX | Earnings momentum factors 15 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_emf_usa_fangma_emf20` | MATRIX | Earnings momentum factors 20 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_emf_usa_fangma_emf25` | MATRIX | Earnings momentum factors 25 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_emf_usa_fangma_emf28` | MATRIX | Earnings momentum factors 28 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_emf_usa_fangma_emf3` | MATRIX | Earnings momentum factors 3 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_emf_usa_fangma_emf30` | MATRIX | Earnings momentum factors 30 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_emf_usa_fangma_emf4` | MATRIX | Earnings momentum factors 4 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_emf_usa_fangma_emf6` | MATRIX | Core factors of big IT companies. |
| `mdl177_fangma_gpam_usa_fangma_gpam1` | MATRIX | A metric evaluating short-term growth or profitability performance for a selected group of large technology companies. |
| `mdl177_fangma_gpam_usa_fangma_gpam10` | MATRIX | A metric measuring long-term growth or profitability performance for a set of leading technology companies. |
| `mdl177_fangma_gpam_usa_fangma_gpam11` | MATRIX | A composite or specialized metric summarizing growth or profitability characteristics for a group of prominent techno… |
| `mdl177_fangma_gpam_usa_fangma_gpam5` | MATRIX | A metric assessing medium-term growth or profitability trends for a group of major technology firms. |
| `mdl177_fangma_mam_usa_fangma_mam11` | MATRIX | Momentum analyst model 11 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_mam_usa_fangma_mam16` | MATRIX | Momentum analyst model 16 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_mam_usa_fangma_mam2` | MATRIX | Momentum analyst model 2 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_mam_usa_fangma_mam3` | MATRIX | Momentum analyst model 3 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_mam_usa_fangma_mam4` | MATRIX | Momentum analyst model 5 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_mam_usa_fangma_mam5` | MATRIX | Momentum analyst model 5 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_mam_usa_fangma_mam6` | MATRIX | Momentum analyst model 6 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_mam_usa_fangma_mam7` | MATRIX | Momentum analyst model 7 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_rvm_usa_fangma_rvm1` | MATRIX | Relative value model 1 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_rvm_usa_fangma_rvm4` | MATRIX | Relative value model 4 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_rvm_usa_fangma_rvm6` | MATRIX | Relative value model 6 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_fangma_vmm_usa_fangma_vmm11` | MATRIX | Value momentum 11 for FANGMA (Facebook, Apple, Netflix, Google, Mircosoft, Amazon) |
| `mdl177_garpanalystmodel_qgp_alert` | MATRIX | Alert Rank |
| `mdl177_garpanalystmodel_qgp_avgrating` | MATRIX | Average of analyst ratings for the stock, reflecting overall analyst sentiment or recommendation |
| `mdl177_garpanalystmodel_qgp_capeff` | MATRIX | Measurement of capital utilization efficiency, showing how effectively the company uses its capital for growth/profit |
| `mdl177_garpanalystmodel_qgp_chgvaluation` | MATRIX | Change in valuation metrics over the last 3 months, reflecting how market valuation of the stock has evolved recently |
| `mdl177_garpanalystmodel_qgp_composite` | MATRIX | Combined score based on GARP-specific metrics, summarizing the overall attractiveness of a stock according to Growth … |
| `mdl177_garpanalystmodel_qgp_growthval` | MATRIX | Valuation adjusted for growth metrics, assessing valuation in the context of company growth prospects |
| `mdl177_garpanalystmodel_qgp_relgrowth` | MATRIX | Rank comparing company's growth metrics against its industry peers, showing relative growth strength |
| `mdl177_garpanalystmodel_qgp_relpegy` | MATRIX | Rolling rank of PEGY ratios over a period, highlighting attractiveness based on earnings growth, price, and yield |
| `mdl177_garpanalystmodel_qgp_roefcf` | MATRIX | Combined measure of profitability (ROE) and cash flow (FCF), ranking stocks by both financial quality factors |
| `mdl177_garpanalystmodel_qgp_valuation` | MATRIX | Rank showing the stock's valuation compared to peers, based on key valuation metrics |
| `mdl177_garpanalystmodel_qgp_vfpriceratio` | MATRIX | Value to Price Rank |
| `mdl177_garpanalystmodel_qgp_wratingchg` | MATRIX | Weighted change in analyst ratings over past 6 months, reflecting recent evolution in analyst sentiment |
| `mdl177_growthanalystmodel_qga_composite_alt` | MATRIX | A combined or aggregated signal summarizing multiple growth-related measurements from the Growth Analyst Model |
| `mdl177_growthanalystmodel_qga_epscapex_alt` | MATRIX | The relationship between EPS growth and capital expenditures, assessing how effectively capital investments drive ear… |
| `mdl177_growthanalystmodel_qga_epstrend_alt` | MATRIX | A measure indicating the directional trend and consistency of earnings per share over time |
| `mdl177_growthanalystmodel_qga_fcfroe_alt` | MATRIX | Return on equity calculated using free cash flow instead of net income, measuring efficiency of generating free cash … |
| `mdl177_growthanalystmodel_qga_iarsales_alt` | MATRIX | Inv Acc Rec to Sales Link |
| `mdl177_growthanalystmodel_qga_ltepssurprise_alt` | MATRIX | Long Term EPS Surprise |
| `mdl177_growthanalystmodel_qga_niroe_alt` | MATRIX | Return on equity calculated using net income, measuring profitability relative to shareholder equity |
| `mdl177_growthanalystmodel_qga_opmarginsales_alt` | MATRIX | The relationship between operating margin and sales, indicating operational profitability as a proportion of sales |
| `mdl177_historicalgrowthfactor_cg3ysales` | MATRIX | Geometric compound annual growth rate of trailing twelve-month sales per share over last 12 quarters |
| `mdl177_historicalgrowthfactor_cg3ysales_alt` | MATRIX | Geometric growth rate of trailing 12-month sales per share over the past 12 quarters |
| `mdl177_historicalgrowthfactor_chg3ycfast` | MATRIX | Three-year change in assets-adjusted trailing twelve-month operating cash flow (recent minus 12 quarters ago, scaled … |
| `mdl177_historicalgrowthfactor_chg3ycfast_alt` | MATRIX | Three-year change in operating cash flow adjusted by average total assets (most recent trailing 12-month minus traili… |
| `mdl177_historicalgrowthfactor_chg3ycfp` | MATRIX | Difference between trailing 12-month cash flow per share and the same metric 12 quarters ago, divided by trading price |
| `mdl177_historicalgrowthfactor_chg3ycfp_alt` | MATRIX | Difference between trailing 12-month cash flow per share now and 12 quarters ago, divided by trading price |
| `mdl177_historicalgrowthfactor_chg3yepsast` | MATRIX | Difference between trailing 12-month EPS (before extra items) and that 12 quarters ago, scaled by average total asset… |
| `mdl177_historicalgrowthfactor_chg3yepsast_alt` | MATRIX | Difference in trailing 12-month earnings per share before extra items versus 12 quarters ago, adjusted by average tot… |
| `mdl177_historicalgrowthfactor_chg3yepsp` | MATRIX | Difference between trailing 12-month EPS and that 12 quarters ago, divided by month-end trading price |
| `mdl177_historicalgrowthfactor_chg3yepsp_alt` | MATRIX | Difference between trailing 12-month earnings per share now and 12 quarters ago, divided by month-end trading price |
| `mdl177_historicalgrowthfactor_chg3yfcfast` | MATRIX | Three-year change in assets-adjusted trailing twelve-month free cash flow (recent minus 12 quarters ago, divided by a… |
| `mdl177_historicalgrowthfactor_chg3yfcfast_alt` | MATRIX | Three-year change in free cash flow adjusted by average total assets (most recent trailing 12-month FCF minus trailin… |
| `mdl177_historicalgrowthfactor_chg3yfcfp` | MATRIX | Difference in trailing twelve-month free cash flow per share over 3 years, divided by month-end share price |
| `mdl177_historicalgrowthfactor_chg3yfcfp_alt` | MATRIX | Difference between trailing 12-month free cash flow per share now and 12 quarters ago, divided by month-end trading p… |
| `mdl177_historicalgrowthfactor_chg3yocfast` | MATRIX | Three-year change in assets-adjusted trailing twelve-month operating cash flow (OCF minus value 12 quarters ago, scal… |
| `mdl177_historicalgrowthfactor_chg3yocfast_alt` | MATRIX | Difference in trailing 12-month operating cash flow per share versus 12 quarters ago, adjusted by average total assets |
| `mdl177_historicalgrowthfactor_chg3yocfp` | MATRIX | Difference in trailing twelve-month operating cash flow per share over last 3 years, divided by share price |
| `mdl177_historicalgrowthfactor_chg3yocfp_alt` | MATRIX | Difference between trailing 12-month operating cash flow per share now and 12 quarters ago, divided by trading price |
| `mdl177_historicalgrowthfactor_chgars` | MATRIX | Change in accounts receivable to sales ratio over 1 year (latest vs. 4 quarters ago) |
| `mdl177_historicalgrowthfactor_chgars_alt` | MATRIX | Change in accounts receivable as a percentage of trailing 12-month sales compared to 4 quarters ago |
| `mdl177_historicalgrowthfactor_chgcf` | MATRIX | Difference between trailing 12-month cash flow and comparable figure from 4 quarters ago, scaled by average total assets |
| `mdl177_historicalgrowthfactor_chgcf_alt` | MATRIX | Change in trailing 12-month cash flow over last year, scaled by average total assets |
| `mdl177_historicalgrowthfactor_chgcfp` | MATRIX | Difference between trailing 12-month cash flow per share and that 4 quarters ago, divided by trading price |
| `mdl177_historicalgrowthfactor_chgcfp_alt` | MATRIX | Difference between trailing 12-month cash flow per share and 12 quarters ago, divided by trading price |
| `mdl177_historicalgrowthfactor_chgeps` | MATRIX | 1-year change in assets-adjusted trailing twelve-month earnings per share before extra items (recent minus 4 quarters… |
| `mdl177_historicalgrowthfactor_chgeps_alt` | MATRIX | Difference in trailing 12-month earnings per share before extra items versus 4 quarters ago, adjusted by average tota… |
| `mdl177_historicalgrowthfactor_chgepsp` | MATRIX | Difference between most recent trailing 12-month EPS and that 4 quarters ago, divided by month-end trading price |
| `mdl177_historicalgrowthfactor_chgepsp_alt` | MATRIX | Difference between most recent trailing 12-month earnings per share and 4 quarters ago, divided by month-end trading … |
| `mdl177_historicalgrowthfactor_chgfcf` | MATRIX | 1-year change in assets-adjusted trailing twelve-month free cash flow (recent minus 4 quarters ago, scaled by average… |
| `mdl177_historicalgrowthfactor_chgfcf_alt` | MATRIX | Change in trailing 12-month free cash flow over last year, divided by average total assets |
| `mdl177_historicalgrowthfactor_chgfcfp` | MATRIX | Difference in trailing twelve-month free cash flow per share over last year, divided by share price |
| `mdl177_historicalgrowthfactor_chgfcfp_alt` | MATRIX | Difference between trailing 12-month free cash flow per share and 4 quarters ago, divided by trading price |
| `mdl177_historicalgrowthfactor_chgis` | MATRIX | Difference between most recent inventory as a percentage of trailing 12-month sales and the same ratio 4 quarters ago |
| `mdl177_historicalgrowthfactor_chgis_alt` | MATRIX | Change in inventory as a percentage of trailing 12-month sales compared to 4 quarters ago |
| `mdl177_historicalgrowthfactor_chgnpm` | MATRIX | Difference between most recent quarterly net profit margin and that 4 quarters ago (1-year change in net profit margin) |
| `mdl177_historicalgrowthfactor_chgnpm_alt` | MATRIX | Most recent quarterly net profit margin minus net profit margin from four quarters ago |
| `mdl177_historicalgrowthfactor_chgocf` | MATRIX | 1-year change in assets-adjusted trailing twelve-month operating cash flow (recent minus value 4 quarters ago, divide… |
| `mdl177_historicalgrowthfactor_chgocf_alt` | MATRIX | Change in trailing 12-month operating cash flow over last year, divided by average total assets |
| `mdl177_historicalgrowthfactor_chgocfp` | MATRIX | Difference between most recent trailing 12-month operating cash flow per share and that 4 quarters ago, divided by tr… |
| `mdl177_historicalgrowthfactor_chgocfp_alt` | MATRIX | Difference between most recent trailing 12-month operating cash flow per share and 4 quarters ago, divided by trading… |
| `mdl177_historicalgrowthfactor_chgopm` | MATRIX | Difference between most recent quarterly operating profit margin and that 4 quarters ago (1-year change in operating … |
| `mdl177_historicalgrowthfactor_chgopm_alt` | MATRIX | Change in quarterly operating profit margin (income from operations divided by total sales) compared to 4 quarters ago |
| `mdl177_historicalgrowthfactor_cv4qcf3y` | MATRIX | Coefficient of variation (stability) of trailing 12-month cash flow per share over the past 3 years |
| `mdl177_historicalgrowthfactor_cv4qcf3y_alt` | MATRIX | Coefficient of variation over 3 years for trailing 12-month cash flow |
| `mdl177_historicalgrowthfactor_cv4qeps3y` | MATRIX | Coefficient of variation (stability) of trailing 12-month earnings per share over the past 3 years |
| `mdl177_historicalgrowthfactor_cv4qeps3y_alt` | MATRIX | Coefficient of variation over 3 years for trailing 12-month earnings per share |
| `mdl177_historicalgrowthfactor_cv4qfcf3y` | MATRIX | Coefficient of variation (stability) of trailing 12-month free cash flow per share over the past 3 years |
| `mdl177_historicalgrowthfactor_cv4qfcf3y_alt` | MATRIX | Coefficient of variation over 3 years for trailing 12-month free cash flow |
| `mdl177_historicalgrowthfactor_cv4qocf3y` | MATRIX | Coefficient of variation (stability) of trailing 12-month operating cash flow per share over the past 3 years |
| `mdl177_historicalgrowthfactor_cv4qocf3y_alt` | MATRIX | Coefficient of variation over 3 years for trailing 12-month operating cash flow |
| `mdl177_historicalgrowthfactor_cv4qsales3y` | MATRIX | Coefficient of variation (stability) of trailing 12-month sales per share over the past 3 years |
| `mdl177_historicalgrowthfactor_cv4qsales3y_alt` | MATRIX | Coefficient of variation of sales over past 4 quarters in the last 3 years |
| `mdl177_historicalgrowthfactor_cvopinc` | MATRIX | Coefficient of variation of operating income per share in the last 12 quarters |
| `mdl177_historicalgrowthfactor_cvopinc_alt` | MATRIX | Coefficient of variation of operating income per share over the last 12 quarters |
| `mdl177_historicalgrowthfactor_div5yg` | MATRIX | Five-year dividend growth rate |
| `mdl177_historicalgrowthfactor_div5yg_alt` | MATRIX | Five-year growth rate in dividends per share |
| `mdl177_historicalgrowthfactor_fcfequity` | MATRIX | Trailing 12-month free cash flow divided by average book equity value (free cash flow to equity measure) |
| `mdl177_historicalgrowthfactor_fcfequity_alt` | MATRIX | Trailing 12-month free cash flow divided by average book equity value for the same period |
| `mdl177_historicalgrowthfactor_pctchg3ycf` | MATRIX | Percent change in trailing 12-month cash flow per share compared to 12 quarters ago (3-year growth) |
| `mdl177_historicalgrowthfactor_pctchg3ycf_alt` | MATRIX | Percent change in trailing 12-month cash flow per share now compared to 12 quarters ago |
| `mdl177_historicalgrowthfactor_pctchg3yeps` | MATRIX | Percent change in trailing twelve-month earnings per share over last three years (comparing recent vs. 12 quarters ago) |
| `mdl177_historicalgrowthfactor_pctchg3yeps_alt` | MATRIX | Percent change in trailing 12-month earnings per share now compared to 12 quarters ago |
| `mdl177_historicalgrowthfactor_pctchg3yfcf` | MATRIX | Percent change in trailing 12-month free cash flow per share compared to 12 quarters ago (3-year growth) |
| `mdl177_historicalgrowthfactor_pctchg3yfcf_alt` | MATRIX | Percent change in trailing 12-month free cash flow per share now compared to 12 quarters ago |
| `mdl177_historicalgrowthfactor_pctchg3yocf` | MATRIX | Three-year percent growth in trailing twelve-month operating cash flow per share (recent vs. 12 quarters ago) |
| `mdl177_historicalgrowthfactor_pctchg3yocf_alt` | MATRIX | Percent change in trailing 12-month operating cash flow per share now compared to 12 quarters ago |
| `mdl177_historicalgrowthfactor_pctchgastto` | MATRIX | Percent change in asset turnover ratio compared to 4 quarters ago (1-year change in asset efficiency) |
| `mdl177_historicalgrowthfactor_pctchgastto_alt` | MATRIX | Percent change in asset turnover ratio (trailing 12-month sales divided by average assets) compared to 4 quarters ago |
| `mdl177_historicalgrowthfactor_pctchgcf` | MATRIX | 1-year percent change in trailing twelve-month cash flow per share compared to value 4 quarters ago |
| `mdl177_historicalgrowthfactor_pctchgcf_alt` | MATRIX | Percent change in trailing 12-month cash flow per share now compared to 4 quarters ago |
| `mdl177_historicalgrowthfactor_pctchgeps` | MATRIX | Percent change in trailing 12-month earnings per share before extra items compared to 4 quarters ago (1-year growth) |
| `mdl177_historicalgrowthfactor_pctchgeps_alt` | MATRIX | Percent change in trailing 12-month earnings per share before extra items now compared to 4 quarters ago |
| `mdl177_historicalgrowthfactor_pctchgfcf` | MATRIX | Percent change in trailing 12-month free cash flow per share compared to 4 quarters ago (1-year growth) |
| `mdl177_historicalgrowthfactor_pctchgfcf_alt` | MATRIX | Percent change in trailing 12-month free cash flow per share now compared to 4 quarters ago |
| `mdl177_historicalgrowthfactor_pctchgocf` | MATRIX | 1-year percent change in trailing twelve-month operating cash flow per share compared to value 4 quarters ago |
| `mdl177_historicalgrowthfactor_pctchgocf_alt` | MATRIX | Percent change in trailing 12-month operating cash flow per share compared to the value four quarters ago |
| `mdl177_historicalgrowthfactor_pctchgqtrast` | MATRIX | 1-year growth rate in quarterly total assets per share, comparing most recent reported value to that of four quarters… |
| `mdl177_historicalgrowthfactor_pctchgqtrast_alt` | MATRIX | Growth in most recent reported quarterly total assets per share compared to four quarters ago |
| `mdl177_historicalgrowthfactor_pctchgqtrsales` | MATRIX | Growth in most recently reported quarterly sales per share compared to 4 quarters ago (1-year change) |
| `mdl177_historicalgrowthfactor_pctchgqtrsales_alt` | MATRIX | Growth in most recent reported quarterly sales per share compared to four quarters ago |
| `mdl177_historicalgrowthfactor_reinrate` | MATRIX | Reinvestment rate: (TTM EPS before extras minus TTM dividends, divided by average book equity per share) |
| `mdl177_historicalgrowthfactor_reinrate_alt` | MATRIX | Reinvestment rate calculated as trailing 12-month EPS minus dividends, divided by average book equity per share |
| `mdl177_historicalgrowthfactor_rsqr4qcf3y` | MATRIX | R-squared of the regression line describing 3-year trend in trailing twelve-month cash flow |
| `mdl177_historicalgrowthfactor_rsqr4qcf3y_alt` | MATRIX | R-squared of the trend line fitted to trailing 12-month cash flow over the past 3 years |
| `mdl177_historicalgrowthfactor_rsqr4qeps3y` | MATRIX | R-squared of the regression line describing 3-year trend in trailing twelve-month earnings per share |
| `mdl177_historicalgrowthfactor_rsqr4qeps3y_alt` | MATRIX | R-squared of the trend line fitted to trailing 12-month earnings per share over the past 3 years |
| `mdl177_historicalgrowthfactor_rsqr4qfcf3y` | MATRIX | R-squared value of the 3-year trend line for trailing 12-month free cash flow, showing how well FCF fits a linear trend |
| `mdl177_historicalgrowthfactor_rsqr4qfcf3y_alt` | MATRIX | R-squared of the trend line fitted to trailing 12-month free cash flow per share over the past 3 years |
| `mdl177_historicalgrowthfactor_rsqr4qocf3y` | MATRIX | R-squared of regression describing 3-year trend in trailing twelve-month operating cash flow |
| `mdl177_historicalgrowthfactor_rsqr4qocf3y_alt` | MATRIX | R-squared of the trend line fitted to trailing 12-month operating cash flow per share over the past 3 years |
| `mdl177_historicalgrowthfactor_rsqr4qsales3y` | MATRIX | R-squared value of the 3-year trend line for trailing 12-month sales, indicating fit to a linear sales growth trend |
| `mdl177_historicalgrowthfactor_rsqr4qsales3y_alt` | MATRIX | R-squared of the trend line fitted to trailing 12-month sales per share over the past 3 years |
| `mdl177_historicalgrowthfactor_saleg5y` | MATRIX | Difference between trailing 12-month sales per share and that 20 quarters ago, divided by average sales over prior 20… |
| `mdl177_historicalgrowthfactor_saleg5y_alt` | MATRIX | Difference between trailing 12-month sales per share and sales 20 quarters ago, scaled by average sales in those 20 q… |
| `mdl177_historicalgrowthfactor_salegstdev` | MATRIX | Standard deviation of year-over-year quarterly sales per share growth during last 12 quarters (sales growth variability) |
| `mdl177_historicalgrowthfactor_salegstdev_alt` | MATRIX | Standard deviation of year-over-year quarterly sales per share growth during last 12 quarters |
| `mdl177_historicalgrowthfactor_salesaccel4q` | MATRIX | Acceleration of sales growth measured over the last four quarters |
| `mdl177_historicalgrowthfactor_salesaccel4q_alt` | MATRIX | Change in sales growth rate over the most recent four quarters (sales acceleration) |
| `mdl177_historicalgrowthfactor_se5yepsg` | MATRIX | Difference between mean long-term residual EPS growth rate and 5-year EPS growth, divided by EPS growth stability |
| `mdl177_historicalgrowthfactor_se5yepsg_alt` | MATRIX | Mean long-term growth rate minus 5-year EPS growth, divided by stability of 5-year EPS growth |
| `mdl177_historicalgrowthfactor_slope4qcf3y` | MATRIX | Slope of 3-year trailing twelve-month cash flow trend calculated over prior 12 quarters |
| `mdl177_historicalgrowthfactor_slope4qcf3y_alt` | MATRIX | Slope coefficient of 3-year trend line of trailing 12-month cash flow per share |
| `mdl177_historicalgrowthfactor_slope4qeps3y` | MATRIX | Slope of the 3-year trend line for trailing 12-month EPS, measuring EPS growth momentum over 3 years |
| `mdl177_historicalgrowthfactor_slope4qeps3y_alt` | MATRIX | Slope coefficient of 3-year trend line of trailing 12-month earnings per share |
| `mdl177_historicalgrowthfactor_slope4qfcf3y` | MATRIX | Slope coefficient of 3-year trailing twelve-month free cash flow trend over prior 12 quarters |
| `mdl177_historicalgrowthfactor_slope4qfcf3y_alt` | MATRIX | Slope coefficient of 3-year trend line of trailing 12-month free cash flow per share |
| `mdl177_historicalgrowthfactor_slope4qocf3y` | MATRIX | Slope of the 3-year trend line for trailing 12-month operating cash flow per share |
| `mdl177_historicalgrowthfactor_slope4qocf3y_alt` | MATRIX | Slope coefficient of 3-year trend line of trailing 12-month operating cash flow per share |
| `mdl177_historicalgrowthfactor_slope4qsales3y` | MATRIX | Slope coefficient of 3-year trailing twelve-month sales trend; measures sales per share growth trend over prior 12 qu… |
| `mdl177_historicalgrowthfactor_slope4qsales3y_alt` | MATRIX | Slope coefficient of 3-year trend line of trailing 12-month sales per share |
| `mdl177_historicalgrowthfactor_susgrowth` | MATRIX | Maximum growth rate a firm can sustain without increasing financial leverage |
| `mdl177_historicalgrowthfactor_susgrowth_alt` | MATRIX | Maximum growth rate a firm can sustain without increasing financial leverage |
| `mdl177_historicalgrowthfactor_totalsaleg` | MATRIX | Yearly trailing twelve-month total sales growth rate (percent change vs. year ago) |
| `mdl177_historicalgrowthfactor_totalsaleg_alt` | MATRIX | Percent change in trailing 12-month total sales compared to the value one year ago |
| `mdl177_historicalgrowthmodel_chgfcf` | MATRIX | Change in trailing 12-month free cash flow over the past year, adjusted for average total assets |
| `mdl177_historicalgrowthmodel_div5yg` | MATRIX | 5-year growth rate of dividends paid by the company |
| `mdl177_historicalgrowthmodel_emm_composite` | MATRIX | Composite score capturing overall earnings momentum signals for the company |
| `mdl177_historicalgrowthmodel_hgm_composite` | MATRIX | Composite score summarizing various historical growth factors for the company |
| `mdl177_historicalgrowthmodel_slope4qsales3y` | MATRIX | The slope coefficient from a trend line regressed on the trailing 12-month sales per share over the past 12 quarters … |
| `mdl177_historicalgrowthmodel_susgrowth` | MATRIX | The maximum sustainable growth rate for the company without increasing its financial leverage |
| `mdl177_industryrrelativevaluefactor_curindbp_` | MATRIX | A stock's current book-to-price ratio minus the industry average, deflated by the industry's standard deviation of BPs |
| `mdl177_industryrrelativevaluefactor_curindbp__alt` | MATRIX | A stock’s current book-to-price ratio minus the industry average, adjusted by dividing with the industry standard dev… |
| `mdl177_industryrrelativevaluefactor_curindcfp_` | MATRIX | A stock's trailing 12-month cash flow-to-price ratio minus the industry average, deflated by the industry's standard … |
| `mdl177_industryrrelativevaluefactor_curindcfp__alt` | MATRIX | A stock’s trailing 12-month cash flow-to-price ratio minus the industry average, adjusted by dividing with the indust… |
| `mdl177_industryrrelativevaluefactor_curindcoreepsp_` | MATRIX | A stock's trailing 12-month core earnings-to-price ratio minus the industry average, deflated by the industry's stand… |
| `mdl177_industryrrelativevaluefactor_curindcoreepsp__alt` | MATRIX | A stock’s trailing 12-month core earnings-to-price ratio minus the industry average, adjusted by dividing with the in… |
| `mdl177_industryrrelativevaluefactor_curinddivp_` | MATRIX | A stock's trailing 12-month dividend yield minus the industry average, deflated by the industry's standard deviation … |
| `mdl177_industryrrelativevaluefactor_curinddivp__alt` | MATRIX | A stock’s trailing 12-month dividend yield minus the industry average, adjusted by dividing with the industry standar… |
| `mdl177_industryrrelativevaluefactor_curindebitdap_` | MATRIX | A stock's trailing 12-month EBITDA-to-price ratio minus the industry average, deflated by the industry's standard dev… |
| `mdl177_industryrrelativevaluefactor_curindebitdap__alt` | MATRIX | A stock’s trailing 12-month EBITDA-to-price ratio minus the industry average, adjusted by dividing with the industry … |
| `mdl177_industryrrelativevaluefactor_curindep_` | MATRIX | A stock's trailing 12-month EPS-to-price ratio minus the industry average, deflated by the industry's standard deviat… |
| `mdl177_industryrrelativevaluefactor_curindep__alt` | MATRIX | A stock’s trailing 12-month earnings per share before extraordinary items-to-price ratio minus the industry average, … |
| `mdl177_industryrrelativevaluefactor_curindfcfp_` | MATRIX | A stock's trailing 12-month free cash flow-to-price ratio minus the industry average, deflated by the industry's stan… |
| `mdl177_industryrrelativevaluefactor_curindfcfp__alt` | MATRIX | A stock’s trailing 12-month free cash flow-to-price ratio minus the industry average, adjusted by dividing with the i… |
| `mdl177_industryrrelativevaluefactor_curindfwdep_` | MATRIX | A stock's forward 4-quarter analysts consensus EPS-to-price ratio minus the industry average, deflated by the industr… |
| `mdl177_industryrrelativevaluefactor_curindfwdep__alt` | MATRIX | A stock’s next 4-quarter analyst consensus EPS estimates-to-price ratio minus the industry average, adjusted by divid… |
| `mdl177_industryrrelativevaluefactor_curindocfp_` | MATRIX | A stock's trailing 12-month operating cash flow-to-price ratio minus the industry average, deflated by the industry's… |
| `mdl177_industryrrelativevaluefactor_curindocfp__alt` | MATRIX | A stock’s trailing 12-month operating cash flow-to-price ratio minus the industry average, adjusted by dividing with … |
| `mdl177_industryrrelativevaluefactor_curindocfta_` | MATRIX | A stock's trailing 12-month operating cash flow-to-total assets ratio minus the industry average, deflated by the ind… |
| `mdl177_industryrrelativevaluefactor_curindocfta__alt` | MATRIX | A stock’s trailing 12-month operating cash flow-to-total assets ratio minus the industry average, adjusted by dividin… |
| `mdl177_industryrrelativevaluefactor_curindsp_` | MATRIX | A stock's trailing 12-month sales-to-price ratio minus the industry average, deflated by the industry's standard devi… |
| `mdl177_industryrrelativevaluefactor_curindsp__alt` | MATRIX | A stock’s trailing 12-month sales-to-price ratio minus the industry average, adjusted by dividing with the industry s… |
| `mdl177_liquidityriskfactor_altmanz_alt` | MATRIX | Altman Z-score: A composite measure predicting bankruptcy risk, calculated using a weighted sum of profitability, lev… |
| `mdl177_liquidityriskfactor_aqi_alt` | MATRIX | Asset Quality Index : It is defined as the year-over-year change of 1 minus the ratio of current assets plus PP&E div… |
| `mdl177_liquidityriskfactor_astcomp_alt` | MATRIX | Asset composition: total current assets divided by total assets from most recent quarter, indicating liquidity propor… |
| `mdl177_liquidityriskfactor_atmcallvol_alt` | MATRIX | Implied volatility of the nearest at-the-money call options, indicator of option market expectations for price fluctu… |
| `mdl177_liquidityriskfactor_atmputvol_alt` | MATRIX | Implied volatility of the nearest at-the-money put options, measuring market expectation of downside risk |
| `mdl177_liquidityriskfactor_bap20d_alt` | MATRIX | 20-day average of the bid-ask spread divided by price, indicating short-term liquidity cost for trading the stock |
| `mdl177_liquidityriskfactor_bdi_alt` | MATRIX | Basic Defensive Interval: number of days a company's cash and receivables can cover daily operating expenses (COGS + … |
| `mdl177_liquidityriskfactor_beta_alt` | MATRIX | 60-Month Beta : It is defined as 0.67 times the 60-month beta plus 0.33Beta is the covariance between a stock's month… |
| `mdl177_liquidityriskfactor_betasigma_alt` | MATRIX | Product of the adjusted 60-month Beta (market sensitivity) and the 60-month Sigma (volatility of monthly price return… |
| `mdl177_liquidityriskfactor_booklev_alt` | MATRIX | Book Leverage ratio: Total assets from most recent quarter divided by book equity, reflecting company capital structure |
| `mdl177_liquidityriskfactor_cashratio_alt` | MATRIX | Liquidity measure: Most recent quarter’s cash and equivalents divided by current liabilities |
| `mdl177_liquidityriskfactor_ccd_alt` | MATRIX | Current Cash Flow Debt Coverage Ratio: Most recent quarterly cash flow from operations minus dividends, divided by cu… |
| `mdl177_liquidityriskfactor_cfleverage_alt` | MATRIX | Cash Flow Leverage: Total liabilities divided by trailing 12-month operating cash flow, a stress test of cash flow co… |
| `mdl177_liquidityriskfactor_covol_alt` | MATRIX | Slope of least squares trend line of last 60 months’ monthly trading volume versus time; measures long-term volume trend |
| `mdl177_liquidityriskfactor_curratio_alt` | MATRIX | Current ratio: Current assets divided by current liabilities (most recent quarter), indicating short-term financial h… |
| `mdl177_liquidityriskfactor_cvvolp20d_alt` | MATRIX | Ratio of coefficient of variation (volatility) of last 20 days’ closing prices to coefficient of variation of daily t… |
| `mdl177_liquidityriskfactor_de_alt` | MATRIX | Long-term debt to equity ratio: Most recent long-term debt divided by book equity; measure of leverage |
| `mdl177_liquidityriskfactor_debtcf_alt` | MATRIX | Sum of most recent reported long-term debt and short-term interest-bearing debt divided by trailing 12-month cash flo… |
| `mdl177_liquidityriskfactor_dfl_alt` | MATRIX | Degree of financial leverage: (Pretax income + interest expense) divided by pretax income, proxy for interest depende… |
| `mdl177_liquidityriskfactor_divcov_alt` | MATRIX | Dividend coverage ratio: company's trailing annual operating earnings divided by annual dividends; reflects ability t… |
| `mdl177_liquidityriskfactor_flowratio_alt` | MATRIX | Flow ratio: (current assets - cash & equivalents) divided by (current liabilities - short-term debt), measuring liqui… |
| `mdl177_liquidityriskfactor_gear_alt` | MATRIX | Capital gearing ratio: long-term debt divided by (total assets minus current liability); measures leverage excluding … |
| `mdl177_liquidityriskfactor_growdura_alt` | MATRIX | Growth Duration |
| `mdl177_liquidityriskfactor_impduration_alt` | MATRIX | Implied Equity Duration |
| `mdl177_liquidityriskfactor_intcov_alt` | MATRIX | Interest Coverage: Quarterly operating income before depreciation divided by quarterly long-term debt interest expens… |
| `mdl177_liquidityriskfactor_liqcoeff_alt` | MATRIX | Liquidity coefficient: regression slope between monthly turnover ratio and monthly stock returns; indicator of liquid… |
| `mdl177_liquidityriskfactor_mad3yttmni_alt` | MATRIX | 3-year mean absolute deviation of trailing 12-month net income, a measure of profit variability |
| `mdl177_liquidityriskfactor_mad3yttmsale_alt` | MATRIX | 3-year mean absolute deviation of trailing 12-month sales, a measure of sales stability/volatility |
| `mdl177_liquidityriskfactor_milliq_alt` | MATRIX | Stock illiquidity measure: Monthly average of daily absolute return divided by daily dollar trading volume |
| `mdl177_liquidityriskfactor_mktcappera_alt` | MATRIX | Market capitalization divided by number of analysts providing estimates; reflects stock interest or coverage per analyst |
| `mdl177_liquidityriskfactor_mktlev_alt` | MATRIX | (Market value of equity + most recent quarterly book debt) divided by market value of equity; leverage measure linkin… |
| `mdl177_liquidityriskfactor_monchgsip_alt` | MATRIX | Monthly change in short interest position; measures month-to-month change in ratio of shares sold short to shares out… |
| `mdl177_liquidityriskfactor_netcashp_alt` | MATRIX | Net cash to equity: (Quarterly cash and equivalents minus long-term and current debt) divided by current market value… |
| `mdl177_liquidityriskfactor_nfaldebt_alt` | MATRIX | Net fixed assets divided by long-term debt, reflecting long-term asset coverage of debt; higher values indicate bette… |
| `mdl177_liquidityriskfactor_nlassets_alt` | MATRIX | Natural logarithm of the most recent quarterly total assets; serves as a size metric |
| `mdl177_liquidityriskfactor_nlmktcap_alt` | MATRIX | Natural logarithm of the cube of stock’s total market value; proxy for firm size (log-transformed) |
| `mdl177_liquidityriskfactor_nlprice_alt` | MATRIX | Natural logarithm of the cube of the stock’s unadjusted closing price; log-transformed price metric |
| `mdl177_liquidityriskfactor_nlsales_alt` | MATRIX | Natural logarithm of the cube of trailing 12-month sales; log-transformed sales size metric |
| `mdl177_liquidityriskfactor_nlvolcap_alt` | MATRIX | Natural logarithm of (trailing 1-year average monthly volume divided by trailing 1-year average of monthly market val… |
| `mdl177_liquidityriskfactor_numest_alt` | MATRIX | Number of analyst estimates for fiscal year 1; proxy for analyst coverage |
| `mdl177_liquidityriskfactor_ocfratio_alt` | MATRIX | Operating cash flow ratio: Most recent quarterly cash flow from operations divided by current liabilities |
| `mdl177_liquidityriskfactor_ohlsonscore_alt` | MATRIX | Ohlson bankruptcy risk score, assessing probability of bankruptcy using financial ratios and firm characteristics |
| `mdl177_liquidityriskfactor_oplev_alt` | MATRIX | Operating leverage: Percent change in TTM operating income (vs previous quarter) divided by percent change in TTM sal… |
| `mdl177_liquidityriskfactor_pcurlia_alt` | MATRIX | Current liabilities per share divided by closing price; reflects short-term obligations relative to market value |
| `mdl177_liquidityriskfactor_qr_alt` | MATRIX | Quick (acid-test) ratio: (Current assets minus inventories) divided by current liabilities, most recent quarter |
| `mdl177_liquidityriskfactor_rerror60m_alt` | MATRIX | Standard error of slope from least squares regression of last 60 months’ monthly returns against S&P 500 returns; mea… |
| `mdl177_liquidityriskfactor_si_ratio_alt` | MATRIX | Short interest ratio: shares sold short divided by average daily volume over last 30 days; estimates days to cover sh… |
| `mdl177_liquidityriskfactor_sigma_alt` | MATRIX | Standard deviation of monthly returns over prior 60 months; measures stock price volatility |
| `mdl177_liquidityriskfactor_sip_alt` | MATRIX | Short interest position: number of shares sold short as reported, reflecting bearish sentiment or hedging activity |
| `mdl177_liquidityriskfactor_tobinq_alt` | MATRIX | Tobin’s Q ratio: (Market value of equity plus debt) divided by total assets (debt at book value); assesses firm valua… |
| `mdl177_liquidityriskfactor_totalcov_alt` | MATRIX | Total coverage ratio: (Cash flow from operations + interest paid + tax paid) divided by (interest + principal paid); … |
| `mdl177_liquidityriskfactor_voldiff_pc_alt` | MATRIX | Difference between ATM put and call implied volatilities; signals option market sentiment and liquidity risk |
| `mdl177_liquidityriskfactor_volto_alt` | MATRIX | Trading turnover ratio: Monthly total trading volume divided by total outstanding shares (recent); velocity of share … |
| `mdl177_liquidityriskfactor_yoychgcr_alt` | MATRIX | Year-over-year change in current ratio; difference in current ratio (current assets/current liabilities) compared to … |
| `mdl177_liquidityriskfactor_yoychgda_alt` | MATRIX | Year-over-year Change in Leverage : It is defined as the difference between the most recent reported quarterly total … |
| `mdl177_momemtumanalystmodel_qma_alpha6m` | MATRIX | Rank representing the stock's six-month alpha change, measuring abnormal returns over the past six months relative to… |
| `mdl177_momemtumanalystmodel_qma_alpha6m_alt` | MATRIX | Rank representing the change in alpha generated by the stock over the past six months, gauging its risk-adjusted outp… |
| `mdl177_momemtumanalystmodel_qma_chgnowc` | MATRIX | Rank of the change in Net Working Capital (NOWC), reflecting shifts in short-term operational liquidity over a recent… |
| `mdl177_momemtumanalystmodel_qma_chgnowc_alt` | MATRIX | Rank based on the change in net working capital, reflecting improvements or deteriorations in the company's liquidity… |
| `mdl177_momemtumanalystmodel_qma_composite` | MATRIX | Momentum Analyst Composite Rank: an aggregated rank combining various analyst momentum signals for the stock |
| `mdl177_momemtumanalystmodel_qma_composite_alt` | MATRIX | Overall composite rank of the momentum analyst model, typically aggregating multiple factor signals into a single mom… |
| `mdl177_momemtumanalystmodel_qma_condsurp` | MATRIX | Conditional Surprise Rank: a rank measuring the degree to which reported results have surprised analyst expectations,… |
| `mdl177_momemtumanalystmodel_qma_condsurp_alt` | MATRIX | Conditional Surprise Rank |
| `mdl177_momemtumanalystmodel_qma_earnexp` | MATRIX | Analyst Expectations Rank: a composite rank based on analyst expectations, specifically averaging earnings revisions … |
| `mdl177_momemtumanalystmodel_qma_earnexp_alt` | MATRIX | Rank reflecting analyst expectations, calculated as an equal-weighted average of analyst earnings revisions and ratin… |
| `mdl177_momemtumanalystmodel_qma_eplinkage` | MATRIX | Earnings Price Linkage Rank: measures the relation between changes in earnings and price response, aggregating factor… |
| `mdl177_momemtumanalystmodel_qma_eplinkage_alt` | MATRIX | Rank representing the linkage between earnings and price, typically an aggregate of change in free cash flow, net wor… |
| `mdl177_momemtumanalystmodel_qma_epsgrwth` | MATRIX | Earnings Growth Rank: rank of change in trailing twelve month earnings per share, scaled by recent closing price, ind… |
| `mdl177_momemtumanalystmodel_qma_epsgrwth_alt` | MATRIX | Rank of earnings growth, measuring changes in trailing twelve month earnings per share scaled by the recent closing s… |
| `mdl177_momemtumanalystmodel_qma_estrev` | MATRIX | Estimate Revisions Rank: rank reflecting the difference between recent upward and downward revisions to next fiscal y… |
| `mdl177_momemtumanalystmodel_qma_estrev_alt` | MATRIX | Rank based on estimate revisions, capturing the difference between recent upward and downward EPS estimate changes ov… |
| `mdl177_momemtumanalystmodel_qma_indrelrtn3m` | MATRIX | Industry Relative 3-Month Return Rank: measures the difference between the stock's three-month return and its industr… |
| `mdl177_momemtumanalystmodel_qma_indrelrtn3m_alt` | MATRIX | Rank of the stock's 3-month return relative to its industry peers over the same period |
| `mdl177_momemtumanalystmodel_qma_lagpricemo` | MATRIX | Lagged 12- to 1-Month Price Momentum Rank: rank of the difference between lagged 12-month return and recent 1-month r… |
| `mdl177_momemtumanalystmodel_qma_lagpricemo_alt` | MATRIX | Rank reflecting lagged price momentum, calculated as the difference between the stock's lagged 12-month return and re… |
| `mdl177_momemtumanalystmodel_qma_mktresponse` | MATRIX | Market Earnings Response Rank: rank of the 4-day return surrounding the company’s most recent earnings report, spanni… |
| `mdl177_momemtumanalystmodel_qma_mktresponse_alt` | MATRIX | Rank gauging market response to earnings, typically the four-day return spanning two days before and after a recent e… |
| `mdl177_momemtumanalystmodel_qma_ratingchg` | MATRIX | Analyst Ratings Change Rank: rank reflecting changes in analyst consensus ratings over the last 4 and 8 weeks |
| `mdl177_momemtumanalystmodel_qma_ratingchg_alt` | MATRIX | Rank measuring recent changes in analyst consensus ratings, based on trends in revisions over the last 4 and 8 weeks |
| `mdl177_momemtumanalystmodel_qma_relpricemo` | MATRIX | Relative Price Momentum Rank: an aggregated rank combining lagged 12-1 month price momentum, risk adjustment, and 6-m… |
| `mdl177_momemtumanalystmodel_qma_relpricemo_alt` | MATRIX | Rank summarizing relative price momentum, often an average of lagged price momentum, risk adjustments, and six-month … |
| `mdl177_momemtumanalystmodel_qma_repearnmom` | MATRIX | Earnings Momentum Rank: an average ranking derived from both earnings growth and earnings surprise for a stock |
| `mdl177_momemtumanalystmodel_qma_repearnmom_alt` | MATRIX | Rank of earnings momentum, generally an average of earnings growth and earnings surprise rankings |
| `mdl177_momemtumanalystmodel_qma_rskadj` | MATRIX | Risk Adjustments Rank: a rank aggregating volatility and growth subfactors, penalizing stocks with high volume volati… |
| `mdl177_momemtumanalystmodel_qma_rskadj_alt` | MATRIX | Rank aggregating risk adjustments, penalizing high volume volatility and large deviations in return for a risk-inform… |
| `mdl177_momemtumanalystmodel_qma_ttmfcfchg` | MATRIX | Change in TTM Free Cash Flow Rank: rank of the two-quarter change in trailing twelve month free cash flow, divided by… |
| `mdl177_momemtumanalystmodel_qma_ttmfcfchg_alt` | MATRIX | Rank representing the change in trailing twelve month free cash flow over two quarters, divided by the value from two… |
| `mdl177_priceanalystmodel_qpa_composite_alt` | MATRIX | A composite price signal generated by the Price Analyst Model, aggregating multiple price-related factors to summariz… |
| `mdl177_priceanalystmodel_qpa_compsn_alt` | MATRIX | Price Analyst Sector-Neutral |
| `mdl177_priceanalystmodel_qpa_indrs_alt` | MATRIX | Industry-relative strength, quantifying a stock's price performance compared to its industry group |
| `mdl177_priceanalystmodel_qpa_rskadjrs_alt` | MATRIX | Risk Adj Relative Strength |
| `mdl177_pricemomemtummodel_indrelrtn5d_` | MATRIX | Stock’s 5-day return minus the average 5-day return of all stocks in the same industry, normalized by the industry re… |
| `mdl177_pricemomemtummodel_pmm_composite` | MATRIX | Composite price momentum signal combining several individual price momentum indicators for a more robust measure of m… |
| `mdl177_pricemomemtummodel_rationalalpha` | MATRIX | Rational Decay Alpha: Measures a stock’s historical 12-month market-adjusted excess return using the intercept from a… |
| `mdl177_pricemomemtummodel_relpricestrength_` | MATRIX | Industry-adjusted 12-month relative price strength: Stock’s 12-month price strength minus the industry average, defla… |
| `mdl177_pricemomemtummodel_visiratio` | MATRIX | Visibility Ratio: Most recent daily trading volume divided by average daily volume over the previous 50 trading days,… |
| `mdl177_pricemomemtummodel_voldiff_pc` | MATRIX | Difference between at-the-money (ATM) Put option volatility and ATM Call option volatility for the stock, indicating … |
| `mdl177_pricemomentumfactor_abr` | MATRIX | Abnormal return around quarterly earnings release (excess return during period around earnings announcement) |
| `mdl177_pricemomentumfactor_abr_alt` | MATRIX | Abnormal Return around QTR Earnings Release; abnormal return calculated in the event window surrounding quarterly ear… |
| `mdl177_pricemomentumfactor_actrtn12m` | MATRIX | Percent change in stock price over the past 12 months, measured with a 1-month lag to avoid lookahead bias |
| `mdl177_pricemomentumfactor_actrtn12m_alt` | MATRIX | Percent change in stock price from month t-13 to month t-1 |
| `mdl177_pricemomentumfactor_actrtn18m` | MATRIX | Percent change in stock price from 19 months ago to 1 month ago (18-month active return, lagged) |
| `mdl177_pricemomentumfactor_actrtn18m_alt` | MATRIX | Percent change in stock price from month t-19 to month t-1 |
| `mdl177_pricemomentumfactor_actrtn1m` | MATRIX | Percent change in stock price in last month |
| `mdl177_pricemomentumfactor_actrtn1m_alt` | MATRIX | Percent change in stock price from month t-1 to month t |
| `mdl177_pricemomentumfactor_actrtn24m` | MATRIX | Percent change in stock price over the past 24 months, measured with a 1-month lag to avoid lookahead bias |
| `mdl177_pricemomentumfactor_actrtn24m_alt` | MATRIX | Percent change in stock price from month t-25 to month t-1 |
| `mdl177_pricemomentumfactor_actrtn2m` | MATRIX | Percent change in stock price over last 2 months |
| `mdl177_pricemomentumfactor_actrtn2m_alt` | MATRIX | Percent change in stock price from month t-2 to month t |
| `mdl177_pricemomentumfactor_actrtn36m` | MATRIX | Percent change in stock price from 37 months ago to 1 month ago (36-month active return, lagged) |
| `mdl177_pricemomentumfactor_actrtn36m_alt` | MATRIX | Percent change in stock price from month t-37 to month t-1 |
| `mdl177_pricemomentumfactor_actrtn3m` | MATRIX | Percent change in stock price over last 3 months |
| `mdl177_pricemomentumfactor_actrtn3m_alt` | MATRIX | Percent change in stock price from month t-3 to month t |
| `mdl177_pricemomentumfactor_actrtn60m` | MATRIX | Percent change in stock price over the past 60 months (5 years), measured with a 1-month lag to avoid lookahead bias |
| `mdl177_pricemomentumfactor_actrtn60m_alt` | MATRIX | 60-Month Active Return with 1-Month Lag; percent price change from month t-61 to month t-1 |
| `mdl177_pricemomentumfactor_actrtn6m` | MATRIX | Percent change in stock price over the past 6 months, measured with a 1-month lag to avoid lookahead bias |
| `mdl177_pricemomentumfactor_actrtn6m_alt` | MATRIX | Percent change in stock price from month t-7 to month t-1 |
| `mdl177_pricemomentumfactor_alpha60m` | MATRIX | The intercept (alpha) from a regression of the stock's monthly returns against the S&P 500 over the past 60 months |
| `mdl177_pricemomentumfactor_alpha60m_alt` | MATRIX | 60-Month Alpha; regression intercept of stock's monthly return vs S&P 500 monthly return over last 60 months |
| `mdl177_pricemomentumfactor_chg6malpha18m` | MATRIX | Nominal change in 18-month alpha over past 6 months |
| `mdl177_pricemomentumfactor_chg6malpha18m_alt` | MATRIX | 6-Month Nominal Change in 18-Month Alpha; the change during the last 6 months of a stock’s 18-month alpha, where alph… |
| `mdl177_pricemomentumfactor_chgalpha12m` | MATRIX | Change in 12-month alpha (regression intercept) over the past 6 months |
| `mdl177_pricemomentumfactor_chgalpha12m_alt` | MATRIX | 6-Month Nominal Change in 12-Month Alpha; 6-month change in 12-month alpha, regression intercept of monthly return vs… |
| `mdl177_pricemomentumfactor_chgalpha36m` | MATRIX | 6-month change in the 36-month alpha (regression intercept) of the stock |
| `mdl177_pricemomentumfactor_chgalpha36m_alt` | MATRIX | The 6-month nominal change in a stock’s 36-month alpha, calculated as the difference in regression intercept (monthly… |
| `mdl177_pricemomentumfactor_chgvolpre4y` | MATRIX | Change in average trading volume over the previous 4 years (compares recent and past activity) |
| `mdl177_pricemomentumfactor_chgvolpre4y_alt` | MATRIX | Change in the most recent 6-month moving average of monthly turnover ratio compared to the 12-month moving average of… |
| `mdl177_pricemomentumfactor_cvpre90dp` | MATRIX | CV of Prior 90-Day Closing Prices |
| `mdl177_pricemomentumfactor_cvpre90dp_alt` | MATRIX | Coefficient of variation of the last 90 closing prices: standard deviation divided by mean of those prices |
| `mdl177_pricemomentumfactor_ff10mrtn` | MATRIX | Fama-French momentum factor (return over 10 months, often lagged by 2 months, standard risk factor) |
| `mdl177_pricemomentumfactor_ff10mrtn_alt` | MATRIX | Fama-French Momentum; percent change in price from month t-12 to t-2, a standard momentum factor definition |
| `mdl177_pricemomentumfactor_high52w` | MATRIX | Ratio of the current (month-end) price to the highest monthly closing price in the past 12 months |
| `mdl177_pricemomentumfactor_high52w_alt` | MATRIX | 52-Week High; month-end price divided by the highest monthly close in past 12 months |
| `mdl177_pricemomentumfactor_indrelrtn4w_` | MATRIX | Industry-relative return over the last 4 weeks: stock's return minus industry average, deflated by industry standard … |
| `mdl177_pricemomentumfactor_indrelrtn4w__alt` | MATRIX | Stock’s return in last 4 weeks minus industry average return over the same period, standardized by industry return st… |
| `mdl177_pricemomentumfactor_indrelrtn5d_` | MATRIX | Industry-relative return over last 5 days: stock's return minus industry average, deflated by industry standard devia… |
| `mdl177_pricemomentumfactor_indrelrtn5d__alt` | MATRIX | 5-day industry-relative return; stock's return over last 5 days minus industry average, standardized by industry retu… |
| `mdl177_pricemomentumfactor_normalmf60d` | MATRIX | 60-Day Normalized Money Flow |
| `mdl177_pricemomentumfactor_normalmf60d_alt` | MATRIX | 60-Day Normalized Money Flow |
| `mdl177_pricemomentumfactor_p50_200ratio` | MATRIX | Ratio of price at 50-day mark to price at 200-day mark (momentum or moving average crossover) |
| `mdl177_pricemomentumfactor_p50_200ratio_alt` | MATRIX | 50-200 Day Stock Price Ratio; moving average over last 50 days divided by moving average over last 200 days |
| `mdl177_pricemomentumfactor_pc_ratio` | MATRIX | Put/Call Ratio: Ratio between traded put and call option volumes (sentiment indicator) |
| `mdl177_pricemomentumfactor_pc_ratio_alt` | MATRIX | Put/Call Ratio; ratio of put options to call options traded, typically a sentiment/contrarian signal |
| `mdl177_pricemomentumfactor_pctabv260low` | MATRIX | Percent the current price is above the lowest trading price in the past 260 days |
| `mdl177_pricemomentumfactor_pctabv260low_alt` | MATRIX | The ratio of a stock's current closing price to its lowest daily low price over the last 260 trading days |
| `mdl177_pricemomentumfactor_po4_52` | MATRIX | Price oscillator measuring difference or momentum between 4-week and 52-week price trends |
| `mdl177_pricemomentumfactor_po4_52_alt` | MATRIX | 4-52 Week Price Oscillator |
| `mdl177_pricemomentumfactor_pr_1536` | MATRIX | Ratio of price over the last 15 weeks versus last 36 weeks (a momentum indicator) |
| `mdl177_pricemomentumfactor_pr_1536_alt` | MATRIX | 15/36 Week Stock Price Ratio; moving average of a stock’s price over the last 15 weeks divided by the moving average … |
| `mdl177_pricemomentumfactor_pr_30w75w` | MATRIX | Ratio of the 30-week moving average price to the 75-week moving average price, indicating short vs long-term momentum |
| `mdl177_pricemomentumfactor_pr_30w75w_alt` | MATRIX | 30-75 Week Stock Price Ratio; moving average of a stock’s prices over the last 30 weeks divided by moving average ove… |
| `mdl177_pricemomentumfactor_pvt51w` | MATRIX | Volume Price Trend indicator over the past 51 weeks, calculated with a 4-week lag; combines price change and volume t… |
| `mdl177_pricemomentumfactor_pvt51w_alt` | MATRIX | 51-Week Volume Price Trend with 4-week Lag; price-volume trend indicator calculated over 51 weeks with a 4-week lag |
| `mdl177_pricemomentumfactor_rationalalpha` | MATRIX | Rational Decay Alpha |
| `mdl177_pricemomentumfactor_rationalalpha_alt` | MATRIX | Rational Decay Alpha; market-adjusted 12-month excess return regression intercept, using a decay-weighted function |
| `mdl177_pricemomentumfactor_relpricestrength_` | MATRIX | Industry-adjusted 12-month price strength: stock's 12-month price strength minus the industry mean, deflated by indus… |
| `mdl177_pricemomentumfactor_relpricestrength__alt` | MATRIX | Industry-adjusted 12-month Relative Price Strength; stock's 12-month relative strength minus industry average, divide… |
| `mdl177_pricemomentumfactor_rsi26w` | MATRIX | Relative Strength Index over 26 weeks (price momentum indicator, compares current price to price 26 weeks ago) |
| `mdl177_pricemomentumfactor_rsi26w_alt` | MATRIX | 26-Week Relative Price Strength; most recent closing price divided by that of 26 weeks ago, showing long-term momentum |
| `mdl177_pricemomentumfactor_rtn2nd6m` | MATRIX | Return over the second most recent 6-month period (i.e., 6-12 months ago) |
| `mdl177_pricemomentumfactor_rtn2nd6m_alt` | MATRIX | Second Preceding 6-month Return; price percent change from month t-12 to month t-7 |
| `mdl177_pricemomentumfactor_rtn39w` | MATRIX | Return over 39 weeks with a 4-week lag (measures momentum over medium term) |
| `mdl177_pricemomentumfactor_rtn39w_alt` | MATRIX | 39-Week Return with 4-week Lag; stock price change from week t-43 to week t-4 |
| `mdl177_pricemomentumfactor_sharpe36m` | MATRIX | Sharpe Ratio for the asset, calculated over a 36-month period (risk-adjusted return for given volatility over 3 years) |
| `mdl177_pricemomentumfactor_sharpe36m_alt` | MATRIX | 36-Month Sharpe Ratio; a measure of risk-adjusted return calculated over the past 36 months by dividing average exces… |
| `mdl177_pricemomentumfactor_skew90cortn` | MATRIX | Skewness of excess daily returns (relative to benchmark) during past 90 days |
| `mdl177_pricemomentumfactor_skew90cortn_alt` | MATRIX | Skewness of 90-Day Stock Daily Excess Returns; skewness of daily excess (over S&P 500) returns in last 90 days |
| `mdl177_pricemomentumfactor_skew90drtn` | MATRIX | Skewness of daily returns over the last 90 days (measures asymmetry of return distribution) |
| `mdl177_pricemomentumfactor_skew90drtn_alt` | MATRIX | Skewness of 90-Day Stock Daily Returns; statistical skewness (3*(mean-median)/std) of stock's daily returns over last… |
| `mdl177_pricemomentumfactor_slope52wp` | MATRIX | Slope of trend line for stock price over the last 52 weeks (strength and direction of long-term price trend) |
| `mdl177_pricemomentumfactor_slope52wp_alt` | MATRIX | The 4-week lagged slope coefficient from the least squares regression of a stock’s closing price against time over th… |
| `mdl177_pricemomentumfactor_slope66wp` | MATRIX | Slope coefficient of least squares regression of weekly closing price over the past 66 weeks, lagged by 4 weeks |
| `mdl177_pricemomentumfactor_slope66wp_alt` | MATRIX | Slope of 66 Week Price Trend Line; 4-week lagged slope coefficient from least squares regression of last 66 weeks' cl… |
| `mdl177_pricemomentumfactor_sortinoratio` | MATRIX | Sortino ratio, measuring risk-adjusted return using downside deviation rather than total volatility |
| `mdl177_pricemomentumfactor_sortinoratio_alt` | MATRIX | Sortino Ratio; risk-adjusted return similar to Sharpe but penalizes only downside volatility, over unspecified period |
| `mdl177_pricemomentumfactor_tstalp` | MATRIX | 1-year price momentum indicator (e.g., correlation of daily log prices over 260 trading days) |
| `mdl177_pricemomentumfactor_tstalp_alt` | MATRIX | 1-Year Price Momentum Indicator; correlation of daily log prices over last 260 days, scaled to measure trend strength |
| `mdl177_pricemomentumfactor_var24m` | MATRIX | Value at Risk (VaR) calculated over the past 24 months, representing potential loss over that horizon at a specified … |
| `mdl177_pricemomentumfactor_var24m_alt` | MATRIX | 24-Month Value at Risk; minimum (worst) monthly price return over the last 20 months, a measure of downside risk |
| `mdl177_pricemomentumfactor_varresirtn` | MATRIX | Variance of residual returns over past 24 months (measures risk not explained by common factors) |
| `mdl177_pricemomentumfactor_varresirtn_alt` | MATRIX | Variance of the stock’s monthly residual return over the last 24 months, where residual return is the stock’s monthly… |
| `mdl177_pricemomentumfactor_visiratio` | MATRIX | Visibility Ratio: recent daily volume divided by average daily volume over prior 50 days (trading activity indicator) |
| `mdl177_pricemomentumfactor_visiratio_alt` | MATRIX | Visibility Ratio; most recent daily trading volume divided by average daily trading volume in prior 50 trading days |
| `mdl177_pricemomentumfactor_volpre6m` | MATRIX | Average trading volume over the preceding 6 months (trading activity measure) |
| `mdl177_pricemomentumfactor_volpre6m_alt` | MATRIX | 6-month moving average of average monthly turnover ratio; measures trading volume normalized by shares outstanding, a… |
| `mdl177_put_put_capmod` | MATRIX | Capital strength module, a composite score measuring a company's financial strength and capital adequacy |
| `mdl177_put_put_capmod_alt` | MATRIX | A composite/module summarizing capital strength factors (e.g. leverage, capital ratios) |
| `mdl177_put_put_cashburn` | MATRIX | Cash burn rate, indicating the rate at which a company is spending its cash reserves |
| `mdl177_put_put_cashburn_alt` | MATRIX | Rate at which a company spends cash, e.g. negative free cash flow in a period |
| `mdl177_put_put_chgalpha` | MATRIX | Six-month alpha change rank, ranking stocks by change in alpha (excess return over benchmark) over the latest six months |
| `mdl177_put_put_chgalpha_alt` | MATRIX | Ranked change in alpha (risk-adjusted excess return) over a six-month period |
| `mdl177_put_put_chgoll` | MATRIX | Change in operating liability leverage, measuring how a company's operating liabilities leverage has changed over a g… |
| `mdl177_put_put_chgoll_alt` | MATRIX | Change in operating liability leverage over a given period |
| `mdl177_put_put_chshrs` | MATRIX | Percentage change in shares outstanding, tracking how the total number of a company's shares has changed over time |
| `mdl177_put_put_chshrs_alt` | MATRIX | Percent change in shares outstanding over a specific period |
| `mdl177_put_put_composite` | MATRIX | Custom small cap composite score aggregating several signals relevant to small-cap stocks |
| `mdl177_put_put_composite_alt` | MATRIX | A custom composite signal designed for small-cap stocks, combining multiple factors |
| `mdl177_put_put_dypeg` | MATRIX | Reciprocal of Dividend Yield-adjusted PEG |
| `mdl177_put_put_dypeg_alt` | MATRIX | Inverse of a PEG ratio adjusted for dividend yield; used for value/growth analysis |
| `mdl177_put_put_equality` | MATRIX | Earnings quality rank, a score or rank assessing the reliability and sustainability of a company's reported earnings |
| `mdl177_put_put_equality_alt` | MATRIX | Rank or score indicating the quality of earnings (e.g., sustainability, reliability) |
| `mdl177_put_put_indepsp` | MATRIX | Industry-relative core earnings per share to price ratio, comparing normalized/core EPS-to-price relative to peers in… |
| `mdl177_put_put_indepsp_alt` | MATRIX | Industry-relative core earnings per share to price ratio |
| `mdl177_put_put_indestep` | MATRIX | Industry-relative leading (estimated forward) EPS-to-price ratio, comparing a stock's forward earnings to price, rela… |
| `mdl177_put_put_indestep_alt` | MATRIX | Industry-relative leading 4 quarters' estimated EPS to price ratio |
| `mdl177_put_put_indfcfp` | MATRIX | Industry-relative free cash flow to price ratio, measuring a company's free cash flow compared to price, adjusted rel… |
| `mdl177_put_put_indfcfp_alt` | MATRIX | Industry-relative ratio of free cash flow to price |
| `mdl177_put_put_indroe` | MATRIX | Industry-relative return on equity, comparing a company's ROE to its industry average |
| `mdl177_put_put_indroe_alt` | MATRIX | Industry-relative return on equity; how a stock's ROE compares to its industry |
| `mdl177_put_put_momod` | MATRIX | Momentum Module |
| `mdl177_put_put_momod_alt` | MATRIX | Momentum composite or module aggregating multiple momentum-related signals |
| `mdl177_put_put_opincev` | MATRIX | Operating income to enterprise value ratio, a valuation metric comparing operating profitability to total firm value |
| `mdl177_put_put_opincev_alt` | MATRIX | Ratio of operating income to enterprise value, indicating operating profitability relative to valuation |
| `mdl177_put_put_qualmod` | MATRIX | Quality module, an aggregated signal evaluating aspects of profitability, stability, and other quality factors |
| `mdl177_put_put_qualmod_alt` | MATRIX | A composite or module aggregating various quality-related financial indicators |
| `mdl177_put_put_siratio` | MATRIX | Short interest ratio, measuring the relative amount of shares shorted compared to available shares or average daily v… |
| `mdl177_put_put_siratio_alt` | MATRIX | Ratio of shares sold short to total shares outstanding or float |
| `mdl177_put_put_strevconf` | MATRIX | Street revision confidence, measuring analyst confidence or consensus in recent earnings or revenue estimate revisions |
| `mdl177_put_put_strevconf_alt` | MATRIX | Confidence in street (analyst) earnings revisions, likely a score or rank |
| `mdl177_put_put_sucf` | MATRIX | Standardized unexpected cash flow, indicating the magnitude of cash flow that deviated from expectations, standardize… |
| `mdl177_put_put_sucf_alt` | MATRIX | Standardized measure of unexpected (surprise) cash flow, normalized across stocks |
| `mdl177_put_put_totcov` | MATRIX | Total Coverage |
| `mdl177_put_put_totcov_alt` | MATRIX | Total Coverage |
| `mdl177_put_put_valmod` | MATRIX | Composite valuation module, an aggregated signal or score representing several valuation metrics for the stock |
| `mdl177_put_put_valmod_alt` | MATRIX | A composite or module aggregating various valuation-related factors for the stock |
| `mdl177_putput_capmod_alt` | MATRIX | Capital Strength Module |
| `mdl177_putput_cashburn_alt` | MATRIX | The rate at which a company is consuming cash or its cash resources, commonly used to assess financial health, especi… |
| `mdl177_putput_chgalpha_alt` | MATRIX | The rank-based measure of change in a stock's six-month alpha, where alpha refers to performance relative to a benchmark |
| `mdl177_putput_chgoll_alt` | MATRIX | Change in the company’s operating liability leverage, tracking shifts in the degree to which operating liabilities ar… |
| `mdl177_putput_chshrs_alt` | MATRIX | Percent change in the company’s shares outstanding, indicating share buybacks, issuance, or dilution over a specific … |
| `mdl177_putput_composite_alt` | MATRIX | A composite factor signal combining various small-cap related signals to produce an overall measure for small cap stocks |
| `mdl177_putput_dypeg_alt` | MATRIX | Reciprocal of Dividend Yield-adjusted PEG |
| `mdl177_putput_equality_alt` | MATRIX | A rank or score assessing the quality of a company’s earnings, possibly based on accruals, persistent profits, or oth… |
| `mdl177_putput_indepsp_alt` | MATRIX | Industry-relative ratio of core Earnings Per Share to Price, comparing a stock’s EPS/Price to its industry peers |
| `mdl177_putput_indestep_alt` | MATRIX | Industry-relative ratio of estimated four-quarter EPS to Price, benchmarking the stock’s forward earnings yield again… |
| `mdl177_putput_indfcfp_alt` | MATRIX | Industry-relative ratio of Free Cash Flow to Price, comparing a stock’s FCF/Price to that of its industry peers |
| `mdl177_putput_indroe_alt` | MATRIX | Industry-relative measure of Return on Equity, comparing the company’s ROE performance to its industry peers |
| `mdl177_putput_momod_alt` | MATRIX | A composite or module measuring momentum, likely combining several short or medium-term price performance or technica… |
| `mdl177_putput_opincev_alt` | MATRIX | Ratio of operating income to enterprise value, a valuation and efficiency metric showing operational profitability re… |
| `mdl177_putput_qualmod_alt` | MATRIX | Quality Module |
| `mdl177_putput_siratio_alt` | MATRIX | Short Interest Ratio, typically the proportion of shares sold short compared to shares outstanding or trading volume,… |
| `mdl177_putput_strevconf_alt` | MATRIX | A signal measuring the confidence or consensus level in analyst or Street earnings revisions, indicating expected rel… |
| `mdl177_putput_sucf_alt` | MATRIX | Standardized Unexpected Cash Flow |
| `mdl177_putput_totcov_alt` | MATRIX | Total Coverage |
| `mdl177_putput_valmod_alt` | MATRIX | Valuation Module |
| `mdl177_relativevaluemodel_capacq` | MATRIX | Capital Acquisition Ratio; trailing 12-month operating cash flow minus cash dividends, divided by total expenditures … |
| `mdl177_relativevaluemodel_fc_estep` | MATRIX | Leading 12-Month Median Earnings Yield; calculated as next fiscal year median consensus earnings estimate divided by … |
| `mdl177_relativevaluemodel_fmrelval` | MATRIX | Fielitz & Muller Relative Intrinsic Value |
| `mdl177_relativevaluemodel_roe` | MATRIX | Return on Equity; trailing 12-month income before extraordinary items divided by average common equity during the sam… |
| `mdl177_relativevaluemodel_rvm_composite` | MATRIX | Composite score from the Relative Value Model, aggregating multiple relative value factors |
| `mdl177_relativevaluemodel_ttmfcfp` | MATRIX | Trailing Twelve Month Free Cash Flow-to-Price; trailing 12-month free cash flow per share divided by month-end tradin… |
| `mdl177_surpriseanalystmodel_qsa_composite` | MATRIX | Overall composite rank from the Surprise Analyst Model integrating estimate trend, efficiency, and other signals |
| `mdl177_surpriseanalystmodel_qsa_efficiency` | MATRIX | Fundamentals Rank |
| `mdl177_surpriseanalystmodel_qsa_estexpect` | MATRIX | Rank indicating the recent direction of analysts' earnings estimate revisions for the stock (upward vs downward) |
| `mdl177_surpriseanalystmodel_qsa_percent` | MATRIX | Model-estimated probability (percent) that the company will deliver an earnings surprise versus analyst consensus |
| `mdl177_surpriseanalystmodel_qsa_surpsn` | MATRIX | Surprise Analyst Sector-Neutral Rank |
| `mdl177_v1_400_abr` | MATRIX | Abnormal return around quarterly earnings release; measures stock's excess return in the event-window of earnings rep… |
| `mdl177_v1_400_booklev` | MATRIX | Book Leverage: most recently reported quarterly total assets divided by book equity, indicating the leverage ratio us… |
| `mdl177_v1_400_capexast` | MATRIX | Capital expenditure-to-total assets: trailing 12-month capital expenditures divided by total assets from most recent … |
| `mdl177_v1_400_cashburnrate` | MATRIX | Cash burn rate: negative of (cash from operations plus cash from investments) divided by (cash plus short-term invest… |
| `mdl177_v1_400_curindbp_` | MATRIX | Industry relative book-to-market ratio: stock's book-to-price ratio minus industry average, deflated by standard devi… |
| `mdl177_v1_400_curindebitdap_` | MATRIX | Industry relative trailing 12-month EBITDA-to-price ratio: stock's EBITDA-to-price minus industry average, deflated b… |
| `mdl177_v1_400_curindep_` | MATRIX | Industry relative trailing 12-month EPS-to-price ratio: stock's EPS-to-price minus industry average, deflated by indu… |
| `mdl177_v1_400_curindfcfp_` | MATRIX | Industry relative trailing 12-month free cash flow-to-price ratio: stock's FCF-to-price minus industry average, defla… |
| `mdl177_v1_400_curindsp_` | MATRIX | Industry relative trailing 12-month sales-to-price ratio: stock's TTM sales-to-price minus industry average, deflated… |
| `mdl177_v1_400_fc_proformaep` | MATRIX | Trailing 12-month pro forma earnings divided by trading price; earnings-to-price ratio using pro forma (adjusted) ear… |
| `mdl177_v1_400_fy1epsskew` | MATRIX | Skewness of the distribution of analysts' leading 12-month earnings per share (EPS) estimates for a stock; measures a… |
| `mdl177_v1_400_indrelrecd_` | MATRIX | Industry-adjusted doubtful account receivables: asset-adjusted annual doubtful receivables minus industry mean, defla… |
| `mdl177_v1_400_indrelrtn4w_` | MATRIX | 4-week industry relative return: stock's 4-week return minus industry average, deflated by industry standard deviatio… |
| `mdl177_v1_400_indrelrtn5d_` | MATRIX | 5-day industry relative return: stock's return in last 5 days minus industry average, deflated by industry standard d… |
| `mdl177_v1_400_p50_200ratio` | MATRIX | Ratio of 50-day moving average price to 200-day moving average price; a measure of short-term vs long-term momentum |
| `mdl177_v1_400_pctchgqtrast` | MATRIX | Growth in total assets per share over the past year, comparing the latest reported quarterly total assets to those of… |
| `mdl177_v1_400_pcurlia` | MATRIX | Current liabilities per share divided by closing price; measures proportion of liabilities relative to market value p… |
| `mdl177_v1_400_pr_1536` | MATRIX | Ratio of 15-week moving average price to 36-week moving average price for a stock; momentum indicator over medium and… |
| `mdl177_v1_400_rdsale` | MATRIX | R&D intensity: average research and development expenses over trailing 12 months divided by total sales in the same p… |
| `mdl177_v1_400_reinrate` | MATRIX | Reinvestment rate: trailing 12-month earnings per share before extra items, less trailing 12-month dividends per shar… |
| `mdl177_v1_400_roic` | MATRIX | Return on Invested Capital: trailing 12-month net income and interest expense divided by average invested capital (co… |
| `mdl177_v1_400_sucf` | MATRIX | Standardized unexpected cash flow; unexpected component of cash flow, likely measured relative to expectations or his… |
| `mdl177_v1_400_sue` | MATRIX | Standardized unexpected earnings; measure of surprise in reported earnings relative to analyst forecasts, standardize… |
| `mdl177_v1_400_tobinq` | MATRIX | Tobin's Q: market value of equity plus debt divided by total assets; assesses whether market values firm's assets hig… |
| `mdl177_v1_400_ttmaccu` | MATRIX | Accounting accruals: trailing 12-month net income minus trailing 12-month operating cash flow, scaled by beginning to… |
| `mdl177_v1_400_ttmsaleev` | MATRIX | TTM sales-to-enterprise value: trailing 12-month sales divided by most recent enterprise value (EV: market value of e… |
| `mdl177_v1_400_uar` | MATRIX | Unexpected change in accounts receivable: actual change in accounts receivable minus expected (prior year's closing b… |
| `mdl177_v1_400_visiratio` | MATRIX | Visibility ratio: most recent daily trading volume divided by average daily trading volume over previous 50 days; mea… |
| `mdl177_v1_400_yoychgda` | MATRIX | Year-over-year change in leverage: difference between most recent quarterly total liabilities as a percentage of tota… |
| `mdl177_valanalystmodel_qva_alertrank` | MATRIX | Alert Rank |
| `mdl177_valanalystmodel_qva_balsht` | MATRIX | Rank of balance sheet strength (cash and equivalents relative to market capitalization) |
| `mdl177_valanalystmodel_qva_capexdep` | MATRIX | Capex to Depreciation Rank |
| `mdl177_valanalystmodel_qva_cashflow` | MATRIX | Rank of cash flow strength (free cash flow relative to market capitalization) |
| `mdl177_valanalystmodel_qva_chgacc` | MATRIX | Change in Net Op Working Capital Rank |
| `mdl177_valanalystmodel_qva_chgato` | MATRIX | Change in Asset Turnover Rank |
| `mdl177_valanalystmodel_qva_chginv` | MATRIX | Change in Inventory Rank |
| `mdl177_valanalystmodel_qva_composite` | MATRIX | Composite rank integrating multiple Value Analyst factors |
| `mdl177_valanalystmodel_qva_earnquality` | MATRIX | Rank of earnings quality or stability |
| `mdl177_valanalystmodel_qva_earnval` | MATRIX | Earnings Valuation Rank |
| `mdl177_valanalystmodel_qva_epmodule` | MATRIX | Earnings Cyclicality Rank |
| `mdl177_valanalystmodel_qva_finstmt` | MATRIX | Financial Statement Rank |
| `mdl177_valanalystmodel_qva_incstmt` | MATRIX | Income Stmt Rank |
| `mdl177_valanalystmodel_qva_invsentiment` | MATRIX | Investor Sentiment Rank |
| `mdl177_valanalystmodel_qva_mgtsignaling` | MATRIX | Management Signaling Rank |
| `mdl177_valanalystmodel_qva_pegy` | MATRIX | Rank based on PEGY metric (Price/Earnings/Growth/Yield) |
| `mdl177_valanalystmodel_qva_shortfall` | MATRIX | Rank related to earnings shortfalls (occurrence/size) |
| `mdl177_valanalystmodel_qva_valuation` | MATRIX | Valuation Rank |
| `mdl177_valanalystmodel_qva_yoychgdebt` | MATRIX | Rank based on year-over-year change in debt issuance |
| `mdl177_valanalystmodel_qva_yoychgshares` | MATRIX | Rank based on year-over-year change in shares outstanding |
| `mdl177_valueanalystmodel_qva_alertrank` | MATRIX | Alert Rank |
| `mdl177_valueanalystmodel_qva_alertrank_alt` | MATRIX | Alert Rank |
| `mdl177_valueanalystmodel_qva_balsht` | MATRIX | Rank of balance sheet strength, likely cash & equivalents to market cap |
| `mdl177_valueanalystmodel_qva_balsht_alt` | MATRIX | Rank of balance sheet strength, typically cash and equivalents to market capitalization |
| `mdl177_valueanalystmodel_qva_capexdep` | MATRIX | Rank of ratio of capital expenditures to depreciation for the stock |
| `mdl177_valueanalystmodel_qva_capexdep_alt` | MATRIX | Rank based on the ratio of capital expenditures to depreciation |
| `mdl177_valueanalystmodel_qva_cashflow` | MATRIX | Rank of free cash flow relative to market cap for the stock |
| `mdl177_valueanalystmodel_qva_cashflow_alt` | MATRIX | Rank based on free cash flow relative to market capitalization |
| `mdl177_valueanalystmodel_qva_chgacc` | MATRIX | Rank of change in net operating working capital for the stock |
| `mdl177_valueanalystmodel_qva_chgacc_alt` | MATRIX | Rank of change in net operating working capital for a stock compared to peers |
| `mdl177_valueanalystmodel_qva_chgato` | MATRIX | Rank of the change in asset turnover for a stock compared to peers |
| `mdl177_valueanalystmodel_qva_chgato_alt` | MATRIX | Rank of change in asset turnover, indicating shifts in efficiency of asset utilization |
| `mdl177_valueanalystmodel_qva_chginv` | MATRIX | Rank of change in inventory levels for the stock |
| `mdl177_valueanalystmodel_qva_chginv_alt` | MATRIX | Rank based on the change in inventory levels relative to other companies |
| `mdl177_valueanalystmodel_qva_composite` | MATRIX | Overall composite rank aggregating Value Analyst factors for the stock |
| `mdl177_valueanalystmodel_qva_composite_alt` | MATRIX | Overall composite rank summarizing multiple Value Analyst signals for a stock |
| `mdl177_valueanalystmodel_qva_earnquality` | MATRIX | Rank of the quality or sustainability of earnings |
| `mdl177_valueanalystmodel_qva_earnquality_alt` | MATRIX | Rank of earnings quality, reflecting the reliability and sustainability of reported earnings |
| `mdl177_valueanalystmodel_qva_earnval` | MATRIX | Rank of earnings valuation, likely earnings yield or related valuation metric |
| `mdl177_valueanalystmodel_qva_earnval_alt` | MATRIX | Rank based on earnings valuation metrics for the stock |
| `mdl177_valueanalystmodel_qva_epmodule` | MATRIX | Rank of earnings cyclicality measures for the stock |
| `mdl177_valueanalystmodel_qva_epmodule_alt` | MATRIX | Rank of cyclicality measures of a company’s earnings, indicating earnings stability or volatility |
| `mdl177_valueanalystmodel_qva_finstmt` | MATRIX | Rank based on composite assessment of financial statements |
| `mdl177_valueanalystmodel_qva_finstmt_alt` | MATRIX | Rank based on a composite of multiple financial statement metrics |
| `mdl177_valueanalystmodel_qva_incstmt` | MATRIX | Rank based on operating income to enterprise value from income statement |
| `mdl177_valueanalystmodel_qva_incstmt_alt` | MATRIX | Rank based on a key income statement metric (operating income to enterprise value) compared to other stocks |
| `mdl177_valueanalystmodel_qva_invsentiment` | MATRIX | Rank of investor sentiment related to the stock |
| `mdl177_valueanalystmodel_qva_invsentiment_alt` | MATRIX | Rank reflecting investor sentiment signals for the stock |
| `mdl177_valueanalystmodel_qva_mgtsignaling` | MATRIX | Rank of management signaling behaviors, such as insider buying/selling |
| `mdl177_valueanalystmodel_qva_mgtsignaling_alt` | MATRIX | Rank based on management signaling signals (e.g., insider trading, guidance changes) |
| `mdl177_valueanalystmodel_qva_pegy` | MATRIX | Rank based on PEGY (Price/Earnings to Growth & Yield), a valuation metric |
| `mdl177_valueanalystmodel_qva_pegy_alt` | MATRIX | Rank based on Price/Earnings to Growth and Yield, combining valuation, growth, and yield metrics |
| `mdl177_valueanalystmodel_qva_shortfall` | MATRIX | Rank of earnings shortfall compared to expectations or historical norms |
| `mdl177_valueanalystmodel_qva_shortfall_alt` | MATRIX | Rank reflecting the degree to which earnings fall short of expectations or guidance |
| `mdl177_valueanalystmodel_qva_valuation` | MATRIX | Rank of the stock's valuation metrics relative to the universe |
| `mdl177_valueanalystmodel_qva_valuation_alt` | MATRIX | Rank based on valuation metrics, such as book ratios and cash flow multiples |
| `mdl177_valueanalystmodel_qva_yoychgdebt` | MATRIX | Rank of year-over-year change in debt issuance for the stock |
| `mdl177_valueanalystmodel_qva_yoychgdebt_alt` | MATRIX | Rank of year-over-year change in debt issuance, showing how much new debt a company has taken on |
| `mdl177_valueanalystmodel_qva_yoychgshares` | MATRIX | Rank of year-over-year change in shares outstanding for the stock |
| `mdl177_valueanalystmodel_qva_yoychgshares_alt` | MATRIX | Rank based on year-over-year change in shares outstanding |
| `mdl177_valuemomemtummodel_earningsexpectationmodule` | MATRIX | Module capturing factors related to analyst or market expectations of future earnings, including consensus forecasts … |
| `mdl177_valuemomemtummodel_earningspricelinkmodule` | MATRIX | Earnings-Price Link Module |
| `mdl177_valuemomemtummodel_earningsqualitymodule` | MATRIX | Module assessing the quality or sustainability of reported earnings, examining accruals, cash flow alignment, and per… |
| `mdl177_valuemomemtummodel_earningsvaluationmodule` | MATRIX | Module comprising signals that measure valuation based on earnings, such as price-to-earnings or earnings yield ratios |
| `mdl177_valuemomemtummodel_financialstatementmodule` | MATRIX | Module containing factors or signals derived from financial statements such as balance sheet, income statement, and c… |
| `mdl177_valuemomemtummodel_investorsentimentmodule` | MATRIX | Module representing signals that capture investor sentiment, such as relative performance, short interest, analyst up… |
| `mdl177_valuemomemtummodel_managementsignalingmodule` | MATRIX | Module containing signals derived from management actions that may signal future prospects, such as insider trades, g… |
| `mdl177_valuemomemtummodel_pricemomentummodule` | MATRIX | Module focused on price momentum signals, reflecting trends or persistence in stock price movements over time |
| `mdl177_valuemomemtummodel_reportedearningsmomentummodule` | MATRIX | Module tracking the momentum (trend, change, acceleration) in reported earnings, focusing on recent earnings announce… |
| `mdl177_valuemomemtummodel_vm_compositesn` | MATRIX | Value Momentum Composite SN |
| `mdl177_valuemomemtummodel_vma_composite` | MATRIX | Primary composite score combining value and momentum modules/signals into a unified ranking for each stock |
| `mdl177_vra2_dvm_composite` | MATRIX | Composite score measuring deep value characteristics for US equities, aggregating multiple valuation-related signals … |
| `mdl177_vra2_qma_epsgrwth` | MATRIX | Ranking of earnings per share growth for US equities, representing the relative EPS growth signal among stocks in the… |
| `mdl177_vra_earningsqualitymodule` | MATRIX | A model-based, composite signal evaluating all aspects of a stock’s earnings quality, integrating various indicators … |
| `mdl177_vra_investorsentimentmodule` | MATRIX | Investor Sentiment Module |
| `mdl177_vra_managementsignalingmodule` | MATRIX | Management Signaling Module |
| `mdl177_vra_qma_epsgrwth` | MATRIX | A rank measure of a stock's earnings growth relative to peers, indicating how strong its earnings growth is compared … |
| `mdl177_vra_qsa_efficiency` | MATRIX | A quantitative ranking of a stock's fundamental efficiency, summarizing how well the company's financials reflect ope… |
| `mdl177_vra_qva_earnquality` | MATRIX | A composite rank of earnings quality using multiple metrics such as earnings shortfall and inventory changes, reflect… |
| `mdl177_vra_qva_valuation` | MATRIX | A rank summarizing valuation metrics (e.g., price/book, price/earnings) to indicate how attractive a stock's valuatio… |
| `mdl177_vra_surpriseforecastmodule` | MATRIX | Surprise Forecaster Module |
| `mdl77_2400_chg12msip` | MATRIX | 12-Month Change in Short Interest Position: It is defined as the 12-month relative change in short interest position … |
| `mdl77_2400_chg12mtotdebt` | MATRIX | 12-Month Change in Total Debt: It is defined as the 12-month relative change in total debt, where total debt is the s… |
| `mdl77_2400_chginvavgast` | MATRIX | Change in Inventory to Average Assets: It is defined as the 12-month change in the quarterly total inventories scaled… |
| `mdl77_2400_chgqtrepssurp` | MATRIX | Change in Real Earnings Surprise: It is defined as the change in quarterly earnings surprise (Actual EPS - Consensus … |
| `mdl77_2400_cpgspea2y` | MATRIX | 2-Year Ahead EPS Growth Percentage Change: It is defined as a stock's most recent consensus analysts earnings forecas… |
| `mdl77_2400_ctpmto` | MATRIX | The exponentially weighted put-to-call ratio for out-of-the-money options. |
| `mdl77_2400_earnshortfall` | MATRIX | Earnings Shortfall: It is defined as the difference between reported accounting earnings and free cash flow, scaled b… |
| `mdl77_2400_ga` | MATRIX | Aggregate Gamma: It is defined as the open interest weighted sum of the gamma for all options associated with a stock. |
| `mdl77_2400_impvol` | MATRIX | Implied Volatility: It is defined as the average implied volatility of the nearest-to-expiration at-the-money option … |
| `mdl77_2400_irttmsalesev` | MATRIX | Stock's trailing 12-month sales-to-enterprise (SEV) value less the average of the SEVs of all stocks in the same indu… |
| `mdl77_2400_md` | MATRIX | Distress Measure: It is defined as the financial distress model employed by Campbell, Hilscher, and Szilagyi (2008) a… |
| `mdl77_2400_pbroeresidual` | MATRIX | Price-to-Book Return-on-Equity Combination (PB-ROE): An adjustment to the classic price-to-book model incorporating f… |
| `mdl77_2400_rev3my1std` | MATRIX | The change in a stock's current analysts mean earnings estimate for fiscal year 1 less that of 3 months ago, scaled b… |
| `mdl77_2400_rev3my2std` | MATRIX | 3-M Revision in FY2 EPS Forecasts: Dispersion Relative: It is defined as the change in a stock's current analysts mea… |
| `mdl77_2400_rmi` | MATRIX | Volatility Spread: It is defined as the average implied volatility of the nearest-to-expiration at-the-money option c… |
| `mdl77_2400_vefcomtt` | MATRIX | TTM Operating Cash Flow-to-Enterprise Value: It is defined as the trailing 12-month operating cash flow per share for… |
| `mdl77_2400_yen` | MATRIX | Normalized Earnings Yield: It is defined as the average of three normalized earnings calculated by ROE, NPM, and EPS … |
| `mdl77_25rel5ycoreepsp` | MATRIX | 5-yr Relative TTM Core Earnings-to-Price: It is defined as a stock's current trailing 12-month core earnings-to-price… |
| `mdl77_25saleicap` | MATRIX | The trailing 12-month total revenues divided by the average of the invested capital in the same period. |
| `mdl77_25yearrelativevaluefactor_rel5ybp` | MATRIX | 5-yr Relative Book-to-Market: It is defined as a stock's current book-to-market ratio (BP) minus the average of the B… |
| `mdl77_25yearrelativevaluefactor_rel5ycfp` | MATRIX | 5-yr Relative TTM Cash Flow-to-Price: It is defined as a stock's current trailing 12-month cash flow-to-price ratio (… |
| `mdl77_25yearrelativevaluefactor_rel5ydivp` | MATRIX | 5-yr Relative TTM Dividend Yield: It is defined as a stock's current dividend yield (DivYield) minus the average of t… |
| `mdl77_25yearrelativevaluefactor_rel5yebitdap` | MATRIX | 5-yr Relative TTM EBITDA-to-Price: It is defined as a stock's current trailing 12-month EBITDA per share-to-price rat… |
| `mdl77_25yearrelativevaluefactor_rel5yep` | MATRIX | 5-yr Relative TTM Earnings-to-Price: It is defined as a stock's current trailing 12-month earnings per share before e… |
| `mdl77_25yearrelativevaluefactor_rel5yfcfp` | MATRIX | 5-yr Relative TTM Free Cash Flow-to-Price: It is defined as a stock's current trailing 12-month free cash flow-to-pri… |
| `mdl77_25yearrelativevaluefactor_rel5yocfp` | MATRIX | 5-yr Relative TTM Oper Cash Flow-to-Price: It is defined as a stock's current trailing 12-month operating cash flow-t… |
| `mdl77_25yearrelativevaluefactor_rel5ysp` | MATRIX | 5-Yr Relative TTM Sales-to-Price: It is defined as a stock's current trailing 12-month sales-to-price ratio (SP) minu… |
| `mdl77_2_dvm_composite` | MATRIX | Score based on a strategy that selects for stocks in a universe of stocks by comparing different financial metrics as… |
| `mdl77_2_htwrgspe_amq` | MATRIX | Earnings Growth Rank: It is defined as the one-quarter change in a stock's trailing twelve-month earnings per share, … |
| `mdl77_2ad` | MATRIX | Total Debt to Total Assets: It is defined as the most recently reported total debt divided by total assets. |
| `mdl77_2adverint` | MATRIX | Advertising Intensity: It is defined as a stock's advertising expense in the last fiscal year divided by last fiscal … |
| `mdl77_2am_amv` | MATRIX | Momentum Analyst II: This model is composed of 40% Price Momentum, 30% Fundamental Growth, 20% Reported Earnings Mome… |
| `mdl77_2amv` | MATRIX | Score based on the equal-weighted average of the Momentum Analyst and Value Analyst ranks |
| `mdl77_2av_amv` | MATRIX | Value Analyst II: This model is composed of 30% Financial Statement Valuation, 30% Earnings Quality, 20% Earnings Val… |
| `mdl77_2capacq` | MATRIX | Capital Acquisition Ratio: It is defined as the trailing 12-month operating cash flow less the trailing 12-month cash… |
| `mdl77_2capdistp` | MATRIX | The sum of trailing 1-year dividends for every share and the estimated trailing 1-year stock issued for each share, w… |
| `mdl77_2ccacw` | MATRIX | Working Capital Accruals: It equals to: Increase in Accounts Receivables + Increase in Inventory + Decrease in Accoun… |
| `mdl77_2chgreccast` | MATRIX | YOY Chg in Acct Receivable to Current Assets: It is defined as the percent change in the most recent quarterly report… |
| `mdl77_2cusip_sedol` | MATRIX | Unix modification time of raw file |
| `mdl77_2deepvaluefactor_apemtt` | MATRIX | An indicator that standardizes and compares relative share price between time periods and among companies. |
| `mdl77_2deepvaluefactor_bpemtt` | MATRIX | The company's performance in trailing 1-year before taking into account non-recurring gain or loss. Stock divided by … |
| `mdl77_2deepvaluefactor_cashp` | MATRIX | Cash-to-Price: It is defined as the most recently reported cash and equivalents per share of a company divided by tra… |
| `mdl77_2deepvaluefactor_cashsev` | MATRIX | Cash to Enterprise Value: It is defined as the total cash & equivalents divided by the sum of the market value of com… |
| `mdl77_2deepvaluefactor_coreepsp` | MATRIX | TTM Core Earnings-to-Price: It is defined as the trailing 12-month earnings per share from operations for a stock def… |
| `mdl77_2deepvaluefactor_curep` | MATRIX | Current Earnings Yield: It is defined as the sum of the most recently reported 3 quarters EPS and analysts' consensus… |
| `mdl77_2deepvaluefactor_divyield` | MATRIX | TTM Dividend Yield: It is defined as the trailing 12-month dividends per share for a stock divided by its month-end t… |
| `mdl77_2deepvaluefactor_ebitdaev` | MATRIX | TTM EBITDA-to-Enterprise Value: It is defined as the trailing 12-month earnings before interest, taxes, depreciation,… |
| `mdl77_2deepvaluefactor_ebitdap` | MATRIX | TTM EBITDA-to-Price: It is defined as the trailing 12-month earnings before interest, taxes, depreciation and amortiz… |
| `mdl77_2deepvaluefactor_ebop` | MATRIX | Edwards-Bell-Ohlson Value-to-Price: It is defined as a stock's valuation based on the Edwards-Bell-Ohlson (EBO) model… |
| `mdl77_2deepvaluefactor_estep` | MATRIX | Leading 12-Month Median Earnings Yield: It is defined as the next fiscal year median consensus earnings estimate divi… |
| `mdl77_2deepvaluefactor_indidivy` | MATRIX | Indicated Dividend Yield: It is defined as the last quarterly dividend declared multiplied by 4, scaled by month-end … |
| `mdl77_2deepvaluefactor_lumqca` | MATRIX | Acquisition Multiple: It is defined as the most recent quarterly reported invested capital divided by the trailing 12… |
| `mdl77_2deepvaluefactor_nnastp` | MATRIX | Net Current Assets-to-Price: It is defined as the current assets per share minus total liabilities per share divided … |
| `mdl77_2deepvaluefactor_past` | MATRIX | Price-to-Total Assets: It is defined as a stock's month-end trading price divided by the most recent quarterly report… |
| `mdl77_2deepvaluefactor_pb` | MATRIX | Book-to-Market: It is defined as the most recently reported book value per share for a stock deflated by its month-en… |
| `mdl77_2deepvaluefactor_pedwf` | MATRIX | Leading 12-Month Mean Earnings Yield: It is defined as the next 4-quarter's mean consensus earnings estimate divided … |
| `mdl77_2deepvaluefactor_pfcf` | MATRIX | Forward Free Cash Flow-to-Price: It is defined as the next 4-quarter's mean consensus earnings estimate plus trailing… |
| `mdl77_2deepvaluefactor_pfcfmtt` | MATRIX | TTM Free Cash Flow-to-Price: It is defined as the trailing 12-month free cash flow per share for a stock divided by i… |
| `mdl77_2deepvaluefactor_pfcmtt` | MATRIX | TTM Cash Flow-to-Price: It is defined as the trailing 12-month cash flows per share for a stock scaled by its trading… |
| `mdl77_2deepvaluefactor_pfcomtt` | MATRIX | TTM Operating Cash Flow-to-Price: It is defined as the trailing 12-month operating cash flow per share for a stock di… |
| `mdl77_2deepvaluefactor_pfgmtt` | MATRIX | TTM Growth Flow-to-Price: It is defined as the sum of trailing 12-month growth flow value per share for a stock divid… |
| `mdl77_2deepvaluefactor_pqipmtt` | MATRIX | The most recent trailing 12-month operating and nonoperating income per share before provisions for income taxes and … |
| `mdl77_2deepvaluefactor_proformaep` | MATRIX | TTM Pro Forma Earnings-to-Price: It is defined as the trailing 12-month earnings scaled by the trading price. |
| `mdl77_2deepvaluefactor_psmtt` | MATRIX | TTM Sales-to-Price: It is defined as the most recently reported trailing 12-month sales per share for a stock deflate… |
| `mdl77_2deepvaluefactor_pvan` | MATRIX | Net Asset Value to Price: It is defined as the most recent book value of net assets per share (NAV) by the closing pr… |
| `mdl77_2deepvaluefactor_ttmcapexp` | MATRIX | TTM Capital Expenditures-to-Price: It is defined as the trailing 12-month capital expenditures per share for a stock … |
| `mdl77_2deepvaluefactor_ttmsaleev` | MATRIX | TTM Sales-to-Enterprise Value: It is defined as the trailing 12-month sales for a stock divided by the most recent en… |
| `mdl77_2deepvaluefactor_vefcfmtt` | MATRIX | TTM Free Cash Flow-to-Enterprise Value: It is defined as the trailing 12-month free cash flow (FCF) for a stock scale… |
| `mdl77_2deepvaluefactor_vesspem21f` | MATRIX | Forward 12-M EPS-to-Enterprise Value: It is defined as the consensus forward 12-month earnings per share forecast div… |
| `mdl77_2deepvaluefactor_ydp` | MATRIX | Predicted Dividend Yield: It is defined as an assumed payout ratio multiplied by the next 4-quarter consensus earning… |
| `mdl77_2deepvaluemodel_chgshare` | MATRIX | Percent Change in Shares Outstanding: It is defined as the percent change in a company's current number of outstandin… |
| `mdl77_2deepvaluemodel_indidivy` | MATRIX | Indicated Dividend Yield: It is defined as the last quarterly dividend declared multiplied by 4, scaled by month-end … |
| `mdl77_2deepvaluemodel_vefcfmtt` | MATRIX | TTM Free Cash Flow-to-Enterprise Value: It is defined as the trailing 12-month free cash flow (FCF) for a stock scale… |
| `mdl77_2dv_currroe` | MATRIX | Current Return On Equity |
| `mdl77_2dv_yoychgat` | MATRIX | YOY Chg in Asset Turnover: Year-over-year Change in Asset Turnover |
| `mdl77_2dvm_composite` | MATRIX | Deep Value Composite: Deep Value Composite Score |
| `mdl77_2earningmomentumfactor400_dypeg` | MATRIX | Reciprocal of Dividend Yield-adjusted PEG: It is defined as the reciprocal of a stock's forward 12-month P/E ratio di… |
| `mdl77_2earningmomentumfactor400_fcfroey1p` | MATRIX | Product of TTM FCF Yield and Forward ROE: It is defined as the trailing 12-month free cash flow per share multiplied … |
| `mdl77_2earningmomentumfactor400_fcus` | MATRIX | Standardized Unexpected Cash Flow: It is defined as the most recent quarterly operating cash flow minus that of 4 qua… |
| `mdl77_2earningmomentumfactor400_fqsurstd` | MATRIX | Most Recent Earnings Surprise: It is defined as the most recent quarterly earnings surprise (actual fiscal quarter EP… |
| `mdl77_2earningmomentumfactor400_fy1epsskew` | MATRIX | The skewness of the distribution of a series of leading 12-month earnings consensus estimates. |
| `mdl77_2earningmomentumfactor400_gspea1q` | MATRIX | 1-Quarter Ahead EPS Growth: It is defined as a stock's most recent fiscal quarter consensus earnings forecast less th… |
| `mdl77_2earningmomentumfactor400_gspea1y` | MATRIX | 1-Year Ahead EPS Growth: It is defined as the most recent consensus earnings forecast for the next 4-quarters minus t… |
| `mdl77_2earningmomentumfactor400_gspea2y` | MATRIX | 2-Year Ahead EPS Growth: It is defined as the most recent consensus earnings forecast for fiscal year 2 minus the con… |
| `mdl77_2earningmomentumfactor400_gtl` | MATRIX | Long-Term Growth Rate Estimates: It is defined as the consensus long-term growth forecast. It generally represents an… |
| `mdl77_2earningmomentumfactor400_gtlm6ghc` | MATRIX | 6-M Change in Long-term Growth Estimates: It is defined as the percent change in the most recent mean consensus long-… |
| `mdl77_2earningmomentumfactor400_lagegp` | MATRIX | Lagged Inverse of PEG Ratio: It is defined as the trailing 12-month earnings per share before extraordinary items tim… |
| `mdl77_2earningmomentumfactor400_mrspe` | MATRIX | Street Revision Magnitude: It is defined as the 3-month change in the median FY1 consensus earnings forecast, scaled … |
| `mdl77_2earningmomentumfactor400_numrevq1` | MATRIX | Net Number ofRevisions for Fiscal QTR 1: It is defined as the number of fiscal quarter 1 upward earnings forecast rev… |
| `mdl77_2earningmomentumfactor400_numrevy1` | MATRIX | Net Number ofRevisions for Fiscal Year 1: It is defined as the weighted average of the number of FY1 analyst earnings… |
| `mdl77_2earningmomentumfactor400_pelh` | MATRIX | Street Revision Confidence: It is defined as the sum of the 3-month change in the highest and lowest FY1 earnings est… |
| `mdl77_2earningmomentumfactor400_perg` | MATRIX | Risk-adjusted PEG Ratio: It is defined as the stock price divided by the leading 12-month consensus earnings forecast… |
| `mdl77_2earningmomentumfactor400_pge` | MATRIX | Estimates on the next 1-year average earnings scaled by company's prospects on growth and its stock price. |
| `mdl77_2earningmomentumfactor400_qepsferr` | MATRIX | Prior Fiscal Quarter Forecast Error: It is defined as the difference between the actual earnings per share and consen… |
| `mdl77_2earningmomentumfactor400_ratrev6m` | MATRIX | Street Rating Revision: It is defined as the 6-month average of the change in the average analyst recommendation trac… |
| `mdl77_2earningmomentumfactor400_rev1q1` | MATRIX | Revision in Fiscal QTR 1 EPS Forecasts: It is defined as the change in the current consensus earnings forecast for fi… |
| `mdl77_2earningmomentumfactor400_rev3y1` | MATRIX | The change in the analysts' projection on company's performance for fiscal year 1 less that of 3 months ago, deflated… |
| `mdl77_2earningmomentumfactor400_rev3y2` | MATRIX | 3-M Revision in FY2 EPS Forecasts: It is defined as the change in the current mean consensus earnings estimate for fi… |
| `mdl77_2earningmomentumfactor400_rev6` | MATRIX | Averaged Last 6-M EPS Revisions for FY1: It is defined as the average of prior 6-month monthly changes in a stock's c… |
| `mdl77_2earningmomentumfactor400_salesurp` | MATRIX | Sales Surprise: It is defined as the most recent reported quarterly sales minus consensus sales forecasts, divided by… |
| `mdl77_2earningmomentumfactor400_spe1yfvc` | MATRIX | FY1 EPS Estimates Dispersion: It is defined as the standard deviation of analyst earnings estimates for fiscal year 1… |
| `mdl77_2earningmomentumfactor400_spe2yfvc` | MATRIX | FY2 EPS Forecast Dispersion: It is defined as the standard deviation of analyst earnings estimates for fiscal year 2 … |
| `mdl77_2earningmomentumfactor400_stdevfy1epsp` | MATRIX | Std Dev of FY1 EPS Estimates-to-Price: It is defined as the standard deviation of analyst forecasts for fiscal year 1… |
| `mdl77_2earningmomentumfactor400_stdevfy2epsp` | MATRIX | Std Dev of FY2 EPS Estimates-to-Price: It is defined as the standard deviation of analyst forecasts for fiscal year 2… |
| `mdl77_2earningmomentumfactor400_stockrating` | MATRIX | Street Consensus Rating: It is defined as the consensus recommendation for a company. |
| `mdl77_2earningmomentumfactor400_sue` | MATRIX | Standardized Unexpected Earnings: It is defined as the most recent quarterly earnings per share minus that of 4 quart… |
| `mdl77_2earningmomentumfactor400_surp` | MATRIX | Real Earnings Surprise: It is defined as the difference between the actual earnings per share and consensus forecasts… |
| `mdl77_2earningmomentumfactor400_y2repsg` | MATRIX | 2-Year Projected EPS Growth: It is defined as the most recent consensus earnings forecast for fiscal year 2 minus the… |
| `mdl77_2earningmomentumfactor400_y3sur` | MATRIX | Volatility-adj 3-yr Projected EPS Growth: It is defined as the consensus earnings forecast for the current quarter mi… |
| `mdl77_2earningsmomemtummodel_emm_composite` | MATRIX | Model composition based on earnings momentum |
| `mdl77_2earningsmomemtummodel_fc_fcfroey1p` | MATRIX | Product of TTM FCF Yield and Forward ROE: It is defined as the trailing 12-month free cash flow per share multiplied … |
| `mdl77_2earningsmomemtummodel_fc_fqsurstd` | MATRIX | Most Recent Quarterly Earnings Surprise: It is defined as a stock's most recent quarterly earnings surprise (actual f… |
| `mdl77_2earningsmomemtummodel_fc_numrevy1` | MATRIX | Net Number ofRevisions for Fiscal Year 1: It is defined as the weighted average of the number of FY1 analyst earnings… |
| `mdl77_2earningsmomemtummodel_fc_rev3y2` | MATRIX | 3-M Revision in FY2 EPS Forecasts: It is defined as the change in a stock's current analysts mean earnings estimate f… |
| `mdl77_2earningsmomemtummodel_fc_y2repsg` | MATRIX | 2-Year Projected EPS Growth: It is defined as a stock's most recent consensus analysts earnings forecast for fiscal y… |
| `mdl77_2earningsmomemtummodel_gtl` | MATRIX | Long-Term Growth Rate Estimates: It is defined as the consensus long-term growth forecast. It generally represents an… |
| `mdl77_2earningsmomemtummodel_pge_cf` | MATRIX | Estimates on the next 1-year average earnings scaled by company's prospects on growth and its stock price. |
| `mdl77_2earningsmomemtummodel_spe2yfvc_cf` | MATRIX | FY2 EPS Forecast Dispersion: It is defined as the standard deviation of analyst earnings estimates for fiscal year 2 … |
| `mdl77_2earningsqualityfactor_ccacw` | MATRIX | Working Capital Accruals: It equals to: Increase in Accounts Receivables + Increase in Inventory + Decrease in Accoun… |
| `mdl77_2earningsqualityfactor_chgsgasale` | MATRIX | Change in QTR SG&A Expenses vs Sales: It is defined as the difference between the yearly change in quarterly Selling,… |
| `mdl77_2earningsqualityfactor_chgshare` | MATRIX | Percent Change in Shares Outstanding: It is defined as the percent change in a company's current number of outstandin… |
| `mdl77_2earningsqualityfactor_cogsinvt` | MATRIX | Change in TTM COGS vs Inventory Level: It is defined as the absolute value of the difference between the yearly perce… |
| `mdl77_2earningsqualityfactor_cre` | MATRIX | Earnings Response Coefficient: It is defined as the slope coefficient between market-adjusted returns around the time… |
| `mdl77_2earningsqualityfactor_dpcapex` | MATRIX | Change in TTM Depreciation vs CapEx: It is defined as the absolute value of the difference between the yearly percent… |
| `mdl77_2earningsqualityfactor_epschgetr` | MATRIX | EPS from Change in Effective Tax Rate: It is defined as the trailing 12-month pre-tax income per share times the diff… |
| `mdl77_2earningsqualityfactor_indrelrecd_` | MATRIX | Industry-adjusted Doubtful Account Receivables: It is defined as a stock's asset-adjusted annual doubtful receivables… |
| `mdl77_2earningsqualityfactor_lccau` | MATRIX | Unexpected Change in Accrued Liabilities: It is defined as the difference between the most recent fiscal year's accru… |
| `mdl77_2earningsqualityfactor_opincltd` | MATRIX | Change in TTM Oper Income vs LT Debt: It is defined as the difference between the yearly percent change in operating … |
| `mdl77_2earningsqualityfactor_pau` | MATRIX | Unexpected Change in Accounts Payable: It is defined as the difference between current accounts payable and the expec… |
| `mdl77_2earningsqualityfactor_pedu` | MATRIX | Unexpected Change in Depreciation: It is defined as the difference between the trailing 12-month depreciation expense… |
| `mdl77_2earningsqualityfactor_rau` | MATRIX | Unexpected Change in Accounts Receivable: It is defined as the difference between current accounts receivable and the… |
| `mdl77_2earningsqualityfactor_saleeps` | MATRIX | Change in TTM Sales vs. EPS: It is defined as the absolute value of the difference between the yearly percent change … |
| `mdl77_2earningsqualityfactor_salegpm` | MATRIX | Change in QTR Sales vs Gross Margin: It is defined as the difference between the yearly change in most recent reporte… |
| `mdl77_2earningsqualityfactor_salerec` | MATRIX | Change in TTM Sales vs Accounts Receivable: It is defined as the difference between the yearly percent change in trai… |
| `mdl77_2earningsqualityfactor_spefcn` | MATRIX | Change in TTM EPS vs Oper Cash Flows: It is defined as the absolute value of the difference between the yearly percen… |
| `mdl77_2earningsqualityfactor_ttmaccu` | MATRIX | Accounting Accruals: It is defined as the difference between the trailing 12-month net income and the trailing 12-mon… |
| `mdl77_2earningsqualityfactor_vniu` | MATRIX | The difference of inventory between present and expected levels. |
| `mdl77_2earningsqualityfactor_yoychgaa` | MATRIX | Change in Accruals to Assets: It is defined as the trailing 12-month income before extra items less the trailing 12-m… |
| `mdl77_2ee_am_amv` | MATRIX | The equal-weighted average of the Monthly Net Number of forward earnings yield (1) Estimate Revisions and 3-Month Rev… |
| `mdl77_2exdisspi` | MATRIX | 24-Month Unusual Items to Sales: It is defined as the sum of the absolute value of extraordinary items, discontinued … |
| `mdl77_2fc_curindfwdep_` | MATRIX | Industry Relative Leading 4-QTRs EPS to Price: It is defined as a stock's next 4-quarter's analysts consensus earning… |
| `mdl77_2fc_dypeg` | MATRIX | Reciprocal of Dividend Yield-adjusted PEG: It is defined as the reciprocal of a stock's forward 12-month P/E ratio di… |
| `mdl77_2fc_ebop` | MATRIX | Stock's valuation based on a model deflated by its month-end trading price. The model measures a firm's intrinsic val… |
| `mdl77_2fc_fwdroe` | MATRIX | Forward Return on Equity: It is defined as a stock's analysts earnings estimates for next four quarters divided by it… |
| `mdl77_2fc_numest` | MATRIX | The number of analysts' earnings estimates for fiscal year 1 for a stock. |
| `mdl77_2fc_rel5yfwdep` | MATRIX | 5-yr Relative Leading 12-Month Earnings Yield: It is defined as a stock's current next 4-quarter's consensus analyst … |
| `mdl77_2fc_rev3y1` | MATRIX | The change in the analysts' projection on company's performance for fiscal year 1 less that of 3 months ago, deflated… |
| `mdl77_2fc_rev3y2` | MATRIX | 3-M Revision in FY2 EPS Forecasts: It is defined as the change in the current mean consensus earnings estimate for fi… |
| `mdl77_2fc_rev6` | MATRIX | Averaged Last 6-M EPS Revisions for FY1: It is defined as the average of prior 6-month monthly changes in a stock's c… |
| `mdl77_2fc_stdevfy1epsp` | MATRIX | Std Dev of FY1 EPS Estimates-to-Price: It is defined as the standard deviation of analyst forecasts for fiscal year 1… |
| `mdl77_2fc_stdevfy2epsp` | MATRIX | Std Dev of FY2 EPS Estimates-to-Price: It is defined as the standard deviation of analyst forecasts for fiscal year 2… |
| `mdl77_2fwdroe` | MATRIX | Forward Return on Equity: It is defined as a stock's analysts earnings estimates for the next 4 quarters divided by i… |
| `mdl77_2garpanalystmodel_qgp_alert` | MATRIX | Alert Rank: Alert Rank |
| `mdl77_2garpanalystmodel_qgp_avgrating` | MATRIX | Avg Analyst Rating: Avg Analyst Rating |
| `mdl77_2garpanalystmodel_qgp_capeff` | MATRIX | Capital Effectiveness: Capital Effectiveness |
| `mdl77_2garpanalystmodel_qgp_chgvaluation` | MATRIX | 3M Chg in Valuation: 3M Chg in Valuation |
| `mdl77_2garpanalystmodel_qgp_composite` | MATRIX | Analyst score based on growth and value investing attributes |
| `mdl77_2garpanalystmodel_qgp_growthval` | MATRIX | Growth Valuation: Growth Valuation |
| `mdl77_2garpanalystmodel_qgp_relgrowth` | MATRIX | Relative Growth Rank: Relative Growth Rank |
| `mdl77_2garpanalystmodel_qgp_relpegy` | MATRIX | Rolling Relative PEGY: Rolling Relative PEGY |
| `mdl77_2garpanalystmodel_qgp_roefcf` | MATRIX | ROE x FCF Rank: ROE x FCF Rank |
| `mdl77_2garpanalystmodel_qgp_valuation` | MATRIX | Valuation Rank: Valuation Rank |
| `mdl77_2garpanalystmodel_qgp_vfpriceratio` | MATRIX | Value to Price Rank: Value to Price Rank |
| `mdl77_2garpanalystmodel_qgp_wratingchg` | MATRIX | Weighted Ratings Change |
| `mdl77_2gdna_6351_rp` | MATRIX | 15/36 Week Stock Price Ratio: It is defined as the moving average of a stock's prices in the last 15 weeks divided by… |
| `mdl77_2gdna_actrtn12m` | MATRIX | 12-Month Active Return with 1-Month Lag: It is defined as the percent change in price for a stock from month t-13 to … |
| `mdl77_2gdna_actrtn18m` | MATRIX | 18-Month Active Return with 1-Month Lag: It is defined as the percent change in price for a stock from month t-19 to … |
| `mdl77_2gdna_actrtn1m` | MATRIX | 1-Month Active Return: It is defined as the percent change in price for a stock from month t-1 to month t. |
| `mdl77_2gdna_actrtn24m` | MATRIX | 24-Month Active Return with 1-Month Lag: It is defined as the percent change in price for a stock from month t-25 to … |
| `mdl77_2gdna_actrtn2m` | MATRIX | 2-Month Active Return: It is defined as the percent change in price for a stock from month t-2 to month t. |
| `mdl77_2gdna_actrtn36m` | MATRIX | 36-Month Active Return with 1-Month Lag: It is defined as the percent change in price for a stock from month t-37 to … |
| `mdl77_2gdna_actrtn3m` | MATRIX | 3-Month Active Return: It is defined as the percent change in price for a stock from month t-3 to month t. |
| `mdl77_2gdna_actrtn60m` | MATRIX | 60-Month Active Return with 1-Month Lag: It is defined as the percent change in price for a stock from month t-61 to … |
| `mdl77_2gdna_actrtn6m` | MATRIX | 6-Month Active Return with 1-Month Lag: It is defined as the percent change in price for a stock from month t-7 to mo… |
| `mdl77_2gdna_actrtn9m` | MATRIX | 9-Month Active Return with 1-Month Lag: It is defined as a stock's price percent change from month t-10 to month t-1. |
| `mdl77_2gdna_ags` | MATRIX | SG&A Expenses-to-Sales: It is defined as the trailing 12-month selling, general management, and administration expens… |
| `mdl77_2gdna_alpha60m` | MATRIX | 60-Month Alpha: It is defined as the intercept of the regression line which best fits a stock's monthly price return … |
| `mdl77_2gdna_aoer` | MATRIX | Retained Earnings-to-Total Assets: It is defined as the reported cumulative retained earnings from the most recent qu… |
| `mdl77_2gdna_aor` | MATRIX | Return on Assets: It is defined as the trailing 12-month income before extra items divided by the average of total as… |
| `mdl77_2gdna_apemtt` | MATRIX | An indicator that standardizes and compares relative share price between time periods and among companies. |
| `mdl77_2gdna_aspanratio` | MATRIX | Stock's quarterly operating assets minus its operating liabilities deflated by the lagged total assets. |
| `mdl77_2gdna_astcomp` | MATRIX | Asset Composition: It is defined as the total current assets from the most recent quarter divided by the total assets… |
| `mdl77_2gdna_astto` | MATRIX | Assets Turnover Ratio: It is defined as the trailing 12-month sales divided by the most recently reported quarterly a… |
| `mdl77_2gdna_beta` | MATRIX | 60-Month Beta: It is defined as 0.67 times the 60-month beta plus 0.33. Beta is the covariance between a stock's mont… |
| `mdl77_2gdna_betasigma` | MATRIX | Product of Beta and Sigma: It is defined as the product of the adjusted 60-month Beta and 60-month Sigma (standard de… |
| `mdl77_2gdna_bmpo` | MATRIX | Operating Profit Margin: It is defined as the most recently reported quarterly operating income divided by the corres… |
| `mdl77_2gdna_booklev` | MATRIX | Book Leverage: It is defined as the most recently reported quarterly total assets divided by the book equity. |
| `mdl77_2gdna_bpemtt` | MATRIX | The company's performance in trailing 1-year before taking into account non-recurring gain or loss, divided by its mo… |
| `mdl77_2gdna_capacq` | MATRIX | Capital Acquisition Ratio: It is defined as the trailing 12-month operating cash flow less the trailing 12-month cash… |
| `mdl77_2gdna_capexast` | MATRIX | Capital Expenditure-to-Total Assets: It is defined as trailing 12-month capital expenditures divided by the total ass… |
| `mdl77_2gdna_capexsale` | MATRIX | TTM Capital Expenditures-to-Sales: It is defined as trailing 12-month capital expenditures divided by trailing 12-mon… |
| `mdl77_2gdna_cashburnrate` | MATRIX | Cash Burn Rate: It is defined as: -(Cash From Operations + Cash from Investments)/(Cash + Short-term Investments). |
| `mdl77_2gdna_cashc` | MATRIX | Cash Cycle: It is defined as the average inventory days plus the average collection days minus the average payable days. |
| `mdl77_2gdna_cashp` | MATRIX | Cash-to-Price: It is defined as the most recently reported cash and equivalents per share of a company divided by tra… |
| `mdl77_2gdna_cashratio` | MATRIX | Cash & Equivalents-to-Current Liabilities: It is defined as the most recently reported quarterly cash & equivalents d… |
| `mdl77_2gdna_cashsale` | MATRIX | The mean value of company's assets in the trailing 1-year divided by the trailing 1-year revenues. |
| `mdl77_2gdna_cashsev` | MATRIX | Cash to Enterprise Value: It is defined as the total cash & equivalents divided by the sum of the market value of com… |
| `mdl77_2gdna_cfita` | MATRIX | TTM Cash Flow from Investment to Total Assets: It is defined as the trailing 12-month cash flow from the investing po… |
| `mdl77_2gdna_cfleverage` | MATRIX | Cash Flow Leverage: It is defined as the total liabilities divided by the trailing 12-month operating cash flow. |
| `mdl77_2gdna_cfroi` | MATRIX | Cash Flow Return on Invested Capital: It is defined as the trailing 12-month cash flow divided by the average investe… |
| `mdl77_2gdna_cg3ysales` | MATRIX | The geometric growth rate of the trailing 12-month sales per share in the last 12 quarters. |
| `mdl77_2gdna_chg3ycfast` | MATRIX | 3-yr Change in Assets-adj TTM Cash Flow: It is defined as the most recently reported trailing 12-month operating cash… |
| `mdl77_2gdna_chg3yepsast` | MATRIX | 3-yr Change in Assets-adj TTM EPS: It is defined as the trailing 12-month earnings per share before extra items (EPS)… |
| `mdl77_2gdna_chg3yepsp` | MATRIX | The difference between the trailing 12-month earnings per share and that of 12 quarters ago for a stock divided by it… |
| `mdl77_2gdna_chg3yfcfast` | MATRIX | 3-yr Chg in Assets-adj TTM Free Cash Flow: It is defined as the trailing 12-month free cash flow minus 12 quarters ag… |
| `mdl77_2gdna_chg3yocfast` | MATRIX | 3-Yr Change in Assets-Adj TTM Oper Cash Flow: It is defined as the most recently reported trailing 12-month operating… |
| `mdl77_2gdna_chg6malpha18m` | MATRIX | 6-Month Nominal Change in 18-Month Alpha: It is defined as the 6-month change in a stock's 18-month alpha, which equa… |
| `mdl77_2gdna_chgalpha12m` | MATRIX | 6-Month Nominal Change in 12-Month Alpha: It is defined as the 6-month change in a stock's 12-month alpha, which equa… |
| `mdl77_2gdna_chgalpha36m` | MATRIX | 6-Month Nominal Change in 36-Month Alpha: It is defined as the 6-month change in a stock's 36-month alpha, which equa… |
| `mdl77_2gdna_chgars` | MATRIX | 1-yr Chg in Acct Receivable as Percentage ofSales: It is defined as the change between the last reported accounts rec… |
| `mdl77_2gdna_chgnoa` | MATRIX | Change in Net Operating Assets: It is defined as the year-over-year change of net operating assets to total assets, w… |
| `mdl77_2gdna_chgollev` | MATRIX | Change in Operating Liability Leverage: It is defined as the current quarter operating liability leverage less the op… |
| `mdl77_2gdna_chgsgasale` | MATRIX | Change in QTR SG&A Expenses vs Sales: It is defined as the difference between the yearly change in quarterly Selling,… |
| `mdl77_2gdna_chgshare` | MATRIX | Percent Change in Shares Outstanding: It is defined as the percent change in a company's current number of outstandin… |
| `mdl77_2gdna_chgvolpre4y` | MATRIX | 4-Year Change in the Average Trading Volume: It is defined as the change in the most recent 6-month moving average of… |
| `mdl77_2gdna_cogsinvt` | MATRIX | Change in TTM COGS vs Inventory Level: It is defined as the absolute value of the difference between the yearly perce… |
| `mdl77_2gdna_covol` | MATRIX | 60-Month Trading Volume Trend: It is defined as the slope of the least squares regression line of the last 60 months … |
| `mdl77_2gdna_curindbp_` | MATRIX | Industry Relative Book-to-Market: It is defined as a stock's current book-to-price ratio (BP) less the average of the… |
| `mdl77_2gdna_curindcfp_` | MATRIX | Industry Relative TTM Cash Flow-to-Price: It is defined as a stock's trailing 12-month cash flow-to-price ratio (CFP)… |
| `mdl77_2gdna_curinddivp_` | MATRIX | Industry Relative TTM Dividend Yield: It is defined as a stock's trailing 12-month dividend yield (DivYield) less the… |
| `mdl77_2gdna_curindebitdap_` | MATRIX | Industry Relative TTM EBITDA-to-Price: It is defined as a stock's trailing 12-month EBITDA-to-price ratio (EBITDAP) l… |
| `mdl77_2gdna_curindep_` | MATRIX | Industry Relative TTM EPS-to-Price: It is defined as a stock's trailing 12-month earnings per share before extra item… |
| `mdl77_2gdna_curindfcfp_` | MATRIX | Industry Relative TTM Free Cash Flow-to-Price: It is defined as a stock's trailing 12-month free cash flow-to-price r… |
| `mdl77_2gdna_curindocfp_` | MATRIX | Industry Relative TTM Oper Cash Flow-to-Price: It is defined as a stock's trailing 12-month operating cash flow-to-pr… |
| `mdl77_2gdna_curindocfta_` | MATRIX | Industry Relative TTM Oper Cash Flow-to-Total Assets: It is defined as a stock's trailing 12-month operating cash flo… |
| `mdl77_2gdna_curindsp_` | MATRIX | Industry Relative TTM Sales-to-Price: It is defined as a stock's trailing 12-month sales-to-price ratio (SP) less the… |
| `mdl77_2gdna_curratio` | MATRIX | Current Ratio: It is defined as the reported current assets from the most recent quarter divided by the current liabi… |
| `mdl77_2gdna_cvvolp20d` | MATRIX | 20-Day Volume Volatility to Price Volatility: It is defined as the coefficient of variation of the last 20 days of cl… |
| `mdl77_2gdna_cws` | MATRIX | Working Capital-to-Trailing 12-Month Sales: It is defined as the average of working capital for the trailing 12 month… |
| `mdl77_2gdna_dcc` | MATRIX | Current Cash Flow Debt Coverage Ratio: It is defined as the most recently reported quarterly cash flow from operation… |
| `mdl77_2gdna_debtcf` | MATRIX | The sum of the most recent reported long-term debt and short-term interest-bearing debt divided by the trailing 12-mo… |
| `mdl77_2gdna_divcf` | MATRIX | Dividends-to-Cash Flow: It is defined as the trailing 12-month cash dividends divided by the trailing 12-month cash f… |
| `mdl77_2gdna_divcov` | MATRIX | Company's trailing 1-year profits scaled by its annual dividends. |
| `mdl77_2gdna_divyield` | MATRIX | TTM Dividend Yield: It is defined as the trailing 12-month dividends per share for a stock divided by its month-end t… |
| `mdl77_2gdna_dpcapex` | MATRIX | Change in TTM Depreciation vs CapEx: It is defined as the absolute value of the difference between the yearly percent… |
| `mdl77_2gdna_ebitdaev` | MATRIX | TTM EBITDA-to-Enterprise Value: It is defined as the trailing 12-month earnings before interest, taxes, depreciation,… |
| `mdl77_2gdna_ebitdap` | MATRIX | TTM EBITDA-to-Price: It is defined as the trailing 12-month earnings before interest, taxes, depreciation and amortiz… |
| `mdl77_2gdna_ed` | MATRIX | Long-term Debt-to-Equity: It is defined as the most recently reported total long-term debt divided by total book equity. |
| `mdl77_2gdna_epschgetr` | MATRIX | EPS from Change in Effective Tax Rate: It is defined as the trailing 12-month pre-tax income per share times the diff… |
| `mdl77_2gdna_equityto` | MATRIX | The trailing 12-month sales divided by the average of trailing 12-month reported book equity. |
| `mdl77_2gdna_fc_estep` | MATRIX | Leading 12-Month Median Earnings Yield: It is defined as the next fiscal year median consensus earnings estimate divi… |
| `mdl77_2gdna_fc_fcfroey1p` | MATRIX | Product of TTM FCF Yield and Forward ROE: It is defined as the trailing 12-month free cash flow per share multiplied … |
| `mdl77_2gdna_fc_numrevy1` | MATRIX | Net Number ofRevisions for Fiscal Year 1: It is defined as the weighted average of the number of FY1 analyst earnings… |
| `mdl77_2gdna_fcfequity` | MATRIX | TTM Free Cash Flow to Equity: It is defined as the trailing 12-month free cash flow divided by the average book equit… |
| `mdl77_2gdna_fcfghc` | MATRIX | 1-yr Chg in Assets-adj TTM Free Cash Flow: It is defined as the trailing 12-month free cash flow minus 4 quarters ago… |
| `mdl77_2gdna_fcfroi` | MATRIX | Free Cash Flow Return on Invested Capital: It is defined as the trailing 12-month free cash flow divided by the avera… |
| `mdl77_2gdna_fcfsale` | MATRIX | TTM Free Cash Flow-to-TTM Sales: It is defined as the trailing 12-month free cash flow divided by the trailing 12-mon… |
| `mdl77_2gdna_fcghc` | MATRIX | 1-yr Change in Assets-adj TTM Cash Flow: It is defined as the trailing 12-month cash flow minus comparable trailing 1… |
| `mdl77_2gdna_fcoghc` | MATRIX | 1-yr Chg in Assets-adj TTM Oper Cash Flow: It is defined as the most recently reported trailing 12-month operating ca… |
| `mdl77_2gdna_fixastto` | MATRIX | The trailing 12-month sales divided by the average of the total fixed assets in the same period. |
| `mdl77_2gdna_flowratio` | MATRIX | Flow Ratio: It is defined as the difference between current assets and cash & equivalents divided by the difference b… |
| `mdl77_2gdna_gear` | MATRIX | Capital Gearing Ratio: It is defined as the long-term debt divided by the difference between total assets and current… |
| `mdl77_2gdna_gtl` | MATRIX | Long-Term Growth Rate Estimates: It is defined as the consensus long-term growth forecast. It generally represents an… |
| `mdl77_2gdna_gtlm6ghc` | MATRIX | 6-M Change in Long-term Growth Estimates: It is defined as the percent change in the most recent mean consensus long-… |
| `mdl77_2gdna_high52w` | MATRIX | 52-Week High: It is defined as the month-end price divided by the highest monthly closing price in the past 12 months. |
| `mdl77_2gdna_ica` | MATRIX | Abnormal Capital Investment: It is defined as the change in a firm's most recent trailing 12-month capital investment… |
| `mdl77_2gdna_idb` | MATRIX | Basic Defensive Interval: It measures how many days that a company can cover its daily operating expenses (cost of go… |
| `mdl77_2gdna_indrelcroe_` | MATRIX | Stock's lagged quarterly return on equity (ROE) minus the average of the ROEs of all stocks in the same industry defl… |
| `mdl77_2gdna_indrelrecd_` | MATRIX | Industry-adjusted Doubtful Account Receivables: It is defined as a stock's asset-adjusted annual doubtful receivables… |
| `mdl77_2gdna_indrelrtn4w_` | MATRIX | 4-Week Industry Relative Return: It is defined as a stock's return in the last 4 weeks minus the average of the compa… |
| `mdl77_2gdna_indrelrtn5d_` | MATRIX | Stock's return in the last 5 days minus the average of the comparable returns of all stocks in the same industry, the… |
| `mdl77_2gdna_invast` | MATRIX | The current inventory level deflated by the total assets from the most recent quarter. |
| `mdl77_2gdna_iqa` | MATRIX | Asset Quality Index: It is defined as the year-over-year change of 1 minus the ratio of current assets plus PP&E divi… |
| `mdl77_2gdna_lagegp` | MATRIX | Lagged Inverse of PEG Ratio: It is defined as the trailing 12-month earnings per share before extraordinary items tim… |
| `mdl77_2gdna_lfd` | MATRIX | The sum of the trailing 12-month pretax income and the trailing 12-month interest expense divided by the trailing 12-… |
| `mdl77_2gdna_liqcoeff` | MATRIX | Liquidity Coefficient: It is the slope of the regression between the monthly stock trading turnover ratio (X) and the… |
| `mdl77_2gdna_lumqca` | MATRIX | Acquisition Multiple: It is defined as the most recent quarterly reported invested capital divided by the trailing 12… |
| `mdl77_2gdna_m42rav` | MATRIX | 24-Month Value at Risk: It is defined as the minimum of a stock's monthly price return in the last 20-month period. |
| `mdl77_2gdna_m6dn2ntr` | MATRIX | Second Preceding 6-month Return: It is defined as the percent change in a stock's price from month t-12 to month t-7. |
| `mdl77_2gdna_milliq` | MATRIX | Stock Illiquidity: It is defined as the monthly average of the daily absolute return to the daily dollar trading volu… |
| `mdl77_2gdna_mktcappera` | MATRIX | Stock's current market cap divided by the number of analysts providing Fiscal Year 1 earnings estimates. |
| `mdl77_2gdna_mktlev` | MATRIX | Stock's total market value plus the most recent reported quarterly book debt, then divided by the market value. |
| `mdl77_2gdna_mpn` | MATRIX | Net Profit Margin: It is defined as the most recently reported quarterly net income after tax divided by the correspo… |
| `mdl77_2gdna_mpnghc` | MATRIX | 1-Yr Change in Net Profit Margin: It is defined as the most recent quarterly net profit margin (NPM) minus the NPM 4 … |
| `mdl77_2gdna_mpoghc` | MATRIX | 1-yr Change in Operating Profit Margin: It is defined as the most recent quarterly operating profit margin minus that… |
| `mdl77_2gdna_netcashp` | MATRIX | Net Cash to Equity: It is defined as most recently reported quarterly cash & equivalents less the long-term debt and … |
| `mdl77_2gdna_netdebt` | MATRIX | Net Debt Ratio: It is defined as the net debt divided by the sum of the net debt, preferred stock, and common stock, … |
| `mdl77_2gdna_nfaldebt` | MATRIX | Net Fixed Assets to Long-term Debt: It is defined as the most recent quarterly reported net fixed assets divided by t… |
| `mdl77_2gdna_niper` | MATRIX | Net Income per Employee: It is defined as the income after taxes for the trailing 12-months divided by the number of … |
| `mdl77_2gdna_nlassets` | MATRIX | Natural Logarithm of Total Assets: It is defined as the natural logarithm of the most recent quarterly reported total… |
| `mdl77_2gdna_nlmktcap` | MATRIX | Natural Logarithm of Market Capitalization: It is defined as the natural logarithm of the cube of a stock's total mar… |
| `mdl77_2gdna_nlprice` | MATRIX | Natural Logarithm of Closing Price: It is defined as the natural logarithm of the cubic of a stock's unadjusted closi… |
| `mdl77_2gdna_nlsales` | MATRIX | Natural Logarithm of TTM Sales: It is defined as the natural logarithm of the cubic of a company's trailing 12-month … |
| `mdl77_2gdna_nlvolcap` | MATRIX | The natural logarithm of the quotient of the trailing 1-year average of the monthly volume to the trailing 1-year ave… |
| `mdl77_2gdna_nnastp` | MATRIX | Net Current Assets-to-Price: It is defined as the current assets per share minus total liabilities per share divided … |
| `mdl77_2gdna_noato` | MATRIX | Net Operating Asset Turnover: It is defined as trailing-12-month sales divided by the last 4 quarters' average net op… |
| `mdl77_2gdna_nopatmargin` | MATRIX | NOPAT Margin: It is defined as: (Net Income + Interest Expense*(1-Effective Tax Rate))/Net Sales. All items are for t… |
| `mdl77_2gdna_ntrm01ff` | MATRIX | Fama-French Momentum: It is defined as the percent change in a stock's price from month t-12 to month t-2. |
| `mdl77_2gdna_ocfast` | MATRIX | Operating Cash Flow to Assets: It is defined as the trailing 12-month net cash flow from operations divided by the av… |
| `mdl77_2gdna_ocfmargin` | MATRIX | Operating Cash Flow Profit Margin: It is defined as the trailing 12-month cash flow from operations scaled by the tra… |
| `mdl77_2gdna_ocfratio` | MATRIX | Operating Cash Flow Ratio: It is defined as a stock's most recently reported quarterly cash flow from operations divi… |
| `mdl77_2gdna_ocfroi` | MATRIX | Oper Cash Flow Return on Invested Capital: It is defined as the trailing 12-month operating cash flow divided by the … |
| `mdl77_2gdna_ollev` | MATRIX | Operating Liability Leverage: It is defined as 1 minus the ratio of (short-term debt + long-term debt + common equity… |
| `mdl77_2gdna_opincltd` | MATRIX | Change in TTM Oper Income vs LT Debt: It is defined as the difference between the yearly percent change in operating … |
| `mdl77_2gdna_oplev` | MATRIX | Operating Leverage: It is defined as the percent change in the trailing 12-month operating income from the previous q… |
| `mdl77_2gdna_otvni` | MATRIX | Inventory Turnover Ratio: It is defined as the trailing 12-month cost of goods sold divided by the average of invento… |
| `mdl77_2gdna_p50_00ratio` | MATRIX | 50-200 Day Stock Price Ratio: It is defined as the moving average of a stock's prices in the last 50 days divided by … |
| `mdl77_2gdna_past` | MATRIX | Price-to-Total Assets: It is defined as a stock's month-end trading price divided by the most recent quarterly report… |
| `mdl77_2gdna_pau` | MATRIX | Unexpected Change in Accounts Payable: It is defined as the difference between current accounts payable and the expec… |
| `mdl77_2gdna_pb` | MATRIX | Book-to-Market: It is defined as the most recently reported book value per share for a stock deflated by its month-en… |
| `mdl77_2gdna_pca` | MATRIX | Average Collection Period: It is defined as the average of the trailing 12-month reported accounts receivable times 3… |
| `mdl77_2gdna_pctabv260low` | MATRIX | Price Above Last 260-Day Lowest Trading Price: It is defined as a stock's current closing price divided by its lowest… |
| `mdl77_2gdna_pctchg3ycf` | MATRIX | The percent change in a stock's most recent trailing 12-month cash flow per share as compared to itself 12 quarters ago. |
| `mdl77_2gdna_pctchg3yeps` | MATRIX | The percent change in a stock's most recent trailing 12-month earnings per share as compared to itself 12 quarters ago. |
| `mdl77_2gdna_pctchg3yfcf` | MATRIX | 3-yr Growth in TTM Free Cash Flow: It is defined as the percent change in a stock's most recent trailing 12-month fre… |
| `mdl77_2gdna_pctchg3yocf` | MATRIX | 3-yr Growth in TTM Oper Cash Flow: It is defined as the percent change in a stock's most recent trailing 12-month ope… |
| `mdl77_2gdna_pctchgastto` | MATRIX | 1-yr Change in Asset Turnover Ratio: It is defined as the percent change in the most recent asset turnover ratio as c… |
| `mdl77_2gdna_pctchgcf` | MATRIX | 1-yr Growth in TTM Cash Flow: It is defined as the percent change in a stock's most recent trailing 12-month cash flo… |
| `mdl77_2gdna_pctchgeps` | MATRIX | The percent change in a stock's most recent trailing 12-month earnings per share before extra items as compared to it… |
| `mdl77_2gdna_pctchgfcf` | MATRIX | 1-yr Growth in TTM Free Cash Flow: It is defined as the percent change in a stock's most recent trailing 12-month fre… |
| `mdl77_2gdna_pctchgocf` | MATRIX | 1-yr Growth in TTM Oper Cash Flow: It is defined as the percent change of a stock's most recent trailing 12-month ope… |
| `mdl77_2gdna_pctchgqtrast` | MATRIX | 1-Yr Change in Total Assets: It is defined as the growth in the most recent reported quarterly total assets per share… |
| `mdl77_2gdna_pctchgqtrsales` | MATRIX | 1-yr Change in Sales: It is defined as the growth in most recent reported quarterly sales per share as compared to 4 … |
| `mdl77_2gdna_pcurlia` | MATRIX | Current Liabilities-to-Price: It is defined as a stock's most recently reported quarterly current liabilities per sha… |
| `mdl77_2gdna_pd09erpvc` | MATRIX | CV of Prior 90-Day Closing Prices: It is defined as the standard deviation of a stock's last 90 days closing prices d… |
| `mdl77_2gdna_pedu` | MATRIX | Unexpected Change in Depreciation: It is defined as the difference between the trailing 12-month depreciation expense… |
| `mdl77_2gdna_pedwf_cf` | MATRIX | Leading 12-Month Mean Earnings Yield: It is defined as the next 4 quarters' mean consensus earnings estimate divided … |
| `mdl77_2gdna_perg` | MATRIX | Risk-adjusted PEG Ratio: It is defined as the stock price divided by the leading 12-month consensus earnings forecast… |
| `mdl77_2gdna_pfcf_cf` | MATRIX | Forward Free Cash Flow-to-Price: It is defined as the next 4-quarter's mean consensus earnings estimate plus trailing… |
| `mdl77_2gdna_pfcfghc` | MATRIX | The difference between the trailing 12-month free cash flow per share and that of 4 quarters ago for a stock divided … |
| `mdl77_2gdna_pfcfmtt` | MATRIX | TTM Free Cash Flow-to-Price: It is defined as the trailing 12-month free cash flow per share for a stock divided by i… |
| `mdl77_2gdna_pfcfy3ghc` | MATRIX | 3-yr Change in Price-adj TTM FCF: It is defined as the difference between the most recently reported trailing 12-mont… |
| `mdl77_2gdna_pfcghc` | MATRIX | The difference between the trailing 12-month cash flow per share and that of 12 quarters ago for a stock divided by i… |
| `mdl77_2gdna_pfcmtt` | MATRIX | TTM Cash Flow-to-Price: It is defined as the trailing 12-month cash flows per share for a stock scaled by its trading… |
| `mdl77_2gdna_pfcoghc` | MATRIX | The difference between the most recently reported trailing 12-month operating cash flow per share and that of 4 quart… |
| `mdl77_2gdna_pfcomtt` | MATRIX | TTM Operating Cash Flow-to-Price: It is defined as the trailing 12-month operating cash flow per share for a stock di… |
| `mdl77_2gdna_pfcoy3ghc` | MATRIX | The difference between the trailing 12-month operating cash flow per share and that of 12 quarters ago for a stock di… |
| `mdl77_2gdna_pfcy3ghc` | MATRIX | The difference between the trailing 12-month cash flow per share and that of 12 quarters ago comparable trailing 12-m… |
| `mdl77_2gdna_pfgmtt` | MATRIX | TTM Growth Flow-to-Price: It is defined as the sum of trailing 12-month growth flow value per share for a stock divid… |
| `mdl77_2gdna_pge_cf` | MATRIX | Estimates on the next 1-year average earnings scaled by company's prospects on growth and its stock price. |
| `mdl77_2gdna_pinoa` | MATRIX | Pretax Return on Net Operating Assets: It is defined as the trailing 12-month operating income after depreciation div… |
| `mdl77_2gdna_ppa` | MATRIX | Average Payable Period: It is defined as the average of the trailing 12-month accounts payable times 365 divided by t… |
| `mdl77_2gdna_pqipmtt` | MATRIX | The most recent trailing 12-month operating and nonoperating income per share before provisions for income taxes and … |
| `mdl77_2gdna_psmtt` | MATRIX | TTM Sales-to-Price: It is defined as the most recently reported trailing 12-month sales per share for a stock deflate… |
| `mdl77_2gdna_pspeghc` | MATRIX | The difference between the most recently reported trailing 12-month earnings per share and that of 4 quarters ago for… |
| `mdl77_2gdna_pvan` | MATRIX | Net Asset Value to Price: It is defined as the most recent book value of net assets per share (NAV) by the closing pr… |
| `mdl77_2gdna_rationalalpha` | MATRIX | Rational Decay Alpha: It evaluates stocks based on their historical 12-month market (S&P 500) adjusted excess return … |
| `mdl77_2gdna_ratrev6m` | MATRIX | Street Rating Revision: It is defined as the 6-month average of the change in the average analyst recommendation trac… |
| `mdl77_2gdna_rau` | MATRIX | Unexpected Change in Accounts Receivable: It is defined as the difference between current accounts receivable and the… |
| `mdl77_2gdna_rdsale` | MATRIX | R&D Intensity: It is defined as the average of the research & development expenses in the trailing 12 months deflated… |
| `mdl77_2gdna_reinrate` | MATRIX | Reinvestment Rate: It is defined as the trailing 12-month earnings per share before extra items less the trailing 12-… |
| `mdl77_2gdna_rel5ybp` | MATRIX | 5-Year Relative Book-to-Market: It is defined as a stock's current book-to-market ratio (BP) minus the average of the… |
| `mdl77_2gdna_rel5ycfp` | MATRIX | 5-yr Relative TTM Cash Flow-to-Price: It is defined as a stock's current trailing 12-month cash flow-to-price ratio (… |
| `mdl77_2gdna_rel5ydivp` | MATRIX | 5-yr Relative TTM Dividend Yield: It is defined as a stock's current dividend yield (DivYield) minus the average of t… |
| `mdl77_2gdna_rel5yebitdap` | MATRIX | 5-yr Relative TTM EBITDA-to-Price: It is defined as a stock's current trailing 12-month EBITDA per share-to-price rat… |
| `mdl77_2gdna_rel5yep` | MATRIX | 5-yr Relative TTM Earnings-to-Price: It is defined as a stock's current trailing 12-month earnings per share before e… |
| `mdl77_2gdna_rel5yfcfp` | MATRIX | 5-yr Relative TTM Free Cash Flow-to-Price: It is defined as a stock's current trailing 12-month free cash flow-to-pri… |
| `mdl77_2gdna_rel5yocfp` | MATRIX | 5-yr Relative TTM Oper Cash Flow-to-Price: It is defined as a stock's current trailing 12-month operating cash flow-t… |
| `mdl77_2gdna_rel5ysp` | MATRIX | 5-yr Relative TTM Sales-to-Price: It is defined as a stock's current trailing 12-month sales-to-price ratio (SP) minu… |
| `mdl77_2gdna_relpricestrength_` | MATRIX | Industry-adjusted 12-month Relative Price Strength: It is defined as a stock's 12-month relative price-strength (PS) … |
| `mdl77_2gdna_rerror60m` | MATRIX | Regression Error of 60-Month CAPM: It is defined as the standard error of the slope of the least squares regression l… |
| `mdl77_2gdna_revper` | MATRIX | Revenue per Employee: It is defined as the trailing 12-month total sales divided by the number of employees at the en… |
| `mdl77_2gdna_roe` | MATRIX | Return on Equity: It is defined as the trailing 12-month income before extra items divided by the average of common e… |
| `mdl77_2gdna_roic` | MATRIX | Return on Invested Capital: It is defined as the trailing 12-month net income and interest expenses divided by the av… |
| `mdl77_2gdna_rq` | MATRIX | Quick Ratio: It is defined as the current assets less inventories from the most recent quarter divided by the total c… |
| `mdl77_2gdna_saleeps` | MATRIX | Change in TTM Sales vs EPS: It is defined as the absolute value of the difference between the yearly percent change i… |
| `mdl77_2gdna_saleg5y` | MATRIX | 5-yr Sales Growth: It is defined as the difference between the trailing 12-month sales per share (SALE) and the SALE … |
| `mdl77_2gdna_salegpm` | MATRIX | Change in QTR Sales vs. Gross Margin: It is defined as the difference between the yearly change in most recent report… |
| `mdl77_2gdna_salerec` | MATRIX | Change in TTM Sales vs Accounts Receivable: It is defined as the difference between the yearly percent change in trai… |
| `mdl77_2gdna_sighc` | MATRIX | 1-yr Chg in QTR Inventory as Percentage ofSales: It is defined as the most recently reported inventory as a percentag… |
| `mdl77_2gdna_sigma` | MATRIX | Stock Return Volatility: It is defined as the standard deviation of a stock's monthly returns in the prior 60 months. |
| `mdl77_2gdna_skew90cortn` | MATRIX | Skewness of 90-Day Stock Daily Excess Returns: It is defined as the skewness of the distribution of a stock's daily e… |
| `mdl77_2gdna_skew90drtn` | MATRIX | Skewness of 90-Day Stock Daily Returns: It is defined as the skewness (measure of lack of symmetry) of the distributi… |
| `mdl77_2gdna_slope52wp` | MATRIX | Slope of 52-Week Price Trend Line: It is defined as the 4-week lagged slope coefficient of the least squares regressi… |
| `mdl77_2gdna_slope66wp` | MATRIX | Slope of 66 Week Price Trend Line: It is defined as the 4-week lagged slope coefficient of the least squares regressi… |
| `mdl77_2gdna_spe2yfvc_cf` | MATRIX | FY2 EPS Forecast Dispersion: It is defined as the standard deviation of analyst earnings estimates for fiscal year 2 … |
| `mdl77_2gdna_spefcn` | MATRIX | Change in TTM EPS vs Oper Cash Flows: It is defined as the absolute value of the difference between the yearly percen… |
| `mdl77_2gdna_speghc` | MATRIX | 1-yr Change in Assets-adj TTM EPS: It is defined as the trailing 12-month earnings per share before extra items (EPS)… |
| `mdl77_2gdna_stockrating` | MATRIX | Street Consensus Rating: It is defined as the consensus recommendation for a company. |
| `mdl77_2gdna_surp` | MATRIX | Real Earnings Surprise: It is defined as the difference between the actual earnings per share and consensus forecasts… |
| `mdl77_2gdna_susgrowth` | MATRIX | The maximum growth rate a firm can sustain without having to increase financial leverage. |
| `mdl77_2gdna_tobinq` | MATRIX | Tobin Q: It is defined as the market value of equity (E) plus debt (D) divided by assets (A), or (E + D)/A. D is meas… |
| `mdl77_2gdna_totalcov` | MATRIX | Total Coverage: It equals (Cash Flow from Operations + Interest Paid + Tax Paid)/ (Interest + Principal Paid). |
| `mdl77_2gdna_totalsaleg` | MATRIX | Yearly TTM Total Sales Growth Rate: It is defined as the percent change in a company's trailing 12-month total sales … |
| `mdl77_2gdna_tstalp` | MATRIX | 1-Year Price Momentum Indicator: It is defined as: (CORREL*(260-2)^.5)/(1-CORREL^2)^.5. CORREL is the correlation coe… |
| `mdl77_2gdna_ttmaccu` | MATRIX | Accounting Accruals: It is defined as the difference between the trailing 12-month net income and the trailing 12-mon… |
| `mdl77_2gdna_ttmcapexp` | MATRIX | TTM Capital Expenditures-to-Price: It is defined as the trailing 12-month capital expenditures per share for a stock … |
| `mdl77_2gdna_ttmsaleev` | MATRIX | TTM Sales-to-Enterprise Value: It is defined as the trailing 12-month sales for a stock divided by the most recent en… |
| `mdl77_2gdna_varresirtn` | MATRIX | 24-Month Residual Return Variance: It is defined as the variance of a stock's monthly residual return in the last 24 … |
| `mdl77_2gdna_vefcfmtt` | MATRIX | TTM Free Cash Flow-to-Enterprise Value: It is defined as the trailing 12-month free cash flow (FCF) for a stock scale… |
| `mdl77_2gdna_vesspem21f_cf` | MATRIX | Forward 12-M EPS-to-Enterprise Value: It is defined as the consensus forward 12-month earnings per share forecast div… |
| `mdl77_2gdna_visiratio` | MATRIX | The Visibility Ratio: It equals a stock's most recent daily trading volume divided by the average daily trading volum… |
| `mdl77_2gdna_vnicw` | MATRIX | Working Capital to Inventory: It is defined as the most recent quarterly reported working capital divided by the inve… |
| `mdl77_2gdna_vniu` | MATRIX | The difference of inventory between present and expected levels. |
| `mdl77_2gdna_voctni` | MATRIX | Interest Coverage: It is defined as the most recently reported quarterly operating income before depreciation divided… |
| `mdl77_2gdna_volpre6m` | MATRIX | The 6-month moving average of average monthly turnover ratio. |
| `mdl77_2gdna_volto` | MATRIX | Trading Turnover Ratio: It is defined as the monthly total trading volume divided by the most recently reported total… |
| `mdl77_2gdna_w57w03_rp` | MATRIX | 30-75 Week Stock Price Ratio: It is defined as the moving average of a stock's prices in the last 30 weeks divided by… |
| `mdl77_2gdna_w62isr` | MATRIX | 26-Week Relative Price Strength: It is defined as a stock's most recent weekly closing price divided by its weekly cl… |
| `mdl77_2gdna_w93ntr` | MATRIX | 39-Week Return with 4-week Lag: It is defined as a stock's price change from week t-43 to week t-4. |
| `mdl77_2gdna_wcast` | MATRIX | Working Capital-to-Total Assets: It is defined as the average working capital in the trailing 12 months divided by th… |
| `mdl77_2gdna_ydp_cf` | MATRIX | Predicted Dividend Yield: It is defined as an assumed payout ratio multiplied by the next 4-quarter consensus earning… |
| `mdl77_2gdna_yoychgaa` | MATRIX | Change in Accruals to Assets: It is defined as the trailing 12-month income before extra items less the trailing 12-m… |
| `mdl77_2gdna_yoychgcr` | MATRIX | Year-over-year Change in Current Ratio: It is defined as the most recent reported quarterly current ratio and the cur… |
| `mdl77_2gdna_yoychgda` | MATRIX | Year-over-year Change in Leverage: It is defined as the difference between the most recent reported quarterly total l… |
| `mdl77_2gdna_yoychggpm` | MATRIX | Yearly Change In Gross Profit Margin: It is defined as the most recent quarterly reported gross profit margin minus t… |
| `mdl77_2gdna_yoychgroa` | MATRIX | Yearly Change in Return on Assets: It is defined as the most recent trailing 12-month income before extra items as a … |
| `mdl77_2gf_am_amv` | MATRIX | Fundamental Growth: This submodule is the equal-weighted average of 1-year Growth in TTM EPS, the 1-year Change in As… |
| `mdl77_2globaldevnorthamericasensitivityfactor_apsales` | MATRIX | Asia-Pacific Sales Exposure: It is defined as the annual aggregate sales for Asia-Pacific as reported by the company … |
| `mdl77_2globaldevnorthamericasensitivityfactor_ceroe` | MATRIX | The trailing 12-month funds from operations divided by the average of the current and previous year. |
| `mdl77_2globaldevnorthamericasensitivityfactor_dsu` | MATRIX | The beta coefficient estimated by a multiple regression of returns on several macroeconomic aspects over 60 months. |
| `mdl77_2globaldevnorthamericasensitivityfactor_emeasales` | MATRIX | EMEA Sales Exposure: It is defined as the annual aggregate sales for EMEA as reported by the company divided by total… |
| `mdl77_2globaldevnorthamericasensitivityfactor_inflation` | MATRIX | The beta coefficient estimated by a multiple regression of returns on several macroeconomic aspects over 60 months. |
| `mdl77_2globaldevnorthamericasensitivityfactor_lasales` | MATRIX | Latin America Sales Exposure: It is defined as the annual aggregate sales for Latin America as reported by the compan… |
| `mdl77_2globaldevnorthamericasensitivityfactor_nasales` | MATRIX | North America Sales Exposure: It is defined as the annual aggregate sales for North America as reported by the compan… |
| `mdl77_2globaldevnorthamericasensitivityfactor_oilprice` | MATRIX | The beta coefficient estimated by a multiple regression of returns on several macroeconomic aspects over 60 months. |
| `mdl77_2globaldevnorthamericasensitivityfactor_pi` | MATRIX | Industrial Production Sensitivity: It is defined as the beta coefficient to Change in Industrial Production, which is… |
| `mdl77_2globaldevnorthamericasensitivityfactor_prc` | MATRIX | Credit Risk Premium Sensitivity: It is defined as the beta coefficient to Change in Credit Risk Premium, which is est… |
| `mdl77_2globaldevnorthamericasensitivityfactor_sh` | MATRIX | Housing Starts Sensitivity: It is defined as the beta coefficient to Change in Housing Starts, which is estimated by … |
| `mdl77_2globaldevnorthamericasensitivityfactor_xiv` | MATRIX | Market Volatility Sensitivity: It is defined as the beta coefficient to Change in Market Volatility, which is estimat… |
| `mdl77_2globaldevnorthamericasensitivityfactor_yieldsprd` | MATRIX | Yield Curve Slope Sensitivity: It is defined as the beta coefficient to Change in Slope of Term Structure, which is e… |
| `mdl77_2gpm_composite` | MATRIX | GARP Model Composite: GARP Model Composite |
| `mdl77_2growthanalystmodel2_qga_ltepssurprise` | MATRIX | Long Term EPS Surprise: Long Term EPS Surprise |
| `mdl77_2growthanalystmodel_qga_composite` | MATRIX | Growth Analyst Composite |
| `mdl77_2growthanalystmodel_qga_epscapex` | MATRIX | EPS Growth to CapEx Link |
| `mdl77_2growthanalystmodel_qga_epstrend` | MATRIX | EPS Trend |
| `mdl77_2growthanalystmodel_qga_fcfroe` | MATRIX | Free Cash Flow ROE |
| `mdl77_2growthanalystmodel_qga_iarsales` | MATRIX | Inv Acc Rec to Sales Link |
| `mdl77_2growthanalystmodel_qga_niroe` | MATRIX | Net Income ROE |
| `mdl77_2growthanalystmodel_qga_opmarginsales` | MATRIX | Op Margin to Sales Link |
| `mdl77_2gspea2y_cf` | MATRIX | 2-Year Ahead EPS Growth: It is defined as the most recent consensus earnings forecast for fiscal year 2 minus the con… |
| `mdl77_2historicalgrowthfactor_chg3ycfast` | MATRIX | 3-yr Change in Assets-adj TTM Cash Flow: It is defined as the most recently reported trailing 12-month operating cash… |
| `mdl77_2historicalgrowthfactor_chg3yepsast` | MATRIX | 3-yr Change in Assets-adj TTM EPS: It is defined as the trailing 12-month earnings per share before extra items (EPS)… |
| `mdl77_2historicalgrowthfactor_chg3yepsp` | MATRIX | The difference between the trailing 12-month earnings per share and that of 12-quarters ago for a stock divided by it… |
| `mdl77_2historicalgrowthfactor_chg3yfcfast` | MATRIX | 3-Yr Chg in Assets-Adj TTM Free Cash Flow: It is defined as the trailing 12-month free cash flow minus 12 quarters ag… |
| `mdl77_2historicalgrowthfactor_chg3yocfast` | MATRIX | 3-yr Change in Assets-adj TTM Oper Cash Flow: It is defined as the most recently reported trailing 12-month operating… |
| `mdl77_2historicalgrowthfactor_chgars` | MATRIX | 1-yr Chg in Acct Receivable as Percentage ofSales: It is defined as the change between the last reported accounts rec… |
| `mdl77_2historicalgrowthfactor_cv4qsales3y` | MATRIX | The standard deviation of prior 12 quarters' trailing 12-month sales for individual shares scaled to the mean of itse… |
| `mdl77_2historicalgrowthfactor_cvopinc` | MATRIX | CV of Oper Income per Share in Last 12 QTRs: It is defined as the standard deviation of the trailing 12-month operati… |
| `mdl77_2historicalgrowthfactor_div5yg` | MATRIX | 5-Year Dividend Growth Rate: It is defined as the 5-year growth in dividends. |
| `mdl77_2historicalgrowthfactor_fcfequity` | MATRIX | TTM Free Cash Flow to Equity: It is defined as the trailing 12-month free cash flow divided by the average book equit… |
| `mdl77_2historicalgrowthfactor_fcfghc` | MATRIX | 1-yr Chg in Assets-adj TTM Free Cash Flow: It is defined as the trailing 12-month free cash flow minus 4 quarters ago… |
| `mdl77_2historicalgrowthfactor_fcghc` | MATRIX | 1-yr Change in Assets-adj TTM Cash Flow: It is defined as the trailing 12-month cash flow minus comparable trailing 1… |
| `mdl77_2historicalgrowthfactor_fcoghc` | MATRIX | 1-yr Chg in Assets-adj TTM Oper Cash Flow: It is defined as the most recently reported trailing 12-month operating ca… |
| `mdl77_2historicalgrowthfactor_mpnghc` | MATRIX | 1-Yr Change in Net Profit Margin: It is defined as the most recent quarterly net profit margin (NPM) minus the NPM 4 … |
| `mdl77_2historicalgrowthfactor_mpoghc` | MATRIX | 1-yr Change in Operating Profit Margin: It is defined as the most recent quarterly operating profit margin minus that… |
| `mdl77_2historicalgrowthfactor_pctchg3ycf` | MATRIX | The percent change in a stock's most recent trailing 12-month cash flow per share as compared to itself 12 quarters ago. |
| `mdl77_2historicalgrowthfactor_pctchg3yeps` | MATRIX | The percent change in a stock's most recent trailing 12-month earnings per share as compared to itself 12 quarters ago. |
| `mdl77_2historicalgrowthfactor_pctchg3yfcf` | MATRIX | 3-yr Growth in TTM Free Cash Flow: It is defined as the percent change in a stock's most recent trailing 12-month fre… |
| `mdl77_2historicalgrowthfactor_pctchg3yocf` | MATRIX | 3-yr Growth in TTM Oper Cash Flow: It is defined as the percent change in a stock's most recent trailing 12-month ope… |
| `mdl77_2historicalgrowthfactor_pctchgastto` | MATRIX | 1-Yr Change in Asset Turnover Ratio: It is defined as the percent change in the most recent asset turnover ratio as c… |
| `mdl77_2historicalgrowthfactor_pctchgcf` | MATRIX | 1-yr Growth in TTM Cash Flow: It is defined as the percent change in a stock's most recent trailing 12-month cash flo… |
| `mdl77_2historicalgrowthfactor_pctchgeps` | MATRIX | The percent change in a stock's most recent trailing 12-month earnings per share before extra items as compared to it… |
| `mdl77_2historicalgrowthfactor_pctchgfcf` | MATRIX | 1-yr Growth in TTM Free Cash Flow: It is defined as the percent change in a stock's most recent trailing 12-month fre… |
| `mdl77_2historicalgrowthfactor_pctchgocf` | MATRIX | 1-Year Growth in TTM Operating Cash Flow: It is defined as the percent change of a stock's most recent trailing 12-mo… |
| `mdl77_2historicalgrowthfactor_pctchgqtrast` | MATRIX | 1-yr Change in Total Assets: It is defined as the growth in the most recent reported quarterly total assets per share… |
| `mdl77_2historicalgrowthfactor_pctchgqtrsales` | MATRIX | 1-yr Change in Sales: It is defined as the growth in most recent reported quarterly sales per share as compared to 4 … |
| `mdl77_2historicalgrowthfactor_pfcfghc` | MATRIX | The difference between the trailing 12-month free cash flow per share and that of 4 quarters ago for a stock divided … |
| `mdl77_2historicalgrowthfactor_pfcfy3ghc` | MATRIX | 3-yr Change in Price-adj TTM FCF: It is defined as the difference between the most recently reported trailing 12-mont… |
| `mdl77_2historicalgrowthfactor_pfcghc` | MATRIX | The difference between the trailing 12-month cash flow per share and that of 12 quarters ago for a stock divided by i… |
| `mdl77_2historicalgrowthfactor_pfcoghc` | MATRIX | The difference between the most recently reported trailing 12-month operating cash flow per share and that of 4 quart… |
| `mdl77_2historicalgrowthfactor_pfcoy3ghc` | MATRIX | The difference between the trailing 12-month operating cash flow per share and that of 12 quarters ago for a stock di… |
| `mdl77_2historicalgrowthfactor_pfcy3ghc` | MATRIX | The difference between the trailing 12-month cash flow per share and that of 12 quarters ago comparable trailing 12-m… |
| `mdl77_2historicalgrowthfactor_pspeghc` | MATRIX | The difference between the most recently reported trailing 12-month earnings per share and that of 4 quarters ago for… |
| `mdl77_2historicalgrowthfactor_reinrate` | MATRIX | Reinvestment Rate: It is defined as the trailing 12-month earnings per share before extra items less the trailing 12-… |
| `mdl77_2historicalgrowthfactor_rsqr4qsales3y` | MATRIX | The conditional square of the correlation between monthly dates and the corresponding trailing 12-month sales per sha… |
| `mdl77_2historicalgrowthfactor_saleg5y` | MATRIX | 5-Yr Sales Growth: It is defined as the difference between the trailing 12-month sales per share (SALE) and the SALE … |
| `mdl77_2historicalgrowthfactor_salegstdev` | MATRIX | Sales Growth Rate Standard Deviation: It is defined as the standard deviation of the year-over-year quarterly sales p… |
| `mdl77_2historicalgrowthfactor_salesaccel4q` | MATRIX | 4-Quarter Sales Acceleration: It is defined as the slope of the regression line between year-over-year sales growth a… |
| `mdl77_2historicalgrowthfactor_se5yepsg` | MATRIX | Stability-Adjusted Residual Growth Rate: It is defined as a stock's mean long-term growth rate minus its 5-year histo… |
| `mdl77_2historicalgrowthfactor_sighc` | MATRIX | 1-yr Chg in QTR Inventory as Percentage ofSales: It is defined as the most recently reported inventory as a percentag… |
| `mdl77_2historicalgrowthfactor_slope4qcf3y` | MATRIX | Slope of 3-yr TTM Cash Flow Trend Line: It is defined as the slope coefficient between monthly dates and the correspo… |
| `mdl77_2historicalgrowthfactor_slope4qeps3y` | MATRIX | Slope of 3-yr TTM EPS Trend Line: It is defined as the slope coefficient between monthly dates and the corresponding … |
| `mdl77_2historicalgrowthfactor_slope4qfcf3y` | MATRIX | Slope of 3-yr TTM Free Cash Flow Trend Line: It is defined as the slope coefficient between monthly dates and the cor… |
| `mdl77_2historicalgrowthfactor_slope4qocf3y` | MATRIX | Slope of 3-Yr TTM Oper Cash Flow Trend Line: It is defined as the slope coefficient between monthly dates and the cor… |
| `mdl77_2historicalgrowthfactor_slope4qsales3y` | MATRIX | Slope of 3-Yr TTM Sales Trend Line: It is defined as the slope coefficient between monthly dates and the correspondin… |
| `mdl77_2historicalgrowthfactor_speghc` | MATRIX | 1-yr Change in Assets-adj TTM EPS: It is defined as the trailing 12-month earnings per share before extra items (EPS)… |
| `mdl77_2historicalgrowthfactor_susgrowth` | MATRIX | The maximum growth rate a firm can sustain without having to increase financial leverage. |
| `mdl77_2historicalgrowthfactor_totalsaleg` | MATRIX | Yearly TTM Total Sales Growth Rate: It is defined as the percent change in a company's trailing 12-month total sales … |
| `mdl77_2historicalgrowthfactor_y3fcfq4rqsr` | MATRIX | R-Sqr of 3-yr TTM FCF Trend Line: It is defined as the conditional square of the correlation between monthly dates an… |
| `mdl77_2historicalgrowthfactor_y3fcfq4vc` | MATRIX | Stability of 3-yr TTM Free Cash Flow: It is defined as the standard deviation of the last 12 quarters' trailing 12-mo… |
| `mdl77_2historicalgrowthfactor_y3fcoq4rqsr` | MATRIX | R-Sqr of 3-yr TTM Oper Cash Flow Trend Line: It is defined as the conditional square of the correlation between month… |
| `mdl77_2historicalgrowthfactor_y3fcoq4vc` | MATRIX | The standard deviation of the ratio for the values that the company generates scaled by its mean in the previous 12 q… |
| `mdl77_2historicalgrowthfactor_y3fcq4rqsr` | MATRIX | R-Sqr of 3-yr TTM Cash Flow Trend Line: It is defined as the conditional square of the correlation between monthly da… |
| `mdl77_2historicalgrowthfactor_y3fcq4vc` | MATRIX | Stability of 3-Yr TTM Cash Flow: It is defined as the standard deviation of the prior 12 quarters' trailing 12-month … |
| `mdl77_2historicalgrowthfactor_y3speq4rqsr` | MATRIX | R-Sqr of 3-yr TTM EPS Trend Line: It is defined as the conditional square of the correlation between monthly dates an… |
| `mdl77_2historicalgrowthfactor_y3speq4vc` | MATRIX | Stability of 3-yr TTM Earnings per Share: It is defined as the standard deviation of the last 12 quarters' trailing 1… |
| `mdl77_2industryrrelativevaluefactor_curindbp_` | MATRIX | Industry Relative Book-to-Market: It is defined as a stock's current book-to-price ratio (BP) less the average of the… |
| `mdl77_2industryrrelativevaluefactor_curindcfp_` | MATRIX | Industry Relative TTM Cash Flow-to-Price: It is defined as a stock's trailing 12-month cash flow-to-price ratio (CFP)… |
| `mdl77_2industryrrelativevaluefactor_curindcoreepsp_` | MATRIX | Industry Relative TTM Core Earnings-to-Price: It is defined as a stock's trailing 12-month core earnings-to-price rat… |
| `mdl77_2industryrrelativevaluefactor_curinddivp_` | MATRIX | Industry Relative TTM Dividend Yield: It is defined as a stock's trailing 12-month dividend yield (DivYield) less the… |
| `mdl77_2industryrrelativevaluefactor_curindebitdap_` | MATRIX | Industry Relative TTM EBITDA-to-Price: It is defined as a stock's trailing 12-month EBITDA-to-price ratio (EBITDAP) l… |
| `mdl77_2industryrrelativevaluefactor_curindep_` | MATRIX | Industry Relative TTM EPS-to-Price: It is defined as a stock's trailing 12-month earnings per share before extra item… |
| `mdl77_2industryrrelativevaluefactor_curindfcfp_` | MATRIX | Industry Relative TTM Free Cash Flow-to-Price: It is defined as a stock's trailing 12-month free cash flow-to-price r… |
| `mdl77_2industryrrelativevaluefactor_curindfwdep_` | MATRIX | Industry Relative Leading 4-QTRs EPS to Price: It is defined as a stock's next 4-quarter's analysts consensus earning… |
| `mdl77_2industryrrelativevaluefactor_curindocfp_` | MATRIX | Industry Relative TTM Oper Cash Flow-to-Price: It is defined as a stock's trailing 12-month operating cash flow-to-pr… |
| `mdl77_2industryrrelativevaluefactor_curindocfta_` | MATRIX | Industry Relative TTM Oper Cash Flow-to-Total Assets: It is defined as a stock's trailing 12-month operating cash flo… |
| `mdl77_2industryrrelativevaluefactor_curindsp_` | MATRIX | Industry Relative TTM Sales-to-Price: It is defined as a stock's trailing 12-month sales-to-price ratio (SP) less the… |
| `mdl77_2liquidityriskfactor_altmanz` | MATRIX | Altman Z Score: Altman Z = 1.2* (Current Assets - Current Liabilities)/TA + 1.4*Retained Earnings/TA + 3.3*Earnings b… |
| `mdl77_2liquidityriskfactor_astcomp` | MATRIX | Asset Composition: It is defined as the total current assets from the most recent quarter divided by the total assets… |
| `mdl77_2liquidityriskfactor_atmcallvol` | MATRIX | At the Money Call Option Implied Volatility: It is defined as the time-weighted average implied volatility of the nea… |
| `mdl77_2liquidityriskfactor_atmputvol` | MATRIX | At the Money Put Option Implied Volatility: It is defined as the time-weighted average implied volatility of the near… |
| `mdl77_2liquidityriskfactor_bap20d` | MATRIX | A proxy to market liquidity based on the difference between the highest price that a buyer is willing to pay for an a… |
| `mdl77_2liquidityriskfactor_beta` | MATRIX | 60-Month Beta: It is defined as 0.67 times the 60-month beta plus 0.33. Beta is the covariance between a stock's mont… |
| `mdl77_2liquidityriskfactor_betasigma` | MATRIX | Product of Beta and Sigma: It is defined as the product of the adjusted 60-month Beta and 60-month Sigma (standard de… |
| `mdl77_2liquidityriskfactor_booklev` | MATRIX | Book Leverage: It is defined as the most recently reported quarterly total assets divided by the book equity. |
| `mdl77_2liquidityriskfactor_cashratio` | MATRIX | Cash & Equivalents-to-Current Liabilities: It is defined as the most recently reported quarterly cash & equivalents d… |
| `mdl77_2liquidityriskfactor_cfleverage` | MATRIX | Cash Flow Leverage: It is defined as the total liabilities divided by the trailing 12-month operating cash flow. |
| `mdl77_2liquidityriskfactor_covol` | MATRIX | 60-Month Trading Volume Trend: It is defined as the slope of the least squares regression line of the last 60 months … |
| `mdl77_2liquidityriskfactor_curratio` | MATRIX | Current Ratio: It is defined as the reported current assets from the most recent quarter divided by the current liabi… |
| `mdl77_2liquidityriskfactor_cvvolp20d` | MATRIX | 20-Day Volume Volatility to Price Volatility: It is defined as the coefficient of variation of the last 20 days of cl… |
| `mdl77_2liquidityriskfactor_dcc` | MATRIX | Current Cash Flow Debt Coverage Ratio: It is defined as the most recently reported quarterly cash flow from operation… |
| `mdl77_2liquidityriskfactor_debtcf` | MATRIX | The sum of the most recent reported long-term debt and short-term interest-bearing debt divided by the trailing 12-mo… |
| `mdl77_2liquidityriskfactor_divcov` | MATRIX | Company's trailing 1-year profits scaled by its annual dividends. |
| `mdl77_2liquidityriskfactor_ed` | MATRIX | Long-term Debt-to-Equity: It is defined as the most recently reported total long-term debt divided by total book equity. |
| `mdl77_2liquidityriskfactor_flowratio` | MATRIX | Flow Ratio: It is defined as the difference between current assets and cash & equivalents divided by the difference b… |
| `mdl77_2liquidityriskfactor_gear` | MATRIX | Capital Gearing Ratio: It is defined as the long-term debt divided by the difference between total assets and current… |
| `mdl77_2liquidityriskfactor_growdura` | MATRIX | Growth Duration: It is defined as the natural log of the ratio of a stock's leading 12-month PE to the leading 12-mon… |
| `mdl77_2liquidityriskfactor_idb` | MATRIX | Basic Defensive Interval: It measures how many days that a company can cover its daily operating expenses (cost of go… |
| `mdl77_2liquidityriskfactor_impduration` | MATRIX | Implied Equity Duration: It is an equity risk measure based on Macaulay's traditional measure of bond duration. It co… |
| `mdl77_2liquidityriskfactor_iqa` | MATRIX | Asset Quality Index: It is defined as the year-over-year change of 1 minus the ratio of current assets plus PP&E divi… |
| `mdl77_2liquidityriskfactor_lfd` | MATRIX | The sum of the trailing 12-month pretax income and the trailing 12-month interest expense divided by the trailing 12-… |
| `mdl77_2liquidityriskfactor_liqcoeff` | MATRIX | Liquidity Coefficient: It is the slope of the regression between the monthly stock trading turnover ratio (X) and the… |
| `mdl77_2liquidityriskfactor_mad3yttmni` | MATRIX | 3-Year MAD of TTM Net Income: It is defined as the mean absolute deviation of the last 12 quarters' trailing 12-month… |
| `mdl77_2liquidityriskfactor_mad3yttmsale` | MATRIX | 3-yr MAD of TTM Sales: It is defined as the mean absolute deviation of 12-quarter trailing 12-month sales deflated by… |
| `mdl77_2liquidityriskfactor_milliq` | MATRIX | Stock Illiquidity: It is defined as the monthly average of the daily absolute return to the daily dollar trading volu… |
| `mdl77_2liquidityriskfactor_mktcappera` | MATRIX | Stock's current market cap divided by the number of analysts providing Fiscal Year 1 earnings estimates. |
| `mdl77_2liquidityriskfactor_mktlev` | MATRIX | Stock's total market value plus the most recent reported quarterly book debt, then divided by the market value. |
| `mdl77_2liquidityriskfactor_monchgsip` | MATRIX | Monthly Change in Short Interest Position: It is defined as the month-to-month change of the ratio of shares sold sho… |
| `mdl77_2liquidityriskfactor_netcashp` | MATRIX | Net Cash to Equity: It is defined as most recently reported quarterly cash & equivalents less the long-term debt and … |
| `mdl77_2liquidityriskfactor_nfaldebt` | MATRIX | Net Fixed Assets to Long-term Debt: It is defined as the most recent quarterly reported net fixed assets divided by t… |
| `mdl77_2liquidityriskfactor_nlassets` | MATRIX | Natural Logarithm of Total Assets: It is defined as the natural logarithm of the most recent quarterly reported total… |
| `mdl77_2liquidityriskfactor_nlmktcap` | MATRIX | Natural Logarithm of Market Capitalization: It is defined as the natural logarithm of the cubic of a stock's total ma… |
| `mdl77_2liquidityriskfactor_nlprice` | MATRIX | Natural Logarithm of Closing Price: It is defined as the natural logarithm of the cubic of a stock's unadjusted closi… |
| `mdl77_2liquidityriskfactor_nlsales` | MATRIX | Natural Logarithm of TTM Sales: It is defined as the natural logarithm of the cubic of a company's trailing 12-month … |
| `mdl77_2liquidityriskfactor_nlvolcap` | MATRIX | The natural logarithm of the quotient of the trailing 1-year average of the monthly volume to the trailing 1-year ave… |
| `mdl77_2liquidityriskfactor_numest` | MATRIX | The number of analysts' earnings estimates for fiscal year 1 for a stock. |
| `mdl77_2liquidityriskfactor_ocfratio` | MATRIX | Operating Cash Flow Ratio: It is defined as a stock's most recently reported quarterly cash flow from operations divi… |
| `mdl77_2liquidityriskfactor_ohlsonscore` | MATRIX | Ohlson Bankruptcy Score: It is a model assessing a company's probability of bankruptcy by considering firm size, capi… |
| `mdl77_2liquidityriskfactor_oplev` | MATRIX | Operating Leverage: It is defined as the percent change in the trailing 12-month operating income from the previous q… |
| `mdl77_2liquidityriskfactor_pcurlia` | MATRIX | Current Liabilities-to-Price: It is defined as a stock's most recently reported quarterly current liabilities per sha… |
| `mdl77_2liquidityriskfactor_rerror60m` | MATRIX | Regression Error of 60-Month CAPM: It is defined as the standard error of the slope of the least squares regression l… |
| `mdl77_2liquidityriskfactor_rq` | MATRIX | Quick Ratio: It is defined as the current assets less inventories from most recent quarter divided by the total curre… |
| `mdl77_2liquidityriskfactor_si_ratio` | MATRIX | Short Interest Ratio: It is defined as the number of shares sold short divided by the average daily trading volume of… |
| `mdl77_2liquidityriskfactor_sigma` | MATRIX | Stock Return Volatility: It is defined as the standard deviation of a stock's monthly returns in the prior 60 months. |
| `mdl77_2liquidityriskfactor_sip` | MATRIX | Short Interest Position: It is defined as the number of shares sold short divided by common shares outstanding. |
| `mdl77_2liquidityriskfactor_tobinq` | MATRIX | Tobin q: It is defined as the market value of equity (E) plus debt (D) divided by assets (A), or (E + D)/A. D is meas… |
| `mdl77_2liquidityriskfactor_totalcov` | MATRIX | Total Coverage: It equals (Cash Flow from Operations + Interest Paid + Tax Paid) / (Interest + Principal Paid). |
| `mdl77_2liquidityriskfactor_voctni` | MATRIX | Interest Coverage: It is defined as the most recently reported quarterly operating income before depreciation divided… |
| `mdl77_2liquidityriskfactor_voldiff_pc` | MATRIX | ATM Put Volatility - ATM Call Volatility: It is defined as the difference between the time-weighted average implied v… |
| `mdl77_2liquidityriskfactor_volto` | MATRIX | Trading Turnover Ratio: It is defined as the monthly total trading volume divided by the most recently reported total… |
| `mdl77_2liquidityriskfactor_yoychgcr` | MATRIX | Year-over-year Change in Current Ratio: It is defined as the most recent reported quarterly current ratio and the cur… |
| `mdl77_2liquidityriskfactor_yoychgda` | MATRIX | Year-over-year Change in Leverage: It is defined as the difference between the most recent reported quarterly total l… |
| `mdl77_2me_am_amv` | MATRIX | Reported Earnings Momentum: This submodule is 50% Standardized Unexpected Cash Flow, 25% Real Earnings Surprise, and … |
| `mdl77_2min1ygrossmargin` | MATRIX | 1-Year Trough Gross Margin: It is defined as the 1-year minimum value of a stock's quarterly gross profit margin. |
| `mdl77_2min1yopmargin` | MATRIX | 1-Year Trough Operating Margin: It is defined as the 1-year minimum value of a stock's quarterly operating profit mar… |
| `mdl77_2min2ygrossmargin` | MATRIX | 2-Year Trough Gross Margin: It is defined as the 2-year minimum value of a stock's quarterly gross profit margin. |
| `mdl77_2min2yopmargin` | MATRIX | 2-Year Trough Operating Margin: It is defined as the 2-year minimum value of a stock's quarterly operating profit mar… |
| `mdl77_2min3ygrossmargin` | MATRIX | 3-Year Trough Gross Margin: It is defined as the 3-year minimum value of a stock's quarterly gross profit margin. |
| `mdl77_2min3yopmargin` | MATRIX | 3-Year Trough Operating Margin: It is defined as the 3-year minimum value of a stock's quarterly operating profit mar… |
| `mdl77_2momemtumanalystmodel_ghcfcfmtt_amq` | MATRIX | Change in TTM Free Cash Flow Rank: It is defined as the 2Q change in a stock's trailing twelve-month free cash flow, … |
| `mdl77_2momemtumanalystmodel_htwrgspe_amq` | MATRIX | Earnings Growth Rank: It is defined as the one-quarter change in a stock's trailing twelve-month earnings per share, … |
| `mdl77_2momemtumanalystmodel_jdaksr_amq` | MATRIX | Risk Adjustments Rank: It is defined as the aggregation of five non-linear price and trading volume volatility and gr… |
| `mdl77_2momemtumanalystmodel_qma_alpha6m` | MATRIX | Six-Month Alpha Change Rank: It is defined as the 6-month change in a stock's 12-month alpha, as calculated by a roll… |
| `mdl77_2momemtumanalystmodel_qma_chgnowc` | MATRIX | Change in Net Working Capital Rank: It is defined as the one-quarter change in a stock's recent net current working c… |
| `mdl77_2momemtumanalystmodel_qma_composite` | MATRIX | The composite of the Earnings Momentum Rank, the Analyst Expectations Rank, the Earnings-Price Link Rank, and the Rel… |
| `mdl77_2momemtumanalystmodel_qma_condsurp` | MATRIX | Conditional Surprise Rank: It is defined as the average of a stock's recent earnings surprise, its cost of goods sold… |
| `mdl77_2momemtumanalystmodel_qma_earnexp` | MATRIX | Analyst Expectations Rank: It is defined as the equal weighted average of the Earnings Revisions and the Ratings Chan… |
| `mdl77_2momemtumanalystmodel_qma_eplinkage` | MATRIX | The equal-weighted average of the Change in Free Cash Flow Rank, the Industry Relative 3-Month Return Rank, the Marke… |
| `mdl77_2momemtumanalystmodel_qma_estrev` | MATRIX | Estimate Revisions Rank: It is defined as the difference between the number of recent upward and downward revisions t… |
| `mdl77_2momemtumanalystmodel_qma_indrelrtn3m` | MATRIX | The difference of a company's 3-month profit compared to its respective industry classification. |
| `mdl77_2momemtumanalystmodel_qma_lagpricemo` | MATRIX | Lagged 12- to 1-Month Price MomRank: It is defined as the difference between a stock's lagged 12-month return and its… |
| `mdl77_2momemtumanalystmodel_qma_mktresponse` | MATRIX | Market Earnings Response Rank: It is defined as the 4-day return for a stock, spanning the 2 days before to the day a… |
| `mdl77_2momemtumanalystmodel_qma_ratingchg` | MATRIX | The trend in sell-side analysts' consensus ratings (standardized 1 = strong buy to 5 = strong sell) revisions over th… |
| `mdl77_2momemtumanalystmodel_qma_relpricemo` | MATRIX | Relative Price Momentum Rank: It is defined as the equal-weighted average of the Lagged 12- to 1-Month Price Momentum… |
| `mdl77_2momemtumanalystmodel_qma_repearnmom` | MATRIX | Earnings Momentum Rank: It is defined as the equal-weighted average of the Earnings Growth and Earnings Surprise Rank… |
| `mdl77_2mp_am_amv` | MATRIX | Price Momentum: This submodule is 30% 5-day Industry Relative Return, 30% Industry-adjusted 12-month Relative Price S… |
| `mdl77_2mqf_ags` | MATRIX | SG&A Expenses-to-Sales: It is defined as the trailing 12-month selling, general management, and administration expens… |
| `mdl77_2mqf_aoer` | MATRIX | Retained Earnings-to-Total Assets: It is defined as the reported cumulative retained earnings from the most recent qu… |
| `mdl77_2mqf_aor` | MATRIX | Return on Assets: It is defined as the trailing 12-month income before extra items divided by the average of total as… |
| `mdl77_2mqf_aspanratio` | MATRIX | Stock's quarterly operating assets minus its operating liabilities deflated by the lagged total assets. |
| `mdl77_2mqf_astto` | MATRIX | Assets Turnover Ratio: It is defined as the trailing 12-month sales divided by the most recently reported quarterly a… |
| `mdl77_2mqf_bmpo` | MATRIX | Operating Profit Margin: It is defined as the most recently reported quarterly operating income divided by the corres… |
| `mdl77_2mqf_capexast` | MATRIX | Capital Expenditure-to-Total Assets: It is defined as trailing 12-month capital expenditures divided by the total ass… |
| `mdl77_2mqf_capexsale` | MATRIX | TTM Capital Expenditures-to-Sales: It is defined as trailing 12-month capital expenditures divided by trailing 12-mon… |
| `mdl77_2mqf_cashburnrate` | MATRIX | Cash Burn Rate: It is defined as: -(Cash From Operations + Cash from Investments) / (Cash + Short-term Investments). |
| `mdl77_2mqf_cashc` | MATRIX | Cash Cycle: It is defined as the average inventory days plus the average collection days minus the average payable days. |
| `mdl77_2mqf_cashsale` | MATRIX | The company's performance in trailing 1-year before taking into account non-recurring gain or loss, divided by its mo… |
| `mdl77_2mqf_cfita` | MATRIX | TTM Cash Flow from Investment to Total Assets: It is defined as the trailing 12-month cash flow from the investing po… |
| `mdl77_2mqf_cfroi` | MATRIX | Cash Flow Return on Invested Capital: It is defined as the trailing 12-month cash flow divided by the average investe… |
| `mdl77_2mqf_chgnoa` | MATRIX | Change in Net Operating Assets: It is defined as the year-over-year change of net operating assets to total assets, w… |
| `mdl77_2mqf_chgollev` | MATRIX | Change in Operating Liability Leverage: It is defined as the current quarter operating liability leverage less the op… |
| `mdl77_2mqf_chgreccast` | MATRIX | YOY Chg in Acct Receivable to Current Assets: It is defined as the percent change in the most recent quarterly report… |
| `mdl77_2mqf_cws` | MATRIX | Working Capital-to-Trailing 12-Month Sales: It is defined as the average of working capital for the trailing 12 month… |
| `mdl77_2mqf_divcf` | MATRIX | Dividends-to-Cash Flow: It is defined as the trailing 12-month cash dividends divided by the trailing 12-month cash f… |
| `mdl77_2mqf_equityto` | MATRIX | The trailing 12-month sales divided by the average of trailing 12-month reported book equity. |
| `mdl77_2mqf_fcfroi` | MATRIX | Free Cash Flow Return on Invested Capital: It is defined as the trailing 12-month free cash flow divided by the avera… |
| `mdl77_2mqf_fcfsale` | MATRIX | TTM Free Cash Flow-to-TTM Sales: It is defined as the trailing 12-month free cash flow divided by the trailing 12-mon… |
| `mdl77_2mqf_fixastto` | MATRIX | The trailing 12-month sales divided by the average of the total fixed assets in the same period. |
| `mdl77_2mqf_ica` | MATRIX | Abnormal Capital Investment: It is defined as the change in a firm's most recent trailing 12-month capital investment… |
| `mdl77_2mqf_indrelcroe_` | MATRIX | Stock's lagged quarterly return on equity (ROE) minus the average of the ROEs of all stocks in the same industry defl… |
| `mdl77_2mqf_invast` | MATRIX | The current inventory level deflated by the total assets from the most recent quarter. |
| `mdl77_2mqf_mpn` | MATRIX | Net Profit Margin: It is defined as the most recently reported quarterly net income after tax divided by the correspo… |
| `mdl77_2mqf_netdebt` | MATRIX | Net Debt Ratio: It is defined as the net debt divided by the sum of the net debt, preferred stock, and common stock, … |
| `mdl77_2mqf_niper` | MATRIX | Net Income per Employee: It is defined as the income after taxes for the trailing 12-months divided by the number of … |
| `mdl77_2mqf_noato` | MATRIX | Net Operating Asset Turnover: It is defined as trailing 12-month sales divided by the last 4-quarters average net ope… |
| `mdl77_2mqf_nopatmargin` | MATRIX | NOPAT Margin: It is defined as: (Net Income + Interest Expense*(1-Effective Tax Rate))/Net Sales. All items are for t… |
| `mdl77_2mqf_ocfast` | MATRIX | Operating Cash Flow to Assets: It is defined as the trailing 12-month net cash flow from operations divided by the av… |
| `mdl77_2mqf_ocfmargin` | MATRIX | Operating Cash Flow Profit Margin: It is defined as the trailing 12-month cash flow from operations scaled by the tra… |
| `mdl77_2mqf_ocfroi` | MATRIX | Operating Cash Flow Return on Invested Capital: It is defined as the trailing 12-month operating cash flow divided by… |
| `mdl77_2mqf_ollev` | MATRIX | Operating Liability Leverage: It is defined as 1 minus the ratio of (short-term debt + long-term debt + common equity… |
| `mdl77_2mqf_otvni` | MATRIX | Inventory Turnover Ratio: It is defined as the trailing 12-month cost of goods sold divided by the average of invento… |
| `mdl77_2mqf_pca` | MATRIX | Average Collection Period: It is defined as the average of the trailing 12-month reported accounts receivable times 3… |
| `mdl77_2mqf_pinoa` | MATRIX | Pretax Return on Net Operating Assets: It is defined as the trailing 12-month operating income after depreciation div… |
| `mdl77_2mqf_ppa` | MATRIX | Average Payable Period: It is defined as the average of the trailing 12-month accounts payable times 365 divided by t… |
| `mdl77_2mqf_rdsale` | MATRIX | R&D Intensity: It is defined as the average of the research & development expenses in the trailing 12 months deflated… |
| `mdl77_2mqf_revper` | MATRIX | Revenue per Employee: It is defined as the trailing 12-month total sales divided by the number of employees at the en… |
| `mdl77_2mqf_roe` | MATRIX | Return on Equity: It is defined as the trailing 12-month income before extra items divided by the average of common e… |
| `mdl77_2mqf_roic` | MATRIX | Return on Invested Capital: It is defined as the trailing 12-month net income and interest expenses divided by the av… |
| `mdl77_2mqf_vnicw` | MATRIX | Working Capital to Inventory: It is defined as the most recent quarterly reported working capital divided by the inve… |
| `mdl77_2mqf_wcast` | MATRIX | Working Capital-to-Total Assets: It is defined as the average working capital in the trailing 12 months divided by th… |
| `mdl77_2mqf_yoychggpm` | MATRIX | Yearly Change In Gross Profit Margin: It is defined as the most recent quarterly reported gross profit margin minus t… |
| `mdl77_2mqf_yoychgroa` | MATRIX | Yearly Change in Return on Assets: It is defined as the most recent trailing 12-month income before extra items as a … |
| `mdl77_2mrspe_cf` | MATRIX | The 3-month change in analysts' median earnings forecast for a stock's fiscal 1 scaled by the current mean estimate. |
| `mdl77_2nef` | MATRIX | Net External Financing: It is defined as the sum of the net cash from the change in common equity, the change in pref… |
| `mdl77_2over` | MATRIX | Overhead-to-Sales: It is defined as the trailing 12-month operating income less depreciation minus income before extr… |
| `mdl77_2pe_wt` | MATRIX | Time-Weighted Earnings Yield: This factor uses a time-weighted combination of FY1 and FY2 earnings estimates to creat… |
| `mdl77_2pelh_cf` | MATRIX | Street Revision Confidence: It is defined as the sum of the 3-month change in the highest and lowest FY1 earnings est… |
| `mdl77_2priceanalystmodel2_qpa_composite` | MATRIX | Score based on analysts |
| `mdl77_2priceanalystmodel_nspmoc_apq` | MATRIX | Price Analyst Sector-Neutral: Price Analyst Sector-Neutral |
| `mdl77_2priceanalystmodel_qpa_indrs` | MATRIX | Industry Relative Strength: Industry Relative Strength |
| `mdl77_2priceanalystmodel_srjdaksr_apq` | MATRIX | Risk Adj Relative Strength : Risk Adj Relative Strength |
| `mdl77_2pricemomemtummodel2_indrelrtn5d_` | MATRIX | Stock's return in the last 5 days minus the average of the comparable returns of all stocks in the same industry, the… |
| `mdl77_2pricemomemtummodel_pmm_composite` | MATRIX | Score based on price momentum |
| `mdl77_2pricemomemtummodel_rationalalpha` | MATRIX | Rational Decay Alpha: It evaluates stocks based on their historical 12-month market (S&P 500) adjusted excess return … |
| `mdl77_2pricemomemtummodel_relpricestrength_` | MATRIX | Industry-Adjusted 12-Month Relative Price Strength: It is defined as a stock's 12-month relative price strength (PS) … |
| `mdl77_2pricemomemtummodel_visiratio` | MATRIX | The Visibility Ratio: It equals a stock's most recent daily trading volume divided by the average daily trading volum… |
| `mdl77_2pricemomemtummodel_voldiff_pc` | MATRIX | ATM Put Volatility - ATM Call Volatility: It is defined as the difference between the time weighted average implied v… |
| `mdl77_2pricemomentumfactor_5_4op` | MATRIX | One minus the quotient of a stock's last 52-week price exponential moving average divided by its last 4-week price ex… |
| `mdl77_2pricemomentumfactor_6351_rp` | MATRIX | 15/36 Week Stock Price Ratio: It is defined as the moving average of a stock's prices in the last 15 weeks divided by… |
| `mdl77_2pricemomentumfactor_actrtn12m` | MATRIX | 12-Month Active Return with 1-month Lag: It is defined as the percent change in price for a stock from month t-13 to … |
| `mdl77_2pricemomentumfactor_actrtn18m` | MATRIX | 18-Month Active Return with 1-Month Lag: It is defined as the percent change in price for a stock from month t-19 to … |
| `mdl77_2pricemomentumfactor_actrtn1m` | MATRIX | 1-Month Active Return: It is defined as the percent change in price for a stock from month t-1 to month t. |
| `mdl77_2pricemomentumfactor_actrtn24m` | MATRIX | 24-Month Active Return with 1-Month Lag: It is defined as the percent change in price for a stock from month t-25 to … |
| `mdl77_2pricemomentumfactor_actrtn2m` | MATRIX | 2-Month Active Return: It is defined as the percent change in price for a stock from month t-2 to month t. |
| `mdl77_2pricemomentumfactor_actrtn36m` | MATRIX | 36-Month Active Return with 1-Month Lag: It is defined as the percent change in price for a stock from month t-37 to … |
| `mdl77_2pricemomentumfactor_actrtn3m` | MATRIX | 3-Month Active Return: It is defined as the percent change in price for a stock from month t-3 to month t. |
| `mdl77_2pricemomentumfactor_actrtn60m` | MATRIX | 60-Month Active Return with 1-Month Lag: It is defined as the percent change in price for a stock from month t-61 to … |
| `mdl77_2pricemomentumfactor_actrtn6m` | MATRIX | 6-Month Active Return with 1-Month Lag: It is defined as the percent change in price for a stock from month t-7 to mo… |
| `mdl77_2pricemomentumfactor_alpha60m` | MATRIX | 60-Month Alpha: It is defined as the intercept of the regression line which best fits a stock's monthly price return … |
| `mdl77_2pricemomentumfactor_chg6malpha18m` | MATRIX | 6-Month Nominal Change in 18-Month Alpha: It is defined as the 6-month change in a stock's 18-month alpha, which equa… |
| `mdl77_2pricemomentumfactor_chgalpha12m` | MATRIX | 6-Month Nominal Change in 12-Month Alpha: It is defined as the 6-month change in a stock's 12-month alpha, which equa… |
| `mdl77_2pricemomentumfactor_chgalpha36m` | MATRIX | 6-Month Nominal Change in 36-Month Alpha: It is defined as the 6-month change in a stock's 36-month alpha, which equa… |
| `mdl77_2pricemomentumfactor_chgvolpre4y` | MATRIX | 4-Year Change in the Average Trading Volume: It is defined as the change in the most recent 6-month moving average of… |
| `mdl77_2pricemomentumfactor_high52w` | MATRIX | 52-Week High: It is defined as the month-end price divided by the highest monthly closing price in the past 12 months. |
| `mdl77_2pricemomentumfactor_indrelrtn4w_` | MATRIX | 4-week Industry Relative Return: It is defined as a stock's return in the last 4 weeks minus the average of the compa… |
| `mdl77_2pricemomentumfactor_indrelrtn5d_` | MATRIX | Stock's return in the last 5 days minus the average of the comparable returns of all stocks in the same industry, the… |
| `mdl77_2pricemomentumfactor_m42rav` | MATRIX | 24-Month Value at Risk: It is defined as the minimum of a stock's monthly price return in the last 20-month period. |
| `mdl77_2pricemomentumfactor_m6dn2ntr` | MATRIX | Second Preceding 6-Month Return: It is defined as the percent change in a stock's price from month t-12 to month t-7. |
| `mdl77_2pricemomentumfactor_normalmf60d` | MATRIX | The 60-day average of a stock's daily money flow divided by daily total dollar volume. |
| `mdl77_2pricemomentumfactor_ntrm01ff` | MATRIX | Fama-French Momentum: It is defined as the percent change in a stock's price from month t-12 to month t-2. |
| `mdl77_2pricemomentumfactor_p50_00ratio` | MATRIX | 50-200 Day Stock Price Ratio: It is defined as the moving average of a stock's prices in the last 50 days divided by … |
| `mdl77_2pricemomentumfactor_pc_ratio` | MATRIX | Put/Call Ratio: It is defined as the open interest in 7 near-the-money (1 at-the-money, next 3 above and next 3 below… |
| `mdl77_2pricemomentumfactor_pctabv260low` | MATRIX | Price Above Last 260-Day Lowest Trading Price: It is defined as a stock's current closing price divided by its lowest… |
| `mdl77_2pricemomentumfactor_pd09erpvc` | MATRIX | CV of Prior 90-Day Closing Prices: It is defined as the standard deviation of a stock's last 90 days closing prices d… |
| `mdl77_2pricemomentumfactor_rationalalpha` | MATRIX | Rational Decay Alpha: It evaluates stocks based on their historical 12-month market (S&P 500) adjusted excess return … |
| `mdl77_2pricemomentumfactor_rba` | MATRIX | Abnormal Return around QTR Earnings Release: It is defined as the sum of a stock's daily market-adjusted price return… |
| `mdl77_2pricemomentumfactor_relpricestrength_` | MATRIX | Industry-adjusted 12-month Relative Price Strength: It is defined as a stock's 12-month relative price-strength (PS) … |
| `mdl77_2pricemomentumfactor_sharpe36m` | MATRIX | Changes in company's monthly profit in the last 3 years compared to its profit 3 months ago. |
| `mdl77_2pricemomentumfactor_skew90cortn` | MATRIX | Skewness of 90-Day Stock Daily Excess Returns: It is defined as the skewness of the distribution of a stock's daily e… |
| `mdl77_2pricemomentumfactor_skew90drtn` | MATRIX | Skewness of 90-Day Stock Daily Returns: It is defined as the skewness (measure of lack of symmetry) of the distributi… |
| `mdl77_2pricemomentumfactor_slope52wp` | MATRIX | Slope of 52-Week Price Trend Line: It is defined as the 4-week lagged slope coefficient of the least squares regressi… |
| `mdl77_2pricemomentumfactor_slope66wp` | MATRIX | Slope of 66 Week Price Trend Line: It is defined as the 4-week lagged slope coefficient of the least squares regressi… |
| `mdl77_2pricemomentumfactor_sortinoratio` | MATRIX | Sortino Ratio: It is defined as a stock's annualized average monthly total return over the last 36 months less the av… |
| `mdl77_2pricemomentumfactor_tstalp` | MATRIX | 1-Year Price Momentum Indicator: It is defined as: (CORREL*(260-2)^.5)/(1-CORREL^2)^.5. CORREL is the correlation coe… |
| `mdl77_2pricemomentumfactor_varresirtn` | MATRIX | 24-Month Residual Return Variance: It is defined as the variance of a stock's monthly residual return in the last 24 … |
| `mdl77_2pricemomentumfactor_visiratio` | MATRIX | The Visibility Ratio: It equals a stock's most recent daily trading volume divided by the average daily trading volum… |
| `mdl77_2pricemomentumfactor_volpre6m` | MATRIX | The 6-month moving average of average monthly turnover ratio. |
| `mdl77_2pricemomentumfactor_w15tvp` | MATRIX | This field determines the strength of trends and warns of reversals. |
| `mdl77_2pricemomentumfactor_w57w03_rp` | MATRIX | 30-75 Week Stock Price Ratio: It is defined as the moving average of a stock's prices in the last 30 weeks divided by… |
| `mdl77_2pricemomentumfactor_w62isr` | MATRIX | 26-Week Relative Price Strength: It is defined as a stock's most recent weekly closing price divided by its weekly cl… |
| `mdl77_2pricemomentumfactor_w93ntr` | MATRIX | 39-Week Return with 4-week Lag: It is defined as a stock's price change from week t-43 to week t-4. |
| `mdl77_2put_put_capmod` | MATRIX | Capital Strength Module: It is defined as the equal-weighted average of the Industry Relative ROE, Change in Shares O… |
| `mdl77_2put_put_cashburn` | MATRIX | Cash Burn Rate: It is defined as: -(Cash From Operations + Cash from Investments)/(Cash + Short-term Investments). |
| `mdl77_2put_put_chgalpha` | MATRIX | Six-Month Alpha Change Rank: It is defined as the six-month change in a stock's twelve-month alpha, as calculated by … |
| `mdl77_2put_put_chgoll` | MATRIX | Change in Operating Liability Leverage: It is defined as the current quarter operating liability leverage less the op… |
| `mdl77_2put_put_chshrs` | MATRIX | Percent Change in Shares Outstanding: It is defined as the percent change in a company's current number of outstandin… |
| `mdl77_2put_put_dypeg` | MATRIX | Reciprocal of Dividend Yield-adjusted PEG: It is defined as the reciprocal of a stock's forward 12-month P/E ratio di… |
| `mdl77_2put_put_equality` | MATRIX | Earnings Quality Rank: It is defined as the equal weighted composite of the Earnings Shortfall, Change in Inventory, … |
| `mdl77_2put_put_indepsp` | MATRIX | Industry Relative Core EPS to Price: It is defined as a stock's trailing 12-month earnings per share before extra ite… |
| `mdl77_2put_put_indestep` | MATRIX | Industry Relative Leading 4-QTRs EPS to Price: It is defined as a stock's trailing 12-month earnings per share before… |
| `mdl77_2put_put_indfcfp` | MATRIX | Industry Relative Free Cash Flow-to-Price: It is defined as a stock's trailing 12-month free cash flow-to-price ratio… |
| `mdl77_2put_put_indroe` | MATRIX | Company's ability to generate profit. |
| `mdl77_2put_put_momod` | MATRIX | The mean of three components: unexpected changes in expense or profit, and consumer confidence report. |
| `mdl77_2put_put_opincev` | MATRIX | Operating Income to EV: It is defined as a stock's ratio of trailing 4Q operating income to enterprise value (OpInc/EV). |
| `mdl77_2put_put_qualmod` | MATRIX | Quality Module: It is defined as the aggregation of the Earnings Quality (90%) and Short-Interest Ratio (10%) factors. |
| `mdl77_2put_put_siratio` | MATRIX | Short-Interest Ratio: It is defined as short-interest to average monthly volume. |
| `mdl77_2put_put_strevconf` | MATRIX | Street Revision Confidence: It is defined as the sum of the 3-month change in a stock's analysts' highest earnings fo… |
| `mdl77_2put_put_sucf` | MATRIX | Standardized Unexpected Cash Flow: It is defined as a stock's most recent reported quarterly operating cash flow minu… |
| `mdl77_2put_put_totcov` | MATRIX | Total Coverage: It equals (Cash Flow from Operations + Interest Paid + Tax Paid) / (Interest + Principal Paid). |
| `mdl77_2put_put_valmod` | MATRIX | The weighted average of various financial ratios related to a company's profits. |
| `mdl77_2qe_av_amv` | MATRIX | Earnings Quality: This submodule is 20% 1-year Change in Asset Turnover Ratio, 20% Current Cash Flow Debt Coverage, 2… |
| `mdl77_2rel5yfwdep` | MATRIX | 5-yr Relative Leading 12-Month Earnings Yield: It is defined as a stock's current next 4-quarter's consensus analyst … |
| `mdl77_2relativevaluemodel_capacq` | MATRIX | Capital Acquisition Ratio: It is defined as the trailing 12-month operating cash flow less than the trailing 12-month… |
| `mdl77_2relativevaluemodel_fc_estep` | MATRIX | Leading 12-Month Median Earnings Yield: It is defined as the next fiscal year median consensus earnings estimate divi… |
| `mdl77_2relativevaluemodel_fmrelval` | MATRIX | Fielitz & Muller Relative Intrinsic Value: It is defined as a derivative of the two-stage dividend discount model, to… |
| `mdl77_2relativevaluemodel_pfcfmtt` | MATRIX | TTM Free Cash Flow-to-Price: It is defined as the trailing 12-month free cash flow per share for a stock divided by i… |
| `mdl77_2relativevaluemodel_roe` | MATRIX | Return on Equity: It is defined as the trailing 12-month income before extra items divided by the average of common e… |
| `mdl77_2relativevaluemodel_rvm_composite` | MATRIX | Model composite based on an asset's worth that takes into account the value of similar assets. |
| `mdl77_2sensitivityfactor400_actrtn9m` | MATRIX | 9-Month Active Return with 1-Month Lag: It is defined as a stock's price percent change from month t-10 to month t-1. |
| `mdl77_2sensitivityfactor400_apsales` | MATRIX | Asia-Pacific Sales Exposure: It is defined as the annual aggregate sales for Asia-Pacific as reported by the company … |
| `mdl77_2sensitivityfactor400_capexdeplink` | MATRIX | Capital Expenditures to Depreciation Linkage: It is defined as the absolute value of the difference between ranked (1… |
| `mdl77_2sensitivityfactor400_ceroe` | MATRIX | The trailing 12-month funds from operations divided by the average of the current and previous year. |
| `mdl77_2sensitivityfactor400_dsu` | MATRIX | The beta coefficient estimated by a multiple regression of returns on several macroeconomic aspects over 60 months. |
| `mdl77_2sensitivityfactor400_emeasales` | MATRIX | EMEA Sales Exposure: It is defined as the annual aggregate sales for EMEA as reported by the company divided by total… |
| `mdl77_2sensitivityfactor400_inflation` | MATRIX | The beta coefficient estimated by a multiple regression of returns on several macroeconomic aspects over 60 months. |
| `mdl77_2sensitivityfactor400_lasales` | MATRIX | Latin America Sales Exposure: It is defined as the annual aggregate sales for Latin America as reported by the compan… |
| `mdl77_2sensitivityfactor400_nasales` | MATRIX | North America Sales Exposure: It is defined as the annual aggregate sales for North America as reported by the compan… |
| `mdl77_2sensitivityfactor400_oilprice` | MATRIX | The beta coefficient estimated by a multiple regression of returns on several macroeconomic aspects over 60 months. |
| `mdl77_2sensitivityfactor400_pi` | MATRIX | Industrial Production Sensitivity: It is defined as the beta coefficient to Change in Industrial Production, which is… |
| `mdl77_2sensitivityfactor400_prc` | MATRIX | Credit Risk Premium Sensitivity: It is defined as the beta coefficient to Change in Credit Risk Premium, which is est… |
| `mdl77_2sensitivityfactor400_sh` | MATRIX | Housing Starts Sensitivity: It is defined as the beta coefficient to Change in Housing Starts, which is estimated by … |
| `mdl77_2sensitivityfactor400_ttmopincev` | MATRIX | TTM Operating Income to Enterprise Value: It is defined as the trailing 12-month operating income (before depreciatio… |
| `mdl77_2sensitivityfactor400_xiv` | MATRIX | Market Volatility Sensitivity: It is defined as the beta coefficient to Change in Market Volatility, which is estimat… |
| `mdl77_2sensitivityfactor400_yieldsprd` | MATRIX | Yield Curve Slope Sensitivity: It is defined as the beta coefficient to Change in Slope of Term Structure, which is e… |
| `mdl77_2sf_av_amv` | MATRIX | Financial Statement Valuation: This submodule is the equal-weighted average of Price-to-Book ROE Combination, TTM Ope… |
| `mdl77_2si_av_amv` | MATRIX | Investor Sentiment: This submodule is the equal-weighted average of the Short Interest Position, 12-month change in S… |
| `mdl77_2spe1yfvc_cf` | MATRIX | FY1 EPS Estimates Dispersion: It is defined as the standard deviation of analyst earnings estimates for fiscal year 1… |
| `mdl77_2surpriseanalystmodel_qsa_composite` | MATRIX | Surprise Analyst Composite Rank |
| `mdl77_2surpriseanalystmodel_qsa_efficiency` | MATRIX | Fundamentals Rank |
| `mdl77_2surpriseanalystmodel_qsa_estexpect` | MATRIX | Estimate Trend Rank |
| `mdl77_2surpriseanalystmodel_qsa_percent` | MATRIX | Probability of Surprise (%) |
| `mdl77_2surpriseanalystmodel_qsa_surpsn` | MATRIX | Rank based on analysts' surprise |
| `mdl77_2valueanalystmodel_ccaghc_avq` | MATRIX | The 1-year change in a company's trailing 4Q net operating working capital, scaled by current total assets. |
| `mdl77_2valueanalystmodel_qva_alertrank` | MATRIX | The aggregate of the Earnings Quality (50%), Investor Sentiment (25%) and Management Signaling (25%) Rank. |
| `mdl77_2valueanalystmodel_qva_capexdep` | MATRIX | Capex to Depreciation Rank: It is defined as a company's trailing 12-month capital expenditures divided by the traili… |
| `mdl77_2valueanalystmodel_qva_cashflow` | MATRIX | Cash Flow Rank: It is defined as a stock's ratio of trailing 4Q free cash flow to market capitalization (FCF/P). |
| `mdl77_2valueanalystmodel_qva_chgato` | MATRIX | Change in Asset Turnover Rank: It is defined as the one-year change in a company's asset turnover (TTM Sales/Total As… |
| `mdl77_2valueanalystmodel_qva_chginv` | MATRIX | The one-year change in a company's trailing 4Q inventory, scaled by current total assets |
| `mdl77_2valueanalystmodel_qva_composite` | MATRIX | The equal-weighted combinations of ranks based on intrinsic value of stock and the quality of earnings. |
| `mdl77_2valueanalystmodel_qva_earnquality` | MATRIX | Earnings Quality Rank: It is defined as the equal-weighted composite of the Earnings Shortfall, Change in Inventory, … |
| `mdl77_2valueanalystmodel_qva_earnval` | MATRIX | The equal-weighted average of ranks based on price, earnings, growth, and yield. |
| `mdl77_2valueanalystmodel_qva_epmodule` | MATRIX | Earnings Cyclicality Rank: It is defined as the aggregated ranking of a company's 3-year low 4Q EPS to enterprise val… |
| `mdl77_2valueanalystmodel_qva_finstmt` | MATRIX | Financial Statement Rank: It is defined as the equal-weighted average of the Income Statement Rank (OpInc/Price), the… |
| `mdl77_2valueanalystmodel_qva_invsentiment` | MATRIX | The equal weighted sum based on a ratio of number of stocks and those that have been sold short by investors. |
| `mdl77_2valueanalystmodel_qva_mgtsignaling` | MATRIX | The sum of the indicators based on the changes in the number of stocks, and the company's financial status. |
| `mdl77_2valueanalystmodel_qva_pegy` | MATRIX | PEGY Rank: It is defined as the aggregated ranking of a company's price, earnings, estimated long-term growth, and di… |
| `mdl77_2valueanalystmodel_qva_shortfall` | MATRIX | Earnings Shortfall Rank: It is defined as the difference between recent 4Q operating income before depreciation and t… |
| `mdl77_2valueanalystmodel_qva_valuation` | MATRIX | Valuation Rank: It is defined as the equal-weighted average of the Financial Statement Rank and the Earnings Valuatio… |
| `mdl77_2valueanalystmodel_qva_yoychgdebt` | MATRIX | Chg in Debt Issuance Rank: It is defined as a company's change in total debt over the last 12 months. |
| `mdl77_2valueanalystmodel_qva_yoychgshares` | MATRIX | Change in Shares Outstanding Rank: It is defined as a company's change in common shares outstanding over the last 12 … |
| `mdl77_2valueanalystmodel_tmtscni_avq` | MATRIX | Income Stmt Rank: It is defined as a stock's ratio of trailing 4Q operating income to enterprise value (OpInc/EV). |
| `mdl77_2valuemomemtummodel_earningsexpectationmodule` | MATRIX | Earnings Expectation Module |
| `mdl77_2valuemomemtummodel_earningspricelinkmodule` | MATRIX | Earnings-Price Link Module |
| `mdl77_2valuemomemtummodel_earningsqualitymodule` | MATRIX | Earnings Quality Module |
| `mdl77_2valuemomemtummodel_earningsvaluationmodule` | MATRIX | Earnings Valuation Module |
| `mdl77_2valuemomemtummodel_financialstatementmodule` | MATRIX | Financial Statement Module |
| `mdl77_2valuemomemtummodel_investorsentimentmodule` | MATRIX | Investor Sentiment Module |
| `mdl77_2valuemomemtummodel_managementsignalingmodule` | MATRIX | Management Signaling Module |
| `mdl77_2valuemomemtummodel_pricemomentummodule` | MATRIX | Price Momentum Module |
| `mdl77_2valuemomemtummodel_reportedearningsmomentummodule` | MATRIX | Reported Earnings Momentum Module |
| `mdl77_2valuemomemtummodel_vm_compositesn` | MATRIX | Model composition based on momentum with sector neutral |
| `mdl77_2valuemomemtummodel_vma_composite` | MATRIX | Model composition based on momentum |
| `mdl77_2ve_av_amv` | MATRIX | The equal-weighted average of financial ratios based on a company's profits. |
| `mdl77_400_6351_rp` | MATRIX | 15/36 Week Stock Price Ratio: It is defined as the moving average of a stock's prices in the last 15 weeks divided by… |
| `mdl77_400_booklev` | MATRIX | Book Leverage: It is defined as the most recently reported quarterly total assets divided by the book equity. |
| `mdl77_400_capexast` | MATRIX | Capital Expenditure-to-Total Assets: It is defined as trailing 12-month capital expenditures divided by the total ass… |
| `mdl77_400_cashburnrate` | MATRIX | Cash Burn Rate: It is defined as: -(Cash From Operations + Cash from Investments)/(Cash + Short-term Investments). |
| `mdl77_400_curindbp_` | MATRIX | Industry Relative Book-to-Market: It is defined as a stock's current book-to-price ratio (BP) less the average of the… |
| `mdl77_400_curindebitdap_` | MATRIX | Industry Relative TTM EBITDA-to-Price: It is defined as a stock's trailing 12-month EBITDA-to-price ratio (EBITDAP) l… |
| `mdl77_400_curindep_` | MATRIX | Industry Relative TTM EPS-to-Price: It is defined as a stock's trailing 12-month earnings per share before extra item… |
| `mdl77_400_curindfcfp_` | MATRIX | Industry Relative TTM Free Cash Flow-to-Price: It is defined as a stock's trailing 12-month free cash flow-to-price r… |
| `mdl77_400_curindsp_` | MATRIX | Industry Relative TTM Sales-to-Price: It is defined as a stock's trailing 12-month sales-to-price ratio (SP) less the… |
| `mdl77_400_fc_proformaep` | MATRIX | TTM Pro Forma Earnings-to-Price: It is defined as the trailing 12-month earnings scaled by the trading price. |
| `mdl77_400_fcus` | MATRIX | Standardized Unexpected Cash Flow: It is defined as the most recent quarterly operating cash flow minus that of 4 qua… |
| `mdl77_400_fy1epsskew` | MATRIX | The skewness of the distribution of a series of leading 12-month earnings consensus estimates. |
| `mdl77_400_indrelrecd_` | MATRIX | Industry-adjusted Doubtful Account Receivables: It is defined as a stock's asset-adjusted annual doubtful receivables… |
| `mdl77_400_indrelrtn4w_` | MATRIX | 4-week Industry Relative Return: It is defined as a stock's return in the last 4 weeks minus the average of the compa… |
| `mdl77_400_indrelrtn5d_` | MATRIX | Stock's return in the last 5 days minus the average of the comparable returns of all stocks in the same industry, the… |
| `mdl77_400_p50_200ratio` | MATRIX | 50-200 Day Stock Price Ratio: It is defined as the moving average of a stock's prices in last 50 days divided by the … |
| `mdl77_400_pctchgqtrast` | MATRIX | 1-yr Change in Total Assets: It is defined as the growth in the most recent reported quarterly total assets per share… |
| `mdl77_400_pcurlia` | MATRIX | Current Liabilities-to-Price: It is defined as a stock's most recently reported quarterly current liabilities per sha… |
| `mdl77_400_rau` | MATRIX | Unexpected Change in Accounts Receivable: It is defined as the difference between current accounts receivable and the… |
| `mdl77_400_rba` | MATRIX | Abnormal Return around QTR Earnings Release: It is defined as the sum of a stock's daily market-adjusted price return… |
| `mdl77_400_rdsale` | MATRIX | R&D Intensity: It is defined as the average of the research & development expenses in the trailing 12-months deflated… |
| `mdl77_400_reinrate` | MATRIX | Reinvestment Rate: It is defined as the trailing 12-month earnings per share before extra items less the trailing 12-… |
| `mdl77_400_roic` | MATRIX | Return on Invested Capital: It is defined as the trailing 12-month net income and interest expenses divided by the av… |
| `mdl77_400_sue` | MATRIX | Standardized Unexpected Earnings: It is defined as the most recent quarterly earnings per share minus that of 4 quart… |
| `mdl77_400_tobinq` | MATRIX | Tobin q: It is defined as the market value of equity (E) plus debt (D) divided by assets (A), or (E + D)/A. D is meas… |
| `mdl77_400_ttmaccu` | MATRIX | Accounting Accruals: It is defined as the difference between the trailing 12-month net income and the trailing 12-mon… |
| `mdl77_400_ttmsaleev` | MATRIX | TTM Sales-to-Enterprise Value: It is defined as the trailing 12-month sales for a stock divided by the most recent en… |
| `mdl77_400_visiratio` | MATRIX | The Visibility Ratio: It equals a stock's most recent daily trading volume divided by the average daily trading volum… |
| `mdl77_400_yoychgda` | MATRIX | Year-over-year Change in Leverage: It is defined as the difference between the most recent reported quarterly total l… |
| `mdl77_actrtn1m` | MATRIX | 1-Month Active Return: It is defined as the percent change in price for a stock from month t-1 to month t. |
| `mdl77_altmanz` | MATRIX | Altman Z Score: Altman Z = 1.2* (Current Assets - Current Liabilities)/TA + 1.4*Retained Earnings/TA + 3.3*Earnings b… |
| `mdl77_aspanratio` | MATRIX | Stock's quarterly operating assets minus its operating liabilities deflated by the lagged total assets |
| `mdl77_astcomp` | MATRIX | Asset Composition: It is defined as the total current assets from the most recent quarter divided by the total assets… |
| `mdl77_astto` | MATRIX | Assets Turnover Ratio: It is defined as the trailing 12-month sales divided by the most recently reported quarterly a… |
| `mdl77_atmcallvol` | MATRIX | At the Money Call Option Implied Volatility: It is defined as the time-weighted average implied volatility of the nea… |
| `mdl77_cashsev` | MATRIX | Cash to Enterprise Value: It is defined as the total cash & equivalents divided by the sum of the market value of com… |
| `mdl77_ccacw` | MATRIX | Working Capital Accruals: It equals to: Increase in Accounts Receivables + Increase in Inventory + Decrease in Accoun… |
| `mdl77_chgnoa` | MATRIX | Change in Net Operating Assets: It is defined as the year-over-year change of net operating assets to total assets, w… |
| `mdl77_chgollev` | MATRIX | Change in Operating Liability Leverage: It is defined as the current quarter operating liability leverage less the op… |
| `mdl77_chgsgasale` | MATRIX | Change in QTR SG&A Expenses vs Sales: It is defined as the difference between the yearly change in quarterly Selling,… |
| `mdl77_curratio` | MATRIX | Current Ratio: It is defined as the reported current assets from most recent quarter divided by the current liabiliti… |
| `mdl77_deepvaluefactor_apemtt` | MATRIX | An indicator that standardizes and compares relative share price between time periods and among companies. |
| `mdl77_deepvaluefactor_bpemtt` | MATRIX | The company's performance in trailing 1-year before taking into account non-recurring gain or loss. Stock divided by … |
| `mdl77_deepvaluefactor_cashp` | MATRIX | Cash-to-Price: It is defined as the most recently reported cash and equivalents per share of a company divided by tra… |
| `mdl77_deepvaluefactor_cashsev` | MATRIX | Cash to Enterprise Value: It is defined as the total cash & equivalents divided by the sum of the market value of com… |
| `mdl77_deepvaluefactor_coreepsp` | MATRIX | TTM Core Earnings-to-Price: It is defined as the trailing 12-month earnings per share from operations for a stock def… |
| `mdl77_deepvaluefactor_curep` | MATRIX | Current Earnings Yield: It is defined as the sum of the most recently reported 3 quarters EPS and analysts' consensus… |
| `mdl77_deepvaluefactor_divyield` | MATRIX | TTM Dividend Yield: It is defined as the trailing 12-month dividends per share for a stock divided by its month-end t… |
| `mdl77_deepvaluefactor_ebitdaev` | MATRIX | TTM EBITDA-to-Enterprise Value: It is defined as the trailing 12-month earnings before interest, taxes, depreciation,… |
| `mdl77_deepvaluefactor_ebitdap` | MATRIX | TTM EBITDA-to-Price: It is defined as the trailing 12-month earnings before interest, taxes, depreciation, and amorti… |
| `mdl77_deepvaluefactor_ebop` | MATRIX | Edwards-Bell-Ohlson Value-to-Price: It is defined as a stock's valuation based on the Edwards-Bell-Ohlson (EBO) model… |
| `mdl77_deepvaluefactor_estep` | MATRIX | Leading 12-Month Median Earnings Yield: It is defined as the next fiscal year median consensus earnings estimate divi… |
| `mdl77_deepvaluefactor_indidivy` | MATRIX | Indicated Dividend Yield: It is defined as the last quarterly dividend declared multiplied by 4, scaled by month-end … |
| `mdl77_deepvaluefactor_lumqca` | MATRIX | Acquisition Multiple: It is defined as the most recent quarterly reported invested capital divided by the trailing 12… |
| `mdl77_deepvaluefactor_nnastp` | MATRIX | Net Current Assets-to-Price: It is defined as the current assets per share minus total liabilities per share divided … |
| `mdl77_deepvaluefactor_past` | MATRIX | Price-to-Total Assets: It is defined as a stock's month-end trading price divided by the most recent quarterly report… |
| `mdl77_deepvaluefactor_pb` | MATRIX | Book-to-Market: It is defined as the most recently reported book value per share for a stock deflated by its month-en… |
| `mdl77_deepvaluefactor_pedwf` | MATRIX | Leading 12-Month Mean Earnings Yield: It is defined as the next 4-quarter's mean consensus earnings estimate divided … |
| `mdl77_deepvaluefactor_pfcf` | MATRIX | Forward Free Cash Flow-to-Price: It is defined as the next 4-quarter's mean consensus earnings estimate plus trailing… |
| `mdl77_deepvaluefactor_pfcfmtt` | MATRIX | TTM Free Cash Flow-to-Price: It is defined as the trailing 12-month free cash flow per share for a stock divided by i… |
| `mdl77_deepvaluefactor_pfcmtt` | MATRIX | TTM Cash Flow-to-Price: It is defined as the trailing 12-month cash flows per share for a stock scaled by its trading… |
| `mdl77_deepvaluefactor_pfcomtt` | MATRIX | TTM Operating Cash Flow-to-Price: It is defined as the trailing 12-month operating cash flow per share for a stock di… |
| `mdl77_deepvaluefactor_pfgmtt` | MATRIX | TTM Growth Flow-to-Price: It is defined as the sum of trailing 12-month growth flow value per share for a stock divid… |
| `mdl77_deepvaluefactor_pqipmtt` | MATRIX | The most recent trailing 12-month operating and nonoperating income per share before provisions for income taxes and … |
| `mdl77_deepvaluefactor_proformaep` | MATRIX | TTM Pro Forma Earnings-to-Price: It is defined as the trailing 12-month earnings scaled by the trading price. |
| `mdl77_deepvaluefactor_psmtt` | MATRIX | TTM Sales-to-Price: It is defined as the most recently reported trailing 12-month sales per share for a stock deflate… |
| `mdl77_deepvaluefactor_pvan` | MATRIX | Net Asset Value to Price: It is defined as the most recent book value of net assets per share (NAV) by the closing pr… |
| `mdl77_deepvaluefactor_ttmcapexp` | MATRIX | TTM Capital Expenditures-to-Price: It is defined as the trailing 12-month capital expenditures per share for a stock … |
| `mdl77_deepvaluefactor_ttmsaleev` | MATRIX | TTM Sales-to-Enterprise Value: It is defined as the trailing 12-month sales for a stock divided by the most recent en… |
| `mdl77_deepvaluefactor_vefcfmtt` | MATRIX | TTM Free Cash Flow-to-Enterprise Value: It is defined as the trailing 12-month free cash flow (FCF) for a stock scale… |
| `mdl77_deepvaluefactor_vesspem21f` | MATRIX | Forward 12-Month EPS-to-Enterprise Value: It is defined as the consensus forward 12-month earnings per share forecast… |
| `mdl77_deepvaluefactor_ydp` | MATRIX | Predicted Dividend Yield: It is defined as an assumed payout ratio multiplied by the next 4-quarter consensus earning… |
| `mdl77_devnorthamericashortsentimentfactor_act_util` | MATRIX | Account Utility |
| `mdl77_devnorthamericashortsentimentfactor_benchmark_fee` | MATRIX | Benchmark fee |
| `mdl77_devnorthamericashortsentimentfactor_conc_ratio` | MATRIX | Concentration ratio |
| `mdl77_devnorthamericashortsentimentfactor_days_to_cover` | MATRIX | Days to Cover |
| `mdl77_devnorthamericashortsentimentfactor_dmd_conc` | MATRIX | Demand concentration |
| `mdl77_devnorthamericashortsentimentfactor_dmd_supply` | MATRIX | Demand Supply |
| `mdl77_devnorthamericashortsentimentfactor_inv_conc` | MATRIX | Inventory concentration |
| `mdl77_devnorthamericashortsentimentfactor_lend_supply` | MATRIX | Lend supply |
| `mdl77_devnorthamericashortsentimentfactor_onloan_conc` | MATRIX | On loan concentration |
| `mdl77_devnorthamericashortsentimentfactor_tni_ths` | MATRIX | Short Interest Ratio |
| `mdl77_devnorthamericashortsentimentfactor_util` | MATRIX | Utility |
| `mdl77_divcov` | MATRIX | Company's trailing 1-year profits scaled by its annual dividends. |
| `mdl77_earningmomentumfactor_dypeg` | MATRIX | Reciprocal of Dividend Yield-adjusted PEG: It is defined as the reciprocal of a stock's forward 12-month P/E ratio di… |
| `mdl77_earningmomentumfactor_fcfroey1p` | MATRIX | Product of TTM FCF Yield and Forward ROE: It is defined as the trailing 12-month free cash flow per share multiplied … |
| `mdl77_earningmomentumfactor_fcus` | MATRIX | Standardized Unexpected Cash Flow: It is defined as the most recent quarterly operating cash flow minus that of 4 qua… |
| `mdl77_earningmomentumfactor_fqsurstd` | MATRIX | Most Recent Earnings Surprise: It is defined as the most recent quarterly earnings surprise (actual fiscal quarter EP… |
| `mdl77_earningmomentumfactor_fy1epsskew` | MATRIX | The skewness of the distribution of a series leading 12-month earnings consensus estimates. |
| `mdl77_earningmomentumfactor_gspea1q` | MATRIX | 1-Quarter Ahead EPS Growth: It is defined as a stock's most recent fiscal quarter consensus earnings forecast less th… |
| `mdl77_earningmomentumfactor_gspea1y` | MATRIX | 1-Year Ahead EPS Growth: It is defined as the most recent consensus earnings forecast for the next 4-quarters minus t… |
| `mdl77_earningmomentumfactor_gspea2y` | MATRIX | 2-Year Ahead EPS Growth: It is defined as the most recent consensus earnings forecast for fiscal year 2 minus the con… |
| `mdl77_earningmomentumfactor_gtl` | MATRIX | Long-Term Growth Rate Estimates: It is defined as the consensus long-term growth forecast. It generally represents an… |
| `mdl77_earningmomentumfactor_gtlm6ghc` | MATRIX | 6-M Change in Long-term Growth Estimates: It is defined as the percent change in the most recent mean consensus long-… |
| `mdl77_earningmomentumfactor_lagegp` | MATRIX | Lagged Inverse of PEG Ratio: It is defined as the trailing 12-month earnings per share before extraordinary items tim… |
| `mdl77_earningmomentumfactor_mrspe` | MATRIX | Street Revision Magnitude: It is defined as the 3-month change in the median FY1 consensus earnings forecast, scaled … |
| `mdl77_earningmomentumfactor_numrevq1` | MATRIX | Net Number ofRevisions for Fiscal QTR 1: It is defined as the number of fiscal quarter 1 upward earnings forecast rev… |
| `mdl77_earningmomentumfactor_numrevy1` | MATRIX | Net Number ofRevisions for Fiscal Year 1: It is defined as the weighted average of the number of FY1 analyst earnings… |
| `mdl77_earningmomentumfactor_pelh` | MATRIX | Street Revision Confidence: It is defined as the sum of the 3-month change in the highest and lowest FY1 earnings est… |
| `mdl77_earningmomentumfactor_perg` | MATRIX | Risk-adjusted PEG Ratio: It is defined as the stock price divided by the leading 12-month consensus earnings forecast… |
| `mdl77_earningmomentumfactor_pge` | MATRIX | Estimates on the next 1 year average earnings scaled by company's prospects on growth and its stock price. |
| `mdl77_earningmomentumfactor_qepsferr` | MATRIX | Prior Fiscal Quarter Forecast Error: It is defined as the difference between the actual earnings per share and consen… |
| `mdl77_earningmomentumfactor_ratrev6m` | MATRIX | Street Rating Revision: It is defined as the 6-month average of the change in the average analyst recommendation trac… |
| `mdl77_earningmomentumfactor_rev1q1` | MATRIX | Revision in Fiscal QTR 1 EPS Forecasts: It is defined as the change in the current consensus earnings forecast for fi… |
| `mdl77_earningmomentumfactor_rev3y1` | MATRIX | The change in the analysts' projection on company's performance for fiscal year 1 less that of 3 months ago, deflated… |
| `mdl77_earningmomentumfactor_rev3y2` | MATRIX | 3-M Revision in FY2 EPS Forecasts: It is defined as the change in the current mean consensus earnings estimate for fi… |
| `mdl77_earningmomentumfactor_rev6` | MATRIX | Averaged Last 6-M EPS Revisions for FY1: It is defined as the average of the prior 6 months' monthly changes in a sto… |
| `mdl77_earningmomentumfactor_salesurp` | MATRIX | Sales Surprise: It is defined as the most recent reported quarterly sales minus consensus sales forecasts, divided by… |
| `mdl77_earningmomentumfactor_spe1yfvc` | MATRIX | FY1 EPS Estimates Dispersion: It is defined as the standard deviation of analyst earnings estimates for fiscal year 1… |
| `mdl77_earningmomentumfactor_spe2yfvc` | MATRIX | FY2 EPS Forecast Dispersion: It is defined as the standard deviation of analyst earnings estimates for fiscal year 2 … |
| `mdl77_earningmomentumfactor_stdevfy1epsp` | MATRIX | Std Dev of FY1 EPS Estimates-to-Price: It is defined as the standard deviation of analyst forecasts for fiscal year 1… |
| `mdl77_earningmomentumfactor_stdevfy2epsp` | MATRIX | Std Dev of FY2 EPS Estimates-to-Price: It is defined as the standard deviation of analyst forecasts for fiscal year 2… |
| `mdl77_earningmomentumfactor_stockrating` | MATRIX | Street Consensus Rating: It is defined as the consensus recommendation for a company. |
| `mdl77_earningmomentumfactor_sue` | MATRIX | Standardized Unexpected Earnings: It is defined as the most recent quarterly earnings per share minus that of 4 quart… |
| `mdl77_earningmomentumfactor_surp` | MATRIX | Real Earnings Surprise: It is defined as the difference between the actual earnings per share and consensus forecasts… |
| `mdl77_earningmomentumfactor_y2repsg` | MATRIX | 2-Year Projected EPS Growth: It is defined as the most recent consensus earnings forecast for fiscal year 2 minus the… |
| `mdl77_earningmomentumfactor_y3sur` | MATRIX | Volatility-adj 3-yr Projected EPS Growth: It is defined as the consensus earnings forecast for the current quarter mi… |
| `mdl77_earningsmomemtummodel_chgsup` | MATRIX | Change in EPS Surprise: It is defined as the quarterly change in EPS surprise. |
| `mdl77_earningsmomemtummodel_emm_composite` | MATRIX | Model composition based on earnings momentum |
| `mdl77_earningsmomemtummodel_fc_fcfroey1p` | MATRIX | Product of TTM FCF Yield and Forward ROE: It is defined as the trailing 12-month free cash flow per share multiplied … |
| `mdl77_earningsmomemtummodel_fc_fqsurstd` | MATRIX | Most Recent Quarterly Earnings Surprise: It is defined as a stock's most recent quarterly earnings surprise (actual f… |
| `mdl77_earningsmomemtummodel_fc_numrevy1` | MATRIX | Net Number ofRevisions for Fiscal Year 1: It is defined as the weighted average of the number of FY1 analyst earnings… |
| `mdl77_earningsmomemtummodel_fc_rev3y2` | MATRIX | 3-M Revision in FY2 EPS Forecasts: It is defined as the change in a stock's current analysts mean earnings estimate f… |
| `mdl77_earningsmomemtummodel_fc_y2repsg` | MATRIX | 2-Year Projected EPS Growth: It is defined as a stock's most recent consensus analysts' earnings forecast for fiscal … |
| `mdl77_earningsmomemtummodel_gtl` | MATRIX | Long-Term Growth Rate Estimates: It is defined as the consensus long-term growth forecast. It generally represents an… |
| `mdl77_earningsmomemtummodel_pge_cf` | MATRIX | Estimates on the next 1 year average earnings scaled by company's prospects on growth and its stock price. |
| `mdl77_earningsmomemtummodel_spe2yfvc_cf` | MATRIX | FY2 EPS Forecast Dispersion: It is defined as the standard deviation of analyst earnings estimates for fiscal year 2 … |
| `mdl77_earningsqualityfactor_ccacw` | MATRIX | Working Capital Accruals: It equals to: Increase in Accounts Receivables + Increase in Inventory + Decrease in Accoun… |
| `mdl77_earningsqualityfactor_chgsgasale` | MATRIX | Change in QTR SG&A Expenses vs Sales: It is defined as the difference between the yearly change in quarterly Selling,… |
| `mdl77_earningsqualityfactor_chgshare` | MATRIX | Percent Change in Shares Outstanding: It is defined as the percent change in a company's current number of outstandin… |
| `mdl77_earningsqualityfactor_cogsinvt` | MATRIX | Change in TTM COGS vs Inventory Level: It is defined as the absolute value of the difference between the yearly perce… |
| `mdl77_earningsqualityfactor_cre` | MATRIX | Earnings Response Coefficient: It is defined as the slope coefficient between market-adjusted returns around the time… |
| `mdl77_earningsqualityfactor_dpcapex` | MATRIX | Change in TTM Depreciation vs CapEx: It is defined as the absolute value of the difference between the yearly percent… |
| `mdl77_earningsqualityfactor_epschgetr` | MATRIX | EPS from Change in Effective Tax Rate: It is defined as the trailing 12-month pre-tax income per share times the diff… |
| `mdl77_earningsqualityfactor_indrelrecd_` | MATRIX | Industry-adjusted Doubtful Account Receivables: It is defined as a stock's asset-adjusted annual doubtful receivables… |
| `mdl77_earningsqualityfactor_lccau` | MATRIX | Unexpected Change in Accrued Liabilities: It is defined as the difference between the most recent fiscal year's accru… |
| `mdl77_earningsqualityfactor_opincltd` | MATRIX | Change in TTM Oper Income vs. LT Debt: It is defined as the difference between the yearly percent change in operating… |
| `mdl77_earningsqualityfactor_pau` | MATRIX | Unexpected Change in Accounts Payable: It is defined as the difference between current accounts payable and the expec… |
| `mdl77_earningsqualityfactor_pedu` | MATRIX | Unexpected Change in Depreciation: It is defined as the difference between the trailing 12-month depreciation expense… |
| `mdl77_earningsqualityfactor_rau` | MATRIX | Unexpected Change in Accounts Receivable: It is defined as the difference between current accounts receivable and the… |
| `mdl77_earningsqualityfactor_saleeps` | MATRIX | Change in TTM Sales vs. EPS: It is defined as the absolute value of the difference between the yearly percent change … |
| `mdl77_earningsqualityfactor_salegpm` | MATRIX | Change in QTR Sales vs Gross Margin: It is defined as the difference between the yearly change in the most recent rep… |
| `mdl77_earningsqualityfactor_salerec` | MATRIX | Change in TTM Sales vs Accounts Receivable: It is defined as the difference between the yearly percent change in trai… |
| `mdl77_earningsqualityfactor_spefcn` | MATRIX | Change in TTM EPS vs. Oper Cash Flows: It is defined as the absolute value of the difference between the yearly perce… |
| `mdl77_earningsqualityfactor_ttmaccu` | MATRIX | Accounting Accruals: It is defined as the difference between the trailing 12-month net income and the trailing 12-mon… |
| `mdl77_earningsqualityfactor_vniu` | MATRIX | The difference of inventory between present and expected levels. |
| `mdl77_earningsqualityfactor_yoychgaa` | MATRIX | Change in Accruals to Assets: It is defined as the trailing 12-month income before extra items less the trailing 12-m… |
| `mdl77_earningsqualitymodule` | MATRIX | Earnings Quality Module |
| `mdl77_emmcomposite_emm_composite` | MATRIX | Model composition based on earnings momentum |
| `mdl77_equityto` | MATRIX | The trailing 12-month sales divided by the average of trailing 12-month reported book equity. |
| `mdl77_fa_capacq` | MATRIX | Capital Acquisition Ratio: It is defined as the trailing 12-month operating cash flow less the trailing 12-month cash… |
| `mdl77_fa_ebitdaev` | MATRIX | TTM EBITDA-to-Enterprise Value: It is defined as the trailing 12-month earnings before interest, taxes, depreciation,… |
| `mdl77_fa_fcfroi` | MATRIX | Free Cash Flow Return on Invested Capital: It is defined as the trailing 12-month free cash flow divided by the avera… |
| `mdl77_fa_ollev` | MATRIX | Operating Liability Leverage: It is defined as 1 minus the ratio of (short-term debt + long-term debt + common equity… |
| `mdl77_fa_past` | MATRIX | Price-to-Total Assets: It is defined as a stock's month-end trading price divided by the most recent quarterly report… |
| `mdl77_fa_pb` | MATRIX | Book-to-Market: It is defined as the most recently reported book value per share for a stock deflated by its month-en… |
| `mdl77_fa_pedwf_cf` | MATRIX | Leading 12-Month Mean Earnings Yield: It is defined as the next 4 quarters' mean consensus earnings estimate divided … |
| `mdl77_fa_pfcf_cf` | MATRIX | Forward Free Cash Flow-to-Price: It is defined as the next 4 quarters' mean consensus earnings estimate plus trailing… |
| `mdl77_fa_pfcfmtt` | MATRIX | TTM Free Cash Flow-to-Price: It is defined as the trailing 12-month free cash flow per share for a stock divided by i… |
| `mdl77_fa_pge_cf` | MATRIX | Estimates on the next 1-year average earnings scaled by company's prospects on growth and its stock price. |
| `mdl77_fa_ppa` | MATRIX | Average Payable Period: It is defined as the average of the trailing 12-month accounts payable times 365 divided by t… |
| `mdl77_fa_rq` | MATRIX | Quick Ratio: It is defined as the current assets less inventories from the most recent quarter divided by the total c… |
| `mdl77_fa_vefcfmtt` | MATRIX | TTM Free Cash Flow-to-Enterprise Value: It is defined as the trailing 12-month free cash flow (FCF) for a stock scale… |
| `mdl77_fa_vesspem21f_cf` | MATRIX | Forward 12-M EPS-to-Enterprise Value: It is defined as the consensus forward 12-month earnings per share forecast div… |
| `mdl77_fa_y3fcq4vc` | MATRIX | Stability of 3-yr TTM Cash Flow: It is defined as the standard deviation of the prior 12 quarters' trailing 12-month … |
| `mdl77_fa_ydp_cf` | MATRIX | Predicted Dividend Yield: It is defined as an assumed payout ratio multiplied by the next 4-quarter consensus earning… |
| `mdl77_fangma_dvf22` | MATRIX | Deep value factors 22 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_dvm1` | MATRIX | Deep value model 1 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_dvm2` | MATRIX | Deep Value Model 2 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_dvm3` | MATRIX | Deep value model 3 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_dvm4` | MATRIX | Deep value model 4 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_dvm5` | MATRIX | Deep Value Model 5 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_emf15` | MATRIX | Earnings momentum factors 15 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_emf20` | MATRIX | Earnings Momentum Factors 20 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_emf25` | MATRIX | Earnings momentum factors 25 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_emf28` | MATRIX | Earnings momentum factors 28 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_emf3` | MATRIX | Earnings Momentum Factors 3 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_emf30` | MATRIX | Earnings momentum factors 30 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_emf4` | MATRIX | Earnings momentum factors 4 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_emf6` | MATRIX | Core factors of big IT companies. |
| `mdl77_fangma_gpam1` | MATRIX | to_fill |
| `mdl77_fangma_gpam10` | MATRIX | to_fill |
| `mdl77_fangma_gpam11` | MATRIX | to_fill |
| `mdl77_fangma_gpam5` | MATRIX | to_fill |
| `mdl77_fangma_mam11` | MATRIX | Momentum Analyst Model 11 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_mam16` | MATRIX | Momentum analyst model 16 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_mam2` | MATRIX | Momentum analyst model 2 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_mam3` | MATRIX | Momentum analyst model 3 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_mam4` | MATRIX | Momentum analyst model 5 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_mam5` | MATRIX | Momentum Analyst Model 5 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_mam6` | MATRIX | Momentum Analyst Model 6 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_mam7` | MATRIX | Momentum Analyst Model 7 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_rvm1` | MATRIX | Relative value model 1 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_rvm4` | MATRIX | Relative value model 4 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_rvm6` | MATRIX | Relative Value Model 6 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fangma_vmm11` | MATRIX | Value momentum 11 for FANGMA (Facebook, Apple, Netflix, Google, Microsoft, Amazon) |
| `mdl77_fc_y2repsg` | MATRIX | 2-Year Projected EPS Growth: It is defined as the most recent consensus earnings forecast for fiscal year 2 minus the… |
| `mdl77_fixastto` | MATRIX | The trailing 12-month sales divided by the average of the total fixed assets in the same period. |
| `mdl77_flowratio` | MATRIX | Flow Ratio: It is defined as the difference between current assets and cash & equivalents divided by the difference b… |
| `mdl77_garpanalystmodel_qgp_alert` | MATRIX | Alert Rank: Alert Rank |
| `mdl77_garpanalystmodel_qgp_avgrating` | MATRIX | Avg Analyst Rating: Avg Analyst Rating |
| `mdl77_garpanalystmodel_qgp_capeff` | MATRIX | Capital Effectiveness: Capital Effectiveness |
| `mdl77_garpanalystmodel_qgp_chgvaluation` | MATRIX | 3M Chg in Valuation: 3M Chg in Valuation |
| `mdl77_garpanalystmodel_qgp_composite` | MATRIX | Analyst score based on growth and value investing attributes |
| `mdl77_garpanalystmodel_qgp_growthval` | MATRIX | Growth Valuation : Growth Valuation |
| `mdl77_garpanalystmodel_qgp_relgrowth` | MATRIX | Relative Growth Rank: Relative Growth Rank |
| `mdl77_garpanalystmodel_qgp_relpegy` | MATRIX | Rolling Relative PEGY: Rolling Relative PEGY |
| `mdl77_garpanalystmodel_qgp_roefcf` | MATRIX | ROE x FCF Rank: ROE x FCF Rank |
| `mdl77_garpanalystmodel_qgp_valuation` | MATRIX | Valuation Rank: Valuation Rank |
| `mdl77_garpanalystmodel_qgp_vfpriceratio` | MATRIX | Value to Price Rank: Value to Price Rank |
| `mdl77_garpanalystmodel_qgp_wratingchg` | MATRIX | Weighted Ratings Change |
| `mdl77_growthanalystmodel_qga_composite` | MATRIX | Growth Analyst Composite |
| `mdl77_growthanalystmodel_qga_epscapex` | MATRIX | EPS Growth to CapEx Link |
| `mdl77_growthanalystmodel_qga_epstrend` | MATRIX | EPS Trend |
| `mdl77_growthanalystmodel_qga_fcfroe` | MATRIX | Free Cash Flow ROE |
| `mdl77_growthanalystmodel_qga_iarsales` | MATRIX | Inv Acc Rec to Sales Link |
| `mdl77_growthanalystmodel_qga_ltepssurprise` | MATRIX | Long Term EPS Surprise |
| `mdl77_growthanalystmodel_qga_niroe` | MATRIX | Net Income ROE |
| `mdl77_growthanalystmodel_qga_opmarginsales` | MATRIX | Op Margin to Sales Link |
| `mdl77_gspea2y_cf` | MATRIX | 2-Year Ahead EPS Growth: It is defined as the most recent consensus earnings forecast for fiscal year 2 minus the con… |
| `mdl77_hgm_composite` | MATRIX | Score based on past growth patterns: Historical Growth Model Composite |
| `mdl77_historicalgrowthfactor_cg3ysales` | MATRIX | The geometric growth rate of the trailing 12-month sales per share in the last 12 quarters. |
| `mdl77_historicalgrowthfactor_chg3ycfast` | MATRIX | 3-Yr Change in Assets-Adj TTM Cash Flow: It is defined as the most recently reported trailing 12-month operating cash… |
| `mdl77_historicalgrowthfactor_chg3yepsast` | MATRIX | 3-yr Change in Assets-adj TTM EPS: It is defined as the trailing 12-month earnings per share before extra items (EPS)… |
| `mdl77_historicalgrowthfactor_chg3yepsp` | MATRIX | The difference between the trailing 12-month earnings per share and that of 12-quarters ago for a stock divided by it… |
| `mdl77_historicalgrowthfactor_chg3yfcfast` | MATRIX | 3-yr Chg in Assets-adj TTM Free Cash Flow: It is defined as the trailing 12-month free cash flow minus 12 quarters ag… |
| `mdl77_historicalgrowthfactor_chg3yocfast` | MATRIX | 3-Yr Change in Assets-Adj TTM Oper Cash Flow: It is defined as the most recently reported trailing 12-month operating… |
| `mdl77_historicalgrowthfactor_chgars` | MATRIX | 1-yr Chg in Acct Receivable as Percentage ofSales: It is defined as the change between the last reported accounts rec… |
| `mdl77_historicalgrowthfactor_cv4qsales3y` | MATRIX | The standard deviation of prior 12-quarters' trailing 12-month sales for individual share scaled to the mean of itsel… |
| `mdl77_historicalgrowthfactor_cvopinc` | MATRIX | CV of Oper Income per Share in Last 12 QTRs: It is defined as the standard deviation of the trailing 12-month operati… |
| `mdl77_historicalgrowthfactor_div5yg` | MATRIX | 5-Year Dividend Growth Rate: It is defined as the 5-year growth in dividends. |
| `mdl77_historicalgrowthfactor_fcfequity` | MATRIX | TTM Free Cash Flow to Equity: It is defined as the trailing 12-month free cash flow divided by the average book equit… |
| `mdl77_historicalgrowthfactor_fcfghc` | MATRIX | 1-yr Chg in Assets-adj TTM Free Cash Flow: It is defined as the trailing 12-month free cash flow minus 4 quarters ago… |
| `mdl77_historicalgrowthfactor_fcghc` | MATRIX | 1-Year Change in Assets-Adj TTM Cash Flow: It is defined as the trailing 12-month cash flow minus comparable trailing… |
| `mdl77_historicalgrowthfactor_fcoghc` | MATRIX | 1-yr Chg in Assets-adj TTM Oper Cash Flow: It is defined as the most recently reported trailing 12-month operating ca… |
| `mdl77_historicalgrowthfactor_mpnghc` | MATRIX | 1-Yr Change in Net Profit Margin: It is defined as the most recent quarterly net profit margin (NPM) minus the NPM 4 … |
| `mdl77_historicalgrowthfactor_mpoghc` | MATRIX | 1-Year Change in Operating Profit Margin: It is defined as the most recent quarterly operating profit margin minus th… |
| `mdl77_historicalgrowthfactor_pctchg3ycf` | MATRIX | The percent change in a stock's most recent trailing 12-month cash flow per share as compared to itself 12 quarters ago. |
| `mdl77_historicalgrowthfactor_pctchg3yeps` | MATRIX | The percent change in a stock's most recent trailing 12-month earnings per share as compared to itself 12 quarters ago. |
| `mdl77_historicalgrowthfactor_pctchg3yfcf` | MATRIX | 3-yr Growth in TTM Free Cash Flow: It is defined as the percent change in a stock's most recent trailing 12-month fre… |
| `mdl77_historicalgrowthfactor_pctchg3yocf` | MATRIX | 3-Yr Growth in TTM Oper Cash Flow: It is defined as the percent change in a stock's most recent trailing 12-month ope… |
| `mdl77_historicalgrowthfactor_pctchgastto` | MATRIX | 1-Year Change in Asset Turnover Ratio: It is defined as the percent change in the most recent asset turnover ratio as… |
| `mdl77_historicalgrowthfactor_pctchgcf` | MATRIX | 1-yr Growth in TTM Cash Flow: It is defined as the percent change in a stock's most recent trailing 12-month cash flo… |
| `mdl77_historicalgrowthfactor_pctchgeps` | MATRIX | The percent change in a stock's most recent trailing 12-month earnings per share before extra items as compared to it… |
| `mdl77_historicalgrowthfactor_pctchgfcf` | MATRIX | 1-yr Growth in TTM Free Cash Flow: It is defined as the percent change in a stock's most recent trailing 12-month fre… |
| `mdl77_historicalgrowthfactor_pctchgocf` | MATRIX | 1-yr Growth in TTM Oper Cash Flow: It is defined as the percent change of a stock's most recent trailing 12-month ope… |
| `mdl77_historicalgrowthfactor_pctchgqtrast` | MATRIX | 1-yr Change in Total Assets: It is defined as the growth in the most recent reported quarterly total assets per share… |
| `mdl77_historicalgrowthfactor_pctchgqtrsales` | MATRIX | 1-yr Change in Sales: It is defined as the growth in most recent reported quarterly sales per share as compared to 4 … |
| `mdl77_historicalgrowthfactor_pfcfghc` | MATRIX | The difference between the trailing 12-month free cash flow per share and that of 4 quarters ago for a stock divided … |
| `mdl77_historicalgrowthfactor_pfcfy3ghc` | MATRIX | 3-yr Change in Price-adj TTM FCF: It is defined as the difference between the most recently reported trailing 12-mont… |
| `mdl77_historicalgrowthfactor_pfcghc` | MATRIX | The difference between the trailing 12-month cash flow per share and that of 12 quarters ago for a stock divided by i… |
| `mdl77_historicalgrowthfactor_pfcoghc` | MATRIX | The difference between the most recently reported trailing 12-month operating cash flow per share and that of 4 quart… |
| `mdl77_historicalgrowthfactor_pfcoy3ghc` | MATRIX | The difference between the trailing 12-month operating cash flow per share and that of 12 quarters ago for a stock di… |
| `mdl77_historicalgrowthfactor_pfcy3ghc` | MATRIX | The difference between the trailing 12-month cash flow per share and that of 12 quarters ago comparable trailing 12-m… |
| `mdl77_historicalgrowthfactor_pspeghc` | MATRIX | The difference between the most recently reported trailing 12-month earnings per share and that of 4 quarters ago for… |
| `mdl77_historicalgrowthfactor_reinrate` | MATRIX | Reinvestment Rate: It is defined as the trailing 12-month earnings per share before extra items less the trailing 12-… |
| `mdl77_historicalgrowthfactor_rsqr4qsales3y` | MATRIX | The conditional square of the correlation between monthly dates and the corresponding trailing 12-month sales per sha… |
| `mdl77_historicalgrowthfactor_saleg5y` | MATRIX | 5-yr Sales Growth: It is defined as the difference between the trailing 12-month sales per share (SALE) and the SALE … |
| `mdl77_historicalgrowthfactor_salegstdev` | MATRIX | Sales Growth Rate Standard Deviation: It is defined as the standard deviation of the year-over-year quarterly sales p… |
| `mdl77_historicalgrowthfactor_salesaccel4q` | MATRIX | 4-Quarter Sales Acceleration: It is defined as the slope of the regression line between year-over-year sales growth a… |
| `mdl77_historicalgrowthfactor_se5yepsg` | MATRIX | Stability-Adjusted Residual Growth Rate: It is defined as a stock's mean long-term growth rate minus its 5-year histo… |
| `mdl77_historicalgrowthfactor_sighc` | MATRIX | 1-yr Chg in QTR Inventory as Percentage ofSales: It is defined as the most recently reported inventory as a percentag… |
| `mdl77_historicalgrowthfactor_slope4qcf3y` | MATRIX | Slope of 3-yr TTM Cash Flow Trend Line: It is defined as the slope coefficient between monthly dates and the correspo… |
| `mdl77_historicalgrowthfactor_slope4qeps3y` | MATRIX | Slope of 3-yr TTM EPS Trend Line: It is defined as the slope coefficient between monthly dates and the corresponding … |
| `mdl77_historicalgrowthfactor_slope4qfcf3y` | MATRIX | Slope of 3-yr TTM Free Cash Flow Trend Line: It is defined as the slope coefficient between monthly dates and the cor… |
| `mdl77_historicalgrowthfactor_slope4qocf3y` | MATRIX | Slope of 3-Yr TTM Oper Cash Flow Trend Line: It is defined as the slope coefficient between monthly dates and the cor… |
| `mdl77_historicalgrowthfactor_slope4qsales3y` | MATRIX | Slope of 3-yr TTM Sales Trend Line: It is defined as the slope coefficient between monthly dates and the correspondin… |
| `mdl77_historicalgrowthfactor_speghc` | MATRIX | 1-yr Change in Assets-adj TTM EPS: It is defined as the trailing 12-month earnings per share before extra items (EPS)… |
| `mdl77_historicalgrowthfactor_susgrowth` | MATRIX | The maximum growth rate a firm can sustain without having to increase financial leverage. |
| `mdl77_historicalgrowthfactor_totalsaleg` | MATRIX | Yearly TTM Total Sales Growth Rate: It is defined as the percent change in a company's trailing 12-month total sales … |
| `mdl77_historicalgrowthfactor_y3fcfq4rqsr` | MATRIX | R-Sqr of 3-yr TTM FCF Trend Line: It is defined as the conditional square of the correlation between monthly dates an… |
| `mdl77_historicalgrowthfactor_y3fcfq4vc` | MATRIX | Stability of 3-yr TTM Free Cash Flow: It is defined as the standard deviation of the last 12 quarters' trailing 12-mo… |
| `mdl77_historicalgrowthfactor_y3fcoq4rqsr` | MATRIX | R-Sqr of 3-yr TTM Oper Cash Flow Trend Line: It is defined as the conditional square of the correlation between month… |
| `mdl77_historicalgrowthfactor_y3fcoq4vc` | MATRIX | The standard deviation of the ratio for the values that a company generates scaled by its mean in the previous 12 qua… |
| `mdl77_historicalgrowthfactor_y3fcq4rqsr` | MATRIX | R-Sqr of 3-yr TTM Cash Flow Trend Line: It is defined as the conditional square of the correlation between monthly da… |
| `mdl77_historicalgrowthfactor_y3fcq4vc` | MATRIX | Stability of 3-Year TTM Cash Flow: It is defined as the standard deviation of the prior 12 quarters' trailing 12-mont… |
| `mdl77_historicalgrowthfactor_y3speq4rqsr` | MATRIX | R-Sqr of 3-yr TTM EPS Trend Line: It is defined as the conditional square of the correlation between monthly dates an… |
| `mdl77_historicalgrowthfactor_y3speq4vc` | MATRIX | Stability of 3-yr TTM Earnings per Share: It is defined as the standard deviation of the last 12 quarters' trailing 1… |
| `mdl77_historicalgrowthmodel_div5yg` | MATRIX | 5-Year Dividend Growth Rate: It is defined as the 5-year growth in dividends. |
| `mdl77_historicalgrowthmodel_emm_composite` | MATRIX | Model composition based on earnings momentum |
| `mdl77_historicalgrowthmodel_fcfghc` | MATRIX | 1-yr Chg in Assets-adj TTM Free Cash Flow: It is defined as the trailing 12-month free cash flow minus 4 quarters ago… |
| `mdl77_historicalgrowthmodel_slope4qsales3y` | MATRIX | Slope of 3-yr TTM Sales Trend Line: It is defined as the slope coefficient between monthly dates and the correspondin… |
| `mdl77_historicalgrowthmodel_susgrowth` | MATRIX | The maximum growth rate a firm can sustain without having to increase financial leverage. |
| `mdl77_htwrgspe_amq` | MATRIX | Earnings Growth Rank: It is defined as the one-quarter change in a stock's trailing twelve-month earnings per share, … |
| `mdl77_industryrrelativevaluefactor_curindbp_` | MATRIX | Industry Relative Book-to-Market: It is defined as a stock's current book-to-price ratio (BP) less the average of the… |
| `mdl77_industryrrelativevaluefactor_curindcfp_` | MATRIX | Industry Relative TTM Cash Flow-to-Price: It is defined as a stock's trailing 12-month cash flow-to-price ratio (CFP)… |
| `mdl77_industryrrelativevaluefactor_curindcoreepsp_` | MATRIX | Industry Relative TTM Core Earnings-to-Price: It is defined as a stock's trailing 12-month core earnings-to-price rat… |
| `mdl77_industryrrelativevaluefactor_curinddivp_` | MATRIX | Industry Relative TTM Dividend Yield: It is defined as a stock's trailing 12-month dividend yield (DivYield) less the… |
| `mdl77_industryrrelativevaluefactor_curindebitdap_` | MATRIX | Industry Relative TTM EBITDA-to-Price: It is defined as a stock's trailing 12-month EBITDA-to-price ratio (EBITDAP) l… |
| `mdl77_industryrrelativevaluefactor_curindep_` | MATRIX | Industry Relative TTM EPS-to-Price: It is defined as a stock's trailing 12-month earnings per share before extra item… |
| `mdl77_industryrrelativevaluefactor_curindfcfp_` | MATRIX | Industry Relative TTM Free Cash Flow-to-Price: It is defined as a stock's trailing 12-month free cash flow-to-price r… |
| `mdl77_industryrrelativevaluefactor_curindfwdep_` | MATRIX | Industry Relative Leading 4-QTRs EPS to Price: It is defined as a stock's next 4-quarter's analysts' consensus earnin… |
| `mdl77_industryrrelativevaluefactor_curindocfp_` | MATRIX | Industry Relative TTM Oper Cash Flow-to-Price: It is defined as a stock's trailing 12-month operating cash flow-to-pr… |
| `mdl77_industryrrelativevaluefactor_curindocfta_` | MATRIX | Industry Relative TTM Oper Cash Flow-to-Total Assets: It is defined as a stock's trailing 12-month operating cash flo… |
| `mdl77_industryrrelativevaluefactor_curindsp_` | MATRIX | Industry Relative TTM Sales-to-Price: It is defined as a stock's trailing 12-month sales-to-price ratio (SP) less the… |
| `mdl77_investorsentimentmodule` | MATRIX | Investor Sentiment Module |
| `mdl77_liquidityriskfactor_altmanz` | MATRIX | Altman Z Score: Altman Z = 1.2* (Current Assets - Current Liabilities)/TA + 1.4*Retained Earnings/TA + 3.3*Earnings b… |
| `mdl77_liquidityriskfactor_astcomp` | MATRIX | Asset Composition: It is defined as the total current assets from the most recent quarter divided by the total assets… |
| `mdl77_liquidityriskfactor_atmcallvol` | MATRIX | At the Money Call Option Implied Volatility: It is defined as the time-weighted average implied volatility of the nea… |
| `mdl77_liquidityriskfactor_atmputvol` | MATRIX | At the Money Put Option Implied Volatility: It is defined as the time-weighted average implied volatility of the near… |
| `mdl77_liquidityriskfactor_bap20d` | MATRIX | A proxy to market liquidity based on the difference between the highest price that a buyer is willing to pay for an a… |
| `mdl77_liquidityriskfactor_beta` | MATRIX | 60-Month Beta: It is defined as 0.67 times the 60-month beta plus 0.33. Beta is the covariance between a stock's mont… |
| `mdl77_liquidityriskfactor_betasigma` | MATRIX | Product of Beta and Sigma: It is defined as the product of the adjusted 60-month Beta and 60-month Sigma (standard de… |
| `mdl77_liquidityriskfactor_booklev` | MATRIX | Book Leverage: It is defined as the most recently reported quarterly total assets divided by the book equity. |
| `mdl77_liquidityriskfactor_cashratio` | MATRIX | Cash & Equivalents-to-Current Liabilities: It is defined as the most recently reported quarterly cash & equivalents d… |
| `mdl77_liquidityriskfactor_cfleverage` | MATRIX | Cash Flow Leverage: It is defined as the total liabilities divided by the trailing 12-month operating cash flow. |
| `mdl77_liquidityriskfactor_covol` | MATRIX | 60-Month Trading Volume Trend: It is defined as the slope of the least squares regression line of the last 60 months … |
| `mdl77_liquidityriskfactor_curratio` | MATRIX | Current Ratio: It is defined as the reported current assets from the most recent quarter divided by the current liabi… |
| `mdl77_liquidityriskfactor_cvvolp20d` | MATRIX | 20-Day Volume Volatility to Price Volatility: It is defined as the coefficient of variation of the last 20 days of cl… |
| `mdl77_liquidityriskfactor_dcc` | MATRIX | Current Cash Flow Debt Coverage Ratio: It is defined as the most recently reported quarterly cash flow from operation… |
| `mdl77_liquidityriskfactor_debtcf` | MATRIX | The sum of the most recent reported long-term debt and short-term interest-bearing debt divided by the trailing 12-mo… |
| `mdl77_liquidityriskfactor_divcov` | MATRIX | Company's trailing 1-year profits scaled by its annual dividends. |
| `mdl77_liquidityriskfactor_ed` | MATRIX | Long-term Debt-to-Equity: It is defined as the most recently reported total long-term debt divided by total book equity. |
| `mdl77_liquidityriskfactor_flowratio` | MATRIX | Flow Ratio: It is defined as the difference between current assets and cash & equivalents divided by the difference b… |
| `mdl77_liquidityriskfactor_gear` | MATRIX | Capital Gearing Ratio: It is defined as the long-term debt divided by the difference between total assets and current… |
| `mdl77_liquidityriskfactor_growdura` | MATRIX | Growth Duration: It is defined as the natural log of the ratio of a stock's leading 12-month PE to the leading 12-mon… |
| `mdl77_liquidityriskfactor_idb` | MATRIX | Basic Defensive Interval: It measures how many days that a company can cover its daily operating expenses (cost of go… |
| `mdl77_liquidityriskfactor_impduration` | MATRIX | Implied Equity Duration: It is an equity risk measure based on Macaulay's traditional measure of bond duration. It co… |
| `mdl77_liquidityriskfactor_iqa` | MATRIX | Asset Quality Index: It is defined as the year-over-year change of 1 minus the ratio of current assets plus PP&E divi… |
| `mdl77_liquidityriskfactor_lfd` | MATRIX | The sum of the trailing 12-month pretax income and the trailing 12-month interest expense divided by the trailing 12-… |
| `mdl77_liquidityriskfactor_liqcoeff` | MATRIX | Liquidity Coefficient: It is the slope of the regression between the monthly stock trading turnover ratio (X) and the… |
| `mdl77_liquidityriskfactor_mad3yttmni` | MATRIX | 3-yr MAD of TTM Net Income: It is defined as the mean absolute deviation of the last 12 quarters' trailing 12-month n… |
| `mdl77_liquidityriskfactor_mad3yttmsale` | MATRIX | 3-yr MAD of TTM Sales: It is defined as the mean absolute deviation of 12-quarter trailing 12-month sales deflated by… |
| `mdl77_liquidityriskfactor_milliq` | MATRIX | Stock Illiquidity: It is defined as the monthly average of the daily absolute return to the daily dollar trading volu… |
| `mdl77_liquidityriskfactor_mktcappera` | MATRIX | Stock's current market cap divided by the number of analysts providing Fiscal Year 1 earnings estimates. |
| `mdl77_liquidityriskfactor_mktlev` | MATRIX | Stock's total market value plus the most recent reported quarterly book debt then divided by the market value. |
| `mdl77_liquidityriskfactor_monchgsip` | MATRIX | Monthly Change in Short Interest Position: It is defined as the month-to-month change of the ratio of shares sold sho… |
| `mdl77_liquidityriskfactor_netcashp` | MATRIX | Net Cash to Equity: It is defined as most recently reported quarterly cash & equivalents less the long-term debt and … |
| `mdl77_liquidityriskfactor_nfaldebt` | MATRIX | Net Fixed Assets to Long-term Debt: It is defined as the most recent quarterly reported net fixed assets divided by t… |
| `mdl77_liquidityriskfactor_nlassets` | MATRIX | Natural Logarithm of Total Assets: It is defined as the natural logarithm of the most recent quarterly reported total… |
| `mdl77_liquidityriskfactor_nlmktcap` | MATRIX | Natural Logarithm of Market Capitalization: It is defined as the natural logarithm of the cubic of a stock's total ma… |
| `mdl77_liquidityriskfactor_nlprice` | MATRIX | Natural Logarithm of Closing Price: It is defined as the natural logarithm of the cubic of a stock's unadjusted closi… |
| `mdl77_liquidityriskfactor_nlsales` | MATRIX | Natural Logarithm of TTM Sales: It is defined as the natural logarithm of the cubic of a company's trailing 12-month … |
| `mdl77_liquidityriskfactor_nlvolcap` | MATRIX | The natural logarithm of the quotient of the trailing 1-year average of the monthly volume to the trailing 1-year ave… |
| `mdl77_liquidityriskfactor_numest` | MATRIX | The number of analysts' earnings estimates for fiscal year 1 for a stock. |
| `mdl77_liquidityriskfactor_ocfratio` | MATRIX | Operating Cash Flow Ratio: It is defined as a stock's most recently reported quarterly cash flow from operations divi… |
| `mdl77_liquidityriskfactor_ohlsonscore` | MATRIX | Ohlson Bankruptcy Score: It is a model assessing a company's probability of bankruptcy by considering firm size, capi… |
| `mdl77_liquidityriskfactor_oplev` | MATRIX | Operating Leverage: It is defined as the percent change in the trailing 12-month operating income from the previous q… |
| `mdl77_liquidityriskfactor_pcurlia` | MATRIX | Current Liabilities-to-Price: It is defined as a stock's most recently reported quarterly current liabilities per sha… |
| `mdl77_liquidityriskfactor_rerror60m` | MATRIX | Regression Error of 60-Month CAPM: It is defined as the standard error of the slope of the least squares regression l… |
| `mdl77_liquidityriskfactor_rq` | MATRIX | Quick Ratio: It is defined as the current assets less inventories from the most recent quarter divided by the total c… |
| `mdl77_liquidityriskfactor_si_ratio` | MATRIX | Short Interest Ratio: It is defined as the number of shares sold short divided by the average daily trading volume of… |
| `mdl77_liquidityriskfactor_sigma` | MATRIX | Stock Return Volatility: It is defined as the standard deviation of a stock's monthly returns in the prior 60 months. |
| `mdl77_liquidityriskfactor_sip` | MATRIX | Short Interest Position: It is defined as the number of shares sold short divided by common shares outstanding |
| `mdl77_liquidityriskfactor_tobinq` | MATRIX | Tobin q: It is defined as the market value of equity (E) plus debt (D) divided by assets (A), or (E + D)/A. D is meas… |
| `mdl77_liquidityriskfactor_totalcov` | MATRIX | Total Coverage: It equals (Cash Flow from Operations + Interest Paid + Tax Paid)/(Interest + Principal Paid). |
| `mdl77_liquidityriskfactor_voctni` | MATRIX | Interest Coverage: It is defined as the most recently reported quarterly operating income before depreciation divided… |
| `mdl77_liquidityriskfactor_voldiff_pc` | MATRIX | ATM Put Volatility - ATM Call Volatility: It is defined as the difference between the time weighted average implied v… |
| `mdl77_liquidityriskfactor_volto` | MATRIX | Trading Turnover Ratio: It is defined as the monthly total trading volume divided by the most recently reported total… |
| `mdl77_liquidityriskfactor_yoychgcr` | MATRIX | Year-over-year Change in Current Ratio: It is defined as the most recent reported quarterly current ratio and the cur… |
| `mdl77_liquidityriskfactor_yoychgda` | MATRIX | Year-over-year Change in Leverage: It is defined as the difference between the most recent reported quarterly total l… |
| `mdl77_lumqca` | MATRIX | Acquisition Multiple: It is defined as the most recent quarterly reported invested capital divided by the trailing 12… |
| `mdl77_managementsignalingmodule` | MATRIX | Management Signaling Module |
| `mdl77_momemtumanalystmodel_ghcfcfmtt_amq` | MATRIX | Change in TTM Free Cash Flow Rank: It is defined as the 2Q change in a stock's trailing twelve month free cash flow, … |
| `mdl77_momemtumanalystmodel_htwrgspe_amq` | MATRIX | Earnings Growth Rank: It is defined as the one-quarter change in a stock's trailing twelve-month earnings per share, … |
| `mdl77_momemtumanalystmodel_jdaksr_amq` | MATRIX | Risk Adjustments Rank: It is defined as the aggregation of five non-linear price and trading volume volatility and gr… |
| `mdl77_momemtumanalystmodel_qma_alpha6m` | MATRIX | Six-Month Alpha Change Rank: It is defined as the six-month change in a stock's twelve-month alpha, as calculated by … |
| `mdl77_momemtumanalystmodel_qma_chgnowc` | MATRIX | Change in Net Working Capital Rank: It is defined as the one-quarter change in a stock's recent net current working c… |
| `mdl77_momemtumanalystmodel_qma_composite` | MATRIX | The composite of the Earnings Momentum Rank, the Analyst Expectations Rank, the Earnings-Price Link Rank and the Rela… |
| `mdl77_momemtumanalystmodel_qma_condsurp` | MATRIX | Conditional Surprise Rank: It is defined as the average of a stock's recent earnings surprise, its cost of goods sold… |
| `mdl77_momemtumanalystmodel_qma_earnexp` | MATRIX | Analyst Expectations Rank: It is defined as the equal-weighted average of the Earnings Revisions and the Ratings Chan… |
| `mdl77_momemtumanalystmodel_qma_eplinkage` | MATRIX | The equal-weighted average of the Change in Free Cash Flow Rank, the Industry Relative 3-Month Return Rank, the Marke… |
| `mdl77_momemtumanalystmodel_qma_estrev` | MATRIX | Estimate Revisions Rank: It is defined as the difference between the number of recent upward and downward revisions t… |
| `mdl77_momemtumanalystmodel_qma_indrelrtn3m` | MATRIX | The difference of company's 3 months profit compared to its respective by industry classification. |
| `mdl77_momemtumanalystmodel_qma_lagpricemo` | MATRIX | Lagged 12- to 1-Month Price MomRank: It is defined as the difference between a stock's lagged 12-month return and its… |
| `mdl77_momemtumanalystmodel_qma_mktresponse` | MATRIX | Market Earnings Response Rank: It is defined as the four-day return for a stock, spanning the two days before to the … |
| `mdl77_momemtumanalystmodel_qma_ratingchg` | MATRIX | The trend in sell-side analysts' consensus ratings (standardized 1 = strong buy to 5 = strong sell) revisions over th… |
| `mdl77_momemtumanalystmodel_qma_relpricemo` | MATRIX | Relative Price Momentum Rank: It is defined as the equal-weighted average of the Lagged 12- to 1-Month Price Momentum… |
| `mdl77_momemtumanalystmodel_qma_repearnmom` | MATRIX | Earnings Momentum Rank: It is defined as the equal weighted average of the Earnings Growth and Earnings Surprise Rank… |
| `mdl77_monchgsip` | MATRIX | Monthly Change in Short Interest Position: It is defined as the month-to-month change of the ratio of shares sold sho… |
| `mdl77_mpnghc` | MATRIX | 1-Yr Change in Net Profit Margin: It is defined as the most recent quarterly net profit margin (NPM) minus the NPM 4 … |
| `mdl77_netcashp` | MATRIX | Net Cash to Equity: It is defined as most recently reported quarterly cash & equivalents less the long-term debt and … |
| `mdl77_nlvolcap` | MATRIX | The natural logarithm of the quotient of the trailing 1-year average of the monthly volume to the trailing 1-year ave… |
| `mdl77_nnastp` | MATRIX | Net Current Assets-to-Price: It is defined as the current assets per share minus total liabilities per share divided … |
| `mdl77_ocfast` | MATRIX | Operating Cash Flow to Assets: It is defined as the trailing 12-month net cash flow from operations divided by the av… |
| `mdl77_ocfratio` | MATRIX | Operating Cash Flow Ratio: It is defined as a stock's most recently reported quarterly cash flow from operations divi… |
| `mdl77_oearningmomentumfactor_dypeg` | MATRIX | Reciprocal of Dividend Yield-adjusted PEG: It is defined as the reciprocal of a stock's forward 12-month P/E ratio di… |
| `mdl77_oearningmomentumfactor_fcfroey1p` | MATRIX | Product of TTM FCF Yield and Forward ROE: It is defined as the trailing 12-month free cash flow per share multiplied … |
| `mdl77_oearningmomentumfactor_fcus` | MATRIX | Standardized Unexpected Cash Flow: It is defined as the most recent quarterly operating cash flow minus that of 4 qua… |
| `mdl77_oearningmomentumfactor_fqsurstd` | MATRIX | Most Recent Earnings Surprise: It is defined as the most recent quarterly earnings surprise (actual fiscal quarter EP… |
| `mdl77_oearningmomentumfactor_fy1epsskew` | MATRIX | The skewness of the distribution of a series leading 12-month earnings consensus estimates. |
| `mdl77_oearningmomentumfactor_gspea1q` | MATRIX | 1-Quarter Ahead EPS Growth: It is defined as a stock's most recent fiscal quarter consensus earnings forecast less th… |
| `mdl77_oearningmomentumfactor_gspea1y` | MATRIX | 1-Year Ahead EPS Growth: It is defined as the most recent consensus earnings forecast for the next 4 quarters minus t… |
| `mdl77_oearningmomentumfactor_gspea2y` | MATRIX | 2-Year Ahead EPS Growth: It is defined as the most recent consensus earnings forecast for fiscal year 2 minus the con… |
| `mdl77_oearningmomentumfactor_gtl` | MATRIX | Long-Term Growth Rate Estimates: It is defined as the consensus long-term growth forecast. It generally represents an… |
| `mdl77_oearningmomentumfactor_gtlm6ghc` | MATRIX | 6-M Change in Long-term Growth Estimates: It is defined as the percent change in the most recent mean consensus long-… |
| `mdl77_oearningmomentumfactor_lagegp` | MATRIX | Lagged Inverse of PEG Ratio: It is defined as the trailing 12-month earnings per share before extraordinary items tim… |
| `mdl77_oearningmomentumfactor_mrspe` | MATRIX | Street Revision Magnitude: It is defined as the 3-month change in the median FY1 consensus earnings forecast, scaled … |
| `mdl77_oearningmomentumfactor_numrevq1` | MATRIX | Net Number ofRevisions for Fiscal QTR 1: It is defined as the number of fiscal quarter 1 upward earnings forecast rev… |
| `mdl77_oearningmomentumfactor_numrevy1` | MATRIX | Net Number ofRevisions for Fiscal Year 1: It is defined as the weighted average of the number of FY1 analyst earnings… |
| `mdl77_oearningmomentumfactor_pelh` | MATRIX | Street Revision Confidence: It is defined as the sum of the 3-month change in the highest and lowest FY1 earnings est… |
| `mdl77_oearningmomentumfactor_perg` | MATRIX | Risk-Adjusted PEG Ratio: It is defined as the stock price divided by the leading 12-month consensus earnings forecast… |
| `mdl77_oearningmomentumfactor_pge` | MATRIX | Estimates on the next 1-year average earnings scaled by company's prospects on growth and its stock price. |
| `mdl77_oearningmomentumfactor_qepsferr` | MATRIX | Prior Fiscal Quarter Forecast Error: It is defined as the difference between the actual earnings per share and consen… |
| `mdl77_oearningmomentumfactor_ratrev6m` | MATRIX | Street Rating Revision: It is defined as the 6-month average of the change in the average analyst recommendation trac… |
| `mdl77_oearningmomentumfactor_rev1q1` | MATRIX | Revision in Fiscal QTR 1 EPS Forecasts: It is defined as the change in the current consensus earnings forecast for fi… |
| `mdl77_oearningmomentumfactor_rev3y1` | MATRIX | The change in the analysts' projection on company's performance for fiscal year 1 less that of three months ago, defl… |
| `mdl77_oearningmomentumfactor_rev3y2` | MATRIX | 3-M Revision in FY2 EPS Forecasts: It is defined as the change in the current mean consensus earnings estimate for fi… |
| `mdl77_oearningmomentumfactor_rev6` | MATRIX | Averaged Last 6-M EPS Revisions for FY1: It is defined as the average of prior 6-month monthly changes in a stock's c… |
| `mdl77_oearningmomentumfactor_salesurp` | MATRIX | Sales Surprise: It is defined as the most recent reported quarterly sales minus consensus sales forecasts, divided by… |
| `mdl77_oearningmomentumfactor_spe1yfvc` | MATRIX | FY1 EPS Estimates Dispersion: It is defined as the standard deviation of analyst earnings estimates for fiscal year 1… |
| `mdl77_oearningmomentumfactor_spe2yfvc` | MATRIX | FY2 EPS Forecast Dispersion: It is defined as the standard deviation of analyst earnings estimates for fiscal year 2 … |
| `mdl77_oearningmomentumfactor_stdevfy1epsp` | MATRIX | Std Dev of FY1 EPS Estimates-to-Price: It is defined as the standard deviation of analyst forecasts for fiscal year 1… |
| `mdl77_oearningmomentumfactor_stdevfy2epsp` | MATRIX | Std Dev of FY2 EPS Estimates-to-Price: It is defined as the standard deviation of analyst forecasts for fiscal year 2… |
| `mdl77_oearningmomentumfactor_stockrating` | MATRIX | Street Consensus Rating: It is defined as the consensus recommendation for a company. |
| `mdl77_oearningmomentumfactor_sue` | MATRIX | Standardized Unexpected Earnings: It is defined as the most recent quarterly earnings per share minus that of 4 quart… |
| `mdl77_oearningmomentumfactor_surp` | MATRIX | Real Earnings Surprise: It is defined as the difference between the actual earnings per share and consensus forecasts… |
| `mdl77_oearningmomentumfactor_y2repsg` | MATRIX | 2-Year Projected EPS Growth: It is defined as the most recent consensus earnings forecast for fiscal year 2 minus the… |
| `mdl77_oearningmomentumfactor_y3sur` | MATRIX | Volatility-adj 3-yr Projected EPS Growth: It is defined as the consensus earnings forecast for the current quarter mi… |
| `mdl77_oearningsqualityfactor_ccacw` | MATRIX | Working Capital Accruals: It equals to: Increase in Accounts Receivables + Increase in Inventory + Decrease in Accoun… |
| `mdl77_oearningsqualityfactor_chgsgasale` | MATRIX | Change in QTR SG&A Expenses vs Sales: It is defined as the difference between the yearly change in quarterly Selling,… |
| `mdl77_oearningsqualityfactor_chgshare` | MATRIX | Percent Change in Shares Outstanding: It is defined as the percent change in a company's current number of outstandin… |
| `mdl77_oearningsqualityfactor_cogsinvt` | MATRIX | Change in TTM COGS vs Inventory Level: It is defined as the absolute value of the difference between the yearly perce… |
| `mdl77_oearningsqualityfactor_cre` | MATRIX | Earnings Response Coefficient: It is defined as the slope coefficient between market-adjusted returns around the time… |
| `mdl77_oearningsqualityfactor_dpcapex` | MATRIX | Change in TTM Depreciation vs CapEx: It is defined as the absolute value of the difference between the yearly percent… |
| `mdl77_oearningsqualityfactor_epschgetr` | MATRIX | EPS from Change in Effective Tax Rate: It is defined as the trailing 12-month pre-tax income per share times the diff… |
| `mdl77_oearningsqualityfactor_indrelrecd_` | MATRIX | Industry-Adjusted Doubtful Account Receivables: It is defined as a stock's asset-adjusted annual doubtful receivables… |
| `mdl77_oearningsqualityfactor_lccau` | MATRIX | Unexpected Change in Accrued Liabilities: It is defined as the difference between the most recent fiscal year's accru… |
| `mdl77_oearningsqualityfactor_opincltd` | MATRIX | Change in TTM Oper Income vs LT Debt: It is defined as the difference between the yearly percent change in operating … |
| `mdl77_oearningsqualityfactor_pau` | MATRIX | Unexpected Change in Accounts Payable: It is defined as the difference between current accounts payable and the expec… |
| `mdl77_oearningsqualityfactor_pedu` | MATRIX | Unexpected Change in Depreciation: It is defined as the difference between the trailing 12-month depreciation expense… |
| `mdl77_oearningsqualityfactor_rau` | MATRIX | Unexpected Change in Accounts Receivable: It is defined as the difference between current accounts receivable and the… |
| `mdl77_oearningsqualityfactor_saleeps` | MATRIX | Change in TTM Sales vs EPS: It is defined as the absolute value of the difference between the yearly percent change i… |
| `mdl77_oearningsqualityfactor_salegpm` | MATRIX | Change in QTR Sales vs. Gross Margin: It is defined as the difference between the yearly change in most recent report… |
| `mdl77_oearningsqualityfactor_salerec` | MATRIX | Change in TTM Sales vs Accounts Receivable: It is defined as the difference between the yearly percent change in trai… |
| `mdl77_oearningsqualityfactor_spefcn` | MATRIX | Change in TTM EPS vs. Oper Cash Flows: It is defined as the absolute value of the difference between the yearly perce… |
| `mdl77_oearningsqualityfactor_ttmaccu` | MATRIX | Accounting Accruals: It is defined as the difference between the trailing 12-month net income and the trailing 12-mon… |
| `mdl77_oearningsqualityfactor_vniu` | MATRIX | The difference of inventory between present and expected levels. |
| `mdl77_oearningsqualityfactor_yoychgaa` | MATRIX | Change in Accruals to Assets: It is defined as the trailing 12-month income before extra items less the trailing 12-m… |
| `mdl77_ohistoricalgrowthfactor_cg3ysales` | MATRIX | The geometric growth rate of the trailing 12-month sales per share in the last 12 quarters. |
| `mdl77_ohistoricalgrowthfactor_chg3ycfast` | MATRIX | 3-yr Change in Assets-adj TTM Cash Flow: It is defined as the most recently reported trailing 12-month operating cash… |
| `mdl77_ohistoricalgrowthfactor_chg3yepsast` | MATRIX | 3-yr Change in Assets-adj TTM EPS: It is defined as the trailing 12-month earnings per share before extra items (EPS)… |
| `mdl77_ohistoricalgrowthfactor_chg3yepsp` | MATRIX | The difference between the trailing 12-month earnings per share and that of 12 quarters ago for a stock divided by it… |
| `mdl77_ohistoricalgrowthfactor_chg3yfcfast` | MATRIX | 3-yr Chg in Assets-adj TTM Free Cash Flow: It is defined as the trailing 12-month free cash flow minus 12-quarters ag… |
| `mdl77_ohistoricalgrowthfactor_chg3yocfast` | MATRIX | 3-yr Change in Assets-adj TTM Oper Cash Flow: It is defined as the most recently reported trailing 12-month operating… |
| `mdl77_ohistoricalgrowthfactor_chgars` | MATRIX | 1-yr Chg in Acct Receivable as Percentage ofSales: It is defined as the change between the last reported accounts rec… |
| `mdl77_ohistoricalgrowthfactor_cv4qsales3y` | MATRIX | The standard deviation of prior 12 quarters' trailing 12-month sales for individual share scaled to the mean of itsel… |
| `mdl77_ohistoricalgrowthfactor_cvopinc` | MATRIX | CV of Oper Income per Share in Last 12 QTRs: It is defined as the standard deviation of the trailing 12-month operati… |
| `mdl77_ohistoricalgrowthfactor_div5yg` | MATRIX | 5-Year Dividend Growth Rate: It is defined as the 5-year growth in dividends |
| `mdl77_ohistoricalgrowthfactor_fcfequity` | MATRIX | TTM Free Cash Flow to Equity: It is defined as the trailing 12-month free cash flow divided by the average book equit… |
| `mdl77_ohistoricalgrowthfactor_fcfghc` | MATRIX | 1-yr Chg in Assets-adj TTM Free Cash Flow: It is defined as the trailing 12-month free cash flow minus 4 quarters ago… |
| `mdl77_ohistoricalgrowthfactor_fcghc` | MATRIX | 1-yr Change in Assets-adj TTM Cash Flow: It is defined as the trailing 12-month cash flow minus comparable trailing 1… |
| `mdl77_ohistoricalgrowthfactor_fcoghc` | MATRIX | 1-yr Chg in Assets-adj TTM Oper Cash Flow: It is defined as the most recently reported trailing 12-month operating ca… |
| `mdl77_ohistoricalgrowthfactor_mpnghc` | MATRIX | 1-Yr Change in Net Profit Margin: It is defined as the most recent quarterly net profit margin (NPM) minus the NPM 4 … |
| `mdl77_ohistoricalgrowthfactor_mpoghc` | MATRIX | 1-yr Change in Operating Profit Margin: It is defined as the most recent quarterly operating profit margin minus that… |
| `mdl77_ohistoricalgrowthfactor_pctchg3ycf` | MATRIX | The percent change in a stock's most recent trailing 12-month cash flow per share as compared to itself 12 quarters ago. |
| `mdl77_ohistoricalgrowthfactor_pctchg3yeps` | MATRIX | The percent change in a stock's most recent trailing 12-month earnings per share as compared to itself 12 quarters ago. |
| `mdl77_ohistoricalgrowthfactor_pctchg3yfcf` | MATRIX | 3-yr Growth in TTM Free Cash Flow: It is defined as the percent change in a stock's most recent trailing 12-month fre… |
| `mdl77_ohistoricalgrowthfactor_pctchg3yocf` | MATRIX | 3-yr Growth in TTM Oper Cash Flow: It is defined as the percent change in a stock's most recent trailing 12-month ope… |
| `mdl77_ohistoricalgrowthfactor_pctchgastto` | MATRIX | 1-Yr Change in Asset Turnover Ratio: It is defined as the percent change in the most recent asset turnover ratio as c… |
| `mdl77_ohistoricalgrowthfactor_pctchgcf` | MATRIX | 1-yr Growth in TTM Cash Flow: It is defined as the percent change in a stock's most recent trailing 12-month cash flo… |
| `mdl77_ohistoricalgrowthfactor_pctchgeps` | MATRIX | The percent change in a stock's most recent trailing 12-month earnings per share before extra items as compared to it… |
| `mdl77_ohistoricalgrowthfactor_pctchgfcf` | MATRIX | 1-yr Growth in TTM Free Cash Flow: It is defined as the percent change in a stock's most recent trailing 12-month fre… |
| `mdl77_ohistoricalgrowthfactor_pctchgocf` | MATRIX | 1-yr Growth in TTM Oper Cash Flow: It is defined as the percent change of a stock's most recent trailing 12-month ope… |
| `mdl77_ohistoricalgrowthfactor_pctchgqtrast` | MATRIX | 1-Yr Change in Total Assets: It is defined as the growth in the most recent reported quarterly total assets per share… |
| `mdl77_ohistoricalgrowthfactor_pctchgqtrsales` | MATRIX | 1-Year Change in Sales: It is defined as the growth in the most recent reported quarterly sales per share as compared… |
| `mdl77_ohistoricalgrowthfactor_pfcfghc` | MATRIX | The difference between the trailing 12-month free cash flow per share and that of 4 quarters ago for a stock divided … |
| `mdl77_ohistoricalgrowthfactor_pfcfy3ghc` | MATRIX | 3-yr Change in Price-adj TTM FCF: It is defined as the difference between the most recently reported trailing 12-mont… |
| `mdl77_ohistoricalgrowthfactor_pfcghc` | MATRIX | The difference between the trailing 12-month cash flow per share and that of 12 quarters ago for a stock divided by i… |
| `mdl77_ohistoricalgrowthfactor_pfcoghc` | MATRIX | The difference between the most recently reported trailing 12-month operating cash flow per share and that of 4 quart… |
| `mdl77_ohistoricalgrowthfactor_pfcoy3ghc` | MATRIX | The difference between the trailing 12-month operating cash flow per share and that of 12 quarters ago for a stock di… |
| `mdl77_ohistoricalgrowthfactor_pfcy3ghc` | MATRIX | The difference between the trailing 12-month cash flow per share and that of 12 quarters ago comparable trailing 12-m… |
| `mdl77_ohistoricalgrowthfactor_pspeghc` | MATRIX | The difference between the most recently reported trailing 12-month earnings per share and that of 4 quarters ago for… |
| `mdl77_ohistoricalgrowthfactor_reinrate` | MATRIX | Reinvestment Rate: It is defined as the trailing 12-month earnings per share before extra items less the trailing 12-… |
| `mdl77_ohistoricalgrowthfactor_rsqr4qsales3y` | MATRIX | The conditional square of the correlation between monthly dates and the corresponding trailing 12-month sales per sha… |
| `mdl77_ohistoricalgrowthfactor_saleg5y` | MATRIX | 5-yr Sales Growth: It is defined as the difference between the trailing 12-month sales per share (SALE) and the SALE … |
| `mdl77_ohistoricalgrowthfactor_salegstdev` | MATRIX | Sales Growth Rate Standard Deviation: It is defined as the standard deviation of the year-over-year quarterly sales p… |
| `mdl77_ohistoricalgrowthfactor_salesaccel4q` | MATRIX | 4-Quarter Sales Acceleration: It is defined as the slope of the regression line between year-over-year sales growth a… |
| `mdl77_ohistoricalgrowthfactor_se5yepsg` | MATRIX | Stability-Adjusted Residual Growth Rate: It is defined as a stock's mean long-term growth rate minus its 5-year histo… |
| `mdl77_ohistoricalgrowthfactor_sighc` | MATRIX | 1-Yr Chg in QTR Inventory as Percentage ofSales: It is defined as the most recently reported inventory as a percentag… |
| `mdl77_ohistoricalgrowthfactor_slope4qcf3y` | MATRIX | Slope of 3-yr TTM Cash Flow Trend Line: It is defined as the slope coefficient between monthly dates and the correspo… |
| `mdl77_ohistoricalgrowthfactor_slope4qeps3y` | MATRIX | Slope of 3-Yr TTM EPS Trend Line: It is defined as the slope coefficient between monthly dates and the corresponding … |
| `mdl77_ohistoricalgrowthfactor_slope4qfcf3y` | MATRIX | Slope of 3-Year TTM Free Cash Flow Trend Line: It is defined as the slope coefficient between monthly dates and the c… |
| `mdl77_ohistoricalgrowthfactor_slope4qocf3y` | MATRIX | Slope of 3-Yr TTM Oper Cash Flow Trend Line: It is defined as the slope coefficient between monthly dates and the cor… |
| `mdl77_ohistoricalgrowthfactor_slope4qsales3y` | MATRIX | Slope of 3-yr TTM Sales Trend Line: It is defined as the slope coefficient between monthly dates and the correspondin… |
| `mdl77_ohistoricalgrowthfactor_speghc` | MATRIX | 1-yr Change in Assets-adj TTM EPS: It is defined as the trailing 12-month earnings per share before extra items (EPS)… |
| `mdl77_ohistoricalgrowthfactor_susgrowth` | MATRIX | The maximum growth rate a firm can sustain without having to increase financial leverage. |
| `mdl77_ohistoricalgrowthfactor_totalsaleg` | MATRIX | Yearly TTM Total Sales Growth Rate: It is defined as the percent change in a company's trailing 12-month total sales … |
| `mdl77_ohistoricalgrowthfactor_y3fcfq4rqsr` | MATRIX | R-Sqr of 3-yr TTM FCF Trend Line: It is defined as the conditional square of the correlation between monthly dates an… |
| `mdl77_ohistoricalgrowthfactor_y3fcfq4vc` | MATRIX | Stability of 3-Year TTM Free Cash Flow: It is defined as the standard deviation of the last 12 quarters' trailing 12-… |
| `mdl77_ohistoricalgrowthfactor_y3fcoq4rqsr` | MATRIX | R-Sqr of 3-yr TTM Oper Cash Flow Trend Line: It is defined as the conditional square of the correlation between month… |
| `mdl77_ohistoricalgrowthfactor_y3fcoq4vc` | MATRIX | The standard deviation of the ratio for the values that the company generates scaled by its mean in the previous 12 q… |
| `mdl77_ohistoricalgrowthfactor_y3fcq4rqsr` | MATRIX | R-Sqr of 3-yr TTM Cash Flow Trend Line: It is defined as the conditional square of the correlation between monthly da… |
| `mdl77_ohistoricalgrowthfactor_y3fcq4vc` | MATRIX | Stability of 3-yr TTM Cash Flow: It is defined as the standard deviation of the prior 12-quarter's trailing 12-month … |
| `mdl77_ohistoricalgrowthfactor_y3speq4rqsr` | MATRIX | R-Sqr of 3-yr TTM EPS Trend Line: It is defined as the conditional square of the correlation between monthly dates an… |
| `mdl77_ohistoricalgrowthfactor_y3speq4vc` | MATRIX | Stability of 3-yr TTM Earnings per Share: It is defined as the standard deviation of the last 12 quarters' trailing 1… |
| `mdl77_oindustryrrelativevaluefactor_curindbp_` | MATRIX | Industry Relative Book-to-Market: It is defined as a stock's current book-to-price ratio (BP) less the average of the… |
| `mdl77_oindustryrrelativevaluefactor_curindcfp_` | MATRIX | Industry Relative TTM Cash Flow-to-Price: It is defined as a stock's trailing 12-month cash flow-to-price ratio (CFP)… |
| `mdl77_oindustryrrelativevaluefactor_curindcoreepsp_` | MATRIX | Industry Relative TTM Core Earnings-to-Price: It is defined as a stock's trailing 12-month core earnings-to-price rat… |
| `mdl77_oindustryrrelativevaluefactor_curinddivp_` | MATRIX | Industry Relative TTM Dividend Yield: It is defined as a stock's trailing 12-month dividend yield (DivYield) less the… |
| `mdl77_oindustryrrelativevaluefactor_curindebitdap_` | MATRIX | Industry Relative TTM EBITDA-to-Price: It is defined as a stock's trailing 12-month EBITDA-to-price ratio (EBITDAP) l… |
| `mdl77_oindustryrrelativevaluefactor_curindep_` | MATRIX | Industry Relative TTM EPS-to-Price: It is defined as a stock's trailing 12-month earnings per share before extra item… |
| `mdl77_oindustryrrelativevaluefactor_curindfcfp_` | MATRIX | Industry Relative TTM Free Cash Flow-to-Price: It is defined as a stock's trailing 12-month free cash flow-to-price r… |
| `mdl77_oindustryrrelativevaluefactor_curindfwdep_` | MATRIX | Industry Relative Leading 4-QTRs EPS to Price: It is defined as a stock's next 4 quarters' analysts' consensus earnin… |
| `mdl77_oindustryrrelativevaluefactor_curindocfp_` | MATRIX | Industry Relative TTM Oper Cash Flow-to-Price: It is defined as a stock's trailing 12-month operating cash flow-to-pr… |
| `mdl77_oindustryrrelativevaluefactor_curindocfta_` | MATRIX | Industry Relative TTM Oper Cash Flow-to-Total Assets: It is defined as a stock's trailing 12-month operating cash flo… |
| `mdl77_oindustryrrelativevaluefactor_curindsp_` | MATRIX | Industry Relative TTM Sales-to-Price: It is defined as a stock's trailing 12-month sales-to-price ratio (SP) less the… |
| `mdl77_omomemtumanalystmodel_ghcfcfmtt_amq` | MATRIX | Change in TTM Free Cash Flow Rank: It is defined as the 2Q change in a stock's trailing twelve-month free cash flow, … |
| `mdl77_omomemtumanalystmodel_htwrgspe_amq` | MATRIX | Earnings Growth Rank: It is defined as the one quarter change in a stock's trailing twelve month earnings per share, … |
| `mdl77_omomemtumanalystmodel_jdaksr_amq` | MATRIX | Risk Adjustments Rank: It is defined as the aggregation of five non-linear price and trading volume volatility and gr… |
| `mdl77_omomemtumanalystmodel_qma_alpha6m` | MATRIX | Six-Month Alpha Change Rank: It is defined as the six-month change in a stock's twelve-month alpha, as calculated by … |
| `mdl77_omomemtumanalystmodel_qma_chgnowc` | MATRIX | Change in Net Working Capital Rank: It is defined as the one-quarter change in a stock's recent net current working c… |
| `mdl77_omomemtumanalystmodel_qma_composite` | MATRIX | The composite of the Earnings Momentum Rank, the Analyst Expectations Rank, the Earnings-Price Link Rank, and the Rel… |
| `mdl77_omomemtumanalystmodel_qma_condsurp` | MATRIX | Conditional Surprise Rank: It is defined as the average of a stock's recent earnings surprise, its cost of goods sold… |
| `mdl77_omomemtumanalystmodel_qma_earnexp` | MATRIX | Analyst Expectations Rank: It is defined as the equal-weighted average of the Earnings Revisions and the Ratings Chan… |
| `mdl77_omomemtumanalystmodel_qma_eplinkage` | MATRIX | The equal-weighted average of the Change in Free Cash Flow Rank, the Industry Relative 3-Month Return Rank, the Marke… |
| `mdl77_omomemtumanalystmodel_qma_estrev` | MATRIX | Estimate Revisions Rank: It is defined as the difference between the number of recent upward and downward revisions t… |
| `mdl77_omomemtumanalystmodel_qma_indrelrtn3m` | MATRIX | The difference of a company's 3-month profit compared to its respective by industry classification. |
| `mdl77_omomemtumanalystmodel_qma_lagpricemo` | MATRIX | Lagged 12- to 1-Month Price MomRank: It is defined as the difference between a stock's lagged twelve month return and… |
| `mdl77_omomemtumanalystmodel_qma_mktresponse` | MATRIX | Market Earnings Response Rank: It is defined as the four-day return for a stock, spanning the two days before to the … |
| `mdl77_omomemtumanalystmodel_qma_ratingchg` | MATRIX | The trend in sell-side analysts' consensus ratings (standardized 1 = strong buy to 5 = strong sell) revisions over th… |
| `mdl77_omomemtumanalystmodel_qma_relpricemo` | MATRIX | Relative Price Momentum Rank: It is defined as the equal-weighted average of the Lagged 12- to 1-Month Price Momentum… |
| `mdl77_omomemtumanalystmodel_qma_repearnmom` | MATRIX | Earnings Momentum Rank: It is defined as the equal-weighted average of the Earnings Growth and Earnings Surprise Rank… |
| `mdl77_ooearningsmomemtummodel_chgsup` | MATRIX | Change in EPS Surprise: It is defined as the quarterly change in EPS surprise. |
| `mdl77_ooearningsmomemtummodel_emm_composite` | MATRIX | Model composition based on earnings momentum |
| `mdl77_ooearningsmomemtummodel_fc_fcfroey1p` | MATRIX | Product of TTM FCF Yield and Forward ROE: It is defined as the trailing 12-month free cash flow per share multiplied … |
| `mdl77_ooearningsmomemtummodel_fc_fqsurstd` | MATRIX | Most Recent Quarterly Earnings Surprise: It is defined as a stock's most recent quarterly earnings surprise (actual f… |
| `mdl77_ooearningsmomemtummodel_fc_numrevy1` | MATRIX | Net Number ofRevisions for Fiscal Year 1: It is defined as the weighted average of the number of FY1 analyst earnings… |
| `mdl77_ooearningsmomemtummodel_fc_rev3y2` | MATRIX | 3-M Revision in FY2 EPS Forecasts: It is defined as the change in a stock's current analysts' mean earnings estimate … |
| `mdl77_ooearningsmomemtummodel_fc_y2repsg` | MATRIX | 2-Year Projected EPS Growth: It is defined as a stock's most recent consensus analysts' earnings forecast for fiscal … |
| `mdl77_ooearningsmomemtummodel_gtlo` | MATRIX | Long-Term Growth Rate Estimates: It is defined as the consensus long-term growth forecast. It generally represents an… |
| `mdl77_ooearningsmomemtummodel_pge_cf` | MATRIX | Estimates on the next 1-year average earnings scaled by company's prospects on growth and its stock price. |
| `mdl77_ooearningsmomemtummodel_spe2yfvc_cf` | MATRIX | FY2 EPS Forecast Dispersion: It is defined as the standard deviation of analyst earnings estimates for fiscal year 2 … |
| `mdl77_opricemomentumfactor_25_4op` | MATRIX | One minus the quotient of a stock's last 52-week price exponential moving average divided by its last 4-week price ex… |
| `mdl77_opricemomentumfactor_6351_rp` | MATRIX | 15/36 Week Stock Price Ratio: It is defined as the moving average of a stock's prices in the last 15 weeks divided by… |
| `mdl77_opricemomentumfactor_actrtn12m` | MATRIX | 12-Month Active Return with 1-month Lag: It is defined as the percent change in price for a stock from month t-13 to … |
| `mdl77_opricemomentumfactor_actrtn18m` | MATRIX | 18-Month Active Return with 1-Month Lag: It is defined as the percent change in price for a stock from month t-19 to … |
| `mdl77_opricemomentumfactor_actrtn1m` | MATRIX | 1-Month Active Return: It is defined as the percent change in price for a stock from month t-1 to month t. |
| `mdl77_opricemomentumfactor_actrtn24m` | MATRIX | 24-Month Active Return with 1-Month Lag: It is defined as the percent change in price for a stock from month t-25 to … |
| `mdl77_opricemomentumfactor_actrtn2m` | MATRIX | 2-Month Active Return: It is defined as the percent change in price for a stock from month t-2 to month t. |
| `mdl77_opricemomentumfactor_actrtn36m` | MATRIX | 36-Month Active Return with 1-Month Lag: It is defined as the percent change in price for a stock from month t-37 to … |
| `mdl77_opricemomentumfactor_actrtn3m` | MATRIX | 3-Month Active Return: It is defined as the percent change in price for a stock from month t-3 to month t. |
| `mdl77_opricemomentumfactor_actrtn60m` | MATRIX | 60-Month Active Return with 1-Month Lag: It is defined as the percent change in price for a stock from month t-61 to … |
| `mdl77_opricemomentumfactor_actrtn6m` | MATRIX | 6-Month Active Return with 1-Month Lag: It is defined as the percent change in price for a stock from month t-7 to mo… |
| `mdl77_opricemomentumfactor_alpha60m` | MATRIX | 60-Month Alpha: It is defined as the intercept of the regression line which best fits a stock's monthly price return … |
| `mdl77_opricemomentumfactor_chg6malpha18m` | MATRIX | 6-Month Nominal Change in 18-Month Alpha: It is defined as the 6-month change in a stock's 18-month alpha, which equa… |
| `mdl77_opricemomentumfactor_chgalpha12m` | MATRIX | 6-Month Nominal Change in 12-Month Alpha: It is defined as the 6-month change in a stock's 12-month alpha, which equa… |
| `mdl77_opricemomentumfactor_chgalpha36m` | MATRIX | 6-Month Nominal Change in 36-Month Alpha: It is defined as the 6-month change in a stock's 36-month alpha, which equa… |
| `mdl77_opricemomentumfactor_chgvolpre4y` | MATRIX | 4-Year Change in the Average Trading Volume: It is defined as the change in the most recent 6-month moving average of… |
| `mdl77_opricemomentumfactor_high52w` | MATRIX | 52-Week High: It is defined as the month-end price divided by the highest monthly closing price in the past 12 months. |
| `mdl77_opricemomentumfactor_indrelrtn4w_` | MATRIX | 4-Week Industry Relative Return: It is defined as a stock's return in the last 4 weeks minus the average of the compa… |
| `mdl77_opricemomentumfactor_indrelrtn5d_` | MATRIX | Stock's return in the last 5 days minus the average of the comparable returns of all stocks in the same industry, the… |
| `mdl77_opricemomentumfactor_m42rav` | MATRIX | 24-Month Value at Risk: It is defined as the minimum of a stock's monthly price return in the last 20-month period. |
| `mdl77_opricemomentumfactor_m6dn2ntr` | MATRIX | Second Preceding 6-month Return: It is defined as the percent change in a stock's price from month t-12 to month t-7. |
| `mdl77_opricemomentumfactor_normalmf60d` | MATRIX | The 60-day average of a stock's daily money flow divided by daily total dollar volume. |
| `mdl77_opricemomentumfactor_ntrm01ff` | MATRIX | Fama-French Momentum: It is defined as the percent change in a stock's price from month t-12 to month t-2. |
| `mdl77_opricemomentumfactor_p50_200ratio` | MATRIX | 50-200 Day Stock Price Ratio: It is defined as the moving average of a stock's prices in the last 50 days divided by … |
| `mdl77_opricemomentumfactor_pc_ratio` | MATRIX | Put/Call Ratio: It is defined as the open interest in 7 near-the-money (1 at-the-money, next 3 above and next 3 below… |
| `mdl77_opricemomentumfactor_pctabv260low` | MATRIX | Price Above Last 260-day Lowest Trading Price: It is defined as a stock's current closing price divided by its lowest… |
| `mdl77_opricemomentumfactor_pd09erpvc` | MATRIX | CV of Prior 90-Day Closing Prices: It is defined as the standard deviation of a stock's last 90 days closing prices d… |
| `mdl77_opricemomentumfactor_rationalalpha` | MATRIX | Rational Decay Alpha: It evaluates stocks based on their historical 12-month market (S&P 500) adjusted excess return … |
| `mdl77_opricemomentumfactor_rba` | MATRIX | Abnormal Return around QTR Earnings Release: It is defined as the sum of a stock's daily market-adjusted price return… |
| `mdl77_opricemomentumfactor_relpricestrength_` | MATRIX | Industry-adjusted 12-month Relative Price Strength: It is defined as a stock's 12-month relative price strength (PS) … |
| `mdl77_opricemomentumfactor_sharpe36m` | MATRIX | Changes in a company's monthly profit in the last 3 years compared to its profit 3 months ago. |
| `mdl77_opricemomentumfactor_skew90cortn` | MATRIX | Skewness of 90-Day Stock Daily Excess Returns: It is defined as the skewness of the distribution of a stock's daily e… |
| `mdl77_opricemomentumfactor_skew90drtn` | MATRIX | Skewness of 90-Day Stock Daily Returns: It is defined as the skewness (measure of lack of symmetry) of the distributi… |
| `mdl77_opricemomentumfactor_slope52wp` | MATRIX | Slope of 52 Week Price Trend Line: It is defined as the 4-week lagged slope coefficient of the least squares regressi… |
| `mdl77_opricemomentumfactor_slope66wp` | MATRIX | Slope of 66 Week Price Trend Line: It is defined as the 4-week lagged slope coefficient of the least squares regressi… |
| `mdl77_opricemomentumfactor_sortinoratio` | MATRIX | Sortino Ratio: It is defined as a stock's annualized average monthly total return over the last 36-months less the av… |
| `mdl77_opricemomentumfactor_tstalp` | MATRIX | 1-Year Price Momentum Indicator: It is defined as: (CORREL*(260-2)^.5)/(1-CORREL^2)^.5. CORREL is the correlation coe… |
| `mdl77_opricemomentumfactor_varresirtn` | MATRIX | 24-Month Residual Return Variance: It is defined as the variance of a stock's monthly residual return in the last 24 … |
| `mdl77_opricemomentumfactor_visiratio` | MATRIX | The Visibility Ratio: It equals a stock's most recent daily trading volume divided by the average daily trading volum… |
| `mdl77_opricemomentumfactor_volpre6m` | MATRIX | The 6-month moving average of average monthly turnover ratio. |
| `mdl77_opricemomentumfactor_w15tvp` | MATRIX | This field determines the strength of trends and warns of reversals. |
| `mdl77_opricemomentumfactor_w57w03_rp` | MATRIX | 30-75 Week Stock Price Ratio: It is defined as the moving average of a stock's prices in the last 30 weeks divided by… |
| `mdl77_opricemomentumfactor_w62isr` | MATRIX | 26-Week Relative Price Strength: It is defined as a stock's most recent weekly closing price divided by its weekly cl… |
| `mdl77_opricemomentumfactor_w93ntr` | MATRIX | 39-Week Return with 4-week Lag: It is defined as a stock's price change from week t-43 to week t-4. |
| `mdl77_oput_put_capmod` | MATRIX | Capital Strength Module: It is defined as the equal-weighted average of the Industry Relative ROE, Change in Shares O… |
| `mdl77_oput_put_cashburn` | MATRIX | Cash Burn Rate: It is defined as: -(Cash From Operations + Cash from Investments)/(Cash + Short-term Investments). |
| `mdl77_oput_put_chgalpha` | MATRIX | Six-Month Alpha Change Rank: It is defined as the six-month change in a stock's twelve-month alpha, as calculated by … |
| `mdl77_oput_put_chgoll` | MATRIX | Change in Operating Liability Leverage: It is defined as the current quarter operating liability leverage less the op… |
| `mdl77_oput_put_chshrs` | MATRIX | Percent Change in Shares Outstanding: It is defined as the percent change in a company's current number of outstandin… |
| `mdl77_oput_put_composite` | MATRIX | Custom Small Cap Composite: It is defined as the equal-weighted average of the Momentum, Quality, Valuation, and Capi… |
| `mdl77_oput_put_dypeg` | MATRIX | Reciprocal of Dividend Yield-adjusted PEG: It is defined as the reciprocal of a stock's forward 12-month P/E ratio di… |
| `mdl77_oput_put_equality` | MATRIX | Earnings Quality Rank: It is defined as the equal-weighted composite of the Earnings Shortfall, Change in Inventory, … |
| `mdl77_oput_put_indepsp` | MATRIX | Industry Relative Core EPS to Price: It is defined as a stock's trailing 12-month earnings per share before extra ite… |
| `mdl77_oput_put_indestep` | MATRIX | Industry Relative Leading 4-QTRs EPS to Price: It is defined as a stock's trailing 12-month earnings per share before… |
| `mdl77_oput_put_indfcfp` | MATRIX | Industry Relative Free Cash Flow-to-Price: It is defined as a stock's trailing 12-month free cash flow-to-price ratio… |
| `mdl77_oput_put_indroe` | MATRIX | Company's ability to generate profit. |
| `mdl77_oput_put_momod` | MATRIX | The mean of three components: unexpected changes in expense or profit, and consumer confidence report. |
| `mdl77_oput_put_opincev` | MATRIX | Operating Income to EV: It is defined as a stock's ratio of trailing 4Q operating income to enterprise value (OpInc/EV). |
| `mdl77_oput_put_qualmod` | MATRIX | Quality Module: It is defined as the aggregation of the Earnings Quality (90%) and Short-Interest Ratio (10%) factors. |
| `mdl77_oput_put_siratio` | MATRIX | Short-Interest Ratio: It is defined as short-interest to average monthly volume. |
| `mdl77_oput_put_strevconf` | MATRIX | Street Revision Confidence: It is defined as the sum of the 3-month change in a stock's analysts' highest earnings fo… |
| `mdl77_oput_put_sucf` | MATRIX | Standardized Unexpected Cash Flow: It is defined as a stock's most recent reported quarterly operating cash flow minu… |
| `mdl77_oput_put_totcov` | MATRIX | Total Coverage: It equals (Cash Flow from Operations + Interest Paid + Tax Paid) / (Interest + Principal Paid). |
| `mdl77_oput_put_valmod` | MATRIX | The weighted average of various financial ratios related to a company's profits. |
| `mdl77_ovalueanalystmodel_ccaghc_avq` | MATRIX | The 1-year change in a company's trailing 4Q net operating working capital, scaled by current total assets. |
| `mdl77_ovalueanalystmodel_qva_alertrank` | MATRIX | The aggregate of the Earnings Quality (50%), Investor Sentiment (25%) and Management Signaling (25%) Rank. |
| `mdl77_ovalueanalystmodel_qva_balsht` | MATRIX | The ratio of recent cash & cash equivalents to market capitalization for a stock. |
| `mdl77_ovalueanalystmodel_qva_capexdep` | MATRIX | Capex to Depreciation Rank: It is defined as a company's trailing 12-month capital expenditures divided by the traili… |
| `mdl77_ovalueanalystmodel_qva_cashflow` | MATRIX | Cash Flow Rank: It is defined as a stock's ratio of trailing 4Q free cash flow to market capitalization (FCF/P). |
| `mdl77_ovalueanalystmodel_qva_chgato` | MATRIX | Change in Asset Turnover Rank: It is defined as the 1-year change in a company's asset turnover (TTM Sales/Total Asse… |
| `mdl77_ovalueanalystmodel_qva_chginv` | MATRIX | The one-year change in a company's trailing 4Q inventory, scaled by current total assets |
| `mdl77_ovalueanalystmodel_qva_composite` | MATRIX | The equal weighted combinations of ranks based on intrinsic value of stock and the quality of earnings. |
| `mdl77_ovalueanalystmodel_qva_earnquality` | MATRIX | Earnings Quality Rank: It is defined as the equal weighted composite of the Earnings Shortfall, Change in Inventory, … |
| `mdl77_ovalueanalystmodel_qva_earnval` | MATRIX | The equal weighted average of ranks based on price, earnings, growth, and yield. |
| `mdl77_ovalueanalystmodel_qva_epmodule` | MATRIX | Earnings Cyclicality Rank: It is defined as the aggregated ranking of a company's 3-year low 4Q EPS to enterprise val… |
| `mdl77_ovalueanalystmodel_qva_finstmt` | MATRIX | Financial Statement Rank: It is defined as the equal-weighted average of the Income Statement Rank (OpInc/Price), the… |
| `mdl77_ovalueanalystmodel_qva_invsentiment` | MATRIX | The equal-weighted sum based on a ratio of the number of stocks and those that have been sold short by investors. |
| `mdl77_ovalueanalystmodel_qva_mgtsignaling` | MATRIX | The sum of the indicators based on the changes in the number of stocks and the company's financial status. |
| `mdl77_ovalueanalystmodel_qva_pegy` | MATRIX | PEGY Rank: It is defined as the aggregated ranking of a company's price, earnings, estimated long-term growth, and di… |
| `mdl77_ovalueanalystmodel_qva_shortfall` | MATRIX | Earnings Shortfall Rank: It is defined as the difference between recent 4Q operating income before depreciation and t… |
| `mdl77_ovalueanalystmodel_qva_valuation` | MATRIX | Valuation Rank: It is defined as the equal-weighted average of the Financial Statement Rank and the Earnings Valuatio… |
| `mdl77_ovalueanalystmodel_qva_yoychgdebt` | MATRIX | Chg in Debt Issuance Rank: It is defined as a company's change in total debt over the last 12 months. |
| `mdl77_ovalueanalystmodel_qva_yoychgshares` | MATRIX | Change in Shares Outstanding Rank: It is defined as a company's change in common shares outstanding over the last 12 … |
| `mdl77_ovalueanalystmodel_tmtscni_avq` | MATRIX | Income Statement Rank: It is defined as a stock's ratio of trailing 4Q operating income to enterprise value (OpInc/EV). |
| `mdl77_pfcfy3ghc` | MATRIX | 3-yr Change in Price-Adj TTM FCF: It is defined as the difference between the most recently reported trailing 12-mont… |
| `mdl77_pfcoghc` | MATRIX | The difference between the most recently reported trailing 12-month operating cash flow per share and that of 4 quart… |
| `mdl77_priceanalystmodel_nspmoc_apq` | MATRIX | Price Analyst Sector-Neutral |
| `mdl77_priceanalystmodel_qpa_composite` | MATRIX | Score based on analysts |
| `mdl77_priceanalystmodel_qpa_indrs` | MATRIX | Industry Relative Strength |
| `mdl77_priceanalystmodel_srjdaksr_apq` | MATRIX | Risk-Adjusted Relative Strength |
| `mdl77_pricemomemtummodel_indrelrtn5d_` | MATRIX | Stock's return in the last 5 days minus the average of the comparable returns of all stocks in the same industry, the… |
| `mdl77_pricemomemtummodel_pmm_composite` | MATRIX | Price Momentum Model Composite |
| `mdl77_pricemomemtummodel_rationalalpha` | MATRIX | Rational Decay Alpha: It evaluates stocks based on their historical 12-month market (S&P 500) adjusted excess return … |
| `mdl77_pricemomemtummodel_relpricestrength_` | MATRIX | Industry-adjusted 12-month Relative Price Strength: It is defined as a stock's 12-month relative price-strength (PS) … |
| `mdl77_pricemomemtummodel_visiratio` | MATRIX | The Visibility Ratio: It equals a stock's most recent daily trading volume divided by the average daily trading volum… |
| `mdl77_pricemomemtummodel_voldiff_pc` | MATRIX | ATM Put Volatility - ATM Call Volatility: It is defined as the difference between the time-weighted average implied v… |
| `mdl77_pricemomentumfactor_25_4op` | MATRIX | One minus the quotient of a stock's last 52-week price exponential moving average divided by its last 4-week price ex… |
| `mdl77_pricemomentumfactor_6351_rp` | MATRIX | 15/36 Week Stock Price Ratio: It is defined as the moving average of a stock's prices in last 15-week divided by the … |
| `mdl77_pricemomentumfactor_actrtn12m` | MATRIX | 12-Month Active Return with 1-month Lag: It is defined as the percent change in price for a stock from month t-13 to … |
| `mdl77_pricemomentumfactor_actrtn18m` | MATRIX | 18-Month Active Return with 1-Month Lag: It is defined as the percent change in price for a stock from month t-19 to … |
| `mdl77_pricemomentumfactor_actrtn1m` | MATRIX | 1-Month Active Return: It is defined as the percent change in price for a stock from month t-1 to month t. |
| `mdl77_pricemomentumfactor_actrtn24m` | MATRIX | 24-Month Active Return with 1-Month Lag: It is defined as the percent change in price for a stock from month t-25 to … |
| `mdl77_pricemomentumfactor_actrtn2m` | MATRIX | 2-Month Active Return: It is defined as the percent change in price for a stock from month t-2 to month t. |
| `mdl77_pricemomentumfactor_actrtn36m` | MATRIX | 36-Month Active Return with 1-Month Lag: It is defined as the percent change in price for a stock from month t-37 to … |
| `mdl77_pricemomentumfactor_actrtn3m` | MATRIX | 3-Month Active Return: It is defined as the percent change in price for a stock from month t-3 to month t. |
| `mdl77_pricemomentumfactor_actrtn60m` | MATRIX | 60-Month Active Return with 1-Month Lag: It is defined as the percent change in price for a stock from month t-61 to … |
| `mdl77_pricemomentumfactor_actrtn6m` | MATRIX | 6-Month Active Return with 1-Month Lag: It is defined as the percent change in price for a stock from month t-7 to mo… |
| `mdl77_pricemomentumfactor_alpha60m` | MATRIX | 60-Month Alpha: It is defined as the intercept of the regression line which best fits a stock's monthly price return … |
| `mdl77_pricemomentumfactor_chg6malpha18m` | MATRIX | 6-Month Nominal Change in 18-Month Alpha: It is defined as the 6-month change in a stock's 18-month alpha, which equa… |
| `mdl77_pricemomentumfactor_chgalpha12m` | MATRIX | 6-Month Nominal Change in 12-Month Alpha: It is defined as the 6-month change in a stock's 12-month alpha, which equa… |
| `mdl77_pricemomentumfactor_chgalpha36m` | MATRIX | 6-Month Nominal Change in 36-Month Alpha: It is defined as the 6-month change in a stock's 36-month alpha, which equa… |
| `mdl77_pricemomentumfactor_chgvolpre4y` | MATRIX | 4-Year Change in the Average Trading Volume: It is defined as the change in the most recent 6-month moving average of… |
| `mdl77_pricemomentumfactor_high52w` | MATRIX | 52-Week High: It is defined as the month-end price divided by the highest monthly closing price in the past 12 months. |
| `mdl77_pricemomentumfactor_indrelrtn4w_` | MATRIX | 4-Week Industry Relative Return: It is defined as a stock's return in the last 4 weeks minus the average of the compa… |
| `mdl77_pricemomentumfactor_indrelrtn5d_` | MATRIX | Stock's return in the last 5 days minus the average of the comparable returns of all stocks in the same industry, the… |
| `mdl77_pricemomentumfactor_m42rav` | MATRIX | 24-Month Value at Risk: It is defined as the minimum of a stock's monthly price return in the last 20-month period. |
| `mdl77_pricemomentumfactor_m6dn2ntr` | MATRIX | Second Preceding 6-month Return: It is defined as the percent change in a stock's price from month t-12 to month t-7. |
| `mdl77_pricemomentumfactor_normalmf60d` | MATRIX | The 60-day average of a stock's daily money flow divided by daily total dollar volume. |
| `mdl77_pricemomentumfactor_ntrm01ff` | MATRIX | Fama-French Momentum: It is defined as the percent change in a stock's price from month t-12 to month t-2. |
| `mdl77_pricemomentumfactor_p50_200ratio` | MATRIX | 50-200 Day Stock Price Ratio: It is defined as the moving average of a stock's prices in the last 50 days divided by … |
| `mdl77_pricemomentumfactor_pc_ratio` | MATRIX | Put/Call Ratio: It is defined as the open interest in 7 near-the-money (1 at-the-money, next 3 above and next 3 below… |
| `mdl77_pricemomentumfactor_pctabv260low` | MATRIX | Price Above Last 260-Day Lowest Trading Price: It is defined as a stock's current closing price divided by its lowest… |
| `mdl77_pricemomentumfactor_pd09erpvc` | MATRIX | CV of Prior 90-Day Closing Prices: It is defined as the standard deviation of a stock's last 90 days closing prices d… |
| `mdl77_pricemomentumfactor_rationalalpha` | MATRIX | Rational Decay Alpha: It evaluates stocks based on their historical 12-month market (S&P 500) adjusted excess return … |
| `mdl77_pricemomentumfactor_rba` | MATRIX | Abnormal Return around QTR Earnings Release: It is defined as the sum of a stock's daily market-adjusted price return… |
| `mdl77_pricemomentumfactor_relpricestrength_` | MATRIX | Industry-adjusted 12-month Relative Price Strength: It is defined as a stock's 12-month relative price-strength (PS) … |
| `mdl77_pricemomentumfactor_sharpe36m` | MATRIX | Changes in company's monthly profit in the last 3 years compared to its profit 3 months ago. |
| `mdl77_pricemomentumfactor_skew90cortn` | MATRIX | Skewness of 90-Day Stock Daily Excess Returns: It is defined as the skewness of the distribution of a stock's daily e… |
| `mdl77_pricemomentumfactor_skew90drtn` | MATRIX | Skewness of 90-Day Stock Daily Returns: It is defined as the skewness (measure of lack of symmetry) of the distributi… |
| `mdl77_pricemomentumfactor_slope52wp` | MATRIX | Slope of 52-Week Price Trend Line: It is defined as the 4-week lagged slope coefficient of the least squares regressi… |
| `mdl77_pricemomentumfactor_slope66wp` | MATRIX | Slope of 66 Week Price Trend Line: It is defined as the 4-week lagged slope coefficient of the least squares regressi… |
| `mdl77_pricemomentumfactor_sortinoratio` | MATRIX | Sortino Ratio: It is defined as a stock's annualized average monthly total return over the last 36 months less the av… |
| `mdl77_pricemomentumfactor_tstalp` | MATRIX | 1-Year Price Momentum Indicator: It is defined as: (CORREL*(260-2)^.5)/(1-CORREL^2)^.5. CORREL is the correlation coe… |
| `mdl77_pricemomentumfactor_varresirtn` | MATRIX | 24-Month Residual Return Variance: It is defined as the variance of a stock's monthly residual return in the last 24 … |
| `mdl77_pricemomentumfactor_visiratio` | MATRIX | The Visibility Ratio: It equals a stock's most recent daily trading volume divided by the average daily trading volum… |
| `mdl77_pricemomentumfactor_volpre6m` | MATRIX | The 6-month moving average of average monthly turnover ratio. |
| `mdl77_pricemomentumfactor_w15tvp` | MATRIX | This field determines the strength of trends and warns of reversals. |
| `mdl77_pricemomentumfactor_w57w03_rp` | MATRIX | 30-75 Week Stock Price Ratio: It is defined as the moving average of a stock's prices in the last 30 weeks divided by… |
| `mdl77_pricemomentumfactor_w62isr` | MATRIX | 26-Week Relative Price Strength: It is defined as a stock's most recent weekly closing price divided by its weekly cl… |
| `mdl77_pricemomentumfactor_w93ntr` | MATRIX | 39-Week Return with 4-Week Lag: It is defined as a stock's price change from week t-43 to week t-4. |
| `mdl77_put_put_capmod` | MATRIX | Capital Strength Module: It is defined as the equal-weighted average of the Industry Relative ROE, Change in Shares O… |
| `mdl77_put_put_cashburn` | MATRIX | Cash Burn Rate: It is defined as: -(Cash From Operations + Cash from Investments)/(Cash + Short-term Investments). |
| `mdl77_put_put_chgalpha` | MATRIX | Six-Month Alpha Change Rank: It is defined as the 6-month change in a stock's 12-month alpha, as calculated by a roll… |
| `mdl77_put_put_chgoll` | MATRIX | Change in Operating Liability Leverage: It is defined as the current quarter operating liability leverage less the op… |
| `mdl77_put_put_chshrs` | MATRIX | Percent Change in Shares Outstanding: It is defined as the percent change in a company's current number of outstandin… |
| `mdl77_put_put_composite` | MATRIX | Custom Small Cap Composite: It is defined as the equal-weighted average of the Momentum, Quality, Valuation, and Capi… |
| `mdl77_put_put_dypeg` | MATRIX | Reciprocal of Dividend Yield-adjusted PEG: It is defined as the reciprocal of a stock's forward 12-month P/E ratio di… |
| `mdl77_put_put_equality` | MATRIX | Earnings Quality Rank: It is defined as the equal weighted composite of the Earnings Shortfall, Change in Inventory, … |
| `mdl77_put_put_indepsp` | MATRIX | Industry Relative Core EPS to Price: It is defined as a stock's trailing 12-month earnings per share before extra ite… |
| `mdl77_put_put_indestep` | MATRIX | Industry Relative Leading 4-QTRs EPS to Price: It is defined as a stock's trailing 12-month earnings per share before… |
| `mdl77_put_put_indfcfp` | MATRIX | Industry Relative Free Cash Flow-to-Price: It is defined as a stock's trailing 12-month free cash flow-to-price ratio… |
| `mdl77_put_put_indroe` | MATRIX | Company's ability to generate profit. |
| `mdl77_put_put_momod` | MATRIX | The mean of three components: unexpected changes in expense or profit, and the consumer confidence report. |
| `mdl77_put_put_opincev` | MATRIX | Operating Income to EV: It is defined as a stock's ratio of trailing 4Q operating income to enterprise value (OpInc/EV). |
| `mdl77_put_put_qualmod` | MATRIX | Quality Module: It is defined as the aggregation of the Earnings Quality (90%) and Short-Interest Ratio (10%) factors. |
| `mdl77_put_put_siratio` | MATRIX | Short-Interest Ratio: It is defined as short-interest to average monthly volume. |
| `mdl77_put_put_strevconf` | MATRIX | Street Revision Confidence: It is defined as the sum of the 3-month change in a stock's analysts' highest earnings fo… |
| `mdl77_put_put_sucf` | MATRIX | Standardized Unexpected Cash Flow: It is defined as a stock's most recent reported quarterly operating cash flow minu… |
| `mdl77_put_put_totcov` | MATRIX | Total Coverage: It equals (Cash Flow from Operations + Interest Paid + Tax Paid) / (Interest + Principal Paid). |
| `mdl77_put_put_valmod` | MATRIX | The weighted average of various financial ratios related to a company's profits. |
| `mdl77_putput_capmod` | MATRIX | Capital Strength Module: It is defined as the equal-weighted average of the Industry Relative ROE, Change in Shares O… |
| `mdl77_putput_cashburn` | MATRIX | Cash Burn Rate: It is defined as: -(Cash From Operations + Cash from Investments)/(Cash + Short-term Investments). |
| `mdl77_putput_chgalpha` | MATRIX | Six-Month Alpha Change Rank: It is defined as the six-month change in a stock's twelve-month alpha, as calculated by … |
| `mdl77_putput_chgoll` | MATRIX | Change in Operating Liability Leverage: It is defined as the current quarter operating liability leverage less the op… |
| `mdl77_putput_chshrs` | MATRIX | Percent Change in Shares Outstanding: It is defined as the percent change in a company's current number of outstandin… |
| `mdl77_putput_composite` | MATRIX | Custom Small Cap Composite: It is defined as the equal-weighted average of the Momentum, Quality, Valuation, and Capi… |
| `mdl77_putput_dypeg` | MATRIX | Reciprocal of Dividend Yield-adjusted PEG: It is defined as the reciprocal of a stock's forward 12-month P/E ratio di… |
| `mdl77_putput_equality` | MATRIX | Earnings Quality Rank: It is defined as the equal-weighted composite of the Earnings Shortfall, Change in Inventory, … |
| `mdl77_putput_indepsp` | MATRIX | Industry Relative Core EPS to Price: It is defined as a stock's trailing 12-month earnings per share before extra ite… |
| `mdl77_putput_indestep` | MATRIX | Industry Relative Leading 4-QTRs EPS to Price: It is defined as a stock's trailing 12-month earnings per share before… |
| `mdl77_putput_indfcfp` | MATRIX | Industry Relative Free Cash Flow-to-Price: It is defined as a stock's trailing 12-month free cash flow-to-price ratio… |
| `mdl77_putput_indroe` | MATRIX | Company's ability to generate profit. |
| `mdl77_putput_momod` | MATRIX | The mean of 3 components: unexpected changes in expense or profit, and consumer confidence report. |
| `mdl77_putput_opincev` | MATRIX | Operating Income to EV: It is defined as a stock's ratio of trailing 4Q operating income to enterprise value (OpInc/EV). |
| `mdl77_putput_qualmod` | MATRIX | Quality Module: It is defined as the aggregation of the Earnings Quality (90%) and Short-Interest Ratio (10%) factors. |
| `mdl77_putput_siratio` | MATRIX | Short-Interest Ratio: It is defined as short-interest to average monthly volume. |
| `mdl77_putput_strevconf` | MATRIX | Street Revision Confidence: It is defined as the sum of the 3-month change in a stock's analysts' highest earnings fo… |
| `mdl77_putput_sucf` | MATRIX | Standardized Unexpected Cash Flow: It is defined as a stock's most recent reported quarterly operating cash flow minu… |
| `mdl77_putput_totcov` | MATRIX | Total Coverage: It equals (Cash Flow from Operations + Interest Paid + Tax Paid) / (Interest + Principal Paid). |
| `mdl77_putput_valmod` | MATRIX | The weighted average of various financial ratios related to a company's profits. |
| `mdl77_qsa_efficiency` | MATRIX | Fundamentals Rank |
| `mdl77_qva_earnquality` | MATRIX | Earnings Quality Rank: It is defined as the equal-weighted composite of the Earnings Shortfall, Change in Inventory, … |
| `mdl77_qva_valuation` | MATRIX | Valuation Rank: It is defined as the equal-weighted average of the Financial Statement Rank and the Earnings Valuatio… |
| `mdl77_ratrev6m` | MATRIX | Street Rating Revision: It is defined as the 6-month average of the change in the average analyst recommendation trac… |
| `mdl77_rel5ycfp` | MATRIX | 5-yr Relative TTM Cash Flow-to-Price: It is defined as a stock's current trailing 12-month cash flow-to-price ratio (… |
| `mdl77_rel5ycoreepsp` | MATRIX | 5-yr Relative TTM Core Earnings-to-Price: It is defined as a stock's current trailing 12-month core earnings-to-price… |
| `mdl77_rel5yebitdap` | MATRIX | 5-yr Relative TTM EBITDA-to-Price: It is defined as a stock's current trailing 12-month EBITDA per share-to-price rat… |
| `mdl77_rel5yfcfp` | MATRIX | 5-yr Relative TTM Free Cash Flow-to-Price: It is defined as a stock's current trailing 12-month free cash flow-to-pri… |
| `mdl77_rel5yocfp` | MATRIX | 5-yr Relative TTM Oper Cash Flow-to-Price: It is defined as a stock's current trailing 12-month operating cash flow-t… |
| `mdl77_relativevaluemodel_capacq` | MATRIX | Capital Acquisition Ratio: It is defined as the trailing 12-month operating cash flow less the trailing 12-month cash… |
| `mdl77_relativevaluemodel_fc_estep` | MATRIX | Leading 12-Month Median Earnings Yield: It is defined as the next fiscal year median consensus earnings estimate divi… |
| `mdl77_relativevaluemodel_fmrelval` | MATRIX | Fielitz & Muller Relative Intrinsic Value: It is defined as a derivative of the two-stage dividend discount model to … |
| `mdl77_relativevaluemodel_pfcfmtt` | MATRIX | TTM Free Cash Flow-to-Price: It is defined as the trailing 12-month free cash flow per share for a stock divided by i… |
| `mdl77_relativevaluemodel_roe` | MATRIX | Return on Equity: It is defined as the trailing 12-month income before extra items divided by the average of common e… |
| `mdl77_relativevaluemodel_rvm_composite` | MATRIX | Model composition based on arbitrage |
| `mdl77_rerror60m` | MATRIX | Regression Error of 60-Month CAPM: It is defined as the standard error of the slope of the least squares regression l… |
| `mdl77_rsqr4qsales3y` | MATRIX | The conditional square of the correlation between monthly dates and the corresponding trailing 12-month sales per sha… |
| `mdl77_saleicap` | MATRIX | The trailing 12-month total revenues divided by the average of the invested capital in the same period. |
| `mdl77_shortsentimentfactor_act_util` | MATRIX | Account Utility |
| `mdl77_shortsentimentfactor_benchmark_fee` | MATRIX | Benchmark fee |
| `mdl77_shortsentimentfactor_conc_ratio` | MATRIX | Concentration ratio |
| `mdl77_shortsentimentfactor_days_to_cover` | MATRIX | Days to Cover |
| `mdl77_shortsentimentfactor_dmd_conc` | MATRIX | Demand concentration |
| `mdl77_shortsentimentfactor_dmd_supply` | MATRIX | Demand Supply |
| `mdl77_shortsentimentfactor_inv_conc` | MATRIX | Inventory concentration. |
| `mdl77_shortsentimentfactor_lend_supply` | MATRIX | Lend supply |
| `mdl77_shortsentimentfactor_onloan_conc` | MATRIX | On loan concentration |
| `mdl77_shortsentimentfactor_tni_ths` | MATRIX | Short Interest Ratio |
| `mdl77_sighc` | MATRIX | 1-yr Chg in QTR Inventory as Percentage ofSales: It is defined as the most recently reported inventory as a percentag… |
| `mdl77_surpriseanalystmodel_qsa_composite` | MATRIX | Surprise Analyst Composite Rank: Surprise Analyst Composite Rank |
| `mdl77_surpriseanalystmodel_qsa_efficiency` | MATRIX | Fundamentals Rank |
| `mdl77_surpriseanalystmodel_qsa_estexpect` | MATRIX | Estimate Trend Rank |
| `mdl77_surpriseanalystmodel_qsa_percent` | MATRIX | Probability of Surprise (%): Probability of Surprise (%) |
| `mdl77_surpriseanalystmodel_qsa_surpsn` | MATRIX | Rank based on analysts' surprise. |
| `mdl77_surpriseforecastmodule` | MATRIX | Surprise Forecaster Module |
| `mdl77_totalcov` | MATRIX | Total Coverage: It equals (Cash Flow from Operations + Interest Paid + Tax Paid) / (Interest + Principal Paid). |
| `mdl77_valueanalystmodel_ccaghc_avq` | MATRIX | The 1-year change in a company's trailing 4Q net operating working capital, scaled by current total assets. |
| `mdl77_valueanalystmodel_qva_alertrank` | MATRIX | The aggregate of the Earnings Quality (50%), Investor Sentiment (25%), and Management Signaling (25%) Rank. |
| `mdl77_valueanalystmodel_qva_balsht` | MATRIX | The ratio of recent cash & cash equivalents to market capitalization for a stock. |
| `mdl77_valueanalystmodel_qva_capexdep` | MATRIX | Capex to Depreciation Rank: It is defined as a company's trailing 12-month capital expenditures divided by the traili… |
| `mdl77_valueanalystmodel_qva_cashflow` | MATRIX | Cash Flow Rank: It is defined as a stock's ratio of trailing 4Q free cash flow to market capitalization (FCF/P). |
| `mdl77_valueanalystmodel_qva_chgato` | MATRIX | Change in Asset Turnover Rank: It is defined as the 1-year change in a company's asset turnover (TTM Sales/Total Asse… |
| `mdl77_valueanalystmodel_qva_chginv` | MATRIX | The one-year change in a company's trailing 4Q inventory, scaled by current total assets. |
| `mdl77_valueanalystmodel_qva_composite` | MATRIX | The equal-weighted combinations of ranks based on intrinsic value of stock and the quality of earnings. |
| `mdl77_valueanalystmodel_qva_earnquality` | MATRIX | Earnings Quality Rank: It is defined as the equal-weighted composite of the Earnings Shortfall, Change in Inventory, … |
| `mdl77_valueanalystmodel_qva_earnval` | MATRIX | The equal-weighted average of ranks based on price, earnings, growth, and yield. |
| `mdl77_valueanalystmodel_qva_epmodule` | MATRIX | Earnings Cyclicality Rank: It is defined as the aggregated ranking of a company's 3-year low 4Q EPS to enterprise val… |
| `mdl77_valueanalystmodel_qva_finstmt` | MATRIX | Financial Statement Rank: It is defined as the equal-weighted average of the Income Statement Rank (OpInc/Price), the… |
| `mdl77_valueanalystmodel_qva_invsentiment` | MATRIX | The equal weighted sum based on a ratio of number of stocks and those that have been sold short by investors. |
| `mdl77_valueanalystmodel_qva_mgtsignaling` | MATRIX | The sum of the indicators based on the changes in number of stocks, and company's financial status. |
| `mdl77_valueanalystmodel_qva_pegy` | MATRIX | PEGY Rank: It is defined as the aggregated ranking of a company's price, earnings, estimated long-term growth, and di… |
| `mdl77_valueanalystmodel_qva_shortfall` | MATRIX | Earnings Shortfall Rank: It is defined as the difference between recent 4Q operating income before depreciation and t… |
| `mdl77_valueanalystmodel_qva_valuation` | MATRIX | Valuation Rank: It is defined as the equal-weighted average of the Financial Statement Rank and the Earnings Valuatio… |
| `mdl77_valueanalystmodel_qva_yoychgdebt` | MATRIX | Chg in Debt Issuance Rank: It is defined as a company's change in total debt over the last 12 months. |
| `mdl77_valueanalystmodel_qva_yoychgshares` | MATRIX | Change in Shares Outstanding Rank: It is defined as a company's change in common shares outstanding over the last 12 … |
| `mdl77_valueanalystmodel_tmtscni_avq` | MATRIX | Income Stmt Rank : It is defined as a stock's ratio of trailing 4Q operating income to enterprise value (OpInc/EV). |
| `mdl77_valueanalystmodelccaghc_avq` | MATRIX | The 1-year change in a company's trailing 4Q net operating working capital, scaled by current total assets. |
| `mdl77_valueanalystmodelqva_alertrank` | MATRIX | The aggregate of the Earnings Quality (50%), Investor Sentiment (25%), and Management Signaling (25%) Rank. |
| `mdl77_valueanalystmodelqva_balsht` | MATRIX | The ratio of recent cash & cash equivalents to market capitalization for a stock. |
| `mdl77_valueanalystmodelqva_capexdep` | MATRIX | Capex to Depreciation Rank: It is defined as a company's trailing twelve-month capital expenditures divided by the tr… |
| `mdl77_valueanalystmodelqva_cashflow` | MATRIX | Cash Flow Rank: It is defined as a stock's ratio of trailing 4Q free cash flow to market capitalization (FCF/P). |
| `mdl77_valueanalystmodelqva_chgato` | MATRIX | Change in Asset Turnover Rank: It is defined as the 1-year change in a company's asset turnover (TTM Sales/Total Asse… |
| `mdl77_valueanalystmodelqva_chginv` | MATRIX | The 1-year change in a company's trailing 4Q inventory, scaled by current total assets |
| `mdl77_valueanalystmodelqva_composite` | MATRIX | The equal-weighted combinations of ranks based on intrinsic value of stock and the quality of earnings. |
| `mdl77_valueanalystmodelqva_earnquality` | MATRIX | Earnings Quality Rank: It is defined as the equal-weighted composite of the Earnings Shortfall, Change in Inventory, … |
| `mdl77_valueanalystmodelqva_earnval` | MATRIX | The equal-weighted average of ranks based on price, earnings, growth, and yield. |
| `mdl77_valueanalystmodelqva_epmodule` | MATRIX | Earnings Cyclicality Rank: It is defined as the aggregated ranking of a company's 3-year low 4Q EPS to enterprise val… |
| `mdl77_valueanalystmodelqva_finstmt` | MATRIX | Financial Statement Rank: It is defined as the equal weighted average of the Income Statement Rank (OpInc/Price), the… |
| `mdl77_valueanalystmodelqva_invsentiment` | MATRIX | The equal-weighted sum based on a ratio of the number of stocks and those that have been sold short by investors. |
| `mdl77_valueanalystmodelqva_mgtsignaling` | MATRIX | The sum of the indicators based on the changes in number of stocks, and company's financial status. |
| `mdl77_valueanalystmodelqva_pegy` | MATRIX | PEGY Rank: It is defined as the aggregated ranking of a company's price, earnings, estimated long-term growth, and di… |
| `mdl77_valueanalystmodelqva_shortfall` | MATRIX | Earnings Shortfall Rank: It is defined as the difference between recent 4Q operating income before depreciation and t… |
| `mdl77_valueanalystmodelqva_valuation` | MATRIX | Valuation Rank: It is defined as the equal-weighted average of the Financial Statement Rank and the Earnings Valuatio… |
| `mdl77_valueanalystmodelqva_yoychgdebt` | MATRIX | Chg in Debt Issuance Rank: It is defined as a company's change in total debt over the last 12 months. |
| `mdl77_valueanalystmodelqva_yoychgshares` | MATRIX | Change in Shares Outstanding Rank: It is defined as a company's change in common shares outstanding over the last 12 … |
| `mdl77_valueanalystmodeltmtscni_avq` | MATRIX | Income Stmt Rank: It is defined as a stock's ratio of trailing 4Q operating income to enterprise value (OpInc/EV). |
| `mdl77_valuemomemtummodel_earningsexpectationmodule` | MATRIX | Earnings Expectation Module |
| `mdl77_valuemomemtummodel_earningspricelinkmodule` | MATRIX | Earnings-Price Link Module |
| `mdl77_valuemomemtummodel_earningsqualitymodule` | MATRIX | Earnings Quality Module |
| `mdl77_valuemomemtummodel_earningsvaluationmodule` | MATRIX | Earnings Valuation Module |
| `mdl77_valuemomemtummodel_financialstatementmodule` | MATRIX | Financial Statement Module |
| `mdl77_valuemomemtummodel_investorsentimentmodule` | MATRIX | Investor Sentiment Module |
| `mdl77_valuemomemtummodel_managementsignalingmodule` | MATRIX | Management Signaling Module |
| `mdl77_valuemomemtummodel_pricemomentummodule` | MATRIX | Price Momentum Module |
| `mdl77_valuemomemtummodel_reportedearningsmomentummodule` | MATRIX | Reported Earnings Momentum Module |
| `mdl77_valuemomemtummodel_vm_compositesn` | MATRIX | Model composition based on momentum with sector neutral |
| `mdl77_valuemomemtummodel_vma_composite` | MATRIX | Model composition based on momentum |
| `mdl77_voldiff_pc` | MATRIX | ATM Put Volatility - ATM Call Volatility: It is defined as the difference between the time-weighted average implied v… |
| `mdl77_yoychggpm` | MATRIX | Yearly Change in Gross Profit Margin: It is defined as the most recent quarterly reported gross profit margin minus t… |
| `momentum_analyst_composite_score` | MATRIX | Momentum Analyst II: momentum metrics component |
| `net_fy1_analyst_revisions` | MATRIX | Weighted net number of FY1 analyst earnings forecast increases minus decreases within a month, divided by total forec… |
| `net_num_revisions_fiscal_q1` | MATRIX | Net count of analyst EPS forecast revisions for fiscal quarter 1 over a specified period |
| `net_num_revisions_fy1` | MATRIX | Weighted average net number of FY1 analyst earnings forecast increases minus decreases within one month, divided by t… |
| `net_num_revisions_fy1_earnings` | MATRIX | Net number of analyst estimate revisions for Fiscal Year 1, indicating the weighted average of upward minus downward … |
| `net_num_revisions_fy2` | MATRIX | Net number of FY2 analyst forecast revisions (raised minus lowered) within a month, weighted by total forecasts. |
| `normalized_earnings_yield` | MATRIX | Normalized earnings yield; composite metric averaging normalized measures of earnings yield |
| `north_america_sales_exposure` | MATRIX | Proportion of company sales from North America |
| `oil_price_indicator` | MATRIX | Sensitivity of the stock to changes in oil prices, measured by beta coefficient |
| `one_quarter_ahead_eps_growth` | MATRIX | Projected annualized EPS growth for the forthcoming fiscal quarter (Q1) |
| `one_year_ahead_eps_growth` | MATRIX | Consensus forecasted EPS growth for year 1 ahead (projected change in EPS, often scaled by price) |
| `one_year_change_gross_profit_to_assets_2` | MATRIX | Year-on-year change in gross profit to assets ratio. |
| `one_year_change_total_assets` | MATRIX | Percent change in total assets over most recent quarter/year |
| `one_year_eps_growth_rate` | MATRIX | Percent change in trailing twelve month earnings per share, likely over one year |
| `out_of_money_put_call_ratio` | MATRIX | Ratio of out-of-the-money put option volume to call option volume, an indicator of derivative market sentiment |
| `pb_roe_residual_value` | MATRIX | Combined metric of price-to-book and return-on-equity, possibly representing excess return relative to book equity |
| `predicted_dividend_yield` | MATRIX | Predicted dividend yield |
| `price_momentum_module_score` | MATRIX | Price Momentum (submodule of Momentum Analyst II) |
| `prior_quarter_forecast_error` | MATRIX | Forecast error for the prior fiscal quarter’s EPS; difference between actual and forecast EPS for the most recent qua… |
| `proforma_earnings_to_price` | MATRIX | TTM pro forma earnings divided by trading price; profitability relative to price |
| `projected_two_year_eps_growth` | MATRIX | Projected 2-year ahead EPS growth, estimated as the difference between FY2 and FY1 forecasted earnings scaled by shar… |
| `projected_two_year_eps_growth_2` | MATRIX | Consensus forecasted EPS growth for year 2 minus year 1, often scaled by price |
| `quarterly_earnings_surprise_stddev` | MATRIX | Most recent quarterly earnings surprise expressed in standardized units |
| `quarterly_eps_surprise_change` | MATRIX | Change in EPS surprise between recent periods, measuring how the earnings surprise has shifted from one quarter or pe… |
| `quarterly_eps_surprise_delta` | MATRIX | Change in quarterly earnings surprise (actual versus expected EPS) from previous periods |
| `rd_expense_to_sales_2` | MATRIX | R&D Intensity |
| `rd_expense_to_sales_2_v1` | MATRIX | Research and development intensity; R and D expense relative to sales |
| `real_earnings_surprise` | MATRIX | Earnings surprise: deviation of reported EPS from consensus/forecasted EPS |
| `reciprocal_dividend_yield_adjusted_peg` | MATRIX | Reciprocal (inverse) of the dividend yield-adjusted PEG ratio, blending valuation and growth adjusted for dividend yield |
| `reinvestment_rate` | MATRIX | Reinvestment rate; measure of proportion of income or cash flow that is reinvested |
| `return_on_invested_capital_4` | MATRIX | Return on invested capital; profitability measure showing efficiency of capital allocation |
| `revision_fiscal_q1_eps_forecast` | MATRIX | Change in EPS forecast for fiscal quarter 1 over the most recent period; revision in analyst expectations for Q1 |
| `risk_adjusted_peg_ratio` | MATRIX | Risk-adjusted PEG Ratio |
| `sales_surprise_score` | MATRIX | Sales surprise: difference between reported sales/revenue and analyst forecasts for the same period |
| `six_month_average_rating_revision` | MATRIX | Street Rating Revision |
| `six_month_avg_fy1_eps_revision` | MATRIX | Six-month average of revisions to fiscal year 1 EPS estimates; direction and magnitude of analyst changes |
| `six_month_change_long_term_growth` | MATRIX | Six-month change in consensus long-term earnings growth rate forecast; growth momentum |
| `six_month_eps_revision_fy2` | MATRIX | Average of prior six-month changes in consensus FY2 earnings forecasts, scaled by standard deviation. |
| `skewness_leading_12m_eps_estimates` | MATRIX | Skewness of the distribution of leading 12-month or FY1 consensus EPS estimates; asymmetry in analyst views |
| `standardized_unexpected_cash_flow` | MATRIX | Standardized unexpected cash flow; deviation of actual cash flow from predicted or expected, normalized |
| `standardized_unexpected_cashflow` | MATRIX | Standardized Unexpected Cash Flow |
| `standardized_unexpected_earnings` | MATRIX | Standardized Unexpected Earnings |
| `standardized_unexpected_earnings_2` | MATRIX | Standardized Unexpected Earnings |
| `standardized_unexpected_earnings_emfactor` | MATRIX | Standardized unexpected earnings: difference between actual and forecasted EPS, normalized by estimate variability |
| `standardized_unexpected_earnings_v1` | MATRIX | Standardized measure of earnings surprise versus analyst expectations |
| `std_adj_quarterly_earnings_surprise` | MATRIX | Standardized measure of the most recent earnings surprise (reported minus expected EPS), normalized |
| `std_adj_recent_earnings_surprise` | MATRIX | Standardized most recent quarterly earnings surprise comparing actual EPS to expected EPS |
| `stddev_fy1_eps_estimates_to_price` | MATRIX | Standard deviation of Fiscal Year 1 EPS analyst estimates divided by current stock price, reflecting the dispersion a… |
| `stddev_fy2_eps_estimates_to_price` | MATRIX | Standard deviation of consensus EPS estimates for fiscal year 2, scaled by price |
| `sustainable_growth_rate` | MATRIX | Sustainable Growth Rate |
| `sustainable_growth_rate_globaldividend` | MATRIX | Sustainable Growth Rate; maximum growth rate a company can achieve without increasing leverage |
| `ten_year_average_earnings_inflation` | MATRIX | Average inflation rate of earnings over the past ten years. |
| `three_month_change_gross_profit_margin` | MATRIX | Three-month change in gross profit margin. |
| `three_month_change_gross_profit_to_assets` | MATRIX | Three-month change in the ratio of gross profit to assets. |
| `three_month_fy1_eps_revision` | MATRIX | Three-month change in analyst forecasts for fiscal year 1 EPS; latest minus three months ago, scaled |
| `three_month_fy1_eps_revision_std` | MATRIX | Dispersion (standard deviation) of 3-month fiscal year 1 EPS forecast revisions |
| `three_month_fy2_eps_revision` | MATRIX | Three-month change in consensus fiscal year 2 EPS forecasts; analyst revisions, scaled |
| `three_month_fy2_eps_revision_2` | MATRIX | Three-month change in FY2 EPS consensus forecasts |
| `three_month_fy2_eps_revision_std` | MATRIX | 3-M Revision in FY2 EPS Forecasts: Dispersion Relative |
| `three_month_revision_fy2_eps` | MATRIX | Three-month change in FY2 (second forecast year) EPS forecasts |
| `three_year_change_gross_profit_margin_2` | MATRIX | Three-year change in gross profit margin. |
| `three_year_change_gross_profit_to_assets_2` | MATRIX | Three-year change in the ratio of gross profit to assets. |
| `time_weighted_book_value_to_price` | MATRIX | Time-weighted average of book value per share estimates for the next two years divided by close price. |
| `time_weighted_cash_flow_to_price` | MATRIX | Time-weighted average of cash flows per share estimates for the next two years divided by price. |
| `time_weighted_ebitda_to_enterprise_value_2` | MATRIX | Time-weighted EBITDA to enterprise value for the next two years. |
| `time_weighted_eps_stddev_revision` | MATRIX | Six-month average of time-weighted FY1 and FY2 earnings estimate revisions, adjusted by standard deviation. |
| `time_weighted_sales_to_price` | MATRIX | Time-weighted sales per share for the next two years divided by price. |
| `tobins_q_ratio` | MATRIX | Tobin q |
| `tobins_q_ratio_v1` | MATRIX | Market value of equity plus debt divided by total assets; Tobin's Q ratio |
| `trailing_twelve_month_accruals` | MATRIX | Trailing twelve months accruals; measure of earnings quality based on accruals |
| `treynor_index_36m` | MATRIX | Treynor Index, measuring risk-adjusted return based on systematic risk (beta) for the asset or portfolio |
| `treynor_ratio` | MATRIX | Treynor Index; risk-adjusted return ratio dividing excess return by beta (systematic risk), calculated for the stock |
| `treynor_ratio_36m` | MATRIX | Treynor Index, a measure of risk-adjusted return based on systematic risk (beta) rather than total volatility |
| `ttm_operating_cash_flow_to_ev` | MATRIX | Ratio of trailing twelve month operating cash flow to enterprise value, a fundamental valuation metric |
| `ttm_operating_cash_flow_to_price` | MATRIX | Trailing twelve-month operating cash flow-to-price |
| `ttm_operating_income_to_ev` | MATRIX | Ratio of trailing twelve month operating income to enterprise value, measure of earnings yield |
| `ttm_sales_to_enterprise_value` | MATRIX | Trailing twelve months sales divided by enterprise value; sales-based valuation metric |
| `twelve_month_short_interest_change` | MATRIX | 12-Month change in short interest position (number of shorted shares), indicator of sentiment/crowding |
| `twelve_month_total_debt_change_2` | MATRIX | 12-Month change in total debt for the company, measuring debt growth or reduction over the last year |
| `two_year_eps_growth_percent_change` | MATRIX | Percentage change in EPS growth projected two years ahead |
| `two_year_relative_eps_growth` | MATRIX | Projected EPS growth over two years based on consensus forecasts for two years forward |
| `unexpected_accounts_receivable_change` | MATRIX | Unexpected Change in Accounts Receivable |
| `unexpected_accounts_receivable_change_globaldividend` | MATRIX | Unexpected accounts receivable (deviation from expected level, scaled by assets) |
| `unexpected_change_accounts_receivable` | MATRIX | Unexpected accounts receivable; difference between actual and predicted or expected accounts receivable |
| `us_dollar_value_sensitivity` | MATRIX | Sensitivity to changes in US dollar exchange rate |
| `value_analyst_composite_score` | MATRIX | Value Analyst II: valuation metrics component |
| `value_momentum_analyst_score` | MATRIX | Value Momentum Analyst II: composite of value and momentum metrics |
| `visibility_ratio` | MATRIX | Most recent daily volume divided by average daily volume over last 50 days; trading visibility indicator |
| `volatility_adjusted_three_year_eps_growth` | MATRIX | Volatility-adjusted measure of projected EPS growth over three years; accounts for estimate uncertainty |
| `yearly_arithmetic_change_roe_2` | MATRIX | Year-over-year arithmetic change in return on equity. |
| `yearly_change_leverage` | MATRIX | Year-over-year Change in Leverage |
| `yearly_percentage_change_roe` | MATRIX | Year-over-year percentage change in return on equity. |
| `yield_curve_spread` | MATRIX | Sensitivity to changes in the yield curve slope, often measured by bond yield spreads |

## 用法提示（人工补充）

- TODO：典型组合方式、相关的 concept 页面
