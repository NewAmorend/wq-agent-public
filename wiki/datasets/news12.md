---
title: news12 数据集
type: entity
tags:
- dataset
- news
- usa
sources:
- worldquantbrain-api
created: '2026-05-24'
dataset_id: news12
category: news
delay: 1
region: USA
universe: TOP3000
---

<!-- managed by wq-agent wiki import-wq; manual edits below -->

# US News Data

**ID**：`news12`　**Category**：news　**Region**：USA　**Universe**：TOP3000　**Delay**：1

## 描述

This dataset integrates real-time news events and market data to capture the immediate and subsequent price reactions of stocks to a wide range of news and corporate announcements. It includes detailed fields such as news headlines, timestamps, price and volume changes across different trading sessions, analyst actions, earnings surprises, and sector-specific news tags. By quantifying the impact of news on price movements at granular intervals (from seconds to hours), the dataset enables users to identify patterns of underreaction, overreaction, and momentum following news releases. This information is highly valuable for developing event-driven trading strategies, backtesting news-based signals, and enhancing alpha generation by systematically exploiting the relationship between news flow and market behavior.

**字段数**：875

**已用 alpha 数**：128951

## 字段清单（875 项）

| id | type | description |
| --- | --- | --- |
| `actual_earnings_per_share_2` | VECTOR | Actual earnings per share value reported in the news |
| `actual_earnings_per_share_3` | VECTOR | Actual Earnings Per Share value conveyed by the news release |
| `actual_earnings_per_share_4` | VECTOR | Actual Earnings Per Share reported for day 1 in 'All Filter' module |
| `actual_earnings_per_share_value` | VECTOR | Actual Earnings Per Share reported in the news release |
| `actual_earnings_per_share_value_2_1555` | VECTOR | Actual Earnings Per Share value reported in the news |
| `actual_earnings_per_share_value_afterhours` | VECTOR | The actual Earnings Per Share (EPS) value reported and mentioned in the news release |
| `actual_eps_value` | VECTOR | Actual reported Earnings Per Share on Day 1 |
| `actual_eps_value_2` | VECTOR | The actual Earnings Per Share value released in the news event |
| `advantageous_position_flag` | VECTOR | Indicator of whether a long or short position would have been more favorable. |
| `advantageous_position_flag_pre_filter` | VECTOR | Indicator for whether a long (1), neutral (0), or short (-1) position would have been more advantageous, based on mov… |
| `after_hours_vwap_2` | VECTOR | Volume-Weighted Average Price after trade or post-market session on Day 1 |
| `after_hours_vwap_value` | VECTOR | Post session volume weighted average price |
| `after_session_vwap` | VECTOR | Volume weighted average price in the post-session |
| `afterhours_volume_weighted_avg_price` | VECTOR | Post-market Volume Weighted Average Price for the session |
| `aggregate_session_vwap_2` | VECTOR | Volume weighted average price for all sessions combined throughout the day |
| `aggregate_sessions_vwap` | VECTOR | Volume Weighted Average Price across all periods in the session |
| `all_sessions_volume_weighted_avg_price` | VECTOR | Volume Weighted Average Price for all trades during the session |
| `all_sessions_vwap` | VECTOR | Volume Weighted Average Price calculated over all trades within the event window or current day (D1) for the "All" se… |
| `annual_dividend_percent` | VECTOR | Dividend yield percentage for the stock |
| `annual_dividend_percent_2_1555` | VECTOR | Dividend yield percentage (annual dividend divided by stock price) |
| `annual_dividend_percent_of_share_price` | VECTOR | Dividend yield percentage for Day 1 in the filter module |
| `annual_dividend_yield` | VECTOR | Dividend yield (annual dividend / stock price) for the security on Day 1 |
| `annual_dividend_yield_pct` | VECTOR | Dividend yield percentage for the stock in After Hours Day 1 |
| `annual_dividend_yield_pct_2` | VECTOR | Dividend yield ratio (annual dividend divided by stock price, in percentage) |
| `annual_dividend_yield_percent` | VECTOR | Dividend yield percentage for the security on the session day |
| `annual_dividend_yield_percent_2` | VECTOR | Dividend yield percentage for the stock on the event day during pre-market session |
| `annual_dividend_yield_percent_3` | VECTOR | Dividend yield percentage for the stock during the session |
| `average_true_range_14_1555` | VECTOR | Fourteen-day Average True Range, a volatility measure |
| `average_true_range_14d` | VECTOR | 14-period Average True Range (ATR) for the security on the event day, representing recent volatility, in the "All" se… |
| `average_true_range_14day` | VECTOR | Fourteen day Average True Range |
| `average_true_range_14day_3` | VECTOR | Fourteen day Average True Range |
| `average_true_range_14day_filter` | VECTOR | The average true range of the stock over the past fourteen days, measuring volatility |
| `average_true_range_fourteen_periods` | VECTOR | Average True Range over the past 14 days for the security |
| `best_position_indicator` | VECTOR | Long/Short indicator or signal for day 1 in 'All Filter' module |
| `closing_session_volume_count` | VECTOR | Trading volume at main session close |
| `closing_volume` | VECTOR | Trading volume at the close of the main session |
| `current_day_traded_volume` | VECTOR | Current day's session trading volume |
| `current_day_trading_volume` | VECTOR | Total trading volume during the current after-hours session on Day 1 |
| `current_day_trading_volume_2` | VECTOR | Current trading volume in filter module on Day 1 |
| `current_day_volume` | VECTOR | Current trade volume for the security at the time of record/event within event day (D1), "All" session |
| `current_day_volume_2_1555` | VECTOR | Current session trading volume |
| `current_to_average_volume_ratio` | VECTOR | Current session's volume divided by movement volume (Curr_Vol / Mov_Vol) |
| `current_to_average_volume_ratio_2` | VECTOR | Trading volume ratio (vs. prior period) for day 1 in 'All Filter' |
| `current_to_moving_avg_vol_ratio` | VECTOR | Ratio of current session volume to 30-day moving average session volume (Curr_Vol / Mov_Vol) |
| `current_to_moving_avg_volume_ratio` | VECTOR | Current volume divided by movement volume, indicating volume compared to normal movement |
| `current_to_moving_volume_ratio` | VECTOR | Current volume divided by moving average volume (Curr_Vol / Mov_Vol) |
| `current_to_moving_volume_ratio_2_1555` | VECTOR | Ratio of current volume to moving volume; measures relative trading activity |
| `current_trading_volume_2` | VECTOR | Current day's session total trading volume |
| `current_trading_volume_count` | VECTOR | Total trading volume for the current day's session |
| `current_trading_volume_pre` | VECTOR | Current day's session trading volume |
| `end_of_day_closing_price` | VECTOR | End of Day closing price for day 1 in 'All Filter' |
| `end_of_day_high_price` | VECTOR | Highest price reached from time of news to session end |
| `end_of_day_high_price_2` | VECTOR | End-of-day highest trading price for filter module on Day 1 |
| `end_of_day_low_price` | VECTOR | Lowest price from time of news to end of the session |
| `end_of_day_vwap_2` | VECTOR | End of Day Volume-Weighted Average Price for all events on Day 1 |
| `end_of_day_vwap_3` | VECTOR | End of Day Volume Weighted Average Price for day 1 in 'All Filter' module |
| `end_of_session_close_price` | VECTOR | End of Day closing price for the security on Day 1 |
| `end_of_session_high_price` | VECTOR | End of Day high price for the security on Day 1 |
| `end_of_session_low_price` | VECTOR | End of Day low price for the security on Day 1 |
| `end_of_session_trading_volume` | VECTOR | Trading volume at market close in the session |
| `fifth_minimum_gain_loss_time` | VECTOR | The minimum elapsed time among upward or downward moves (L or S) for the 5 minute bucket after the event in the pre-m… |
| `first_minimum_gain_loss_time` | VECTOR | The minimum elapsed time among upward or downward moves (L or S) for the 1 minute bucket after the event in the pre-m… |
| `first_result_value_pre` | VECTOR | First result or outcome value for the pre-market session. |
| `five_minute_price_change_pct` | VECTOR | Analytics or data aggregated into 5-minute intervals during the session |
| `five_minute_price_change_pct_2` | VECTOR | Percent change in price during the first five minutes after event. |
| `five_minute_price_change_pct_3` | VECTOR | Percent price change in the first five minutes after the event. |
| `five_minute_price_change_pct_all` | VECTOR | Percent price change in the first five minutes after the event (all sessions). |
| `five_minute_price_change_pct_pre` | VECTOR | Return, price, or analytic data for the 5 minutes after the news event |
| `five_minute_price_change_percent` | VECTOR | Return or price metric over 5-minute interval after the news event |
| `fourteen_period_atr_all` | VECTOR | 14-period Average True Range (volatility measure) for day 1 in 'All Filter' module |
| `fourteen_period_avg_true_range` | VECTOR | Fourteen day Average True Range |
| `high_price_deviation_std_1555` | VECTOR | (EODHigh - TONLast) divided by the standard deviation of close price over the past 30 days |
| `high_price_excursion_stddev` | VECTOR | High price deviation from mean, measured in standard deviations. |
| `high_price_excursion_stddev_pre` | VECTOR | (EODHigh minus TONLast) divided by the standard deviation of closing price over the previous 30 calendar days for the… |
| `high_price_standard_deviation_excess` | VECTOR | (EODHigh - TONLast) divided by standard deviation of close price over last 30 calendar days |
| `high_price_standard_deviation_excess_afterhours` | VECTOR | (EODHigh - TONLast)/StdDev, quantifies how far the end-of-day high price exceeded the time-of-news last price, normal… |
| `highest_price_pre_news` | VECTOR | Highest price or value reached during the "TON" (Time of News) window on the event day, "All" session |
| `highest_price_pre_news_2` | VECTOR | Highest price reached during the session before the time of news |
| `highest_price_pre_news_2_1555` | VECTOR | Highest price achieved during the session before the time of news |
| `hundredtwenty_minute_price_change_pct` | VECTOR | Percent change in price during the first 120 minutes after event. |
| `hundredtwenty_minute_price_change_pct_pre` | VECTOR | Return, price, or analytic data for the 120 minutes after the news event |
| `long_short_advantage_flag` | VECTOR | Indicator if long or short position would have been more profitable: 1 for long, -1 for short, 0 for equal |
| `long_short_advantage_flag_2` | VECTOR | Indicator of whether a long or short position would have been more advantageous based on end-of-day price movements |
| `long_short_advantage_flag_2_1555` | VECTOR | Indicator if long (1), neutral (0), or short (-1) position would have been more advantageous based on end-of-day high… |
| `long_short_advantage_flag_filter` | VECTOR | Long/Short indicator showing if a long (1), short (-1), or neutral (0) position would have been most advantageous bas… |
| `low_price_deviation_std_1555` | VECTOR | (TONLast - EODLow) divided by standard deviation of close price over past 30 days |
| `low_price_excess_standard_deviation` | VECTOR | (TONLast minus EODLow) divided by the standard deviation of closing price over the previous 30 calendar days for the … |
| `low_price_excursion_stddev` | VECTOR | Standard deviation of low excursion (downward price moves) during or after the event |
| `low_price_standard_deviation_excess` | VECTOR | (TONLast - EODLow) divided by standard deviation of close price over last 30 calendar days |
| `low_price_standard_deviation_excess_afterhours` | VECTOR | (TONLast - EODLow)/StdDev, quantifies how far the time-of-news last price exceeded the end-of-day low price, normaliz… |
| `lowest_price_before_event` | VECTOR | Lowest price before the time of the event. |
| `lowest_price_pre_news` | VECTOR | Lowest price in the Time-Of-News window for the stock on Day 1 |
| `lowest_price_pre_news_3` | VECTOR | Lowest price reached during the session before the time of news |
| `lowest_price_pre_news_3_1555` | VECTOR | Lowest price reached during session before the time of news event |
| `lowest_price_pre_news_filter` | VECTOR | Lowest price reached during the session before time of news |
| `lowest_price_to_session_end` | VECTOR | End of Day Low Price for day 1 in 'All Filter' module |
| `main_actual_earnings_per_share_value` | VECTOR | The actual Earnings Per Share value that was conveyed by the news release |
| `main_current_trading_volume` | VECTOR | Total trading volume during the current day/session |
| `main_end_of_day_close_price` | VECTOR | Session closing price (end of day close) |
| `main_end_of_day_high_price` | VECTOR | Highest price reached between the time of news and end of the session |
| `main_end_of_day_vwap` | VECTOR | Volume weighted average price from event time to session end |
| `main_high_price_pre_news` | VECTOR | Highest price reached during the session before the time of news |
| `main_market_equity_value` | VECTOR | Market capitalization for the company at that session |
| `main_min_minutes_to_four_pct_move` | VECTOR | The minimum of L or S above for each minute bucket |
| `main_min_minutes_to_one_pct_move` | VECTOR | The minimum of L or S above for each minute bucket |
| `main_min_minutes_to_three_pct_move` | VECTOR | The minimum of L or S above for each minute bucket |
| `main_min_minutes_to_two_pct_move` | VECTOR | Minimum of L or S for each minute bucket (lowest threshold crossed in terms of price move per minute) |
| `main_minutes_to_five_pct_up_move` | VECTOR | Number of minutes until price increases by 5 percent after the news event |
| `main_minutes_to_four_pct_down_move` | VECTOR | Number of minutes elapsed before price decreased by 4% |
| `main_minutes_to_four_pct_up_move` | VECTOR | Number of minutes that elapsed before price went up 4 percentage points |
| `main_minutes_to_one_pct_down_move` | VECTOR | Number of minutes that elapsed before price went down 1 percentage point |
| `main_minutes_to_two_pct_up_move` | VECTOR | Number of minutes that elapsed before price went up 2 percentage points |
| `main_opening_gap_percent` | VECTOR | (DayOpen  PrevClose) / PrevClose, percent price gap at open |
| `main_opening_trading_volume` | VECTOR | Main session open volume (trade volume at open time) |
| `main_pct_change_one_twenty_minute_post_news` | VECTOR | Percent price change in the first 120 minutes of the main session after news. |
| `main_pct_change_sixty_minute_post_news` | VECTOR | Percent price change in the first sixty minutes of the main session after news. |
| `main_pct_change_ten_minute_post_news` | VECTOR | Percent price change in the first ten minutes of the main session after news. |
| `main_pct_change_thirty_minute_post_news` | VECTOR | Percent price change in the first thirty minutes of the main session after news. |
| `main_post_session_vwap` | VECTOR | Volume weighted average price for the post-session or period after the event |
| `main_price_at_news_time` | VECTOR | Price at the time of news |
| `main_price_range_deviation_std` | VECTOR | Z-score of daily price range, based on mean and standard deviation over past 30 days |
| `main_session_closing_price` | VECTOR | Closing price at end of session |
| `main_session_low_after_news` | VECTOR | Lowest price reached from time of news through the end of main session |
| `main_session_market_cap` | VECTOR | Market capitalization for the reporting/session day |
| `main_session_minutes_to_five_pct_increase` | VECTOR | Number of minutes until price rose 5 percent after event |
| `main_session_minutes_to_one_pct_decline` | VECTOR | Number of minutes that elapsed before price went down 1 percentage point |
| `main_session_news_time_price` | VECTOR | Price at the time of news release |
| `main_session_ninety_minute_change_pct` | VECTOR | Percent price change in the first ninety minutes after news in the main session. |
| `main_session_performance_vs_benchmark` | VECTOR | Performance metric comparing stock move versus S&P 500 index |
| `main_session_price_range` | VECTOR | Percentage range: (session high - session low) / session low price |
| `main_session_range_to_atr_ratio` | VECTOR | Ratio of current price movement against 14-day average true range, a measure of relative volatility |
| `main_session_thirty_minute_change_pct` | VECTOR | Percent price change in the first thirty minutes after news in the main session. |
| `main_session_volume_ratio` | VECTOR | Current volume divided by 30-day moving average session volume |
| `main_session_volume_stddev` | VECTOR | Standardized anomaly of current trading volume relative to past 30-day volume mean and standard deviation |
| `main_session_volume_weighted_average_price` | VECTOR | Main session Volume Weighted Average Price |
| `main_session_vwap_2` | VECTOR | Main session volume-weighted average price for Day 1 |
| `main_session_vwap_from_news` | VECTOR | Volume weighted average price from time of news to session end |
| `main_session_vwap_pre` | VECTOR | Volume-weighted average price for trades in the main market session |
| `main_session_vwap_pre_filter` | VECTOR | Volume-weighted average price for the main market session |
| `main_share_price_to_earnings_ratio` | VECTOR | Price-to-Earnings Ratio for the stock on the session’s calendar day |
| `main_trading_volume_deviation_std` | VECTOR | (CurrentVolume - AvgVol)/VolStDev, standardized volume deviation over trailing 30 days |
| `market_equity_value_1555` | VECTOR | Market capitalization for the calendar day/session |
| `max_downward_price_move` | VECTOR | Maximum downward price movement (absolute amount) from the time of event/news until end of event day (D1), for the "A… |
| `max_downward_price_move_amt` | VECTOR | Difference between price at news time and session low price after the news |
| `max_downward_price_move_pct` | VECTOR | Percent change from price at news time to session low after the news |
| `max_pct_decrease_post_news` | VECTOR | Maximum downward price movement (absolute value) after the event within the session |
| `max_pct_increase_post_news` | VECTOR | Maximum absolute upward price movement following the news/event during Day 1 |
| `max_upward_price_move` | VECTOR | Maximum upward price movement (absolute value) after the event within the session |
| `max_upward_price_move_pct` | VECTOR | Percent change from price at the time of the news to session high after the news |
| `maximum_downward_amount_pre` | VECTOR | Difference between the price at the time of the news and the lowest price after the news |
| `maximum_downward_movement_amount` | VECTOR | Difference between price at time of news and lowest price after news |
| `maximum_downward_movement_percent` | VECTOR | Lowest percent drop from time of news to post-news session low |
| `maximum_downward_percent_change_1555` | VECTOR | Percent change from the news time price to the lowest price reached after the news |
| `maximum_downward_percent_pre` | VECTOR | Percent change from the price at the time of the news to the lowest price after the news |
| `maximum_downward_price_movement_1555` | VECTOR | Difference between the price at the time of the news and the lowest price after the news |
| `maximum_upward_amount_pre` | VECTOR | Difference between the highest price after the news and the price at the time of the news |
| `maximum_upward_movement_amount` | VECTOR | Maximum upward price movement after the news event, specifically calculated as the highest price after news minus the… |
| `maximum_upward_movement_percent` | VECTOR | Highest percent gain from time of news to post-news session high |
| `maximum_upward_percent_change_1555` | VECTOR | Percent change from the news time price to the highest price reached after the news |
| `maximum_upward_percent_pre` | VECTOR | Percent change from the price at the time of the news to the highest price after the news |
| `maximum_upward_price_movement_1555` | VECTOR | Maximum price increase after the news, calculated as post-news high minus price at news time |
| `min_minutes_to_10pct_move` | VECTOR | 10th percentile value for the selected analytic metric within the session |
| `min_minutes_to_1pct_move` | VECTOR | Value at the first percentile (1st percentile) of a distribution (could be price move, volume, etc.) for event day in… |
| `min_minutes_to_2pct_move` | VECTOR | Minimum minutes to reach a 2 percent price move after news. |
| `min_minutes_to_2pct_move_filter` | VECTOR | Minimum number of minutes taken for price to reach either an upward or downward threshold, per minute bucket |
| `min_minutes_to_3pct_move` | VECTOR | Minimum minutes to reach a 3 percent price move after news. |
| `min_minutes_to_3pct_move_2` | VECTOR | The minimum elapsed minute value among L or S signals for each minute bucket in After Hours Day 1 |
| `min_minutes_to_4pct_move` | VECTOR | Minimum minutes to reach a 4 percent price move after news. |
| `min_minutes_to_5pct_move` | VECTOR | 5th percentile value for the selected analytic metric within the session |
| `min_minutes_to_75pct_move` | VECTOR | 75th percentile value for the security price or metric, Day 1 |
| `min_minutes_to_five_pct_move` | VECTOR | Minimum value of L or S for each minute bucket at 5th minute (or 5% move threshold, depending on data context) |
| `min_minutes_to_five_pct_move_2_1555` | VECTOR | Minimum minutes needed to reach up/down threshold for each minute bucket |
| `min_minutes_to_five_percent_move` | VECTOR | The minimum of L or S above for each minute bucket |
| `min_minutes_to_five_percent_move_all` | VECTOR | 5th percentile value or ranking in day 1 'All Filter' |
| `min_minutes_to_four_pct_move` | VECTOR | Minimum minutes to either a four percent rise or fall in price. |
| `min_minutes_to_four_pct_move_2_1555` | VECTOR | The minimum of L or S above for each minute bucket |
| `min_minutes_to_four_percent_move` | VECTOR | Minimum minutes to reach a four percent price move. |
| `min_minutes_to_one_pct_move` | VECTOR | The minimum elapsed time in minutes for price to move up or down 1 percentage point in each minute bucket |
| `min_minutes_to_one_pct_move_2_1555` | VECTOR | The minimum of L or S above for each minute bucket |
| `min_minutes_to_one_percent_move` | VECTOR | 1st percentile value, indicating value below which 1% of observations fall in the session |
| `min_minutes_to_seventyfive_pct_move_2_1555` | VECTOR | Minimum elapsed time in minutes to reach +75% or -75% price move (whichever comes first) in each minute bucket |
| `min_minutes_to_seventyfive_percent_move` | VECTOR | The minimum of L or S above for each minute bucket |
| `min_minutes_to_seventyfive_percent_move_all` | VECTOR | 75th percentile value, indicating value below which 75% of observations fall in the session |
| `min_minutes_to_ten_pct_move_2_1555` | VECTOR | Minimum elapsed time in minutes to reach +10% or -10% price move (whichever comes first) in each minute bucket |
| `min_minutes_to_ten_percent_move` | VECTOR | 10th percentile value, indicating the value below which 10% of observations fall in the session |
| `min_minutes_to_three_pct_move` | VECTOR | Minimum value of L or S for each minute bucket (i.e. quickest time to reach either up or down threshold) |
| `min_minutes_to_three_pct_move_2_1555` | VECTOR | Minimum elapsed time in minutes to reach +3% or -3% price move (whichever comes first) in each minute bucket |
| `min_minutes_to_three_percent_move` | VECTOR | 3rd percentile value, indicating value below which 3% of observations fall in the session |
| `min_minutes_to_twenty_pct_move_2_1555` | VECTOR | Minimum elapsed time in minutes to reach +20% or -20% price move (whichever comes first) in each minute bucket |
| `min_minutes_to_two_pct_move` | VECTOR | Minimum minutes to either a two percent rise or fall in price. |
| `min_minutes_to_two_pct_move_2_1555` | VECTOR | Minimum elapsed time in minutes to reach +2% or -2% price move (whichever comes first) in each minute bucket |
| `min_minutes_to_two_percent_move` | VECTOR | 2nd percentile value or ranking in day 1 'All Filter' |
| `minimum_minutes_to_five_percent_move` | VECTOR | The minimum elapsed minutes for either an upward (L) or downward (S) price move in each minute bucket, likely at the … |
| `minimum_minutes_to_five_percent_move_2` | VECTOR | Minimum number of minutes for price to move up or down, for each minute bucket, at 5th percentile threshold |
| `minimum_minutes_to_five_percent_move_afterhours` | VECTOR | The minimum elapsed minute value among L or S signals for each minute bucket in After Hours Day 1 |
| `minimum_minutes_to_four_percent_move` | VECTOR | The minimum elapsed minutes for either an upward (L) or downward (S) price move in each minute bucket |
| `minimum_minutes_to_four_percent_move_2` | VECTOR | Minimum number of minutes for price to move up or down, for each minute bucket, at 4th percentile threshold |
| `minimum_minutes_to_four_percent_move_pre` | VECTOR | The minimum elapsed time among upward or downward moves (L or S) for the 4 minute bucket after the event in the pre-m… |
| `minimum_minutes_to_one_percent_move` | VECTOR | The minimum elapsed minutes for either an upward (L) or downward (S) price move in each minute bucket, likely at the … |
| `minimum_minutes_to_one_percent_move_2` | VECTOR | Minimum minutes before price moves by one percent in either direction. |
| `minimum_minutes_to_one_percent_move_afterhours` | VECTOR | The minimum elapsed minute value among L or S signals for each minute bucket in After Hours Day 1 |
| `minimum_minutes_to_seventy_five_percent_move` | VECTOR | The minimum elapsed minutes for either an upward (L) or downward (S) price move in each minute bucket, likely at the … |
| `minimum_minutes_to_three_percent_move` | VECTOR | The minimum elapsed time (in minutes) to either an upward or downward threshold move within 3 percent, computed per m… |
| `minimum_minutes_to_three_percent_move_2` | VECTOR | Minimum number of minutes for price to move up or down, for each minute bucket, at 3rd percentile threshold |
| `minimum_minutes_to_two_percent_move` | VECTOR | For each minute bucket, the minimum of the upward (L) or downward (S) threshold crossing times (i.e., fastest either … |
| `minutes_to_1pct_decline` | VECTOR | Number of minutes before price decreased by 1 percent after news. |
| `minutes_to_1pct_increase` | VECTOR | Analytics value at Level/Tier 1 (commonly primary price or volume level) during event day in the "All" session |
| `minutes_to_1pct_price_decrease_filter` | VECTOR | Number of minutes before price drops by 1 percent after the news |
| `minutes_to_1pct_price_increase_filter` | VECTOR | Minutes elapsed before price increased by 1 percent post-event |
| `minutes_to_2pct_decline` | VECTOR | Number of minutes before price decreased by 2 percent after news. |
| `minutes_to_2pct_increase` | VECTOR | Number of minutes before price increased by 2 percent after news. |
| `minutes_to_2pct_price_increase_filter` | VECTOR | Minutes elapsed before price increased by 2 percent after the event |
| `minutes_to_3pct_decline` | VECTOR | Number of minutes before price decreased by 3 percent after news. |
| `minutes_to_3pct_increase` | VECTOR | Number of minutes before price increased by 3 percent after news. |
| `minutes_to_3pct_price_increase` | VECTOR | Minutes elapsed before price went up by 3 percentage points after the news |
| `minutes_to_3pct_price_increase_filter` | VECTOR | Number of minutes that elapsed before price went up 3 percentage points |
| `minutes_to_4pct_decline` | VECTOR | Number of minutes before price decreased by 4 percent after news. |
| `minutes_to_4pct_increase` | VECTOR | Number of minutes before price increased by 4 percent after news. |
| `minutes_to_4pct_price_increase` | VECTOR | Minutes elapsed before price went up by 4 percentage points after the news |
| `minutes_to_5pct_decline` | VECTOR | Number of minutes before price decreased by 5 percent after news. |
| `minutes_to_5pct_increase` | VECTOR | Number of minutes before price increased by 5 percent after news. |
| `minutes_to_75pct_decline` | VECTOR | Number of minutes before price decreased by 75 percent after news. |
| `minutes_to_75pct_increase` | VECTOR | Number of minutes before price increased by 75 percent after news. |
| `minutes_to_fifth_percent_gain` | VECTOR | Number of minutes elapsed before price increased by 5 percentage points from the time of the news |
| `minutes_to_fifth_percent_loss` | VECTOR | Number of minutes elapsed before the price decreased by 5 percentage points from the event in the pre-market session |
| `minutes_to_first_percent_gain` | VECTOR | Number of minutes elapsed before price increased by 1 percentage point from the time of the news |
| `minutes_to_five_pct_decline` | VECTOR | Number of minutes before price fell 5% after the event |
| `minutes_to_five_pct_down_move_1555` | VECTOR | Number of minutes elapsed before price dropped 5 percentage points after the news |
| `minutes_to_five_pct_increase` | VECTOR | Number of minutes that elapsed before price went up 5 percentage points |
| `minutes_to_five_pct_up_move_1555` | VECTOR | Minutes elapsed before price rose 5 percent above its value at news time |
| `minutes_to_five_percent_drop` | VECTOR | Number of minutes until price drops by 5 percent after the news event |
| `minutes_to_five_percent_drop_all` | VECTOR | Minutes taken for price to decrease by five percent after event (all sessions). |
| `minutes_to_five_percent_gain` | VECTOR | Level 5 value, the 5th rank or tier (e.g., price or volume) in the session |
| `minutes_to_five_percent_loss` | VECTOR | Number of minutes until price dropped 5 percent after event |
| `minutes_to_four_pct_decline` | VECTOR | Number of minutes until price dropped 4% after the event |
| `minutes_to_four_pct_down_move_1555` | VECTOR | Number of minutes elapsed before the price decreased by 4% after the event |
| `minutes_to_four_pct_increase` | VECTOR | Number of minutes until price increased 4% from the event |
| `minutes_to_four_pct_up_move_1555` | VECTOR | Number of minutes required for the price to rise by 4% after the event |
| `minutes_to_four_percent_decline` | VECTOR | Number of minutes that elapsed before price went down 4 percentage points |
| `minutes_to_four_percent_drop` | VECTOR | Minutes taken for price to decrease by four percent after event. |
| `minutes_to_four_percent_gain` | VECTOR | Number of minutes that elapsed before price rose by 4 percent post-news |
| `minutes_to_four_percent_gain_2` | VECTOR | Level 4 value, representing the 4th rank or tier (e.g., price or volume) in the session |
| `minutes_to_four_percent_increase` | VECTOR | Number of minutes that elapsed before price went up 4 percentage points |
| `minutes_to_four_percent_loss` | VECTOR | Number of minutes until price dropped 4 percent after event |
| `minutes_to_four_percent_loss_afterhours` | VECTOR | Number of minutes that elapsed before price went down 4 percentage points after news in After Hours on Day 1 |
| `minutes_to_fourth_percent_gain` | VECTOR | Number of minutes elapsed before price increased by 4 percentage points from the time of the news |
| `minutes_to_fourth_percent_loss` | VECTOR | Number of minutes elapsed before the price decreased by 4 percentage points from the event in the pre-market session |
| `minutes_to_one_pct_decline` | VECTOR | Minutes until price dropped 1% after the news event |
| `minutes_to_one_pct_down_move_1555` | VECTOR | Number of minutes elapsed before the price decreased by 1% after the event |
| `minutes_to_one_pct_increase` | VECTOR | Number of minutes that elapsed before price went up 1 percentage point |
| `minutes_to_one_pct_up_move_1555` | VECTOR | Number of minutes elapsed before price increased 1 percentage point after the news |
| `minutes_to_one_percent_decline_pre` | VECTOR | Number of minutes elapsed before the price decreased by 1 percentage point from the event in the pre-market session |
| `minutes_to_one_percent_gain` | VECTOR | Number of minutes that elapsed before price rose by 1 percent after the news |
| `minutes_to_one_percent_gain_2` | VECTOR | Number of minutes that elapsed before price went up 1 percentage point |
| `minutes_to_second_percent_gain` | VECTOR | Number of minutes elapsed before price increased by 2 percentage points from the time of the news |
| `minutes_to_seventyfive_pct_down_move_1555` | VECTOR | Number of minutes elapsed before price dropped 7.5 percentage points after the news |
| `minutes_to_seventyfive_pct_up_move_1555` | VECTOR | Number of minutes elapsed before price rose 7.5 percentage points after the news |
| `minutes_to_seventyfive_percent_gain` | VECTOR | Minutes taken for price to increase by seventy-five percent after event. |
| `minutes_to_ten_pct_down_move_1555` | VECTOR | Number of minutes elapsed before the price decreased by 10% after the event |
| `minutes_to_ten_pct_up_move_1555` | VECTOR | Number of minutes elapsed before the price increased by 10% after the event |
| `minutes_to_third_percent_gain` | VECTOR | Number of minutes elapsed before price increased by 3 percentage points from the time of the news |
| `minutes_to_third_percent_loss` | VECTOR | Number of minutes elapsed before the price decreased by 3 percentage points from the event in the pre-market session |
| `minutes_to_three_pct_decline` | VECTOR | Minutes elapsed before price fell 3% after the event |
| `minutes_to_three_pct_down_move_1555` | VECTOR | Minutes elapsed before price dropped 3 percent below its value at news time |
| `minutes_to_three_pct_increase` | VECTOR | Number of minutes that elapsed before price went up 3 percentage points |
| `minutes_to_three_pct_up_move_1555` | VECTOR | Minutes elapsed before price rose 3 percent above its value at news time |
| `minutes_to_three_percent_decline` | VECTOR | Number of minutes that elapsed before price went down 3 percentage points |
| `minutes_to_three_percent_drop` | VECTOR | Number of minutes until price drops by 3 percent after the news event |
| `minutes_to_three_percent_drop_all` | VECTOR | Minutes taken for price to decrease by three percent after event (all sessions). |
| `minutes_to_three_percent_gain` | VECTOR | Number of minutes that elapsed before price rose by 3 percent after the news |
| `minutes_to_three_percent_gain_2` | VECTOR | Number of minutes that elapsed before price went up 3 percentage points |
| `minutes_to_three_percent_gain_all` | VECTOR | Minutes taken for price to increase by three percent after event (all sessions). |
| `minutes_to_three_percent_loss` | VECTOR | Number of minutes that elapsed before price went down 3 percentage points |
| `minutes_to_twenty_pct_down_move_1555` | VECTOR | Number of minutes elapsed before the price decreased by 20% after the event |
| `minutes_to_twenty_pct_up_move_1555` | VECTOR | Number of minutes required for the price to rise by 20% after the event |
| `minutes_to_two_pct_decline` | VECTOR | Number of minutes that elapsed before price went down 2 percentage points |
| `minutes_to_two_pct_down_move_1555` | VECTOR | Number of minutes elapsed before the price decreased by 2% after the event |
| `minutes_to_two_pct_increase` | VECTOR | Number of minutes that elapsed before price went up 2 percentage points |
| `minutes_to_two_pct_up_move_1555` | VECTOR | Minutes elapsed before price rose 2 percent above its value at news time |
| `minutes_to_two_percent_decline` | VECTOR | Number of minutes that elapsed before price went down 2 percentage points |
| `minutes_to_two_percent_decline_pre` | VECTOR | Number of minutes elapsed before the price decreased by 2 percentage points from the event in the pre-market session |
| `minutes_to_two_percent_drop` | VECTOR | Number of minutes until price drops by 2 percent after the news event |
| `minutes_to_two_percent_drop_all` | VECTOR | Minutes taken for price to decrease by two percent after event (all sessions). |
| `minutes_to_two_percent_gain` | VECTOR | Number of minutes that elapsed before price rose by 2 percent after the news event |
| `minutes_to_two_percent_gain_2` | VECTOR | Minutes taken for price to increase by two percent after event. |
| `minutes_to_two_percent_loss` | VECTOR | Number of minutes that elapsed before price went down 2 percentage points |
| `minutes_to_two_percent_loss_afterhours` | VECTOR | Number of minutes that elapsed before price went down 2 percentage points after news in After Hours on Day 1 |
| `minutes_until_one_percent_price_decrease` | VECTOR | Number of minutes before the price drops by one percent after news. |
| `minutes_until_one_percent_price_increase` | VECTOR | Level 1 value, representing the top rank or tier (e.g., price or volume) in the relevant session window |
| `minutes_until_seventy_five_percent_price_decrease` | VECTOR | Number of minutes before the price drops by seventy-five percent after news. |
| `mkt_cap_val_2` | VECTOR | Market capitalization of the company during the session/day |
| `mkt_cap_val_3` | VECTOR | Market capitalization of the company at time of news or during session |
| `mkt_cap_val_4` | VECTOR | Market capitalization value of the stock reported for After Hours Day 1 |
| `mkt_cap_val_5` | VECTOR | Market capitalization for the stock on the event day during pre-market session |
| `mkt_cap_val_6` | VECTOR | Market capitalization (total value of company's shares) for the session/date |
| `mkt_cap_val_filter` | VECTOR | Market capitalization of the company at the time of the session |
| `news_all_vwap` | MATRIX | VWAP across all sessions (pre, main, post) |
| `news_atr14` | MATRIX | 14-day Average True Range |
| `news_atr_ratio` | MATRIX | Ratio of current day's price range to 20-day average true range |
| `news_cap` | MATRIX | Reported total market capitalization for the calendar day of the session |
| `news_close_vol` | MATRIX | Main session close volume |
| `news_curr_vol` | MATRIX | Current day's session volume |
| `news_dividend_yield` | MATRIX | Reported annual dividend yield percentage for the calendar day of the session |
| `news_eod_close` | MATRIX | Session closing price |
| `news_eod_high` | MATRIX | Highest price from the time of news to end of session |
| `news_eod_low` | MATRIX | Lowest price from the time of news to end of session |
| `news_eod_vwap` | MATRIX | VWAP from the time of news to the end of the session |
| `news_eps_actual` | MATRIX | Actual Earnings Per Share reported in the news release |
| `news_high_exc_stddev` | MATRIX | Standardized measure of price movement from end-of-day high to last price in the time-of-news window, divided by 30-d… |
| `news_indx_perf` | MATRIX | Difference in percent return between the stock and the S&P 500 ETF over the session: ((EODClose - TONLast) / TONLast)… |
| `news_low_exc_stddev` | MATRIX | Standardized measure of price movement from last price in time-of-news window to end-of-day low, divided by 30-day cl… |
| `news_ls` | MATRIX | Indicates if a long or short position would have been more advantageous, based on comparison of (EODHigh - Last) and … |
| `news_main_vwap` | MATRIX | Main session volume-weighted average price |
| `news_max_dn_amt` | MATRIX | Price at the time of the news minus the after-news low |
| `news_max_dn_ret` | MATRIX | Percent change from price at time of news to lowest price after news |
| `news_max_up_amt` | MATRIX | After-news high minus the price at the time of the news |
| `news_max_up_ret` | MATRIX | Percent change from price at time of news to highest price after news |
| `news_mins_10_chg` | MATRIX | Minimum value among L or S for each minute bucket, indicating the fastest reaction time at the 10th percentile |
| `news_mins_10_pct_dn` | MATRIX | Number of minutes elapsed before price decreases by 10 percentage points after the event |
| `news_mins_10_pct_up` | MATRIX | Number of minutes before the price increased by at least 10 percent after the news release |
| `news_mins_1_chg` | MATRIX | Minimum number of minutes taken for price to move (up or down) 1 percentage point after the event |
| `news_mins_1_pct_dn` | MATRIX | Number of minutes before the price decreased by at least 1 percent after the news release |
| `news_mins_1_pct_up` | MATRIX | Number of minutes before the price increased by at least 1 percent after the news release |
| `news_mins_20_chg` | MATRIX | The minimum of L or S above for 20-minute bucket |
| `news_mins_20_pct_dn` | MATRIX | Number of minutes that elapsed before price went down 20 percentage points |
| `news_mins_20_pct_up` | MATRIX | Number of minutes that elapsed before price went up 20 percentage points |
| `news_mins_2_chg` | MATRIX | Minimum number of minutes taken for price to move (up or down) 2 percentage points after the event |
| `news_mins_2_pct_dn` | MATRIX | Number of minutes before the price decreased by at least 2 percent after the news release |
| `news_mins_2_pct_up` | MATRIX | Number of minutes before the price increased by at least 2 percent after the news release |
| `news_mins_3_chg` | MATRIX | Minimum number of minutes taken for price to move (up or down) 3 percentage points after the event |
| `news_mins_3_pct_dn` | MATRIX | Number of minutes before the price decreased by at least 3 percent after the news release |
| `news_mins_3_pct_up` | MATRIX | Number of minutes before the price increased by at least 3 percent after the news release |
| `news_mins_4_chg` | MATRIX | Minimum value among L or S (minutes to reach positive/negative return thresholds) for each minute bucket, representin… |
| `news_mins_4_pct_dn` | MATRIX | Number of minutes before the price decreased by at least 4 percent after the news release |
| `news_mins_4_pct_up` | MATRIX | Number of minutes before the price increased by at least 4 percent after the news release |
| `news_mins_5_chg` | MATRIX | Minimum value among L or S for each minute bucket, indicating the fastest reaction time at the 5th percentile |
| `news_mins_5_pct_dn` | MATRIX | Number of minutes before the price decreased by at least 5 percent after the news release |
| `news_mins_5_pct_up` | MATRIX | Number of minutes before the price increased by at least 5 percent after the news release |
| `news_mins_7_5_chg` | MATRIX | Minimum value among L or S for each minute bucket, indicating the fastest reaction time at the 75th percentile |
| `news_mins_7_5_pct_dn` | MATRIX | Number of minutes elapsed before price decreases by 7.5 percentage points after the event |
| `news_mins_7_5_pct_up` | MATRIX | Number of minutes elapsed before price increases by 7.5 percentage points after the event |
| `news_mov_vol` | MATRIX | 30-day moving average of session volume |
| `news_open` | MATRIX | Price at the session open |
| `news_open_gap` | MATRIX | Percent difference between current day's open and previous day's close |
| `news_open_vol` | MATRIX | Main session open volume |
| `news_pct_10min` | MATRIX | Percent change in price during the first 10 minutes following the news release |
| `news_pct_120min` | MATRIX | Percent change in price during the first 120 minutes following the news release |
| `news_pct_1min` | MATRIX | Percent change in price during the first minute following the news release |
| `news_pct_30min` | MATRIX | Percent change in price during the first 30 minutes following the news release |
| `news_pct_30sec` | MATRIX | Percent change in price in the 30 seconds after the news release |
| `news_pct_5_min` | MATRIX | Percent change in price during the first 5 minutes following the news release |
| `news_pct_60min` | MATRIX | Percent change in price during the first 60 minutes following the news release |
| `news_pct_90min` | MATRIX | Percent change in price during the first 90 minutes following the news release |
| `news_pe_ratio` | MATRIX | Reported price-to-earnings ratio for the calendar day of the session |
| `news_post_vwap` | MATRIX | Post-session volume-weighted average price |
| `news_pre_vwap` | MATRIX | Pre-session volume-weighted average price |
| `news_prev_close` | MATRIX | Previous trading day’s closing price |
| `news_prev_day_ret` | MATRIX | Percent change between previous day's open and close price |
| `news_prev_vol` | MATRIX | Previous day's session volume |
| `news_range_stddev` | MATRIX | Z-score of current day's trading range compared to 30-day average range, using 30-day range standard deviation |
| `news_ratio_vol` | MATRIX | Ratio of current session volume to 30-day moving average volume |
| `news_session_range` | MATRIX | Difference between session high and session low price |
| `news_session_range_pct` | MATRIX | (Session High Price - Session Low Price) / Session Low Price |
| `news_short_interest` | MATRIX | Ratio of total number of shares sold short to total shares outstanding |
| `news_spy_close` | MATRIX | SPY price at session close |
| `news_spy_last` | MATRIX | SPY last price at the time of the news |
| `news_ton_high` | MATRIX | Highest price reached during the session before the time of news |
| `news_ton_last` | MATRIX | Price at the time of the news |
| `news_ton_low` | MATRIX | Lowest price reached during the session before the time of news |
| `news_tot_ticks` | MATRIX | Total number of ticks during the trading day |
| `news_vol_stddev` | MATRIX | Z-score of current volume compared to 30-day average volume, using 30-day volume standard deviation |
| `ninety_minute_price_change_pct` | VECTOR | Percent price change in the first ninety minutes after news release. |
| `ninety_minute_price_change_pct_2` | VECTOR | Percent change in price during the first ninety minutes after event. |
| `ninety_minute_price_change_pct_3` | VECTOR | Percent price change in the ninety minutes following the event. |
| `ninety_minute_price_change_pct_pre` | VECTOR | Return, price, or analytic data for the 90 minutes after the news event |
| `nws12_afterhsz_01l` | VECTOR | Number of minutes that elapsed before price went up 10 percentage points |
| `nws12_afterhsz_01p` | VECTOR | The minimum of L or S above for 10 minute bucket |
| `nws12_afterhsz_01s` | VECTOR | Number of minutes that elapsed before price went down 10 percentage points |
| `nws12_afterhsz_02l` | VECTOR | Number of minutes that elapsed before price went up 20 percentage points |
| `nws12_afterhsz_02p` | VECTOR | The minimum of L or S above for 20-minute bucket |
| `nws12_afterhsz_02s` | VECTOR | Number of minutes that elapsed before price went down 20 percentage points |
| `nws12_afterhsz_10_min` | VECTOR | The percent change in price in the first 10 minutes following the news release |
| `nws12_afterhsz_120_min` | VECTOR | The percent change in price in the first 120 minutes following the news release |
| `nws12_afterhsz_1_minute` | VECTOR | The percent change in price in the first minute following the news release |
| `nws12_afterhsz_1l` | VECTOR | Number of minutes that elapsed before price went up 1 percentage points |
| `nws12_afterhsz_1p` | VECTOR | The minimum of L or S above for 1-minute bucket |
| `nws12_afterhsz_1s` | VECTOR | Number of minutes that elapsed before price went down 1 percentage point |
| `nws12_afterhsz_2l` | VECTOR | Number of minutes that elapsed before price went up 2 percentage points |
| `nws12_afterhsz_2p` | VECTOR | The minimum of L or S above for 2-minute bucket |
| `nws12_afterhsz_2s` | VECTOR | Number of minutes that elapsed before price went down 2 percentage points |
| `nws12_afterhsz_30_min` | VECTOR | The percent change in price in the first 30 minutes following the news release |
| `nws12_afterhsz_3l` | VECTOR | Number of minutes that elapsed before price went up 3 percentage points |
| `nws12_afterhsz_3p` | VECTOR | The minimum of L or S above for 3-minute bucket |
| `nws12_afterhsz_3s` | VECTOR | Number of minutes that elapsed before price went down 3 percentage points |
| `nws12_afterhsz_41rta` | VECTOR | 14-day Average True Range |
| `nws12_afterhsz_4l` | VECTOR | Number of minutes that elapsed before price went up 4 percentage points |
| `nws12_afterhsz_4p` | VECTOR | The minimum of L or S above for 4-minute bucket |
| `nws12_afterhsz_4s` | VECTOR | Number of minutes that elapsed before price went down 4 percentage points |
| `nws12_afterhsz_57l` | VECTOR | Number of minutes that elapsed before price went up 7.5 percentage points |
| `nws12_afterhsz_57p` | VECTOR | The minimum of L or S above for 7.5-minute bucket |
| `nws12_afterhsz_57s` | VECTOR | Number of minutes that elapsed before price went down 7.5 percentage points |
| `nws12_afterhsz_5_min` | VECTOR | The percent change in price in the first 5 minutes following the news release |
| `nws12_afterhsz_5l` | VECTOR | Number of minutes that elapsed before price went up 5 percentage points |
| `nws12_afterhsz_5p` | VECTOR | The minimum of L or S above for 5-minute bucket |
| `nws12_afterhsz_5s` | VECTOR | Number of minutes that elapsed before price went down 5 percentage points |
| `nws12_afterhsz_60_min` | VECTOR | The percent change in price in the first 60 minutes following the news release |
| `nws12_afterhsz_90_min` | VECTOR | The percent change in price in the first 90 minutes following the news release |
| `nws12_afterhsz_allticks` | VECTOR | Total number of ticks for the trading day |
| `nws12_afterhsz_atrratio` | VECTOR | Ratio of Today Range to 20-day average true range |
| `nws12_afterhsz_close_vol` | VECTOR | Main close volume |
| `nws12_afterhsz_curr_vol` | VECTOR | Current day's session volume |
| `nws12_afterhsz_dayopen` | VECTOR | Price at the session open |
| `nws12_afterhsz_div_y` | VECTOR | Annual yield |
| `nws12_afterhsz_eodclose` | VECTOR | Close price of the session |
| `nws12_afterhsz_eodhigh` | VECTOR | Highest price reached between the time of news and the end of the session |
| `nws12_afterhsz_eodlow` | VECTOR | Lowest price reached between the time of news and the end of the session |
| `nws12_afterhsz_eodvwap` | VECTOR | volume weighted average price between the time of news and the end of the session. |
| `nws12_afterhsz_epsactual` | VECTOR | The actual Earnings Per Share value that was conveyed by the news release |
| `nws12_afterhsz_highexcstddev` | VECTOR | (EODHigh - TONLast)/StdDev, where StdDev is one standard deviation for the close price for 30 calendar days |
| `nws12_afterhsz_lowexcstddev` | VECTOR | (TONLast - EODLow) / StdDev, where StdDev is one standard deviation for the close price for 30 calendar days |
| `nws12_afterhsz_mainvwap` | VECTOR | Main session volume weighted average price |
| `nws12_afterhsz_maxdnamt` | VECTOR | The price at the time of the news minus the after the news low |
| `nws12_afterhsz_maxdown` | VECTOR | Percent change from the price at the time of the news to the after the news low |
| `nws12_afterhsz_maxup` | VECTOR | Percent change from the price at the time of the news to the after the news high |
| `nws12_afterhsz_maxupamt` | VECTOR | The after the news high minus the price at the time of the news |
| `nws12_afterhsz_mktcap` | VECTOR | Reported market capitalization for the calendar day of the session |
| `nws12_afterhsz_mov_vol` | VECTOR | 30-day moving average session volume |
| `nws12_afterhsz_newrecord` | VECTOR | Tracks whether the news is first instance or a duplicate |
| `nws12_afterhsz_newssess` | VECTOR | Index of the session in which the news was reported |
| `nws12_afterhsz_open_vol` | VECTOR | Main open volume |
| `nws12_afterhsz_opengap` | VECTOR | (DayOpen - PrevClose) / PrevClose. |
| `nws12_afterhsz_peratio` | VECTOR | Reported price to earnings ratio for the calendar day of the session |
| `nws12_afterhsz_postvwap` | VECTOR | Post-session volume weighted average price |
| `nws12_afterhsz_prev_vol` | VECTOR | Previous day's session volume |
| `nws12_afterhsz_prevclose` | VECTOR | Previous trading day's close price |
| `nws12_afterhsz_prevday` | VECTOR | Percent change between the previous day's open and close |
| `nws12_afterhsz_prevwap` | VECTOR | Pre session volume weighted average price |
| `nws12_afterhsz_provider` | VECTOR | index of name of the news provider |
| `nws12_afterhsz_range` | VECTOR | Session High Price - Session Low Price) / Session Low Price. |
| `nws12_afterhsz_rangeamt` | VECTOR | Session High Price - Session Low Price |
| `nws12_afterhsz_rangestddev` | VECTOR | (RangeAmt - AvgRange) / RangeStdDev, where AvgRange is the average of the daily range, and RangeStdDev is one standar… |
| `nws12_afterhsz_reportsess` | VECTOR | Index of Session on which the spreadsheet is reporting |
| `nws12_afterhsz_result1` | VECTOR | Percent change between the price at the time of the news release to the price at the close of the session |
| `nws12_afterhsz_result2` | VECTOR | Percent change between the price at the time of the news release to the price at the close of the session |
| `nws12_afterhsz_result_vs_index` | VECTOR | ((EODClose - TONLast) / TONLast) - ((SPYClose - SPYLast) / SPYLast) |
| `nws12_afterhsz_short_interest` | VECTOR | Total number of shares sold short divided by total number of shares outstanding |
| `nws12_afterhsz_sl` | VECTOR | Whether a long or short position would have been more advantageous: If (EODHigh - Last) > (Last - EODLow) Then LS = 1… |
| `nws12_afterhsz_spyclose` | VECTOR | Price of SPY at close of session |
| `nws12_afterhsz_spylast` | VECTOR | Last Price of the SPY at the time of the news |
| `nws12_afterhsz_tonhigh` | VECTOR | Highest price reached during the session before the time of news |
| `nws12_afterhsz_tonlast` | VECTOR | Price at the time of news |
| `nws12_afterhsz_tonlow` | VECTOR | Lowest price reached during the session before the time of the news |
| `nws12_afterhsz_vol_ratio` | VECTOR | Curr_Vol / Mov_Vol |
| `nws12_afterhsz_volstddev` | VECTOR | (CurrentVolume - AvgVol)/VolStDev, where AvgVol is the average of the daily volume, and VolStdDev is one standard dev… |
| `nws12_allz_newrecord` | VECTOR | Tracks whether the news is first instance or a duplicate |
| `nws12_allz_newssess` | VECTOR | Index of session in which the news was reported |
| `nws12_allz_provider` | VECTOR | index of name of the news provider |
| `nws12_allz_reportsess` | VECTOR | Index of Session on which the spreadsheet is reporting |
| `nws12_allz_result1` | VECTOR | Percent change between the price at the time of the news release and the price at the close of the session |
| `nws12_allz_result2` | VECTOR | Percent change between the price at the time of the news release and the price at the close of the session |
| `nws12_mainz_01l` | VECTOR | Number of minutes that elapsed before price went up 10 percentage points |
| `nws12_mainz_01p` | VECTOR | The minimum of L or S above for 10-minute bucket |
| `nws12_mainz_01s` | VECTOR | Number of minutes that elapsed before price went down 10 percentage points |
| `nws12_mainz_02l` | VECTOR | Number of minutes that elapsed before price went up 20 percentage points |
| `nws12_mainz_02p` | VECTOR | The minimum of L or S above for 20-minute bucket |
| `nws12_mainz_02s` | VECTOR | Number of minutes that elapsed before price went down 20 percentage points |
| `nws12_mainz_10_min` | VECTOR | The percent change in price in the first 10 minutes following the news release |
| `nws12_mainz_120_min` | VECTOR | The percent change in price in the first 120 minutes following the news release |
| `nws12_mainz_1_minute` | VECTOR | The percent change in price in the first minute following the news release |
| `nws12_mainz_1l` | VECTOR | Number of minutes that elapsed before price went up 1 percentage point |
| `nws12_mainz_1p` | VECTOR | The minimum of L or S above for 1-minute bucket |
| `nws12_mainz_1s` | VECTOR | Number of minutes that elapsed before price went down 1 percentage point |
| `nws12_mainz_2l` | VECTOR | Number of minutes that elapsed before price went up 2 percentage points |
| `nws12_mainz_2p` | VECTOR | The minimum of L or S above for 2 minute bucket |
| `nws12_mainz_2s` | VECTOR | Number of minutes that elapsed before price went down 2 percentage points |
| `nws12_mainz_30_min` | VECTOR | The percent change in price in the first 30 minutes following the news release |
| `nws12_mainz_30_seconds` | VECTOR | The percent change in price in the 30 seconds following the news release |
| `nws12_mainz_3l` | VECTOR | Number of minutes that elapsed before price went up 3 percentage points |
| `nws12_mainz_3p` | VECTOR | The minimum of L or S above for 3-minute bucket |
| `nws12_mainz_3s` | VECTOR | Number of minutes that elapsed before price went down 3 percentage points |
| `nws12_mainz_41rta` | VECTOR | 14-day Average True Range |
| `nws12_mainz_4l` | VECTOR | Number of minutes that elapsed before price went up 4 percentage points |
| `nws12_mainz_4p` | VECTOR | The minimum of L or S above for 4 minute bucket |
| `nws12_mainz_4s` | VECTOR | Number of minutes that elapsed before price went down 4 percentage points |
| `nws12_mainz_57l` | VECTOR | Number of minutes that elapsed before price went up 7.5 percentage points |
| `nws12_mainz_57p` | VECTOR | The minimum of L or S above for 7.5-minute bucket |
| `nws12_mainz_57s` | VECTOR | Number of minutes that elapsed before price went down 7.5 percentage points |
| `nws12_mainz_5_min` | VECTOR | The percent change in price in the first 5 minutes following the news release |
| `nws12_mainz_5l` | VECTOR | Number of minutes that elapsed before price went up 5 percentage points |
| `nws12_mainz_5p` | VECTOR | The minimum of L or S above for 5-minute bucket |
| `nws12_mainz_5s` | VECTOR | Number of minutes that elapsed before price went down 5 percentage points |
| `nws12_mainz_60_min` | VECTOR | The percent change in price in the first 60 minutes following the news release |
| `nws12_mainz_90_min` | VECTOR | The percent change in price in the first 90 minutes following the news release |
| `nws12_mainz_allticks` | VECTOR | Total number of ticks for the trading day |
| `nws12_mainz_allvwap` | VECTOR | Volume weighted average price of all sessions |
| `nws12_mainz_atrratio` | VECTOR | Ratio of Today Range to 20-day average true range |
| `nws12_mainz_close_vol` | VECTOR | Main close volume |
| `nws12_mainz_curr_vol` | VECTOR | Current day's session volume |
| `nws12_mainz_dayopen` | VECTOR | Price at the session open |
| `nws12_mainz_div_y` | VECTOR | Annual yield |
| `nws12_mainz_eodclose` | VECTOR | Close price of the session |
| `nws12_mainz_eodhigh` | VECTOR | Highest price reached between the time of news and the end of the session |
| `nws12_mainz_eodlow` | VECTOR | Lowest price reached between the time of news and the end of the session. |
| `nws12_mainz_eodvwap` | VECTOR | Volume weighted average price between the time of news and the end of the session |
| `nws12_mainz_epsactual` | VECTOR | The actual Earnings Per Share value that was conveyed by the news release |
| `nws12_mainz_highexcstddev` | VECTOR | (EODHigh - TONLast)/StdDev, where StdDev is one standard deviation for the close price for 30 calendar days |
| `nws12_mainz_lowexcstddev` | VECTOR | (TONLast - EODLow)/StdDev, where StdDev is one standard deviation for the close price for 30 calendar days |
| `nws12_mainz_mainvwap` | VECTOR | Main session volume weighted average price |
| `nws12_mainz_maxdnamt` | VECTOR | The price at the time of the news minus the after the news low |
| `nws12_mainz_maxdown` | VECTOR | Percent change from the price at the time of the news to the after-the-news low |
| `nws12_mainz_maxup` | VECTOR | Percent change from the price at the time of the news to the after the news high |
| `nws12_mainz_maxupamt` | VECTOR | The after-the-news high minus the price at the time of the news |
| `nws12_mainz_mktcap` | VECTOR | Reported market capitalization for the calendar day of the session |
| `nws12_mainz_mov_vol` | VECTOR | 30-day moving average session volume |
| `nws12_mainz_newrecord` | VECTOR | Tracks whether the news is first instance or a duplicate |
| `nws12_mainz_newssess` | VECTOR | Index of session in which the news was reported |
| `nws12_mainz_open_vol` | VECTOR | Main open volume |
| `nws12_mainz_opengap` | VECTOR | (DayOpen - PrevClose) / PrevClose |
| `nws12_mainz_peratio` | VECTOR | Reported price-to-earnings ratio for the calendar day of the session |
| `nws12_mainz_postvwap` | VECTOR | Post session volume weighted average price |
| `nws12_mainz_prev_vol` | VECTOR | Previous day's session volume |
| `nws12_mainz_prevclose` | VECTOR | Previous trading day's close price |
| `nws12_mainz_prevday` | VECTOR | Percent change between the previous day's open and close |
| `nws12_mainz_prevwap` | VECTOR | Pre session volume weighted average price |
| `nws12_mainz_provider` | VECTOR | index of name of the news provider |
| `nws12_mainz_range` | VECTOR | Session High Price - Session Low Price) / Session Low Price. |
| `nws12_mainz_rangeamt` | VECTOR | Session High Price - Session Low Price |
| `nws12_mainz_rangestddev` | VECTOR | (RangeAmt-AvgRange)/RangeStdDev, where AvgRange is the average of the daily range, and RangeStdDev is one standard de… |
| `nws12_mainz_reportsess` | VECTOR | Index of Session on which the spreadsheet is reporting |
| `nws12_mainz_result1` | VECTOR | Percent change between the price at the time of the news release and the price at the close of the session |
| `nws12_mainz_result2` | VECTOR | Percent change between the price at the time of the news release to the price at the close of the session |
| `nws12_mainz_result_vs_index` | VECTOR | ((EODClose - TONLast) / TONLast) - ((SPYClose - SPYLast) / SPYLast) |
| `nws12_mainz_short_interest` | VECTOR | Total number of shares sold short divided by total number of shares outstanding |
| `nws12_mainz_sl` | VECTOR | Whether a long or short position would have been more advantageous: If (EODHigh - Last) > (Last - EODLow) Then LS = 1… |
| `nws12_mainz_spyclose` | VECTOR | Price of SPY at close of session |
| `nws12_mainz_spylast` | VECTOR | Last Price of the SPY at the time of the news |
| `nws12_mainz_tonhigh` | VECTOR | Highest price reached during the session before the time of news |
| `nws12_mainz_tonlast` | VECTOR | Price at the time of news |
| `nws12_mainz_tonlow` | VECTOR | Lowest price reached during the session before the time of the news |
| `nws12_mainz_vol_ratio` | VECTOR | Curr_Vol / Mov_Vol |
| `nws12_mainz_volstddev` | VECTOR | (CurrentVolume - AvgVol)/VolStDev, where AvgVol is the average of the daily volume, and VolStdDev is one standard dev… |
| `nws12_prez_01l` | VECTOR | Number of minutes that elapsed before price went up 10 percentage points |
| `nws12_prez_01p` | VECTOR | The minimum of L or S above for 10-minute bucket |
| `nws12_prez_01s` | VECTOR | Number of minutes that elapsed before price went down 10 percentage points |
| `nws12_prez_02l` | VECTOR | Number of minutes that elapsed before price went up 20 percentage points |
| `nws12_prez_02p` | VECTOR | The minimum of L or S above for 20-minute bucket |
| `nws12_prez_02s` | VECTOR | Number of minutes that elapsed before price went down 20 percentage points |
| `nws12_prez_10_min` | VECTOR | The percent change in price in the first 10 minutes following the news release |
| `nws12_prez_120_min` | VECTOR | The percent change in price in the first 120 minutes following the news release |
| `nws12_prez_1_minute` | VECTOR | The percent change in price in the first minute following the news release |
| `nws12_prez_1l` | VECTOR | Number of minutes that elapsed before price went up 1 percentage point |
| `nws12_prez_1p` | VECTOR | The minimum of L or S above for 1-minute bucket |
| `nws12_prez_1s` | VECTOR | Number of minutes that elapsed before price went down 1 percentage point |
| `nws12_prez_2l` | VECTOR | Number of minutes that elapsed before price went up 2 percentage points |
| `nws12_prez_2p` | VECTOR | The minimum of L or S above for 2-minute bucket |
| `nws12_prez_2s` | VECTOR | Number of minutes that elapsed before price went down 2 percentage points |
| `nws12_prez_30_min` | VECTOR | The percent change in price in the first 30 minutes following the news release |
| `nws12_prez_30_seconds` | VECTOR | The percent change in price in the 30 seconds following the news release |
| `nws12_prez_3l` | VECTOR | Number of minutes that elapsed before price went up 3 percentage points |
| `nws12_prez_3p` | VECTOR | The minimum of L or S above for 3-minute bucket |
| `nws12_prez_3s` | VECTOR | Number of minutes that elapsed before price went down 3 percentage points |
| `nws12_prez_41rta` | VECTOR | Fourteen-day Average True Range |
| `nws12_prez_4l` | VECTOR | Number of minutes that elapsed before price went up 4 percentage points |
| `nws12_prez_4p` | VECTOR | The minimum of L or S above for 4-minute bucket |
| `nws12_prez_4s` | VECTOR | Number of minutes that elapsed before price went down 4 percentage points |
| `nws12_prez_57l` | VECTOR | Number of minutes that elapsed before price went up 7.5 percentage points |
| `nws12_prez_57p` | VECTOR | The minimum of L or S above for 7.5-minute bucket |
| `nws12_prez_57s` | VECTOR | Number of minutes that elapsed before price went down 7.5 percentage points |
| `nws12_prez_5_min` | VECTOR | The percent change in price in the first 5 minutes following the news release |
| `nws12_prez_5l` | VECTOR | Number of minutes that elapsed before price went up 5 percentage points |
| `nws12_prez_5p` | VECTOR | The minimum of L or S above for 5-minute bucket |
| `nws12_prez_5s` | VECTOR | Number of minutes that elapsed before price went down 5 percentage points |
| `nws12_prez_60_min` | VECTOR | The percent change in price in the first 60 minutes following the news release |
| `nws12_prez_90_min` | VECTOR | The percent change in price in the first 90 minutes following the news release |
| `nws12_prez_allticks` | VECTOR | Total number of ticks for the trading day |
| `nws12_prez_allvwap` | VECTOR | Volume weighted average price of all sessions |
| `nws12_prez_atrratio` | VECTOR | Ratio of Today Range to 20-day average true range |
| `nws12_prez_close_vol` | VECTOR | Main close volume |
| `nws12_prez_curr_vol` | VECTOR | Current day's session volume |
| `nws12_prez_dayopen` | VECTOR | Price at the session open |
| `nws12_prez_div_y` | VECTOR | Annual yield |
| `nws12_prez_eodclose` | VECTOR | Close price of the session |
| `nws12_prez_eodhigh` | VECTOR | Highest price reached between the time of news and the end of the session |
| `nws12_prez_eodlow` | VECTOR | Lowest price reached between the time of news and the end of the session. |
| `nws12_prez_eodvwap` | VECTOR | Volume-weighted average price between the time of news and the end of the session |
| `nws12_prez_epsactual` | VECTOR | The actual Earnings Per Share value that was conveyed by the news release |
| `nws12_prez_highexcstddev` | VECTOR | (EODHigh - TONLast)/StdDev, where StdDev is one standard deviation for the close price for 30 calendar days |
| `nws12_prez_lowexcstddev` | VECTOR | (TONLast - EODLow)/StdDev, where StdDev is one standard deviation for the close price for 30 calendar days |
| `nws12_prez_mainvwap` | VECTOR | Main session volume-weighted average price |
| `nws12_prez_maxdnamt` | VECTOR | The price at the time of the news minus the after the news low |
| `nws12_prez_maxdown` | VECTOR | Percent change from the price at the time of the news to the after the news low |
| `nws12_prez_maxup` | VECTOR | Percent change from the price at the time of the news to the after the news high |
| `nws12_prez_maxupamt` | VECTOR | The after-the-news high minus the price at the time of the news |
| `nws12_prez_mktcap` | VECTOR | Reported market capitalization for the calendar day of the session |
| `nws12_prez_mov_vol` | VECTOR | 30-day moving average session volume |
| `nws12_prez_newrecord` | VECTOR | Tracks whether the news is the first instance or a duplicate |
| `nws12_prez_newssess` | VECTOR | Index of session in which the news was reported |
| `nws12_prez_open_vol` | VECTOR | Main open volume |
| `nws12_prez_opengap` | VECTOR | (DayOpen - PrevClose) / PrevClose. |
| `nws12_prez_peratio` | VECTOR | Reported price to earnings ratio for the calendar day of the session |
| `nws12_prez_postvwap` | VECTOR | Post-session volume-weighted average price |
| `nws12_prez_prev_vol` | VECTOR | Previous day's session volume |
| `nws12_prez_prevclose` | VECTOR | Previous trading day's close price |
| `nws12_prez_prevday` | VECTOR | Percent change between the previous day's open and close |
| `nws12_prez_prevwap` | VECTOR | Pre-session volume weighted average price |
| `nws12_prez_provider` | VECTOR | index of name of the news provider |
| `nws12_prez_range` | VECTOR | Session High Price - Session Low Price) / Session Low Price. |
| `nws12_prez_rangeamt` | VECTOR | Session High Price - Session Low Price |
| `nws12_prez_rangestddev` | VECTOR | (RangeAmt-AvgRange)/RangeStdDev, where AvgRange is the average of the daily range, and RangeStdDev is one standard de… |
| `nws12_prez_reportsess` | VECTOR | Index of Session on which the spreadsheet is reporting |
| `nws12_prez_result1` | VECTOR | Percent change between the price at the time of the news release to the price at the close of the session |
| `nws12_prez_result2` | VECTOR | Percent change between the price at the time of the news release to the price at the close of the session |
| `nws12_prez_result_vs_index` | VECTOR | ((EODClose - TONLast) / TONLast) - ((SPYClose - SPYLast) / SPYLast) |
| `nws12_prez_short_interest` | VECTOR | Total number of shares sold short divided by total number of shares outstanding |
| `nws12_prez_sl` | VECTOR | Whether a long or short position would have been more advantageous: If (EODHigh - Last) > (Last - EODLow) Then LS = 1… |
| `nws12_prez_spyclose` | VECTOR | Price of SPY at the close of the session |
| `nws12_prez_spylast` | VECTOR | Last Price of the SPY at the time of the news |
| `nws12_prez_tonhigh` | VECTOR | Highest price reached during the session before the time of the news |
| `nws12_prez_tonlast` | VECTOR | Price at the time of news |
| `nws12_prez_tonlow` | VECTOR | Lowest price reached during the session before the time of the news |
| `nws12_prez_vol_ratio` | VECTOR | Curr_Vol / Mov_Vol |
| `nws12_prez_volstddev` | VECTOR | (CurrentVolume - AvgVol)/VolStDev, where AvgVol is the average of the daily volume, and VolStdDev is one standard dev… |
| `one_minute_price_change_pct` | VECTOR | Percent price change in the first minute after news release. |
| `one_minute_price_change_pct_2` | VECTOR | Return or analytic for the first one-minute interval post-event |
| `one_minute_price_change_pct_all` | VECTOR | Analytics/statistics from the last 1 minute interval in the session |
| `one_minute_price_change_percent` | VECTOR | Percent price change in the first minute after news release. |
| `one_minute_price_change_percent_2` | VECTOR | Return, price, or analytic data for the 1 minute after the news event |
| `onehundredtwenty_minute_price_change_pct` | VECTOR | Percent price change in the first one hundred twenty minutes after news release. |
| `open_gap_percent` | VECTOR | The difference in price between the current day's open and the previous close (gap up or gap down) for the event day,… |
| `opening_gap_percent` | VECTOR | Percentage gap between market open price and previous close, i.e. (DayOpen - PrevClose)/PrevClose |
| `opening_gap_percent_2` | VECTOR | Percentage change from previous close to current open ((DayOpen - PrevClose) / PrevClose) |
| `opening_gap_percent_3` | VECTOR | (DayOpen - PrevClose) / PrevClose, percent gap at open |
| `opening_gap_percent_3_1555` | VECTOR | The percentage difference between the day's opening price and the previous day's closing price |
| `opening_price_gap_percent` | VECTOR | Price gap between market open and previous close for filter module on Day 1 |
| `opening_price_of_day_2` | VECTOR | Price at the session open |
| `opening_price_of_day_filter` | VECTOR | Opening price for the session on event day |
| `opening_session_volume_count` | VECTOR | Opening session trading volume |
| `opening_session_volume_pre` | VECTOR | Volume traded at the session open |
| `opening_volume` | VECTOR | Trading volume at the opening of the main session |
| `optimal_position_indicator` | VECTOR | Whether a long or short position would have been more advantageous; 1 = long, 0 = neutral, -1 = short |
| `pct_change_10m_post_news` | VECTOR | Percent price change in the 10 minutes after news release. |
| `pct_change_10min_post_news` | VECTOR | Return or price change in the 10 minutes after the news in after-hours Day 1 |
| `pct_change_120m_post_news` | VECTOR | Calculated analytics for the 120-minute window following the event/news for event day (D1), "All" session |
| `pct_change_120min_post_news` | VECTOR | Return or price change in the 120 minutes after the news in after-hours Day 1 |
| `pct_change_1m_post_news` | VECTOR | Price, return, or metric measured over the 1-minute window after the event |
| `pct_change_1min_post_news_filter` | VECTOR | Percent price change in the first minute after news release (filtered). |
| `pct_change_30m_post_news` | VECTOR | Percent price change in the 30 minutes after news release. |
| `pct_change_30min_post_news_filter` | VECTOR | Percent price change in the first 30 minutes after news release (filtered). |
| `pct_change_30s_post_news` | VECTOR | Percent price change in the 30 seconds after news release. |
| `pct_change_5m_post_news` | VECTOR | Price, return, or related metric measured over the 5-minute window after the event |
| `pct_change_5min_post_news` | VECTOR | Return or price change in the 5 minutes after the news in after-hours Day 1 |
| `pct_change_60m_post_news` | VECTOR | Calculated analytics over the 60-minute window following the event/news on event day, "All" session |
| `pct_change_60min_post_news_filter` | VECTOR | Percent price change in the first 60 minutes after news release (filtered). |
| `pct_change_90m_post_news` | VECTOR | Percent price change in the 90 minutes after news release. |
| `pct_change_first_minute_post_news_1555` | VECTOR | Percent price change in the first minute after a news event. |
| `pct_change_five_minute_post_news_1555` | VECTOR | Percent price change in the first five minutes following a news release. |
| `pct_change_ninety_minute_post_news_1555` | VECTOR | Percent price change in the first ninety minutes after a news release. |
| `pct_change_one_twenty_minute_post_news_1555` | VECTOR | Percent price change in the first 120 minutes after a news event. |
| `pct_change_sixty_minute_post_news_1555` | VECTOR | Percent price change in the first sixty minutes after a news event. |
| `pct_change_ten_minute_post_news_1555` | VECTOR | Percent price change in the first ten minutes after a news event. |
| `pct_change_thirty_minute_post_news_1555` | VECTOR | Percent price change in the first thirty minutes after a news release. |
| `percent_price_change_120_minutes_post_news` | VECTOR | Analytics/statistics from the last 120 minutes interval in the session |
| `percent_price_change_30_seconds_post_news` | VECTOR | Price or return data over the last 30 seconds on day 1 in 'All Filter' module |
| `percent_price_change_90_minutes_post_news` | VECTOR | Percent change in price during the 90 minutes after the news release. |
| `performance_vs_benchmark` | VECTOR | Difference in stock move/return compared to market benchmark index (e.g., SPY) for the session |
| `performance_vs_benchmark_pre` | VECTOR | Difference between the stock’s return from news to end-of-day and the SPY index return in the same period |
| `position_advantage_flag` | VECTOR | Indicator showing whether long or short position would have been more advantageous |
| `pre_event_high_price` | VECTOR | Highest price achieved during the session before the time the news was released on Day 1 after-hours |
| `pre_event_low_price` | VECTOR | Lowest price reached during session before the news event |
| `pre_market_vwap_2` | VECTOR | Volume Weighted Average Price prior to the event window (pre-trade or pre-market) for the record on event day, "All" … |
| `pre_market_vwap_3` | VECTOR | Volume-weighted average price for trades before the news event in the pre-market session |
| `pre_news_high_price` | VECTOR | Highest price reached during the session before the time of news |
| `pre_news_high_price_afterhours` | VECTOR | Highest price reached during the session before the time of news |
| `pre_news_low_price` | VECTOR | Lowest price reached before the time of the news during the session |
| `pre_news_session_high` | VECTOR | Highest price reached during the session before the time of news |
| `pre_news_session_high_price` | VECTOR | Highest price reached before the time of the news event. |
| `pre_news_session_low` | VECTOR | Lowest price reached during the session before the time of the news |
| `pre_session_closing_price` | VECTOR | Close price of the session |
| `pre_session_range_to_atr_ratio` | VECTOR | Ratio of pre-market session price range to 20-day average true range. |
| `pre_session_vwap_all` | VECTOR | Pre-market Volume Weighted Average Price for the session |
| `premarket_volume_weighted_avg_price` | VECTOR | Volume Weighted Average Price before the session begins |
| `prev_day_open_close_pct_change` | VECTOR | Percent change between the previous day's open and close prices |
| `prev_day_pct_change` | VECTOR | Previous day's price, volume, or related metric for contextual comparison |
| `previous_close_price` | VECTOR | Previous day’s closing price of the security |
| `previous_closing_price_2` | VECTOR | Previous trading day’s closing price |
| `previous_closing_price_3` | VECTOR | Previous trading day's close price |
| `previous_closing_price_3_1555` | VECTOR | Previous trading day's closing price |
| `previous_closing_price_value` | VECTOR | Closing price of the previous trading day |
| `previous_day_open_close_change_pct` | VECTOR | Percent price change between the previous day's open and close |
| `previous_day_open_close_change_pct_all` | VECTOR | Value (price or volume) from the previous day in the session |
| `previous_day_percent_change` | VECTOR | Percent change between the previous day's open and close |
| `previous_day_percent_change_2_1555` | VECTOR | Percent change between previous day's open and close price |
| `previous_day_price_change_percent` | VECTOR | Percent change between the previous day's open and close |
| `previous_day_trading_volume` | VECTOR | Trading volume of the previous trading session/day for the relevant stock |
| `previous_day_trading_volume_2` | VECTOR | Previous day's session volume |
| `previous_day_trading_volume_3` | VECTOR | Previous day's trading volume for the asset in the session |
| `previous_day_volume` | VECTOR | Previous day’s trading volume for the security |
| `previous_day_volume_2` | VECTOR | Previous day's session trading volume |
| `previous_day_volume_2_1555` | VECTOR | Trading volume for the previous day's session |
| `previous_day_volume_count` | VECTOR | Trading volume of the previous day’s main session |
| `previous_session_closing_price` | VECTOR | Previous day's closing price for the stock in day 1 'All Filter' |
| `price_at_event_time` | VECTOR | Price of the stock at the exact time the news was released in the after-hours session, Day 1 |
| `price_at_event_time_pre` | VECTOR | Price at the time of news |
| `price_at_news_time` | VECTOR | Price at the time of news release. |
| `price_at_news_time_2` | VECTOR | Price at the time of news |
| `price_at_news_time_4_1555` | VECTOR | Price at the time of the news event arrival |
| `price_at_time_of_news_release` | VECTOR | Last value for Time Of News (TON), e.g., last traded price or technical objective at event time |
| `price_earnings_ratio` | VECTOR | Price-to-Earnings Ratio for the equity on Day 1 |
| `price_earnings_ratio_pre_session` | VECTOR | Reported price-to-earnings ratio for the stock for the calendar day of the pre-market session |
| `price_range_deviation_std_1555` | VECTOR | Z-score of session’s price range compared to 30-day historical average and standard deviation |
| `price_range_standard_deviation_2` | VECTOR | Standard deviation of the price range (high-low variation) for the event day (D1), "All" session |
| `price_range_standard_deviation_3` | VECTOR | Standard deviation of price range for the session. |
| `price_range_standard_deviation_4` | VECTOR | (RangeAmt minus average range) divided by the standard deviation of daily range over the previous 30 calendar days fo… |
| `price_to_earnings_ratio_3` | VECTOR | Reported price-to-earnings ratio for the calendar day of the session |
| `price_to_earnings_ratio_4` | VECTOR | Reported price to earnings ratio for the calendar day of After Hours Day 1 session |
| `price_to_earnings_ratio_5` | VECTOR | Price-to-earnings ratio reported for the stock on the calendar day of the after-hours session, Day 1 |
| `price_to_earnings_ratio_6` | VECTOR | Price-to-earnings ratio for the entity/event in filter module on Day 1 |
| `price_to_earnings_ratio_value` | VECTOR | Price-to-earnings ratio for the session day |
| `primary_price_change_pct` | VECTOR | First result field for percent price change after news. |
| `primary_price_change_percent_1555` | VECTOR | Percent change in price from news release to session close (primary measure). |
| `primary_result_value` | VECTOR | First result or outcome value for the session. |
| `prior_closing_price_2` | VECTOR | Previous trading day's close price |
| `prior_day_closing_price` | VECTOR | Previous trading day's closing price |
| `prior_day_open_close_change_pct` | VECTOR | Percent change between previous day's open and close |
| `prior_day_open_close_pct_change` | VECTOR | Percent change between previous day's open and previous day's close |
| `prior_day_trading_volume` | VECTOR | Previous day's session trading volume |
| `range_to_atr20_ratio` | VECTOR | Ratio of today's price range to 20-day average true range. |
| `range_to_atr_ratio` | VECTOR | Ratio of today’s price range to 20-day average true range. |
| `range_to_atr_ratio_2` | VECTOR | Ratio of today's price range to 20-day average true range. |
| `relative_performance_vs_benchmark_1555` | VECTOR | Stock price change relative to market index change (SPY) from time of news to end of day |
| `result_value_1` | VECTOR | First result or outcome value for the record. |
| `result_value_2` | VECTOR | Second result or outcome value for the record. |
| `second_minimum_gain_loss_time` | VECTOR | The minimum elapsed time among upward or downward moves (L or S) for the 2 minute bucket after the event in the pre-m… |
| `secondary_price_change_pct` | VECTOR | Second result field for percent price change after news. |
| `secondary_price_change_percent` | VECTOR | Percent change in price from news release to session close (secondary measure). |
| `secondary_price_change_percent_2_1555` | VECTOR | Percent change in price from news release to session close (secondary measure). |
| `secondary_result_value` | VECTOR | Second result or outcome value for the session. |
| `session_closing_price` | VECTOR | Close price of the session |
| `session_closing_price_3` | VECTOR | Price at the close of the after-hours session, Day 1 |
| `session_closing_price_4_1555` | VECTOR | Closing price for the stock at the end of the session |
| `session_high_after_news` | VECTOR | Session high price from time of news until end of market session |
| `session_high_low_price_difference` | VECTOR | High-low price range during the filter period on Day 1 |
| `session_high_post_event` | VECTOR | Highest price reached between news time and end of session |
| `session_high_post_news` | VECTOR | Highest price reached between the time of news and the session end |
| `session_high_post_news_2_1555` | VECTOR | Highest price reached between the time of news and end of session |
| `session_low_after_news` | VECTOR | Lowest price reached between the time of news and the end of the session |
| `session_low_post_event` | VECTOR | Lowest price reached in the period from time of news until the end of the after-hours session, Day 1 |
| `session_low_post_news` | VECTOR | Lowest price reached between the time of news and the session end |
| `session_low_post_news_2_1555` | VECTOR | Lowest price from the time of news until the end of session |
| `session_open_gap_pct` | VECTOR | Percentage difference between session open price and previous close, calculated as (DayOpen - PrevClose) / PrevClose |
| `session_open_gap_pct_filter` | VECTOR | Percent gap between the session opening price and previous closing price |
| `session_open_price` | VECTOR | Opening price of the security on Day 1 |
| `session_open_price_all` | VECTOR | Opening price (or volume) for the day in the session |
| `session_opening_price` | VECTOR | Price at the session open |
| `session_opening_price_2` | VECTOR | Opening price at the start of the session |
| `session_opening_price_3` | VECTOR | Price at the session open |
| `session_opening_price_3_1555` | VECTOR | Opening price of the session |
| `session_opening_price_4` | VECTOR | Opening price at the start of the main trading session on Day 1 |
| `session_opening_volume` | VECTOR | Trading volume during opening period in filter module on Day 1 |
| `session_price_range_2` | VECTOR | The absolute price range (difference between high and low) for the event day (D1) in the "All" session |
| `session_price_range_3` | VECTOR | (Session high price minus session low price) divided by session low price, for the after-hours session, Day 1 |
| `session_price_range_4` | VECTOR | Relative difference between session high and session low expressed as (High - Low) / Low |
| `session_price_range_4_1555` | VECTOR | (Session High Price - Session Low Price) / Session Low Price, representing the relative price range for the session |
| `session_price_range_amount_2` | VECTOR | Difference between session high and session low price (range for the session) |
| `session_price_range_amount_3` | VECTOR | Difference between session’s high and low prices (session high - session low) |
| `session_price_range_amt` | VECTOR | Intraday price range (difference between high and low prices during the session) |
| `session_price_range_amt_2` | VECTOR | Session high price minus session low price in after-hours Day 1 |
| `session_price_range_pct` | VECTOR | (Session high price minus session low price) divided by session low price |
| `session_price_range_percent` | VECTOR | (Session High Price – Session Low Price) / Session Low Price; relative price range for the session |
| `session_price_range_value` | VECTOR | (Session High Price - Session Low Price) divided by Session Low Price for main session |
| `session_price_range_value_2` | VECTOR | Price high-low range amount for day 1 in 'All Filter' |
| `session_range_amount` | VECTOR | Difference between session high and low price |
| `session_range_amount_2` | VECTOR | Difference between session high and session low price |
| `session_range_amount_3` | VECTOR | Difference between the session's high price and session's low price |
| `session_range_amount_3_1555` | VECTOR | Difference between the session’s high price and session’s low price |
| `session_range_standard_deviation` | VECTOR | Z-score of session range, standardized against last 30 days |
| `session_range_standard_deviation_2` | VECTOR | Standard deviation of price range for the session, measures volatility |
| `session_range_to_atr_ratio` | VECTOR | Ratio of today's price range to twenty-day average true range. |
| `session_range_to_atr_ratio_2` | VECTOR | Ratio of post-event price movement to historical 14-day average true range in the after-hours session, Day 1 |
| `session_range_to_atr_ratio_3_1555` | VECTOR | Ratio of session price range to 20-day average true range. |
| `session_range_to_atr_ratio_4` | VECTOR | Ratio of the average true range (volatility measure) to a benchmark (likely price), for Day 1 filter module |
| `share_price_to_earnings_ratio_1555` | VECTOR | Price-to-Earnings ratio for the calendar day/session |
| `shares_sold_short` | VECTOR | Most recent short interest ratio for the stock on Day 1 |
| `shares_sold_short_count` | VECTOR | Short interest data, likely the ratio or number of shares shorted for the stock |
| `shares_sold_short_count_2` | VECTOR | Number of shares sold short divided by average daily trading volume (short interest ratio) |
| `shares_sold_short_count_3` | VECTOR | Short interest ratio or value as of After Hours Day 1 |
| `shares_sold_short_count_4` | VECTOR | Number of shares sold short for the security. |
| `shares_sold_short_count_5_1555` | VECTOR | Ratio of shares sold short to average daily trading volume |
| `shares_sold_short_count_6` | VECTOR | Short interest ratio for the stock during Day 1 |
| `short_position_count` | VECTOR | Short interest ratio (number of shares shorted divided by average daily volume) for the stock on the event day during… |
| `shorted_shares_count_all` | VECTOR | Short interest ratio (shares shorted relative to volume) for day 1 in 'All Filter' |
| `sixty_minute_price_change_pct` | VECTOR | Percent price change in the first sixty minutes after news release. |
| `sixty_minute_price_change_pct_2` | VECTOR | Price or return data over the last 60 minutes on day 1 in 'All Filter' module |
| `sixty_minute_price_change_pct_pre` | VECTOR | Return, price, or analytic data for the 60 minutes after the news event |
| `sixty_minute_price_change_percent` | VECTOR | Percent price change in the first sixty minutes after news release. |
| `spy_etf_close_price` | VECTOR | Closing price of SPY ETF (S&P 500 benchmark), used as market proxy on Day 1 |
| `spy_etf_closing_price` | VECTOR | Price of SPY ETF at close of session |
| `spy_etf_closing_price_2` | VECTOR | Closing price of the SPY ETF (S&P 500) for the after-hours Day 1 session |
| `spy_etf_closing_price_3` | VECTOR | Closing price of the SPY (S&P 500 ETF) at the end of the after-hours session, Day 1 |
| `spy_etf_closing_price_4` | VECTOR | Closing price of SPY ETF for the session |
| `spy_etf_closing_price_4_1555` | VECTOR | Closing price of SPY ETF (market benchmark) during the session |
| `spy_etf_closing_price_5` | VECTOR | Closing price of SPY ETF (S&P 500 proxy) for the session |
| `spy_etf_closing_price_value` | VECTOR | Closing price of SPY ETF in the main session |
| `spy_etf_last_price` | VECTOR | Last traded price of SPY ETF (S&P 500) used as market proxy on Day 1 |
| `spy_etf_last_price_2` | VECTOR | Last traded price for the SPY ETF (S&P 500 index proxy) at the time of the news event |
| `spy_etf_last_price_3` | VECTOR | Last traded price of SPY (S&P 500 ETF) at the moment the news was published in after-hours, Day 1 |
| `spy_etf_last_price_4` | VECTOR | Last price of the SPY ETF at the time of the news |
| `spy_etf_last_price_4_1555` | VECTOR | Last traded price of the SPY ETF at the time of the news |
| `spy_etf_last_price_all` | VECTOR | Last traded price of SPY ETF for day 1 in 'All Filter' |
| `spy_etf_last_trade_price` | VECTOR | Last price of SPY ETF at the moment the news was reported |
| `spy_etf_last_trade_price_3` | VECTOR | Last Price of the SPY at the time of the news |
| `spy_etf_session_close_price` | VECTOR | Closing price of SPY ETF (S&P 500 proxy) for day 1 in 'All Filter' |
| `stddev_of_session_price_range` | VECTOR | (RangeAmt-AvgRange)/RangeStdDev, price range deviation versus 30-day average and standard deviation for After Hours D… |
| `stddev_of_session_price_range_filter` | VECTOR | (RangeAmt-AvgRange)/RangeStdDev where AvgRange is the average daily range and RangeStdDev is one standard deviation o… |
| `stddev_of_trading_volume` | VECTOR | (CurrentVolume - AvgVol)/VolStDev, volume deviation versus 30-day average and standard deviation |
| `stddev_of_trading_volume_filter` | VECTOR | Z-score of current volume vs. 30-day average daily volume and its standard deviation |
| `ten_minute_price_change_pct` | VECTOR | Percent price change in the first ten minutes after news release. |
| `ten_minute_price_change_pct_2` | VECTOR | Percent change in price during the first ten minutes after event. |
| `ten_minute_price_change_pct_3` | VECTOR | Percent price change in the first ten minutes after the event. |
| `ten_minute_price_change_percent` | VECTOR | Percent price change in the first ten minutes after news release. |
| `ten_minute_price_change_percent_2` | VECTOR | Return, price, or analytic data for the 10 minutes after the news event |
| `third_minimum_gain_loss_time` | VECTOR | The minimum elapsed time among upward or downward moves (L or S) for the 3 minute bucket after the event in the pre-m… |
| `thirty_day_moving_average_volume` | VECTOR | 30-day moving average of session trading volume |
| `thirty_day_moving_average_volume_2` | VECTOR | 30-day moving average session volume |
| `thirty_day_moving_average_volume_3` | VECTOR | Change or movement in trading volume during the filter period on Day 1 |
| `thirty_day_moving_average_volume_afterhours` | VECTOR | 30-day moving average of session volume |
| `thirty_day_moving_avg_volume` | VECTOR | 30-day moving average of trading volume. |
| `thirty_day_moving_avg_volume_2` | VECTOR | 30 day moving average session volume |
| `thirty_day_moving_avg_volume_filter` | VECTOR | Moving average of session volume over the previous 30 days |
| `thirty_day_moving_volume` | VECTOR | 30-day moving average session volume |
| `thirty_day_moving_volume_2_1555` | VECTOR | 30-day moving average of session volume |
| `thirty_minute_price_change_pct` | VECTOR | Percent price change in the first thirty minutes after news release. |
| `thirty_minute_price_change_pct_all` | VECTOR | Analytics/statistics from the last 30 minute interval in the session |
| `thirty_minute_price_change_percent` | VECTOR | Return, price, or analytic data for the 30 minutes after the news event |
| `thirty_minute_price_change_percent_afterhours` | VECTOR | Return or price change in the 30 minutes after the news in after-hours Day 1 |
| `thirty_second_price_change_pct` | VECTOR | Percent price change in the thirty seconds after news release. |
| `thirty_second_price_change_pct_2` | VECTOR | Percent change in price during the first thirty seconds after event. |
| `thirty_second_price_change_pct_3` | VECTOR | Percent price change in the thirty seconds after the event. |
| `thirty_second_price_change_pct_pre` | VECTOR | Return, price, or analytic data for the 30 seconds after the news event |
| `thirty_second_price_change_percent` | VECTOR | Return or price metric for 30-second interval after the news event |
| `thirty_second_price_change_percent_2_1555` | VECTOR | Percent price change in the thirty seconds after news release. |
| `total_tick_count` | VECTOR | Total number of recorded trade ticks for the data session/event |
| `total_tick_count_2` | VECTOR | Total number of trade ticks recorded during the trading day |
| `total_tick_count_3` | VECTOR | Total number of trade ticks for the trading day |
| `total_tick_count_4_1555` | VECTOR | Total number of tick trades for that trading day |
| `total_tick_count_for_day_2` | VECTOR | Total number of trades (ticks) for the trading day |
| `total_tick_count_for_session` | VECTOR | Total trade tick count on day 1 in 'All Filter' module |
| `total_tick_count_pre` | VECTOR | Total number of trade ticks for the trading day |
| `trading_volume_deviation_std_1555` | VECTOR | (Current session volume - 30 day average volume) / standard deviation of volume over 30 days |
| `trading_volume_standard_deviation_2` | VECTOR | Z-score of current session volume relative to 30-day average and standard deviation |
| `trading_volume_standard_deviation_3` | VECTOR | Standard deviation of trading volume over the filter period on Day 1 |
| `two_hour_price_change_percent` | VECTOR | Price or return analytics for a 120-minute window after the news event |
| `volume_at_close` | VECTOR | Total trade volume at the end of the session/day (close volume) for the relevant security on event day, "All" session |
| `volume_at_market_open_1555` | VECTOR | Trading volume at the main session’s market open |
| `volume_at_open` | VECTOR | Trading volume at market open. |
| `volume_at_session_close_2` | VECTOR | Volume traded at session close |
| `volume_at_session_close_2_1555` | VECTOR | Trading volume at session close |
| `volume_standard_deviation` | VECTOR | Standard deviation of trading volume following the event on Day 1 |
| `volume_standard_deviation_2` | VECTOR | (CurrentVolume minus average volume) divided by the standard deviation of daily volume over the previous 30 calendar … |
| `volume_to_moving_average_ratio` | VECTOR | Current session trading volume divided by a reference or moving average volume (Curr_Vol / Mov_Vol) |
| `volume_to_moving_avg_ratio` | VECTOR | Trading volume ratio relative to a baseline or prior period in the session |
| `vwap_after_hours` | VECTOR | Post session volume weighted average price |
| `vwap_after_session` | VECTOR | Volume weighted average price after the session following news in after-hours Day 1 |
| `vwap_all_sessions` | VECTOR | Volume weighted average price of all sessions combined |
| `vwap_all_sessions_4_1555` | VECTOR | Volume-weighted average price across all trading sessions on event day |
| `vwap_all_sessions_pre` | VECTOR | Volume-weighted average price for trades across all time periods within the session |
| `vwap_from_news_to_close` | VECTOR | Volume-weighted average price from the time of the news event to the end of the session |
| `vwap_from_news_to_close_2_1555` | VECTOR | Volume-weighted average price from news event time to end of session |
| `vwap_from_news_to_session_end` | VECTOR | Volume-weighted average price from the time of news until session end |
| `vwap_main_session_1555` | VECTOR | Volume-weighted average price during main market session |
| `vwap_post_event_to_close` | VECTOR | Volume-weighted average price from the time of news through end of the after-hours session, Day 1 |
| `vwap_post_session` | VECTOR | Volume-weighted average price for trades after the news event in the pre-market session |
| `vwap_post_session_2_1555` | VECTOR | Volume-weighted average price for post-session trading |
| `vwap_pre_market` | VECTOR | Volume weighted average price in the pre-market session |
| `vwap_pre_session_1555` | VECTOR | Volume-weighted average price during pre-market session |

## 用法提示（人工补充）

- TODO：典型组合方式、相关的 concept 页面
