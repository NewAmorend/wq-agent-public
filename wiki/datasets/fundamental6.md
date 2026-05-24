---
title: fundamental6 数据集
type: entity
tags:
- dataset
- fundamental
- usa
sources:
- worldquantbrain-api
created: '2026-05-24'
dataset_id: fundamental6
category: fundamental
delay: 1
region: USA
universe: TOP3000
---

<!-- managed by wq-agent wiki import-wq; manual edits below -->

# Company Fundamental Data for Equity

**ID**：`fundamental6`　**Category**：fundamental　**Region**：USA　**Universe**：TOP3000　**Delay**：1

## 描述

This dataset provides comprehensive, point-in-time global company fundamental data, capturing daily snapshots of financial statements, balance sheets, cash flows, and key ratios as they were known to the market at each historical date. It includes restatements, amendments, and all changes, ensuring accurate backtesting and minimizing look-ahead bias. The dataset covers a wide range of standardized and normalized financial metrics across regions and industries, making it a critical resource for quantitative research, factor modeling, and alpha generation. By reflecting the true information set available to investors at any given time, it enables robust prediction of price movements and supports the development of systematic investment strategies.

**字段数**：886

**已用 alpha 数**：683216

## 字段清单（886 项）

| id | type | description |
| --- | --- | --- |
| `assets` | MATRIX | Assets - Total |
| `assets_curr` | MATRIX | Current Assets - Total |
| `bookvalue_ps` | MATRIX | Book Value Per Share |
| `capex` | MATRIX | Capital Expenditures |
| `cash` | MATRIX | Cash |
| `cash_st` | MATRIX | Cash and Short-Term Investments |
| `cashflow` | MATRIX | Cashflow (Annual) |
| `cashflow_dividends` | MATRIX | Cash Dividends (Cash Flow) |
| `cashflow_fin` | MATRIX | Financing Activities - Net Cash Flow |
| `cashflow_invst` | MATRIX | Investing Activities - Net Cash Flow |
| `cashflow_op` | MATRIX | Operating Activities - Net Cash Flow |
| `cogs` | MATRIX | Cost of Goods Sold |
| `current_ratio` | MATRIX | Current Ratio |
| `debt` | MATRIX | Debt |
| `debt_lt` | MATRIX | Long-Term Debt - Total |
| `debt_st` | MATRIX | Debt in Current Liabilities |
| `depre_amort` | MATRIX | Depreciation and Amortization - Total |
| `ebit` | MATRIX | Earnings Before Interest and Taxes |
| `ebitda` | MATRIX | Earnings Before Interest |
| `employee` | MATRIX | Employees |
| `enterprise_value` | MATRIX | Enterprise Value |
| `eps` | MATRIX | Earnings Per Share (Basic) - Including Extraordinary Items |
| `equity` | MATRIX | Common/Ordinary Equity - Total |
| `fnd6_acdo` | MATRIX | Current Assets of Discontinued Operations |
| `fnd6_acodo` | MATRIX | Other Current Assets Excl Discontinued Operations |
| `fnd6_acox` | MATRIX | Current Assets - Other - Sundry |
| `fnd6_acqgdwl` | MATRIX | Acquired Assets - Goodwill |
| `fnd6_acqintan` | MATRIX | Acquired Assets - Intangibles |
| `fnd6_adesinda_curcd` | MATRIX | ISO Currency Code - Company Annual Market |
| `fnd6_aldo` | MATRIX | Long-term Assets of Discontinued Operations |
| `fnd6_am` | MATRIX | Amortization of Intangibles |
| `fnd6_aodo` | MATRIX | Other Assets excluding Discontinued Operations |
| `fnd6_aox` | MATRIX | Assets - Other - Sundry |
| `fnd6_aqc` | MATRIX | Acquisitions |
| `fnd6_aqi` | MATRIX | Acquisitions - Income Contribution |
| `fnd6_aqs` | MATRIX | Acquisitions - Sales Contribution |
| `fnd6_beta` | MATRIX | beta |
| `fnd6_capxs` | VECTOR | Capital Expenditures |
| `fnd6_capxv` | MATRIX | Capital Expend Property, Plant and Equipment Schd V |
| `fnd6_caxts` | VECTOR | Cost and Expenses - Total |
| `fnd6_ceql` | MATRIX | Common Equity - Liquidation Value |
| `fnd6_ch` | MATRIX | Cash |
| `fnd6_ci` | MATRIX | Comprehensive Income - Total |
| `fnd6_cibegni` | MATRIX | Comp Inc - Beginning Net Income |
| `fnd6_cicurr` | MATRIX | Comp Inc - Currency Trans Adj |
| `fnd6_cidergl` | MATRIX | Comp Inc - Derivative Gains/Losses |
| `fnd6_cik` | MATRIX | nonimportant technical code |
| `fnd6_cimii` | MATRIX | Comprehensive Income - Noncontrolling Interest |
| `fnd6_ciother` | MATRIX | Comp. Inc. - Other Adj. |
| `fnd6_cipen` | MATRIX | Comprehensive Income - Minimum Pension Adjustment |
| `fnd6_cisecgl` | MATRIX | Comp Inc - Securities Gains/Losses |
| `fnd6_citotal` | MATRIX | Comprehensive Income - Parent |
| `fnd6_city` | MATRIX | the city where a company's corporate headquarters or home office is located |
| `fnd6_cld2` | MATRIX | Capitalized Leases - Due in 2nd Year |
| `fnd6_cld3` | MATRIX | Capitalized Leases - Due in 3rd Year |
| `fnd6_cld4` | MATRIX | Capitalized Leases - Due in 4th Year |
| `fnd6_cld5` | MATRIX | Capitalized Leases - Due in 5th Year |
| `fnd6_cogss` | VECTOR | Cost of Goods Sold |
| `fnd6_cptmfmq_actq` | MATRIX | Current Assets - Total |
| `fnd6_cptmfmq_atq` | MATRIX | Assets - Total |
| `fnd6_cptmfmq_ceqq` | MATRIX | Common/Ordinary Equity - Total |
| `fnd6_cptmfmq_dlttq` | MATRIX | Long-Term Debt - Total |
| `fnd6_cptmfmq_dpq` | MATRIX | Depreciation and Amortization - Total |
| `fnd6_cptmfmq_lctq` | MATRIX | Current Liabilities - Total |
| `fnd6_cptmfmq_oibdpq` | MATRIX | Operating Income Before Depreciation - Quarterly |
| `fnd6_cptmfmq_opepsq` | MATRIX | Earnings Per Share from Operations |
| `fnd6_cptmfmq_saleq` | MATRIX | Sales/Turnover (Net) |
| `fnd6_cptnewqeventv110_actq` | VECTOR | Current Assets - Total |
| `fnd6_cptnewqeventv110_apq` | VECTOR | Accounts Payable/Creditors - Trade |
| `fnd6_cptnewqeventv110_atq` | VECTOR | Assets - Total |
| `fnd6_cptnewqeventv110_ceqq` | VECTOR | Common/Ordinary Equity - Total |
| `fnd6_cptnewqeventv110_dlttq` | VECTOR | Long-Term Debt - Total |
| `fnd6_cptnewqeventv110_dpq` | VECTOR | Depreciation and Amortization - Total |
| `fnd6_cptnewqeventv110_epsf12` | VECTOR | Earnings Per Share (Diluted) - Excluding Extraordinary Items - 12 Months Moving |
| `fnd6_cptnewqeventv110_epsfxq` | VECTOR | Earnings Per Share (Diluted) - Excluding Extraordinary items |
| `fnd6_cptnewqeventv110_epsx12` | VECTOR | Earnings Per Share (Basic) - Excluding Extraordinary Items - 12 Months Moving |
| `fnd6_cptnewqeventv110_lctq` | VECTOR | Current Liabilities - Total |
| `fnd6_cptnewqeventv110_ltq` | VECTOR | Liabilities - Total |
| `fnd6_cptnewqeventv110_nopiq` | VECTOR | Non-Operating Income (Expense) - Total |
| `fnd6_cptnewqeventv110_oeps12` | VECTOR | Earnings Per Share from Operations - 12 Months Moving |
| `fnd6_cptnewqeventv110_oiadpq` | VECTOR | Operating Income After Depreciation - Quarterly |
| `fnd6_cptnewqeventv110_oibdpq` | VECTOR | Operating Income Before Depreciation - Quarterly |
| `fnd6_cptnewqeventv110_opepsq` | VECTOR | Earnings Per Share from Operations |
| `fnd6_cptnewqeventv110_rectq` | VECTOR | Receivables - Total |
| `fnd6_cptnewqeventv110_req` | VECTOR | Retained Earnings |
| `fnd6_cptnewqeventv110_saleq` | VECTOR | Sales/Turnover (Net) |
| `fnd6_cptnewqv1300_actq` | MATRIX | Current Assets - Total |
| `fnd6_cptnewqv1300_apq` | MATRIX | Accounts Payable/Creditors - Trade |
| `fnd6_cptnewqv1300_atq` | MATRIX | Assets - Total |
| `fnd6_cptnewqv1300_ceqq` | MATRIX | Common/Ordinary Equity - Total |
| `fnd6_cptnewqv1300_dlttq` | MATRIX | Long-Term Debt - Total |
| `fnd6_cptnewqv1300_dpq` | MATRIX | Depreciation and Amortization - Total |
| `fnd6_cptnewqv1300_epsf12` | MATRIX | Earnings Per Share (Diluted) - Excluding Extraordinary Items - 12 Months Moving |
| `fnd6_cptnewqv1300_epsfxq` | MATRIX | Earnings Per Share (Diluted) - Excluding Extraordinary items |
| `fnd6_cptnewqv1300_epsx12` | MATRIX | Earnings Per Share (Basic) - Excluding Extraordinary Items - 12 Months Moving |
| `fnd6_cptnewqv1300_lctq` | MATRIX | Current Liabilities - Total |
| `fnd6_cptnewqv1300_ltq` | MATRIX | Liabilities - Total |
| `fnd6_cptnewqv1300_nopiq` | MATRIX | Non-Operating Income (Expense) - Total |
| `fnd6_cptnewqv1300_oeps12` | MATRIX | Earnings Per Share from Operations - 12 Months Moving |
| `fnd6_cptnewqv1300_oiadpq` | MATRIX | Operating Income After Depreciation - Quarterly |
| `fnd6_cptnewqv1300_oibdpq` | MATRIX | Operating Income Before Depreciation - Quarterly |
| `fnd6_cptnewqv1300_opepsq` | MATRIX | Earnings Per Share from Operations |
| `fnd6_cptnewqv1300_rectq` | MATRIX | Receivables - Total |
| `fnd6_cptnewqv1300_req` | MATRIX | Retained Earnings |
| `fnd6_cptnewqv1300_saleq` | MATRIX | Sales/Turnover (Net) |
| `fnd6_cptrank_gvkeymap` | MATRIX | technical code for a company, no need to use it for research |
| `fnd6_cshpri` | MATRIX | Common Shares Used to Calculate Earnings Per Share - Basic |
| `fnd6_cshr` | MATRIX | Common/Ordinary Shareholders |
| `fnd6_cshtr` | MATRIX | Common Shares Traded - Annual |
| `fnd6_cshtrq` | MATRIX | Common Shares Traded - Quarter |
| `fnd6_cstkcv` | MATRIX | Common Stock-Carrying Value |
| `fnd6_cstkcvq` | MATRIX | Common Stock-Carrying Value |
| `fnd6_curcddv` | VECTOR | ISO Currency Code - Dividend |
| `fnd6_currencya_curcd` | MATRIX | ISO Currency Code - Company Annual Market |
| `fnd6_currencyqv1300_curcd` | MATRIX | ISO Currency Code - Company Annual Market |
| `fnd6_dc` | MATRIX | Deferred Charges |
| `fnd6_dclo` | MATRIX | Debt - Capitalized Lease Obligations |
| `fnd6_dcpstk` | MATRIX | Convertible Debt and Preferred Stock |
| `fnd6_dcvsr` | MATRIX | Debt - Senior Convertible |
| `fnd6_dcvsub` | MATRIX | Debt - Subordinated Convertible |
| `fnd6_dcvt` | MATRIX | Debt - Convertible |
| `fnd6_dd` | MATRIX | Debt - Debentures |
| `fnd6_dd1` | MATRIX | Long-Term Debt Due in 1 Year |
| `fnd6_dd1q` | MATRIX | Long-Term Debt Due in 1 Year |
| `fnd6_dd2` | MATRIX | Debt Due in 2nd Year |
| `fnd6_dd3` | MATRIX | Debt Due in 3rd Year |
| `fnd6_dd4` | MATRIX | Debt Due in 4th Year |
| `fnd6_dd5` | MATRIX | Debt Due in 5th Year |
| `fnd6_dilavx` | MATRIX | Dilution Available - Excluding Extraordinary Items |
| `fnd6_divd` | VECTOR | Cash Dividends - Daily |
| `fnd6_dlcch` | MATRIX | Current Debt - Changes |
| `fnd6_dltis` | MATRIX | Long-Term Debt - Issuance |
| `fnd6_dlto` | MATRIX | Debt - Long-Term - Other |
| `fnd6_dltp` | MATRIX | Long-Term Debt - Tied to Prime |
| `fnd6_dltr` | MATRIX | Long-Term Debt - Reduction |
| `fnd6_dm` | MATRIX | Debt - Mortgages & Other Secured |
| `fnd6_dn` | MATRIX | Debt - Notes |
| `fnd6_donr` | MATRIX | Nonrecurring Disc Operations |
| `fnd6_dps` | VECTOR | Depreciation and Amortization |
| `fnd6_dpvieb` | MATRIX | Depreciation (Accumulated) - Ending Balance (Schedule VI) |
| `fnd6_drc` | MATRIX | Deferred Revenue - Current |
| `fnd6_drlt` | MATRIX | Deferred Revenue - Long-term |
| `fnd6_ds` | MATRIX | Debt - Subordinated |
| `fnd6_dudd` | MATRIX | Debt - Unamortized Debt Discount and Other |
| `fnd6_dvpa` | MATRIX | Preferred Dividends in Arrears |
| `fnd6_dvrated` | VECTOR | Indicated Annual Dividend Rate - Daily |
| `fnd6_dxd2` | MATRIX | Debt (excl Capitalized Leases) - Due in 2nd Year |
| `fnd6_dxd3` | MATRIX | Debt (excl Capitalized Leases) - Due in 3rd Year |
| `fnd6_dxd4` | MATRIX | Debt (excl Capitalized Leases) - Due in 4th Year |
| `fnd6_dxd5` | MATRIX | Debt (excl Capitalized Leases) - Due in 5th Year |
| `fnd6_ein` | MATRIX | Employer Identification Number code for the company |
| `fnd6_emps` | VECTOR | Employees |
| `fnd6_esopct` | MATRIX | Common ESOP Obligation - Total |
| `fnd6_esopnr` | MATRIX | Preferred ESOP Obligation - Non-Redeemable |
| `fnd6_esopr` | MATRIX | Preferred ESOP Obligation - Redeemable |
| `fnd6_esubc` | MATRIX | Equity in Net Loss - Earnings |
| `fnd6_esubs` | VECTOR | Equity in Earnings |
| `fnd6_eventv110_aqdq` | VECTOR | Acquisition/Merger Diluted EPS Effect |
| `fnd6_eventv110_aqepsq` | VECTOR | Acquisition/Merger Basic EPS Effect |
| `fnd6_eventv110_cstkcvq` | VECTOR | Common Stock - Carrying Value |
| `fnd6_eventv110_dd1q` | VECTOR | Long Term Debt Due in 1 Year |
| `fnd6_eventv110_dtedq` | VECTOR | Extinguishment of Debt Diluted EPS Effect |
| `fnd6_eventv110_dteepsq` | VECTOR | Extinguishment of Debt Basic EPS Effect |
| `fnd6_eventv110_gdwlid12` | VECTOR | Impairments Diluted EPS - 12mm |
| `fnd6_eventv110_gdwlidq` | VECTOR | Impairment of Goodwill Diluted EPS Effect |
| `fnd6_eventv110_gdwlieps12` | VECTOR | Impairment of Goodwill Basic EPS Effect 12MM |
| `fnd6_eventv110_gdwliepsq` | VECTOR | Impairment of Goodwill Basic EPS Effect |
| `fnd6_eventv110_gldq` | VECTOR | Gain/Loss Diluted EPS Effect |
| `fnd6_eventv110_glepsq` | VECTOR | Gain/Loss Basic EPS Effect |
| `fnd6_eventv110_npq` | VECTOR | Notes Payable |
| `fnd6_eventv110_nrtxtdq` | VECTOR | Nonrecurring Income Taxes Diluted EPS Effect |
| `fnd6_eventv110_nrtxtepsq` | VECTOR | Nonrecurring Income Taxes Basic EPS Effect |
| `fnd6_eventv110_optdrq` | VECTOR | Dividend Rate - Assumption (%) |
| `fnd6_eventv110_optlifeq` | VECTOR | Life of Options - Assumption (# yrs) |
| `fnd6_eventv110_optvolq` | VECTOR | Volatility - Assumption (%) |
| `fnd6_eventv110_pncd12` | VECTOR | Core Pension Adjustment Diluted EPS Effect 12MM |
| `fnd6_eventv110_pncdq` | VECTOR | Core Pension Adjustment Diluted EPS Effect |
| `fnd6_eventv110_pnceps12` | VECTOR | Core Pension Adjustment Basic EPS Effect 12MM |
| `fnd6_eventv110_pncepsq` | VECTOR | Core Pension Adjustment Basic EPS Effect |
| `fnd6_eventv110_pncidq` | VECTOR | Core Pension Interest Adjustment Diluted EPS Effect |
| `fnd6_eventv110_pncwidq` | VECTOR | Core Pension w/o Interest Adjustment Diluted EPS Effect |
| `fnd6_eventv110_pncwiepsq` | VECTOR | Core Pension w/o Interest Adjustment Basic EPS Effect |
| `fnd6_eventv110_setdq` | VECTOR | Settlement (Litigation/Insurance) Diluted EPS Effect |
| `fnd6_eventv110_setepsq` | VECTOR | Settlement (Litigation/Insurance) Basic EPS Effect |
| `fnd6_eventv110_spced12` | VECTOR | S&P Core Earnings EPS Diluted 12MM |
| `fnd6_eventv110_spidq` | VECTOR | Other Special Items Diluted EPS Effect |
| `fnd6_eventv110_spiepsq` | VECTOR | Other Special Items Basic EPS Effect |
| `fnd6_eventv110_txdbcaq` | VECTOR | Current Deferred Tax Asset |
| `fnd6_eventv110_txdbclq` | VECTOR | Current Deferred Tax Liability |
| `fnd6_eventv110_wddq` | VECTOR | Writedowns Diluted EPS Effect |
| `fnd6_eventv110_wdepsq` | VECTOR | Writedowns Basic EPS Effect |
| `fnd6_eventv110_xaccq` | VECTOR | Accrued Expenses |
| `fnd6_exre` | MATRIX | Exchange Rate Effect |
| `fnd6_fatb` | MATRIX | Plant, Property and Equipment at Cost - Buildings |
| `fnd6_fatc` | MATRIX | Plant, Property and Equipment at Cost - Construction in Progress |
| `fnd6_fate` | MATRIX | Plant, Property and Equipment at Cost - Machinery & Equipment |
| `fnd6_fatl` | MATRIX | Property, Plant, and Equipment - Leases at Cost |
| `fnd6_fatn` | MATRIX | Property, Plant, and Equipment - Natural Resources at Cost |
| `fnd6_fato` | MATRIX | Plant, Property and Equipment at Cost - Other |
| `fnd6_fatp` | MATRIX | Plant, Property and Equipment at Cost - Land & Improvements |
| `fnd6_fiao` | MATRIX | Financing Activities - Other |
| `fnd6_fic` | MATRIX | identifies the country in which the company is incorporated or legally registered |
| `fnd6_fopo` | MATRIX | Funds from Operations - Other |
| `fnd6_fopox` | MATRIX | Funds from Operations - Other excluding Option Tax Benefit |
| `fnd6_fyrc` | MATRIX | Unimportant technical code, please ignore for research purposes |
| `fnd6_gdwls` | VECTOR | Goodwill |
| `fnd6_ias` | VECTOR | Identifiable (Total) Assets |
| `fnd6_ibmii` | MATRIX | Income before Extraordinary Items and Noncontrolling Interests |
| `fnd6_ibs` | VECTOR | Income before Extraordinary Items |
| `fnd6_idesindq_curcd` | MATRIX | ISO Currency Code - Company Annual Market |
| `fnd6_idit` | MATRIX | Interest and Related Income - Total |
| `fnd6_iints` | VECTOR | Interest Income |
| `fnd6_incorp` | MATRIX | Incorporated |
| `fnd6_intan` | MATRIX | Intangible Assets - Total |
| `fnd6_intc` | MATRIX | Interest Capitalized |
| `fnd6_intpn` | MATRIX | Interest Paid - Net |
| `fnd6_intseg` | VECTOR | Intersegment Eliminations |
| `fnd6_invfg` | MATRIX | Inventories - Finished Goods |
| `fnd6_invo` | MATRIX | Inventories - Other |
| `fnd6_invrm` | MATRIX | Inventories - Raw Materials |
| `fnd6_invwip` | MATRIX | Inventories - Work In Process |
| `fnd6_itcb` | MATRIX | Investment Tax Credit (Balance Sheet) |
| `fnd6_itci` | MATRIX | Investment Tax Credit (Income Account) |
| `fnd6_ivaco` | MATRIX | Investing Activities - Other |
| `fnd6_ivaeq` | MATRIX | Investment and Advances - Equity |
| `fnd6_ivaeqs` | VECTOR | Investments at Equity |
| `fnd6_ivao` | MATRIX | Investment and Advances - Other |
| `fnd6_ivch` | MATRIX | Increase in Investments |
| `fnd6_ivst` | MATRIX | Short-Term Investments - Total |
| `fnd6_ivstch` | MATRIX | Short-Term Investments - Change |
| `fnd6_lcox` | MATRIX | Current Liabilities - Other - Sundry |
| `fnd6_lcoxdr` | MATRIX | Current Liabilities - Other - Excluding Deferred Revenue |
| `fnd6_lifr` | MATRIX | LIFO Reserve |
| `fnd6_lno` | MATRIX | Liabilities Netting & Other Adjustments |
| `fnd6_loc` | MATRIX | string for locating the Headquarters of the company |
| `fnd6_lol2` | MATRIX | Liabilities Level 2 (Observable) |
| `fnd6_loxdr` | MATRIX | Liabilities - Other - Excluding Deferred Revenue |
| `fnd6_lqpl1` | MATRIX | Liabilities Level 1 (Quoted Prices) |
| `fnd6_lul3` | MATRIX | Liabilities Level 3 (Unobservable) |
| `fnd6_mfma1_aoloch` | MATRIX | Assets and Liabilities - Other - Net Change |
| `fnd6_mfma1_apalch` | MATRIX | Accounts Payable and Accrued Liabilities - Increase/(Decrease) |
| `fnd6_mfma1_at` | MATRIX | Assets - Total |
| `fnd6_mfma1_capx` | MATRIX | Capital Expenditures |
| `fnd6_mfma1_csho` | MATRIX | Common Shares Outstanding |
| `fnd6_mfma1_dp` | MATRIX | Depreciation and Amortization |
| `fnd6_mfma1_dpc` | MATRIX | Depreciation and Amortization (Cash Flow) |
| `fnd6_mfma1_invch` | MATRIX | Mortgages - Decrease (Increase) |
| `fnd6_mfma2_oancf` | MATRIX | Operating Activities - Net Cash Flow |
| `fnd6_mfma2_opeps` | MATRIX | Earnings Per Share from Operations |
| `fnd6_mfma2_recch` | MATRIX | Accounts Receivable - Decrease (Increase) |
| `fnd6_mfma2_revt` | MATRIX | Revenue - Total |
| `fnd6_mfma2_txach` | MATRIX | Income Taxes - Accrued - Increase/(Decrease) |
| `fnd6_mfmq_cheq` | MATRIX | Cash and Short-Term Investments |
| `fnd6_mfmq_cogsq` | MATRIX | Cost of Goods Sold |
| `fnd6_mfmq_cshprq` | MATRIX | Common Shares Used to Calculate Earnings Per Share - Basic |
| `fnd6_mfmq_dlcq` | MATRIX | Debt in Current Liabilities |
| `fnd6_mfmq_ibcomq` | MATRIX | Income Before Extraordinary Items - Available for Common |
| `fnd6_mfmq_mibtq` | MATRIX | Noncontrolling Interests - Total - Balance Sheet - Quarterly |
| `fnd6_mfmq_piq` | MATRIX | Pretax Income |
| `fnd6_mibn` | MATRIX | Noncontrolling Interests - Nonredeemable - Balance Sheet |
| `fnd6_mibt` | MATRIX | Noncontrolling Interests - Total - Balance Sheet |
| `fnd6_mkvalt` | MATRIX | Market Value - Total |
| `fnd6_mkvaltq` | MATRIX | Market Value - Total |
| `fnd6_mrc1` | MATRIX | Rental Commitments - Minimum - 1st Year |
| `fnd6_mrc2` | MATRIX | Rental Commitments - Minimum - 2nd Year |
| `fnd6_mrc3` | MATRIX | Rental Commitments - Minimum - 3rd Year |
| `fnd6_mrc4` | MATRIX | Rental Commitments - Minimum - 4th Year |
| `fnd6_mrc5` | MATRIX | Rental Commitments - Minimum - 5th Year |
| `fnd6_mrct` | MATRIX | Rental Commitments - Minimum - 5-Year Total |
| `fnd6_mrcta` | MATRIX | Thereafter Portion of Leases |
| `fnd6_msa` | MATRIX | Marketable Securities Adjustment |
| `fnd6_naicss` | VECTOR | NAICS Code |
| `fnd6_newa1v1300_aco` | MATRIX | Current Assets - Other - Total |
| `fnd6_newa1v1300_acominc` | MATRIX | Accumulated Other Comprehensive Income (Loss) |
| `fnd6_newa1v1300_act` | MATRIX | Current Assets - Total |
| `fnd6_newa1v1300_ano` | MATRIX | Assets Netting & Other Adjustments |
| `fnd6_newa1v1300_ao` | MATRIX | Assets - Other |
| `fnd6_newa1v1300_aocidergl` | MATRIX | Accum Other Comp Inc - Derivatives Unrealized Gain/Loss |
| `fnd6_newa1v1300_aociother` | MATRIX | Accum Other Comp Inc - Other Adjustments |
| `fnd6_newa1v1300_aocipen` | MATRIX | Accum Other Comp Inc - Min Pension Liab Adj |
| `fnd6_newa1v1300_aol2` | MATRIX | Assets Level 2 (Observable) |
| `fnd6_newa1v1300_aoloch` | MATRIX | Assets and Liabilities - Other - Net Change |
| `fnd6_newa1v1300_ap` | MATRIX | Accounts Payable - Trade |
| `fnd6_newa1v1300_apalch` | MATRIX | Accounts Payable and Accrued Liabilities - Increase/(Decrease) |
| `fnd6_newa1v1300_aqpl1` | MATRIX | Assets Level 1 (Quoted Prices) |
| `fnd6_newa1v1300_at` | MATRIX | Assets - Total |
| `fnd6_newa1v1300_aul3` | MATRIX | Assets Level 3 (Unobservable) |
| `fnd6_newa1v1300_bkvlps` | MATRIX | Book Value Per Share |
| `fnd6_newa1v1300_caps` | MATRIX | Capital Surplus/Share Premium Reserve |
| `fnd6_newa1v1300_capx` | MATRIX | Capital Expenditures |
| `fnd6_newa1v1300_ceq` | MATRIX | Common/Ordinary Equity - Total |
| `fnd6_newa1v1300_ceqt` | MATRIX | Common Equity - Tangible |
| `fnd6_newa1v1300_che` | MATRIX | Cash and Short-Term Investments |
| `fnd6_newa1v1300_chech` | MATRIX | Cash and Cash Equivalents - Increase/(Decrease) |
| `fnd6_newa1v1300_cogs` | MATRIX | Cost of Goods Sold |
| `fnd6_newa1v1300_cshfd` | MATRIX | Common Shares Used to Calc Earnings Per Share - Fully Diluted |
| `fnd6_newa1v1300_cshi` | MATRIX | Common Shares Issued |
| `fnd6_newa1v1300_csho` | MATRIX | Common Shares Outstanding |
| `fnd6_newa1v1300_cstk` | MATRIX | Common/Ordinary Stock (Capital) |
| `fnd6_newa1v1300_dcom` | MATRIX | Deferred Compensation |
| `fnd6_newa1v1300_dlc` | MATRIX | Debt in Current Liabilities - Total |
| `fnd6_newa1v1300_dltt` | MATRIX | Long-Term Debt - Total |
| `fnd6_newa1v1300_dp` | MATRIX | Depreciation and Amortization |
| `fnd6_newa1v1300_dpact` | MATRIX | Depreciation, Depletion and Amortization (Accumulated) |
| `fnd6_newa1v1300_dpc` | MATRIX | Depreciation and Amortization (Cash Flow) |
| `fnd6_newa1v1300_dv` | MATRIX | Cash Dividends (Cash Flow) |
| `fnd6_newa1v1300_dvc` | MATRIX | Dividends Common/Ordinary |
| `fnd6_newa1v1300_dvt` | MATRIX | Dividends - Total |
| `fnd6_newa1v1300_ebit` | MATRIX | Earnings Before Interest and Taxes |
| `fnd6_newa1v1300_ebitda` | MATRIX | Earnings Before Interest |
| `fnd6_newa1v1300_emp` | MATRIX | Employees |
| `fnd6_newa1v1300_epsfi` | MATRIX | Earnings Per Share (Diluted) - Including Extraordinary Items |
| `fnd6_newa1v1300_epsfx` | MATRIX | Earnings Per Share (Diluted) - Excluding Extraordinary Items |
| `fnd6_newa1v1300_epspi` | MATRIX | Earnings Per Share (Basic) - Including Extraordinary Items |
| `fnd6_newa1v1300_epspx` | MATRIX | Earnings Per Share (Basic) - Excluding Extraordinary Items |
| `fnd6_newa1v1300_fca` | MATRIX | Foreign Exchange Income (Loss) |
| `fnd6_newa1v1300_fincf` | MATRIX | Financing Activities - Net Cash Flow |
| `fnd6_newa1v1300_gdwl` | MATRIX | Goodwill |
| `fnd6_newa1v1300_gp` | MATRIX | Gross Profit (Loss) |
| `fnd6_newa1v1300_ib` | MATRIX | Income Before Extraordinary Items |
| `fnd6_newa1v1300_ibadj` | MATRIX | Income Before Extraordinary Items - Adjusted for Common Stock Equivalents |
| `fnd6_newa1v1300_ibc` | MATRIX | Income Before Extraordinary Items (Cash Flow) |
| `fnd6_newa1v1300_ibcom` | MATRIX | Income Before Extraordinary Items - Available for Common |
| `fnd6_newa1v1300_icapt` | MATRIX | Invested Capital - Total |
| `fnd6_newa1v1300_intano` | MATRIX | Other Intangibles |
| `fnd6_newa1v1300_invch` | MATRIX | Mortgages - Decrease (Increase) |
| `fnd6_newa1v1300_invt` | MATRIX | Inventories - Total |
| `fnd6_newa1v1300_ivncf` | MATRIX | Investing Activities - Net Cash Flow |
| `fnd6_newa1v1300_lco` | MATRIX | Current Liabilities - Other - Total |
| `fnd6_newa1v1300_lct` | MATRIX | Current Liabilities - Total |
| `fnd6_newa1v1300_lo` | MATRIX | Liabilities - Other - Total |
| `fnd6_newa1v1300_lse` | MATRIX | Liabilities and Stockholders Equity - Total |
| `fnd6_newa1v1300_lt` | MATRIX | Liabilities - Total |
| `fnd6_newa2v1300_mib` | MATRIX | Minority Interest (Balance Sheet) |
| `fnd6_newa2v1300_mii` | MATRIX | Noncontrolling Interest (Income Account) |
| `fnd6_newa2v1300_ni` | MATRIX | Net Income (Loss) |
| `fnd6_newa2v1300_nopi` | MATRIX | Nonoperating Income (Expense) |
| `fnd6_newa2v1300_oancf` | MATRIX | Operating Activities - Net Cash Flow |
| `fnd6_newa2v1300_oiadp` | MATRIX | Operating Income After Depreciation |
| `fnd6_newa2v1300_oibdp` | MATRIX | Operating Income Before Depreciation |
| `fnd6_newa2v1300_opeps` | MATRIX | Earnings Per Share from Operations |
| `fnd6_newa2v1300_optexd` | MATRIX | Options - Exercised (-) |
| `fnd6_newa2v1300_pi` | MATRIX | Pretax Income |
| `fnd6_newa2v1300_ppegt` | MATRIX | Property, Plant and Equipment - Total (Gross) |
| `fnd6_newa2v1300_ppent` | MATRIX | Property, Plant and Equipment - Total (Net) |
| `fnd6_newa2v1300_prsho` | MATRIX | Redeem Pfd Shares Outs (000) |
| `fnd6_newa2v1300_rdip` | MATRIX | In Process R&D Expense |
| `fnd6_newa2v1300_rdipa` | MATRIX | In-Process R&D Expense After-tax |
| `fnd6_newa2v1300_rdipd` | MATRIX | In Process R&D Expense Diluted EPS Effect |
| `fnd6_newa2v1300_rdipeps` | MATRIX | In Process R&D Expense Basic EPS Effect |
| `fnd6_newa2v1300_re` | MATRIX | Retained Earnings |
| `fnd6_newa2v1300_recch` | MATRIX | Accounts Receivable - Decrease (Increase) |
| `fnd6_newa2v1300_rect` | MATRIX | Receivables - Total |
| `fnd6_newa2v1300_reuna` | MATRIX | Retained Earnings - Unadjusted |
| `fnd6_newa2v1300_revt` | MATRIX | Revenue - Total |
| `fnd6_newa2v1300_sale` | MATRIX | Sales/Turnover (Net) |
| `fnd6_newa2v1300_seq` | MATRIX | Stockholders Equity - Parent |
| `fnd6_newa2v1300_seqo` | MATRIX | Other Stockholders' Equity Adjustments |
| `fnd6_newa2v1300_spced` | MATRIX | S&P Core Earnings EPS Diluted |
| `fnd6_newa2v1300_spceeps` | MATRIX | S&P Core Earnings EPS Basic |
| `fnd6_newa2v1300_spi` | MATRIX | Special Items |
| `fnd6_newa2v1300_stkco` | MATRIX | Stock Compensation Expense |
| `fnd6_newa2v1300_tstk` | MATRIX | Treasury Stock - Total (All Capital) |
| `fnd6_newa2v1300_tstkn` | MATRIX | Treasury Stock - Number of Common Shares |
| `fnd6_newa2v1300_txach` | MATRIX | Income Taxes - Accrued - Increase/(Decrease) |
| `fnd6_newa2v1300_txdb` | MATRIX | Deferred Taxes - Balance Sheet |
| `fnd6_newa2v1300_txditc` | MATRIX | Deferred Taxes and Investment Tax Credit |
| `fnd6_newa2v1300_txp` | MATRIX | Income Taxes Payable |
| `fnd6_newa2v1300_txt` | MATRIX | Income Taxes - Total |
| `fnd6_newa2v1300_wcap` | MATRIX | Working Capital (Balance Sheet) |
| `fnd6_newa2v1300_xidoc` | MATRIX | Extraordinary Items and Discontinued Operations (Cash Flow) |
| `fnd6_newa2v1300_xint` | MATRIX | Interest and Related Expense - Total |
| `fnd6_newa2v1300_xoptd` | MATRIX | Implied Option EPS Diluted |
| `fnd6_newa2v1300_xopteps` | MATRIX | Implied Option EPS Basic |
| `fnd6_newa2v1300_xrd` | MATRIX | Research and Development Expense |
| `fnd6_newa2v1300_xsga` | MATRIX | Selling, General and Administrative Expense |
| `fnd6_newq_xoptdqp` | MATRIX | Implied Option EPS Diluted Preliminary |
| `fnd6_newq_xoptepsqp` | MATRIX | Implied Option EPS Basic Preliminary |
| `fnd6_newq_xoptqp` | MATRIX | Implied Option Expense Preliminary |
| `fnd6_newqeventv110_acchgq` | VECTOR | Accounting Changes - Cumulative Effect |
| `fnd6_newqeventv110_acomincq` | VECTOR | Accumulated Other Comprehensive Income (Loss) |
| `fnd6_newqeventv110_acoq` | VECTOR | Current Assets - Other - Total |
| `fnd6_newqeventv110_altoq` | VECTOR | Other Long-term Assets |
| `fnd6_newqeventv110_ancq` | VECTOR | Non-Current Assets - Total |
| `fnd6_newqeventv110_anoq` | VECTOR | Assets Netting & Other Adjustments |
| `fnd6_newqeventv110_aociderglq` | VECTOR | Accumulated Other Comprehensive Income - Derivatives Unrealized Gain/Loss |
| `fnd6_newqeventv110_aociotherq` | VECTOR | Accum Other Comp Inc - Other Adjustments |
| `fnd6_newqeventv110_aocipenq` | VECTOR | Accum Other Comp Inc - Min Pension Liab Adj |
| `fnd6_newqeventv110_aocisecglq` | VECTOR | Accum. Other Comp. Inc. - Unreal G/L Ret. Int. in Sec. Assets |
| `fnd6_newqeventv110_aol2q` | VECTOR | Assets Level 2 (Observable) |
| `fnd6_newqeventv110_aoq` | VECTOR | Assets - Other - Total |
| `fnd6_newqeventv110_aqaq` | VECTOR | Acquisition/Merger After-Tax |
| `fnd6_newqeventv110_aqpl1q` | VECTOR | Assets Level 1 (Quoted Prices) |
| `fnd6_newqeventv110_aqpq` | VECTOR | Acquisition/Merger Pretax |
| `fnd6_newqeventv110_aul3q` | VECTOR | Assets Level 3 (Unobservable) |
| `fnd6_newqeventv110_capsq` | VECTOR | Capital Surplus/Share Premium Reserve |
| `fnd6_newqeventv110_cheq` | VECTOR | Cash and Short-Term Investments |
| `fnd6_newqeventv110_chq` | VECTOR | Cash |
| `fnd6_newqeventv110_cibegniq` | VECTOR | Comp Inc - Beginning Net Income |
| `fnd6_newqeventv110_cicurrq` | VECTOR | Comp Inc - Currency Trans Adj |
| `fnd6_newqeventv110_ciderglq` | VECTOR | Comprehensive Income - Derivative Gains/Losses |
| `fnd6_newqeventv110_cimiiq` | VECTOR | Comprehensive Income - Noncontrolling Interest |
| `fnd6_newqeventv110_ciotherq` | VECTOR | Comprehensive Income - Other Adjustments |
| `fnd6_newqeventv110_cipenq` | VECTOR | Comp Inc - Minimum Pension Adj |
| `fnd6_newqeventv110_ciq` | VECTOR | Comprehensive Income - Total |
| `fnd6_newqeventv110_cisecglq` | VECTOR | Comp Inc - Securities Gains/Losses |
| `fnd6_newqeventv110_citotalq` | VECTOR | Comprehensive Income - Parent |
| `fnd6_newqeventv110_cogsq` | VECTOR | Cost of Goods Sold |
| `fnd6_newqeventv110_csh12q` | VECTOR | Common Shares Used to Calculate Earnings Per Share - 12 Months Moving |
| `fnd6_newqeventv110_cshfdq` | VECTOR | Common Shares for Diluted EPS |
| `fnd6_newqeventv110_cshiq` | VECTOR | Common Shares Issued |
| `fnd6_newqeventv110_cshopq` | VECTOR | Total Shares Repurchased - Quarter |
| `fnd6_newqeventv110_cshoq` | VECTOR | Common Shares Outstanding |
| `fnd6_newqeventv110_cshprq` | VECTOR | Common Shares Used to Calculate Earnings Per Share - Basic |
| `fnd6_newqeventv110_cstkeq` | VECTOR | Common Stock Equivalents - Dollar Savings |
| `fnd6_newqeventv110_cstkq` | VECTOR | Common/Ordinary Stock (Capital) |
| `fnd6_newqeventv110_dcomq` | VECTOR | Deferred Compensation |
| `fnd6_newqeventv110_diladq` | VECTOR | Dilution Adjustment |
| `fnd6_newqeventv110_dilavq` | VECTOR | Dilution Available - Excluding Extraordinary Items |
| `fnd6_newqeventv110_dlcq` | VECTOR | Debt in Current Liabilities |
| `fnd6_newqeventv110_doq` | VECTOR | Discontinued Operations |
| `fnd6_newqeventv110_dpactq` | VECTOR | Depreciation, Depletion and Amortization (Accumulated) |
| `fnd6_newqeventv110_drcq` | VECTOR | Deferred Revenue - Current |
| `fnd6_newqeventv110_drltq` | VECTOR | Deferred Revenue - Long-term |
| `fnd6_newqeventv110_dteaq` | VECTOR | Extinguishment of Debt After-tax |
| `fnd6_newqeventv110_dtepq` | VECTOR | Extinguishment of Debt Pretax |
| `fnd6_newqeventv110_dvpq` | VECTOR | Dividends - Preferred/Preference |
| `fnd6_newqeventv110_epsfiq` | VECTOR | Earnings Per Share (Diluted) - Including Extraordinary Items |
| `fnd6_newqeventv110_epspiq` | VECTOR | Earnings Per Share (Basic) - Including Extraordinary Items |
| `fnd6_newqeventv110_epspxq` | VECTOR | Earnings Per Share (Basic) - Excluding Extraordinary Items |
| `fnd6_newqeventv110_esopctq` | VECTOR | Common ESOP Obligation - Total |
| `fnd6_newqeventv110_esopnrq` | VECTOR | Preferred ESOP Obligation - Non-Redeemable |
| `fnd6_newqeventv110_esoprq` | VECTOR | Preferred ESOP Obligation - Redeemable |
| `fnd6_newqeventv110_esoptq` | VECTOR | Preferred ESOP Obligation - Total |
| `fnd6_newqeventv110_fcaq` | VECTOR | Foreign Exchange Income (Loss) |
| `fnd6_newqeventv110_gdwlamq` | VECTOR | Amortization of Goodwill |
| `fnd6_newqeventv110_gdwlia12` | VECTOR | Impairments of Goodwill After-Tax - 12MM |
| `fnd6_newqeventv110_gdwliaq` | VECTOR | Impairment of Goodwill After-tax |
| `fnd6_newqeventv110_gdwlipq` | VECTOR | Impairment of Goodwill Pretax |
| `fnd6_newqeventv110_gdwlq` | VECTOR | Goodwill (net) |
| `fnd6_newqeventv110_glaq` | VECTOR | Gain/Loss After-Tax |
| `fnd6_newqeventv110_glcea12` | VECTOR | Gain/Loss on Sale (Core Earnings Adjusted) After-tax 12MM |
| `fnd6_newqeventv110_glceaq` | VECTOR | Gain/Loss on Sale (Core Earnings Adjusted) After-tax |
| `fnd6_newqeventv110_glced12` | VECTOR | Gain/Loss on Sale (Core Earnings Adjusted) Diluted EPS Effect 12MM |
| `fnd6_newqeventv110_glcedq` | VECTOR | Gain/Loss on Sale (Core Earnings Adjusted) Diluted EPS |
| `fnd6_newqeventv110_glceeps12` | VECTOR | Gain/Loss on Sale (Core Earnings Adjusted) Basic EPS Effect 12MM |
| `fnd6_newqeventv110_glceepsq` | VECTOR | Gain/Loss on Sale (Core Earnings Adjusted) Basic EPS Effect |
| `fnd6_newqeventv110_glcepq` | VECTOR | Gain/Loss on Sale (Core Earnings Adjusted) Pretax |
| `fnd6_newqeventv110_glpq` | VECTOR | Gain/Loss Pretax |
| `fnd6_newqeventv110_hedgeglq` | VECTOR | Gain/Loss on Ineffective Hedges |
| `fnd6_newqeventv110_ibadj12` | VECTOR | Income Before Extra Items - Adj for Common Stock Equivalents - 12MM |
| `fnd6_newqeventv110_ibadjq` | VECTOR | Income Before Extraordinary Items - Adjusted for Common Stock Equivalents |
| `fnd6_newqeventv110_ibcomq` | VECTOR | Income Before Extraordinary Items - Available for Common |
| `fnd6_newqeventv110_ibmiiq` | VECTOR | Income before Extraordinary Items and Noncontrolling Interests |
| `fnd6_newqeventv110_ibq` | VECTOR | Income Before Extraordinary Items |
| `fnd6_newqeventv110_icaptq` | VECTOR | Invested Capital - Total - Quarterly |
| `fnd6_newqeventv110_intanoq` | VECTOR | Other Intangibles |
| `fnd6_newqeventv110_intanq` | VECTOR | Intangible Assets - Total |
| `fnd6_newqeventv110_invfgq` | VECTOR | Inventory - Finished Goods |
| `fnd6_newqeventv110_invoq` | VECTOR | Inventory - Other |
| `fnd6_newqeventv110_invrmq` | VECTOR | Inventory - Raw Materials |
| `fnd6_newqeventv110_invtq` | VECTOR | Inventories - Total |
| `fnd6_newqeventv110_invwipq` | VECTOR | Inventory - Work in Process |
| `fnd6_newqeventv110_ivltq` | VECTOR | Total Long-term Investments |
| `fnd6_newqeventv110_ivstq` | VECTOR | Short-Term Investments - Total |
| `fnd6_newqeventv110_lcoq` | VECTOR | Current Liabilities - Other - Total |
| `fnd6_newqeventv110_lltq` | VECTOR | Long-Term Liabilities (Total) |
| `fnd6_newqeventv110_lnoq` | VECTOR | Liabilities Netting & Other Adjustments |
| `fnd6_newqeventv110_lol2q` | VECTOR | Liabilities Level 2 (Observable) |
| `fnd6_newqeventv110_loq` | VECTOR | Liabilities - Other |
| `fnd6_newqeventv110_loxdrq` | VECTOR | Liabilities - Other - Excluding Deferred Revenue |
| `fnd6_newqeventv110_lqpl1q` | VECTOR | Liabilities Level 1 (Quoted Prices) |
| `fnd6_newqeventv110_lseq` | VECTOR | Liabilities and Stockholders' Equity - Total |
| `fnd6_newqeventv110_ltmibq` | VECTOR | Liabilities - Total and Noncontrolling Interest |
| `fnd6_newqeventv110_lul3q` | VECTOR | Liabilities Level 3 (Unobservable) |
| `fnd6_newqeventv110_mibnq` | VECTOR | NonRedeemable Noncontrolling Interest (Balance Sheet) - Quarterly |
| `fnd6_newqeventv110_mibq` | VECTOR | Noncontrolling Interest - Redeemable - Balance Sheet |
| `fnd6_newqeventv110_mibtq` | VECTOR | Noncontrolling Interests - Total - Balance Sheet - Quarterly |
| `fnd6_newqeventv110_miiq` | VECTOR | Noncontrolling Interest - Income Account |
| `fnd6_newqeventv110_msaq` | VECTOR | Accum Other Comp Inc - Marketable Security Adjustments |
| `fnd6_newqeventv110_nrtxtq` | VECTOR | Nonrecurring Income Taxes - After-tax |
| `fnd6_newqeventv110_oepf12` | VECTOR | Earnings Per Share - Diluted - from Operations - 12MM |
| `fnd6_newqeventv110_oepsxq` | VECTOR | Earnings Per Share - Diluted - from Operations |
| `fnd6_newqeventv110_optfvgrq` | VECTOR | Options - Fair Value of Options Granted |
| `fnd6_newqeventv110_optrfrq` | VECTOR | Risk Free Rate - Assumption (%) |
| `fnd6_newqeventv110_piq` | VECTOR | Pretax Income |
| `fnd6_newqeventv110_pnc12` | VECTOR | Pension Core Adjustment - 12mm |
| `fnd6_newqeventv110_pnciapq` | VECTOR | Core Pension Interest Adjustment After-tax Preliminary |
| `fnd6_newqeventv110_pnciaq` | VECTOR | Core Pension Interest Adjustment After-tax |
| `fnd6_newqeventv110_pncidpq` | VECTOR | Core Pension Interest Adjustment Diluted EPS Effect Preliminary |
| `fnd6_newqeventv110_pnciepspq` | VECTOR | Core Pension Interest Adjustment Basic EPS Effect Preliminary |
| `fnd6_newqeventv110_pnciepsq` | VECTOR | Core Pension Interest Adjustment Basic EPS Effect |
| `fnd6_newqeventv110_pncippq` | VECTOR | Core Pension Interest Adjustment Pretax Preliminary |
| `fnd6_newqeventv110_pncipq` | VECTOR | Core Pension Interest Adjustment Pretax |
| `fnd6_newqeventv110_pncpd12` | VECTOR | Core Pension Adjustment 12MM Diluted EPS Effect Preliminary |
| `fnd6_newqeventv110_pncpdq` | VECTOR | Core Pension Adjustment Diluted EPS Effect Preliminary |
| `fnd6_newqeventv110_pncpeps12` | VECTOR | Core Pension Adjustment 12MM Basic EPS Effect Preliminary |
| `fnd6_newqeventv110_pncpepsq` | VECTOR | Core Pension Adjustment Basic EPS Effect Preliminary |
| `fnd6_newqeventv110_pncpq` | VECTOR | Core Pension Adjustment Preliminary |
| `fnd6_newqeventv110_pncq` | VECTOR | Core Pension Adjustment |
| `fnd6_newqeventv110_pncwiapq` | VECTOR | Core Pension w/o Interest Adjustment After-tax Preliminary |
| `fnd6_newqeventv110_pncwiaq` | VECTOR | Core Pension w/o Interest Adjustment After-tax |
| `fnd6_newqeventv110_pncwidpq` | VECTOR | Core Pension w/o Interest Adjustment Diluted EPS Effect Preliminary |
| `fnd6_newqeventv110_pncwiepq` | VECTOR | Core Pension Without Interest Adjustment Basic EPS Effect Preliminary |
| `fnd6_newqeventv110_pncwippq` | VECTOR | Core Pension w/o Interest Adjustment Pretax Preliminary |
| `fnd6_newqeventv110_pncwipq` | VECTOR | Core Pension Without Interest Adjustment Pretax |
| `fnd6_newqeventv110_pnrshoq` | VECTOR | Nonred Pfd Shares Outs (000) - Quarterly |
| `fnd6_newqeventv110_ppegtq` | VECTOR | Property, Plant and Equipment - Total (Gross) - Quarterly |
| `fnd6_newqeventv110_ppentq` | VECTOR | Property Plant and Equipment - Total (Net) |
| `fnd6_newqeventv110_prcaq` | VECTOR | Core Post-Retirement Adjustment |
| `fnd6_newqeventv110_prcd12` | VECTOR | Core Post Retirement Adjustment Diluted EPS Effect 12 MM |
| `fnd6_newqeventv110_prcdq` | VECTOR | Core Post-Retirement Adjustment Diluted EPS Effect |
| `fnd6_newqeventv110_prce12` | VECTOR | Core Post Retirement Adjustment 12MM |
| `fnd6_newqeventv110_prceps12` | VECTOR | Core Post Retirement Adjustment Basic EPS Effect 12MM |
| `fnd6_newqeventv110_prcepsq` | VECTOR | Core Post-Retirement Adjustment Basic EPS Effect |
| `fnd6_newqeventv110_prcpd12` | VECTOR | Core Post-Retirement Adjustment 12MM Diluted EPS Effect Preliminary |
| `fnd6_newqeventv110_prcpdq` | VECTOR | Core Post Retirement Adjustment Diluted EPS Effect Preliminary |
| `fnd6_newqeventv110_prcpeps12` | VECTOR | Core Post-Retirement Adjustment 12MM Basic EPS Effect Preliminary |
| `fnd6_newqeventv110_prcpepsq` | VECTOR | Core Post-Retirement Adjustment Basic EPS Effect Preliminary |
| `fnd6_newqeventv110_prcpq` | VECTOR | Core Post-Retirement Adjustment Preliminary |
| `fnd6_newqeventv110_prcraq` | VECTOR | Repurchase Price - Average per share |
| `fnd6_newqeventv110_prshoq` | VECTOR | Redeem Pfd Shares Outs (000) |
| `fnd6_newqeventv110_pstknq` | VECTOR | Preferred/Preference Stock - Nonredeemable |
| `fnd6_newqeventv110_pstkq` | VECTOR | Preferred/Preference Stock (Capital) - Total |
| `fnd6_newqeventv110_pstkrq` | VECTOR | Preferred/Preference Stock - Redeemable |
| `fnd6_newqeventv110_rcaq` | VECTOR | Restructuring Cost After-tax |
| `fnd6_newqeventv110_rcdq` | VECTOR | Restructuring Cost Diluted EPS Effect |
| `fnd6_newqeventv110_rcepsq` | VECTOR | Restructuring Cost Basic EPS Effect |
| `fnd6_newqeventv110_rcpq` | VECTOR | Restructuring Cost Pretax |
| `fnd6_newqeventv110_rdipaq` | VECTOR | In Process R&D Expense After-tax |
| `fnd6_newqeventv110_rdipdq` | VECTOR | In-Process R&D Expense Diluted EPS Effect |
| `fnd6_newqeventv110_rdipepsq` | VECTOR | In-Process R&D Expense Basic EPS Effect |
| `fnd6_newqeventv110_rdipq` | VECTOR | In Process R&D |
| `fnd6_newqeventv110_recdq` | VECTOR | Receivables - Estimated Doubtful |
| `fnd6_newqeventv110_rectaq` | VECTOR | Accum Other Comp Inc - Cumulative Translation Adjustments |
| `fnd6_newqeventv110_rectoq` | VECTOR | Receivables - Current Other incl. Tax Refunds |
| `fnd6_newqeventv110_rectrq` | VECTOR | Receivables - Trade |
| `fnd6_newqeventv110_reunaq` | VECTOR | Unadjusted Retained Earnings |
| `fnd6_newqeventv110_revtq` | VECTOR | Revenue - Total |
| `fnd6_newqeventv110_rrpq` | VECTOR | Reversal - Restructuring/Acquisition Pretax |
| `fnd6_newqeventv110_seqoq` | VECTOR | Other Stockholders' Equity Adjustments |
| `fnd6_newqeventv110_seqq` | VECTOR | Stockholders' Equity - Total - Quarterly |
| `fnd6_newqeventv110_seta12` | VECTOR | Settlement (Litigation/Insurance) After Tax - 12mm |
| `fnd6_newqeventv110_setaq` | VECTOR | Settlement (Litigation/Insurance) After-tax |
| `fnd6_newqeventv110_setd12` | VECTOR | Settlement (Litigation/Insurance) Diluted EPS Effect 12MM |
| `fnd6_newqeventv110_seteps12` | VECTOR | Settlement (Litigation/Insurance) Basic EPS Effect 12MM |
| `fnd6_newqeventv110_setpq` | VECTOR | Settlement (Litigation/Insurance) Pretax |
| `fnd6_newqeventv110_spce12` | VECTOR | S&P Core Earnings 12MM |
| `fnd6_newqeventv110_spcedpq` | VECTOR | S&P Core Earnings EPS Diluted - Preliminary |
| `fnd6_newqeventv110_spcedq` | VECTOR | S&P Core Earnings EPS Diluted |
| `fnd6_newqeventv110_spceeps12` | VECTOR | S&P Core Earnings EPS Basic 12MM |
| `fnd6_newqeventv110_spceepsp12` | VECTOR | S&P Core 12MM EPS - Basic - Preliminary |
| `fnd6_newqeventv110_spceepspq` | VECTOR | S&P Core Earnings EPS Basic - Preliminary |
| `fnd6_newqeventv110_spceepsq` | VECTOR | S&P Core Earnings EPS Basic |
| `fnd6_newqeventv110_spcep12` | VECTOR | S&P Core Earnings 12MM - Preliminary |
| `fnd6_newqeventv110_spcepd12` | VECTOR | S&P Core Earnings 12MM EPS Diluted - Preliminary |
| `fnd6_newqeventv110_spcepq` | VECTOR | S&P Core Earnings - Preliminary |
| `fnd6_newqeventv110_spceq` | VECTOR | S&P Core Earnings |
| `fnd6_newqeventv110_spioaq` | VECTOR | Other Special Items After-tax |
| `fnd6_newqeventv110_spiopq` | VECTOR | Other Special Items Pretax |
| `fnd6_newqeventv110_spiq` | VECTOR | Special Items |
| `fnd6_newqeventv110_stkcoq` | VECTOR | Stock Compensation Expense |
| `fnd6_newqeventv110_stkcpaq` | VECTOR | After-tax stock compensation |
| `fnd6_newqeventv110_teqq` | VECTOR | Stockholders' Equity - Total - Quarterly |
| `fnd6_newqeventv110_tfvaq` | VECTOR | Total Fair Value Assets |
| `fnd6_newqeventv110_tfvceq` | VECTOR | Total Fair Value Changes including Earnings |
| `fnd6_newqeventv110_tfvlq` | VECTOR | Total Fair Value Liabilities |
| `fnd6_newqeventv110_tstknq` | VECTOR | Treasury Stock - Number of Common Shares |
| `fnd6_newqeventv110_tstkq` | VECTOR | Treasury Stock - Total (All Capital) |
| `fnd6_newqeventv110_txdbaq` | VECTOR | Deferred Tax Asset - Long Term |
| `fnd6_newqeventv110_txdbq` | VECTOR | Deferred Taxes - Balance Sheet |
| `fnd6_newqeventv110_txdiq` | VECTOR | Income Taxes - Deferred |
| `fnd6_newqeventv110_txditcq` | VECTOR | Deferred Taxes and Investment Tax Credit |
| `fnd6_newqeventv110_txpq` | VECTOR | Income Taxes Payable |
| `fnd6_newqeventv110_txtq` | VECTOR | Income Taxes - Total |
| `fnd6_newqeventv110_txwq` | VECTOR | Excise Taxes |
| `fnd6_newqeventv110_wcapq` | VECTOR | Working Capital (Balance Sheet) |
| `fnd6_newqeventv110_wdaq` | VECTOR | Writedowns After-tax |
| `fnd6_newqeventv110_wdpq` | VECTOR | Writedowns Pretax |
| `fnd6_newqeventv110_xidoq` | VECTOR | Extraordinary Items and Discontinued Operations |
| `fnd6_newqeventv110_xintq` | VECTOR | Interest and Related Expense - Total |
| `fnd6_newqeventv110_xiq` | VECTOR | Extraordinary Items |
| `fnd6_newqeventv110_xoprq` | VECTOR | Operating Expense - Total |
| `fnd6_newqeventv110_xopt12` | VECTOR | Implied Option Expense - 12mm |
| `fnd6_newqeventv110_xoptd12` | VECTOR | Implied Option EPS Diluted 12MM |
| `fnd6_newqeventv110_xoptd12p` | VECTOR | Implied Option 12MM EPS Diluted Preliminary |
| `fnd6_newqeventv110_xoptdq` | VECTOR | Implied Option EPS Diluted |
| `fnd6_newqeventv110_xoptdqp` | VECTOR | Implied Option EPS Diluted Preliminary |
| `fnd6_newqeventv110_xopteps12` | VECTOR | Implied Option EPS Basic 12MM |
| `fnd6_newqeventv110_xoptepsp12` | VECTOR | Implied Option 12MM EPS Basic Preliminary |
| `fnd6_newqeventv110_xoptepsq` | VECTOR | Implied Option EPS Basic |
| `fnd6_newqeventv110_xoptepsqp` | VECTOR | Implied Option EPS Basic Preliminary |
| `fnd6_newqeventv110_xoptq` | VECTOR | Implied Option Expense |
| `fnd6_newqeventv110_xoptqp` | VECTOR | Implied Option Expense Preliminary |
| `fnd6_newqeventv110_xrdq` | VECTOR | Research and Development Expense |
| `fnd6_newqeventv110_xsgaq` | VECTOR | Selling, General and Administrative Expenses |
| `fnd6_newqv1300_acomincq` | MATRIX | Accumulated Other Comprehensive Income (Loss) |
| `fnd6_newqv1300_acoq` | MATRIX | Current Assets - Other - Total |
| `fnd6_newqv1300_altoq` | MATRIX | Other Long-term Assets |
| `fnd6_newqv1300_ancq` | MATRIX | Non-Current Assets - Total |
| `fnd6_newqv1300_anoq` | MATRIX | Assets Netting & Other Adjustments |
| `fnd6_newqv1300_aociderglq` | MATRIX | Accum Other Comp Inc - Derivatives Unrealized Gain/Loss |
| `fnd6_newqv1300_aociotherq` | MATRIX | Accumulated Other Comprehensive Income - Other Adjustments |
| `fnd6_newqv1300_aocipenq` | MATRIX | Accum Other Comp Inc - Min Pension Liab Adj |
| `fnd6_newqv1300_aocisecglq` | MATRIX | Accum Other Comp Inc - Unreal G/L Ret Int in Sec Assets |
| `fnd6_newqv1300_aol2q` | MATRIX | Assets Level 2 (Observable) |
| `fnd6_newqv1300_aoq` | MATRIX | Assets - Other - Total |
| `fnd6_newqv1300_aqpl1q` | MATRIX | Assets Level 1 (Quoted Prices) |
| `fnd6_newqv1300_aul3q` | MATRIX | Assets Level 3 (Unobservable) |
| `fnd6_newqv1300_capsq` | MATRIX | Capital Surplus/Share Premium Reserve |
| `fnd6_newqv1300_chq` | MATRIX | Cash |
| `fnd6_newqv1300_cibegniq` | MATRIX | Comp Inc - Beginning Net Income |
| `fnd6_newqv1300_cicurrq` | MATRIX | Comp Inc - Currency Trans Adj |
| `fnd6_newqv1300_ciderglq` | MATRIX | Comp Inc - Derivative Gains/Losses |
| `fnd6_newqv1300_cimiiq` | MATRIX | Comprehensive Income - Noncontrolling Interest |
| `fnd6_newqv1300_ciotherq` | MATRIX | Comp Inc - Other Adj |
| `fnd6_newqv1300_cipenq` | MATRIX | Comp Inc - Minimum Pension Adj |
| `fnd6_newqv1300_ciq` | MATRIX | Comprehensive Income - Total |
| `fnd6_newqv1300_cisecglq` | MATRIX | Comp Inc - Securities Gains/Losses |
| `fnd6_newqv1300_citotalq` | MATRIX | Comprehensive Income - Parent |
| `fnd6_newqv1300_cogsq` | MATRIX | Cost of Goods Sold |
| `fnd6_newqv1300_csh12q` | MATRIX | Common Shares Used to Calculate Earnings Per Share - 12 Months Moving |
| `fnd6_newqv1300_cshfdq` | MATRIX | Common Shares for Diluted EPS |
| `fnd6_newqv1300_cshiq` | MATRIX | Common Shares Issued |
| `fnd6_newqv1300_cshopq` | MATRIX | Total Shares Repurchased - Quarter |
| `fnd6_newqv1300_cshoq` | MATRIX | Common Shares Outstanding |
| `fnd6_newqv1300_cshprq` | MATRIX | Common Shares Used to Calculate Earnings Per Share - Basic |
| `fnd6_newqv1300_cstkq` | MATRIX | Common/Ordinary Stock (Capital) |
| `fnd6_newqv1300_dcomq` | MATRIX | Deferred Compensation |
| `fnd6_newqv1300_dilavq` | MATRIX | Dilution Available - Excluding Extraordinary Items |
| `fnd6_newqv1300_dlcq` | MATRIX | Debt in Current Liabilities |
| `fnd6_newqv1300_dpactq` | MATRIX | Depreciation, Depletion and Amortization (Accumulated) |
| `fnd6_newqv1300_drcq` | MATRIX | Deferred Revenue - Current |
| `fnd6_newqv1300_drltq` | MATRIX | Deferred Revenue - Long-term |
| `fnd6_newqv1300_epsfiq` | MATRIX | Earnings Per Share (Diluted) - Including Extraordinary Items |
| `fnd6_newqv1300_epspiq` | MATRIX | Earnings Per Share (Basic) - Including Extraordinary Items |
| `fnd6_newqv1300_epspxq` | MATRIX | Earnings Per Share (Basic) - Excluding Extraordinary Items |
| `fnd6_newqv1300_esopnrq` | MATRIX | Preferred ESOP Obligation - Non-Redeemable |
| `fnd6_newqv1300_esoprq` | MATRIX | Preferred ESOP Obligation - Redeemable |
| `fnd6_newqv1300_fcaq` | MATRIX | Foreign Exchange Income (Loss) |
| `fnd6_newqv1300_gdwlq` | MATRIX | Goodwill (net) |
| `fnd6_newqv1300_glcea12` | MATRIX | Gain/Loss on Sale (Core Earnings Adjusted) After-tax 12MM |
| `fnd6_newqv1300_glced12` | MATRIX | Gain/Loss on Sale (Core Earnings Adjusted) Diluted EPS Effect 12MM |
| `fnd6_newqv1300_glceeps12` | MATRIX | Gain/Loss on Sale (Core Earnings Adjusted) Basic EPS Effect 12MM |
| `fnd6_newqv1300_ibadj12` | MATRIX | Income Before Extra Items - Adj for Common Stock Equivalents - 12MM |
| `fnd6_newqv1300_ibadjq` | MATRIX | Income Before Extraordinary Items - Adjusted for Common Stock Equivalents |
| `fnd6_newqv1300_ibcomq` | MATRIX | Income Before Extraordinary Items - Available for Common |
| `fnd6_newqv1300_ibmiiq` | MATRIX | Income before Extraordinary Items and Noncontrolling Interests |
| `fnd6_newqv1300_ibq` | MATRIX | Income Before Extraordinary Items |
| `fnd6_newqv1300_icaptq` | MATRIX | Invested Capital - Total - Quarterly |
| `fnd6_newqv1300_intanoq` | MATRIX | Other Intangibles |
| `fnd6_newqv1300_intanq` | MATRIX | Intangible Assets - Total |
| `fnd6_newqv1300_invfgq` | MATRIX | Inventory - Finished Goods |
| `fnd6_newqv1300_invoq` | MATRIX | Inventory - Other |
| `fnd6_newqv1300_invrmq` | MATRIX | Inventory - Raw Materials |
| `fnd6_newqv1300_invtq` | MATRIX | Inventories - Total |
| `fnd6_newqv1300_invwipq` | MATRIX | Inventory - Work in Process |
| `fnd6_newqv1300_ivltq` | MATRIX | Total Long-term Investments |
| `fnd6_newqv1300_ivstq` | MATRIX | Short-Term Investments - Total |
| `fnd6_newqv1300_lcoq` | MATRIX | Current Liabilities - Other - Total |
| `fnd6_newqv1300_lltq` | MATRIX | Long-Term Liabilities (Total) |
| `fnd6_newqv1300_lnoq` | MATRIX | Liabilities Netting & Other Adjustments |
| `fnd6_newqv1300_lol2q` | MATRIX | Liabilities Level 2 (Observable) |
| `fnd6_newqv1300_loq` | MATRIX | Liabilities - Other |
| `fnd6_newqv1300_loxdrq` | MATRIX | Liabilities - Other - Excluding Deferred Revenue |
| `fnd6_newqv1300_lqpl1q` | MATRIX | Liabilities Level 1 (Quoted Prices) |
| `fnd6_newqv1300_lseq` | MATRIX | Liabilities and Stockholders' Equity - Total |
| `fnd6_newqv1300_ltmibq` | MATRIX | Liabilities - Total and Noncontrolling Interest |
| `fnd6_newqv1300_lul3q` | MATRIX | Liabilities Level 3 (Unobservable) |
| `fnd6_newqv1300_mibnq` | MATRIX | Non-Redeemable Noncontrolling Interest (Balance Sheet) - Quarterly |
| `fnd6_newqv1300_mibtq` | MATRIX | Noncontrolling Interests - Total - Balance Sheet - Quarterly |
| `fnd6_newqv1300_miiq` | MATRIX | Noncontrolling Interest - Income Account |
| `fnd6_newqv1300_msaq` | MATRIX | Accumulated Other Comprehensive Income - Marketable Security Adjustments |
| `fnd6_newqv1300_oepf12` | MATRIX | Earnings Per Share - Diluted - from Operations - 12MM |
| `fnd6_newqv1300_oepsxq` | MATRIX | Earnings Per Share - Diluted - from Operations |
| `fnd6_newqv1300_optfvgrq` | MATRIX | Options - Fair Value of Options Granted |
| `fnd6_newqv1300_optrfrq` | MATRIX | Risk-Free Rate - Assumption (%) |
| `fnd6_newqv1300_piq` | MATRIX | Pretax Income |
| `fnd6_newqv1300_pncq` | MATRIX | Core Pension Adjustment |
| `fnd6_newqv1300_ppegtq` | MATRIX | Property, Plant and Equipment - Total (Gross) - Quarterly |
| `fnd6_newqv1300_ppentq` | MATRIX | Property Plant and Equipment - Total (Net) |
| `fnd6_newqv1300_prcaq` | MATRIX | Core Post Retirement Adjustment |
| `fnd6_newqv1300_prcdq` | MATRIX | Core Post Retirement Adjustment Diluted EPS Effect |
| `fnd6_newqv1300_prcepsq` | MATRIX | Core Post Retirement Adjustment Basic EPS Effect |
| `fnd6_newqv1300_prcraq` | MATRIX | Repurchase Price - Average per share |
| `fnd6_newqv1300_rcpq` | MATRIX | Restructuring Cost Pretax |
| `fnd6_newqv1300_rdipaq` | MATRIX | In Process R&D Expense After-tax |
| `fnd6_newqv1300_rdipdq` | MATRIX | In Process R&D Expense Diluted EPS Effect |
| `fnd6_newqv1300_rdipepsq` | MATRIX | In-Process R&D Expense Basic EPS Effect |
| `fnd6_newqv1300_rdipq` | MATRIX | In Process R&D |
| `fnd6_newqv1300_recdq` | MATRIX | Receivables - Estimated Doubtful |
| `fnd6_newqv1300_rectaq` | MATRIX | Accum Other Comp Inc - Cumulative Translation Adjustments |
| `fnd6_newqv1300_rectoq` | MATRIX | Receivables - Current Other incl Tax Refunds |
| `fnd6_newqv1300_rectrq` | MATRIX | Receivables - Trade |
| `fnd6_newqv1300_reunaq` | MATRIX | Unadjusted Retained Earnings |
| `fnd6_newqv1300_revtq` | MATRIX | Revenue - Total |
| `fnd6_newqv1300_seqoq` | MATRIX | Other Stockholders' Equity Adjustments |
| `fnd6_newqv1300_seqq` | MATRIX | Stockholders' Equity - Total - Quarterly |
| `fnd6_newqv1300_spcedpq` | MATRIX | S&P Core Earnings EPS Diluted - Preliminary |
| `fnd6_newqv1300_spcedq` | MATRIX | S&P Core Earnings EPS Diluted |
| `fnd6_newqv1300_spceepsp12` | MATRIX | S&P Core 12MM EPS - Basic - Preliminary |
| `fnd6_newqv1300_spceepspq` | MATRIX | S&P Core Earnings EPS Basic - Preliminary |
| `fnd6_newqv1300_spceepsq` | MATRIX | S&P Core Earnings EPS Basic |
| `fnd6_newqv1300_spcep12` | MATRIX | S&P Core Earnings 12MM - Preliminary |
| `fnd6_newqv1300_spcepd12` | MATRIX | S&P Core Earnings 12MM EPS Diluted - Preliminary |
| `fnd6_newqv1300_spcepq` | MATRIX | S&P Core Earnings - Preliminary |
| `fnd6_newqv1300_spceq` | MATRIX | S&P Core Earnings |
| `fnd6_newqv1300_spiq` | MATRIX | Special Items |
| `fnd6_newqv1300_stkcoq` | MATRIX | Stock Compensation Expense |
| `fnd6_newqv1300_stkcpaq` | MATRIX | After-tax stock compensation |
| `fnd6_newqv1300_teqq` | MATRIX | Stockholders' Equity - Total - Quarterly |
| `fnd6_newqv1300_tfvaq` | MATRIX | Total Fair Value Assets |
| `fnd6_newqv1300_tfvceq` | MATRIX | Total Fair Value Changes including Earnings |
| `fnd6_newqv1300_tfvlq` | MATRIX | Total Fair Value Liabilities |
| `fnd6_newqv1300_tstknq` | MATRIX | Treasury Stock - Number of Common Shares |
| `fnd6_newqv1300_tstkq` | MATRIX | Treasury Stock - Total (All Capital) |
| `fnd6_newqv1300_txdbaq` | MATRIX | Deferred Tax Asset - Long Term |
| `fnd6_newqv1300_txdbq` | MATRIX | Deferred Taxes - Balance Sheet |
| `fnd6_newqv1300_txdiq` | MATRIX | Income Taxes - Deferred |
| `fnd6_newqv1300_txditcq` | MATRIX | Deferred Taxes and Investment Tax Credit |
| `fnd6_newqv1300_txpq` | MATRIX | Income Taxes Payable |
| `fnd6_newqv1300_txtq` | MATRIX | Income Taxes - Total |
| `fnd6_newqv1300_txwq` | MATRIX | Excise Taxes |
| `fnd6_newqv1300_wcapq` | MATRIX | Working Capital (Balance Sheet) |
| `fnd6_newqv1300_xintq` | MATRIX | Interest and Related Expense - Total |
| `fnd6_newqv1300_xoprq` | MATRIX | Operating Expense - Total |
| `fnd6_newqv1300_xoptdq` | MATRIX | Implied Option EPS Diluted |
| `fnd6_newqv1300_xoptepsq` | MATRIX | Implied Option EPS Basic |
| `fnd6_newqv1300_xoptq` | MATRIX | Implied Option Expense |
| `fnd6_newqv1300_xrdq` | MATRIX | Research and Development Expense |
| `fnd6_newqv1300_xsgaq` | MATRIX | Selling, General and Administrative Expenses |
| `fnd6_niadj` | MATRIX | Net Income Adjusted for Common/Ordinary Stock (Capital) Equivalents |
| `fnd6_nis` | VECTOR | Net Income (Loss) |
| `fnd6_nopio` | MATRIX | Nonoperating Income (Expense) - Other |
| `fnd6_nopxs` | VECTOR | Nonoperating Income (Expense) - excluding Interest |
| `fnd6_np` | MATRIX | Notes Payable - Short-Term Borrowings |
| `fnd6_npq` | MATRIX | Notes Payable |
| `fnd6_nxints` | VECTOR | Net Interest Income (Expense) |
| `fnd6_obs` | VECTOR | Order Backlog |
| `fnd6_ocaxs` | VECTOR | Other Costs and Expenses |
| `fnd6_oelim` | VECTOR | Other Eliminations (Income) |
| `fnd6_oiadps` | VECTOR | Operating Income after Depreciation |
| `fnd6_oibdps` | VECTOR | Operating Income before Depreciation |
| `fnd6_oprepsx` | MATRIX | Earnings Per Share - Diluted - from Operations |
| `fnd6_ops` | VECTOR | Operating Profit (Loss) |
| `fnd6_optca` | MATRIX | Options - Cancelled (-) |
| `fnd6_optdr` | MATRIX | Dividend Rate - Assumption (%) |
| `fnd6_optdrq` | MATRIX | Dividend Rate - Assumption (%) |
| `fnd6_optex` | MATRIX | Options Exercisable (000) |
| `fnd6_optfvgr` | MATRIX | Options - Fair Value of Options Granted |
| `fnd6_optgr` | MATRIX | Options - Granted |
| `fnd6_optlife` | MATRIX | Life of Options - Assumption (# yrs) |
| `fnd6_optlifeq` | MATRIX | Life of Options - Assumption (# yrs) |
| `fnd6_optosby` | MATRIX | Options Outstanding - Beginning of Year |
| `fnd6_optosey` | MATRIX | Options Outstanding - End of Year |
| `fnd6_optprcby` | MATRIX | Options Outstanding Beginning of Year - Price |
| `fnd6_optprcca` | MATRIX | Options Cancelled - Price |
| `fnd6_optprcex` | MATRIX | Options Exercised - Price |
| `fnd6_optprcey` | MATRIX | Options Outstanding End of Year - Price |
| `fnd6_optprcgr` | MATRIX | Options Granted - Price |
| `fnd6_optprcwa` | MATRIX | Options Exercisable - Weighted Avg Price |
| `fnd6_optrfr` | MATRIX | Risk-Free Rate - Assumption (%) |
| `fnd6_optvol` | MATRIX | Volatility - Assumption (%) |
| `fnd6_optvolq` | MATRIX | Volatility - Assumption (%) |
| `fnd6_pidom` | MATRIX | Pretax Income - Domestic |
| `fnd6_pifo` | MATRIX | Pretax Income - Foreign |
| `fnd6_pncdq` | MATRIX | Core Pension Adjustment Diluted EPS Effect |
| `fnd6_pncepsq` | MATRIX | Core Pension Adjustment Basic EPS Effect |
| `fnd6_pnrsho` | MATRIX | Nonred Pfd Shares Outs (000) |
| `fnd6_ppents` | VECTOR | Property, Plant & Equipment |
| `fnd6_ppeveb` | MATRIX | Property, Plant, and Equipment - Ending Balance (Schedule V) |
| `fnd6_prcc` | MATRIX | Price Close - Annual |
| `fnd6_prccq` | MATRIX | Price Close - Quarter |
| `fnd6_prch` | MATRIX | Price High - Annual |
| `fnd6_prchq` | MATRIX | Price High - Quarter |
| `fnd6_prcl` | MATRIX | Price Low - Annual |
| `fnd6_prclq` | MATRIX | Price Low - Quarter |
| `fnd6_prstkc` | MATRIX | Purchase of Common and Preferred Stock |
| `fnd6_pstkc` | MATRIX | Preferred Stock - Convertible |
| `fnd6_pstkl` | MATRIX | Preferred Stock - Liquidating Value |
| `fnd6_pstkrv` | MATRIX | Preferred Stock - Redemption Value |
| `fnd6_ptis` | VECTOR | Pretax Income |
| `fnd6_rank` | MATRIX | SP rank with the following meaning: // 0----invalid rank //1----A+//2----A//3----A-//4----B+//5----B//6----B-//7----C… |
| `fnd6_ranks` | VECTOR | Ranking |
| `fnd6_rds` | VECTOR | Research and Development |
| `fnd6_rea` | MATRIX | Retained Earnings - Restatement |
| `fnd6_reajo` | MATRIX | Retained Earnings - Other Adjustments |
| `fnd6_recco` | MATRIX | Receivables - Current - Other |
| `fnd6_recd` | MATRIX | Receivables - Estimated Doubtful |
| `fnd6_recta` | MATRIX | Retained Earnings - Cumulative Translation Adjustment |
| `fnd6_rectr` | MATRIX | Receivables - Trade |
| `fnd6_revts` | VECTOR | Total Revenues |
| `fnd6_sales` | VECTOR | Net Sales |
| `fnd6_salexg` | VECTOR | Export Sales |
| `fnd6_sics` | VECTOR | SIC Code |
| `fnd6_siv` | MATRIX | Sale of Investments |
| `fnd6_snms` | VECTOR | Segment Name |
| `fnd6_spce` | MATRIX | S&P Core Earnings |
| `fnd6_spis` | VECTOR | Special Items |
| `fnd6_sppe` | MATRIX | Sale of Property |
| `fnd6_sppiv` | MATRIX | Sale of Property, Plant and Equipment and Investments - Gain (Loss) |
| `fnd6_sstk` | MATRIX | Sale of Common and Preferred Stock |
| `fnd6_state` | MATRIX | integer for identifying the state of the company |
| `fnd6_stkcpa` | MATRIX | After-tax stock compensation |
| `fnd6_stype` | VECTOR | Segment Type |
| `fnd6_teq` | MATRIX | Stockholders' Equity - Total |
| `fnd6_tfva` | MATRIX | Total Fair Value Assets |
| `fnd6_tfvce` | MATRIX | Total Fair Value Changes including Earnings |
| `fnd6_tfvl` | MATRIX | Total Fair Value Liabilities |
| `fnd6_tlcf` | MATRIX | Tax Loss Carry Forward |
| `fnd6_tstkc` | MATRIX | Treasury Stock - Common |
| `fnd6_txbco` | MATRIX | Excess Tax Benefit Stock Options - Cash Flow Operating |
| `fnd6_txbcof` | MATRIX | Excess Tax Benefit of Stock Options - Cash Flow Financing |
| `fnd6_txc` | MATRIX | Income Taxes - Current |
| `fnd6_txdba` | MATRIX | Deferred Tax Asset - Long Term |
| `fnd6_txdbca` | MATRIX | Deferred Tax Asset - Current |
| `fnd6_txdbcl` | MATRIX | Deferred Tax Liability - Current |
| `fnd6_txdbclq` | MATRIX | Current Deferred Tax Liability |
| `fnd6_txdc` | MATRIX | Deferred Taxes (Cash Flow) |
| `fnd6_txdfed` | MATRIX | Deferred Taxes - Federal |
| `fnd6_txdfo` | MATRIX | Deferred Taxes - Foreign |
| `fnd6_txdi` | MATRIX | Income Taxes - Deferred |
| `fnd6_txds` | MATRIX | Deferred Taxes - State |
| `fnd6_txfed` | MATRIX | Income Taxes - Federal |
| `fnd6_txfo` | MATRIX | Income Taxes - Foreign |
| `fnd6_txndb` | MATRIX | Net Deferred Tax Asset (Liab) - Total |
| `fnd6_txndba` | MATRIX | Net Deferred Tax Asset |
| `fnd6_txndbl` | MATRIX | Net Deferred Tax Liability |
| `fnd6_txndbr` | MATRIX | Deferred Tax Residual |
| `fnd6_txo` | MATRIX | Income Taxes - Other |
| `fnd6_txpd` | MATRIX | Income Taxes Paid |
| `fnd6_txr` | MATRIX | Income Tax Refund |
| `fnd6_txs` | MATRIX | Income Taxes - State |
| `fnd6_txts` | VECTOR | Income Taxes |
| `fnd6_txtubadjust` | MATRIX | Other Unrecognized Tax Benefit Adjustment |
| `fnd6_txtubbegin` | MATRIX | Unrecog. Tax Benefits - Beg of Year |
| `fnd6_txtubend` | MATRIX | Unrecog. Tax Benefits - End of Year |
| `fnd6_txtubposdec` | MATRIX | Decrease - Current Tax Positions |
| `fnd6_txtubposinc` | MATRIX | Increase - Current Tax Positions |
| `fnd6_txtubpospdec` | MATRIX | Decrease - Prior Tax Positions |
| `fnd6_txtubpospinc` | MATRIX | Increase - Prior Tax Positions |
| `fnd6_txtubsettle` | MATRIX | Settlements with Tax Authorities |
| `fnd6_txtubsoflimit` | MATRIX | Lapse of Statute of Limitations |
| `fnd6_txtubtxtr` | MATRIX | Impact on Effective Tax Rate |
| `fnd6_txtubxintbs` | MATRIX | Interest & Penalties Accrued - B/S |
| `fnd6_txtubxintis` | MATRIX | Interest & Penalties Recognized - I/S |
| `fnd6_txw` | MATRIX | Excise Taxes |
| `fnd6_txws` | VECTOR | Excise Taxes |
| `fnd6_weburl` | MATRIX | WEB URL code for the company |
| `fnd6_xacc` | MATRIX | Accrued Expenses |
| `fnd6_xaccq` | MATRIX | Accrued Expenses |
| `fnd6_xad` | MATRIX | Advertising Expense |
| `fnd6_xidos` | VECTOR | Extraordinary Items and Discontinued Operations |
| `fnd6_xintopt` | MATRIX | Implied Option Expense |
| `fnd6_xints` | VECTOR | Interest Expense |
| `fnd6_xopr` | MATRIX | Operating Expenses - Total |
| `fnd6_xpp` | MATRIX | Prepaid Expenses |
| `fnd6_xpr` | MATRIX | Pension and Retirement Expense |
| `fnd6_xrent` | MATRIX | Rental Expense |
| `fnd6_xsgas` | VECTOR | Selling, General & Administrative |
| `fnd6_zipcode` | MATRIX | ZIP code related to the company |
| `goodwill` | MATRIX | Goodwill (net) |
| `income` | MATRIX | Net Income |
| `income_beforeextra` | MATRIX | Income Before Extraordinary Items |
| `income_tax` | MATRIX | Income Taxes - Total |
| `interest_expense` | MATRIX | Interest and Related Expense - Total |
| `inventory` | MATRIX | Inventories - Total |
| `inventory_turnover` | MATRIX | Inventory Turnover |
| `invested_capital` | MATRIX | Invested Capital - Total - Quarterly |
| `liabilities` | MATRIX | Liabilities - Total |
| `liabilities_curr` | MATRIX | Current Liabilities - Total |
| `operating_expense` | MATRIX | Operating Expense - Total |
| `operating_income` | MATRIX | Operating Income After Depreciation - Quarterly |
| `ppent` | MATRIX | Property Plant and Equipment - Total (Net) |
| `pretax_income` | MATRIX | Pretax Income |
| `rd_expense` | MATRIX | Research And Development (Quarterly) |
| `receivable` | MATRIX | Receivables - Total |
| `retained_earnings` | MATRIX | Retained Earnings |
| `return_assets` | MATRIX | Return on Assets |
| `return_equity` | MATRIX | Return on Equity |
| `revenue` | MATRIX | Revenue - Total |
| `sales` | MATRIX | Sales/Turnover (Net) |
| `sales_growth` | MATRIX | Growth in Sales (Quarterly) |
| `sales_ps` | MATRIX | Sales per Share (Quarterly) |
| `sga_expense` | MATRIX | Selling, General and Administrative Expenses |
| `working_capital` | MATRIX | Working Capital (Balance Sheet) |

## 用法提示（人工补充）

- TODO：典型组合方式、相关的 concept 页面
