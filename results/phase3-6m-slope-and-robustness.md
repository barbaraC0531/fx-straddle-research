# Phase 3: 6M IV slope and robustness

The additional Bloomberg history permits a prespecified test of the implied-volatility term structure. The signal is

`TSIV = midpoint(6M ATM IV bid, ask) - midpoint(1M ATM IV bid, ask)`.

Zhang, So and Driouchi (2024) define the same six-minus-one-month characteristic and report a positive relation with subsequent FX straddle returns. The direction was therefore fixed before calculating our returns: buy the two highest slopes and sell the two lowest slopes. The test keeps the existing one-month straddle pricing, two positions per side, USD 250 vega per position, option bid-ask execution, initial forward delta hedge and premium financing. Quotes must be synchronized, no more than five calendar days old, numeric and ordered bid less than or equal to ask. Missing observations are not filled.

## TSIV results

Every TSIV row is compared with raw IV on exactly the same months. The difference test is monthly TSIV net P&L minus matched raw-IV net P&L with Bartlett HAC(4) standard errors. The development q-values apply Benjamini-Hochberg adjustment across the four universe comparisons.

| Universe | Window | Months | TSIV P&L | TSIV Sharpe | Matched IV P&L | Matched IV Sharpe | Difference | HAC p-value | Development q-value |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Original six | 2005-2015 | 130 | $64,036 | 0.42 | $106,082 | 0.74 | -$42,046 | 0.369 | 0.779 |
| Paper nine | 2005-2015 | 123 | $52,318 | 0.38 | $50,158 | 0.36 | $2,160 | 0.959 | 0.959 |
| G10 excluding USD | 2005-2015 | 130 | $54,648 | 0.38 | $28,122 | 0.19 | $26,525 | 0.584 | 0.779 |
| Paper nine plus MXN and HKD | 2005-2015 | 123 | $62,354 | 0.44 | $89,155 | 0.61 | -$26,801 | 0.544 | 0.779 |
| Original six | 2016-2025 | 120 | -$1,640 | -0.01 | $1,013 | 0.01 | -$2,652 | 0.958 | |
| Paper nine | 2016-2025 | 120 | -$22,406 | -0.19 | $17,483 | 0.16 | -$39,889 | 0.296 | |
| G10 excluding USD | 2016-2025 | 120 | -$4,498 | -0.04 | $19,184 | 0.17 | -$23,682 | 0.543 | |
| Paper nine plus MXN and HKD | 2016-2025 | 120 | -$22,502 | -0.18 | $20,274 | 0.16 | -$42,776 | 0.346 | |

TSIV earned positive development P&L in every universe, but it did not significantly improve on raw IV. In the previously inspected 2016-2025 period, all four TSIV portfolios had negative point estimates while the matched raw-IV portfolios were positive. The slope test therefore does not rescue the strategy's later performance.

The synchronized signal rule omits January 2006 because USDCHF lacks a valid matched 1M/6M quote. The DKK universes also omit February-March 2005 and January-May 2011. No observation is substituted or filled. The later period had already been inspected for the baseline and is not an untouched holdout.

## Raw-IV universe comparisons on common months

All four universes share 123 development months and 120 later months. On these identical dates, breadth does not overturn the earlier conclusion.

| Universe | Development P&L | Development Sharpe | Later P&L | Later Sharpe |
| --- | ---: | ---: | ---: | ---: |
| Original six | $105,273 | 0.76 | $1,013 | 0.01 |
| Paper nine | $50,158 | 0.36 | $17,483 | 0.16 |
| G10 excluding USD | $27,171 | 0.19 | $19,184 | 0.17 |
| Paper nine plus MXN and HKD | $89,155 | 0.61 | $20,274 | 0.16 |

No later-period pairwise universe difference is significant. Two unadjusted development comparisons are close to 5%: original six minus G10 has p = 0.050, and G10 minus the eleven-currency universe has p = 0.042. Both have q = 0.150 across the six pairwise comparisons and therefore do not survive the stated multiplicity adjustment.

## Currency concentration

- MXN supplied $79,404 of the original-six development P&L and 61.3% of absolute currency contributions.
- In the eleven-currency development universe, MXN supplied $60,226 and 44.9% of absolute currency contributions.
- The largest development contributor was NOK in paper nine at $41,262 and in G10 excluding USD at $29,757.
- Broader universes reduced the selection and P&L concentration measures, but did not eliminate economically important single-currency exposure.

## Additional-cost breakevens

The table converts positive raw-IV P&L into an average extra one-month execution cost, expressed in implied-volatility points per USD 250-vega trade. It is an equivalent cost threshold, not an observed market quote.

| Universe | Development breakeven vol points | Later breakeven vol points | Later annual drag on $1m capital |
| --- | ---: | ---: | ---: |
| Original six | 0.794 | 0.008 | 0.01% |
| Paper nine | 0.408 | 0.146 | 0.17% |
| G10 excluding USD | 0.223 | 0.160 | 0.19% |
| Paper nine plus MXN and HKD | 0.725 | 0.169 | 0.20% |

The original-six later result is especially fragile: an average additional cost of about $2.11 per selected trade, or 0.008 volatility points at the fixed vega, removes its $1,013 later profit. Forward-cost equivalents are calculated on the small initial delta-hedge notional and should not be read as full-notional FX bid-ask spreads.

## Interpretation

The evidence supports an analysis of why a published cross-sectional FX options effect weakened rather than a claim that a new signal restored strong profitability. The defensible final presentation is:

1. raw IV was profitable in development but weakened sharply after 2015;
2. broader fixed universes produced small positive later point estimates, without significant common-month improvements;
3. the prespecified 6M-minus-1M slope did not improve raw IV and was negative in all later samples;
4. currency concentration and small cost breakevens limit the economic strength of the results.

The repository publishes only derived results. It excludes Bloomberg quote histories, values-only workbooks, terminal screenshots and personal paths.

## Derived data

- [TSIV strategy summaries](../data/phase3_6m_slope_strategy_summary.csv)
- [TSIV paired inference](../data/phase3_6m_slope_paired_comparisons.csv)
- [TSIV monthly paired P&L](../data/phase3_6m_slope_monthly_pnl.csv)
- [Common-month universe summaries](../data/phase3_common_month_summary.csv)
- [Common-month paired universe inference](../data/phase3_common_month_paired_comparisons.csv)
- [Currency concentration](../data/phase3_currency_concentration_summary.csv)
- [Cost breakevens](../data/phase3_cost_breakevens.csv)
