# Phase 3 prespecified currency universes

Phase 3 asks whether the fixed raw-IV strategy is robust to broader currency sets. The universe definitions were recorded before the additional currency returns were evaluated. No currency is added or removed because of its realized strategy P&L.

## Fixed specifications

| Universe | Currency set |
| --- | --- |
| Original six | CAD, CHF, HKD, JPY, MXN, SEK |
| Paper nine | AUD, EUR, GBP, CAD, CHF, JPY, DKK, NOK, SEK |
| G10 excluding USD | AUD, CAD, CHF, EUR, GBP, JPY, NOK, NZD, SEK |
| Paper nine plus MXN and HKD | AUD, EUR, GBP, CAD, CHF, JPY, DKK, NOK, SEK, MXN, HKD |

Every universe applies the same rule. At month-end, rank the 1M ATM implied-volatility midpoint. Buy the two lowest-IV straddles at the ask and sell the two highest-IV straddles at the bid. Each selected position has USD 250 of vega per one-percentage-point volatility move. The portfolio uses one initial forward delta hedge, includes option-spread execution and premium financing, and reports return on USD 1 million of fixed reference capital.

The implementation first reproduced the archived original-six model: 251 expiry months, 1,004 trades, identical selections and a maximum absolute monthly P&L difference of USD 0.00.

## Results

| Universe | Window | Months | Net P&L (USD) | Annualized mean | Annualized vol | Sharpe | Max drawdown |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Original six | Development, 2005–2015 | 131 | 104,054 | 0.95% | 1.32% | 0.72 | 2.33% |
| Original six | Later, 2016–2025 | 120 | 1,013 | 0.01% | 1.13% | 0.01 | 4.15% |
| Paper nine | Development, 2005–2015 | 123 | 50,158 | 0.49% | 1.37% | 0.36 | 2.93% |
| Paper nine | Later, 2016–2025 | 120 | 17,483 | 0.17% | 1.09% | 0.16 | 3.72% |
| G10 excluding USD | Development, 2005–2015 | 131 | 29,236 | 0.27% | 1.35% | 0.20 | 2.65% |
| G10 excluding USD | Later, 2016–2025 | 120 | 19,184 | 0.19% | 1.12% | 0.17 | 3.78% |
| Paper nine plus MXN and HKD | Development, 2005–2015 | 123 | 89,155 | 0.87% | 1.43% | 0.61 | 2.32% |
| Paper nine plus MXN and HKD | Later, 2016–2025 | 120 | 20,274 | 0.20% | 1.29% | 0.16 | 4.51% |

The broader universes have positive later-period point estimates, but later Sharpe ratios remain between 0.16 and 0.17. Breadth therefore does not recover the strength of the original-six development result. The eleven-currency result is also not free of concentration: MXN contributed USD 70,975 over its full 243-month sample, while HKD contributed negative USD 23,085.

Paper nine and the eleven-currency universe each omit eight universe-months because the required USDDKK 1M IV was not observed. No forward fill, backfill or substitution is used. Their reported development samples therefore contain 123 rather than 131 months. A common-month paired comparison with HAC inference remains a next step.

## Data and publication boundary

This repository contains only derived monthly portfolio results, summary statistics, selection labels and currency-level attribution. It excludes Bloomberg IV, spot, forward and rate histories, values-only workbooks, terminal screenshots and personal paths. The underlying workbooks cover January 2005 through December 2025.

## Next work

1. Compare all four universes on their common eligible months using paired monthly P&L differences, HAC standard errors and confidence intervals.
2. Measure concentration and selection frequency by currency and side, including an MXN contribution check for the eleven-currency universe.
3. Calculate the extra forward-spread, margin and financing cost that would reduce each strategy's net P&L to zero.
4. Extend the already fixed illiquidity, momentum and 25-delta-butterfly diagnostics to the prespecified currency sets without changing their definitions.
5. Prespecify a 3M-minus-1M IV slope test using the already collected histories before examining its return results.
6. Convert the validated results into the final paper tables, research memo and presentation conclusions.

Deferred work requiring additional Bloomberg access includes 6M ATM IV, detailed Batch C forward and settlement conventions, and executable 25-delta wing pricing. BRL, KRW, TWD and INR use outright NDF forwards and must not be passed through the deliverable forward-points conversion.

## Reproduce

Run:

```bash
python analyze.py --universes
```

The command calculates each universe's development, later and full-sample P&L, Sharpe and drawdown from `data/prespecified_universe_monthly_pnl.csv`. The complete reported summary is in `data/prespecified_universe_summary.csv`; currency attribution and excluded months are provided in the adjacent Phase 3 CSV files.
