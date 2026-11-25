# Results for all 26 characteristic sorts

Every specification uses the same 109 expiry months, December 2006 through December 2015. Raw uses the signal level. A z-score compares each currency with its own prior 12 observations. An empty signal column means the portfolio omits that characteristic.

Active months count dates with positions. Gross vega is average USD exposure per volatility point across all 109 months. Both P&L columns report cumulative net USD. Matched IV trades raw IV at the same actual gross vega as the strategy each month, including zero in cash months. Sharpe ratios are annualized from monthly net P&L. Dollar figures are rounded independently.

## Single characteristics

| IV | Momentum | Illiquidity | Active months | Mean gross vega | Net P&L | Sharpe | Matched IV P&L | Matched IV Sharpe |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| raw |  |  | 109 | 1,000 | 110,183 | 0.886 | 110,183 | 0.886 |
| z |  |  | 109 | 1,000 | -7,892 | -0.068 | 110,183 | 0.886 |
|  | raw |  | 109 | 1,000 | -67,296 | -0.626 | 110,183 | 0.886 |
|  | z |  | 109 | 1,000 | -90,876 | -0.778 | 110,183 | 0.886 |
|  |  | raw | 109 | 1,000 | 25,385 | 0.164 | 110,183 | 0.886 |
|  |  | z | 109 | 1,000 | -6,239 | -0.047 | 110,183 | 0.886 |

## Two characteristics

| IV | Momentum | Illiquidity | Active months | Mean gross vega | Net P&L | Sharpe | Matched IV P&L | Matched IV Sharpe |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| raw | raw |  | 100 | 601 | 30,830 | 0.309 | 65,653 | 0.832 |
| raw | z |  | 102 | 693 | 28,354 | 0.268 | 61,133 | 0.662 |
| z | raw |  | 103 | 642 | -9,946 | -0.102 | 74,719 | 0.942 |
| z | z |  | 97 | 610 | -8,290 | -0.095 | 71,745 | 0.971 |
| raw |  | raw | 109 | 940 | 77,959 | 0.628 | 111,556 | 0.903 |
| raw |  | z | 101 | 679 | 62,650 | 0.546 | 67,533 | 0.752 |
| z |  | raw | 105 | 761 | 49,442 | 0.387 | 106,939 | 0.986 |
| z |  | z | 103 | 761 | 24,530 | 0.256 | 78,453 | 0.856 |
|  | raw | raw | 105 | 766 | -5,125 | -0.047 | 89,873 | 0.833 |
|  | raw | z | 100 | 674 | -23,337 | -0.253 | 72,695 | 0.774 |
|  | z | raw | 105 | 757 | -2,948 | -0.028 | 75,633 | 0.680 |
|  | z | z | 102 | 706 | -24,246 | -0.248 | 86,628 | 0.798 |

## Three characteristics

| IV | Momentum | Illiquidity | Active months | Mean gross vega | Net P&L | Sharpe | Matched IV P&L | Matched IV Sharpe |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| raw | raw | raw | 78 | 427 | 27,955 | 0.311 | 42,993 | 0.620 |
| raw | raw | z | 35 | 179 | -5,238 | -0.111 | 14,080 | 0.498 |
| raw | z | raw | 81 | 468 | 19,962 | 0.213 | 29,529 | 0.367 |
| raw | z | z | 47 | 243 | 2,726 | 0.057 | 22,055 | 0.478 |
| z | raw | raw | 57 | 275 | 18,319 | 0.233 | 38,211 | 0.693 |
| z | raw | z | 48 | 239 | -7,404 | -0.132 | 14,331 | 0.416 |
| z | z | raw | 47 | 248 | 22,095 | 0.325 | 30,830 | 0.552 |
| z | z | z | 50 | 243 | -1,535 | -0.030 | 18,480 | 0.440 |
