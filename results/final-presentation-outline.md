# Final presentation outline

The final presentation draft is complete. It follows the original proposal's dark-blue volatility design and uses editable charts. The recommended nine-slide sequence is below.

1. **Trading FX Volatility.** Frame the project as a test of what survives the robustness checks.
2. **What we test.** State the raw-IV rule, fixed vega sizing, executable option quotes, hedge convention and robustness questions.
3. **The baseline signal nearly disappears after 2015.** The original-six portfolio falls from USD 104,054 and a 0.72 Sharpe in development to USD 1,013 and a 0.01 Sharpe in 2016–2025.
4. **Broader universes improve later P&L, not conviction.** On 243 common months, the wider universes earn USD 17,483–20,274 later-period P&L, with Sharpe ratios of only 0.16–0.17.
5. **Common-month inference remains weak.** No later-period pairwise universe difference is significant. Two development comparisons with unadjusted p-values near 5% both have Benjamini–Hochberg q = 0.150.
6. **6M minus 1M IV slope does not rescue the strategy.** The prespecified TSIV portfolios are negative in every later sample and never significantly outperform matched raw IV in development.
7. **A few currencies drive much of the development result.** MXN supplies 61.3% of absolute currency contributions in the original six and 44.9% in the eleven-currency universe.
8. **Later profits are easy to erase with extra costs.** An additional 0.008 volatility points, about USD 2.11 per selected trade, removes the original-six later profit.
9. **The research conclusion survives; the trading claim does not.** Do not recommend deployment. Present the project as a transparent study of signal decay, universe sensitivity, concentration and implementation fragility.

## Claims to preserve in the talk

- The 2016–2025 period had already been inspected and is a later-period diagnostic, not an untouched holdout.
- Wider universes change point estimates but do not provide statistically established dominance.
- The 6M-minus-1M signal direction was fixed before returns: buy the highest slopes and sell the lowest slopes.
- Bloomberg errors, stale quotes and bid-greater-than-ask observations are excluded without filling.
- Cost breakevens are equivalent thresholds, not observed dealer quotes.

## Remaining work

- Write the final paper around the same evidence hierarchy.
- Add team names and any course-required cover details to the presentation.
- Decide whether optional broader-universe illiquidity, momentum or butterfly extensions are worth the remaining time. They are not required for the main conclusion.
