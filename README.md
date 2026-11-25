# What does momentum buy in FX options?

This study compares three ways to select one-month currency straddles. Each month we buy two straddles and sell two others. We rank six USD pairs by implied volatility (IV), past straddle returns, or the width of the IV bid–ask spread.

**Low-IV straddles earned the strongest net P&L during development.** Momentum winners subsequently paid more at expiry than losers on average, but their entry premiums were higher still. The raw-IV strategy also earned very little in the later period, which matters when interpreting its early lead.

![Cumulative net P&L of the IV, momentum and illiquidity portfolios from December 2005 through December 2015](figures/cumulative-pnl.svg)

## Results on the same 121 months

All three signals were available from December 2005 through December 2015, measured by expiry. P&L is in USD after modeled option bid–ask execution and premium financing. Each portfolio uses the same USD vega budget.

| Monthly sort | Buy | Sell | Cumulative net P&L | Annualized Sharpe |
| --- | --- | --- | ---: | ---: |
| Implied volatility | Lowest IV | Highest IV | +112,602 | 0.84 |
| Straddle momentum | Past winners | Past losers | −70,744 | −0.62 |
| Illiquidity | Narrowest IV spreads | Widest IV spreads | +29,760 | 0.18 |

### Why the return denominator matters

On the same momentum holdings, the winners’ subsequent return per dollar of entry premium exceeded the losers’ by **12.8 percentage points** on average. On equal forward notional, winners paid **68.2 basis points** more at expiry but cost **82.5 basis points** more upfront. The spread on notional was **−14.3 basis points**. Both comparisons use unhedged straddles at entry mid premiums. The dollar P&L in the table uses executable quote sides, a hedge and equal vega per position.

Zhang, So and Driouchi report a **+39.9 percentage point** momentum spread on premium with two currencies per side (online appendix, Table A11). They rank nine currencies weekly. The different currency sets, formation frequencies and lookbacks leave the source of the gap open. [Paper and online appendix](https://doi.org/10.1093/rof/rfae002) · [Authors’ factor data](https://raymondhyso.com/research)

### How well did raw IV carry forward?

On its full development period (February 2005–December 2015, 131 months), raw IV earned **USD 104,054** with a **0.72 Sharpe**. Applying the same rule over January 2016–December 2025 (120 months) earned **USD 1,013** with a **0.01 Sharpe**. This later period had already been inspected for the baseline. The momentum and illiquidity comparisons use development data only.

## Portfolio construction

- The six pairs are USD/CAD, USD/CHF, USD/HKD, USD/JPY, USD/MXN and USD/SEK. Each European straddle combines a call and put struck at the one-month forward and held to a next-month-end expiry proxy.
- Raw IV uses the one-month ATM midpoint. Illiquidity uses ask IV less bid IV. Momentum sums the nine most recent unhedged straddle returns whose expiries strictly precede entry. The underlying raw-IV sort follows [Fullwood, James and Marsh (2021)](https://doi.org/10.1016/j.jfineco.2021.04.030).
- Each of the four positions starts with USD 250 vega per volatility point. Longs pay ask and shorts receive bid. An initial forward delta hedge is held through expiry. Returns use USD 1 million of fixed reference capital. The model omits forward execution spreads and margin costs.

## Reproduce the reported results

Run `python analyze.py` with Python 3.9 or later. It reads [monthly portfolio results](data/monthly_pnl.csv), selects the common development months and calculates P&L, Sharpe, drawdown and the two momentum spreads. For the chart, install Matplotlib and run `python analyze.py --plot`.

The CSV contains derived portfolio results rounded to cents and momentum spreads rounded to four decimals. Empty cells mark unavailable or unevaluated observations. Repricing the underlying trades requires separate access to the historical IV bid/ask, spot, one-month forward and USD funding inputs.
