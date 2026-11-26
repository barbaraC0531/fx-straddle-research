"""Summarize the aggregate FX straddle results bundled with this repository."""

import argparse
import csv
from collections import defaultdict
from datetime import date
from math import sqrt
from pathlib import Path
from statistics import mean, stdev


ROOT = Path(__file__).resolve().parent
SERIES = {
    "Raw IV": "raw_iv_usd",
    "Momentum": "momentum_usd",
    "Illiquidity": "illiquidity_usd",
}
CAPITAL = 1_000_000
DEVELOPMENT_END = "2015-12"
UNIVERSE_LABELS = {
    "original_six": "Original six",
    "paper_nine": "Paper nine",
    "g10_ex_usd": "G10 ex USD",
    "paper_nine_plus_mxn_hkd": "Paper nine + MXN + HKD",
}


def metrics(values):
    cumulative = peak = drawdown = 0.0
    for value in values:
        cumulative += value
        peak = max(peak, cumulative)
        drawdown = max(drawdown, peak - cumulative)
    return cumulative, sqrt(12) * mean(values) / stdev(values), 100 * drawdown / CAPITAL


def print_row(label, values):
    pnl, sharpe, drawdown = metrics(values)
    print(f"{label:<20} {len(values):>6} {pnl:>14,.0f} {sharpe:>9.2f} {drawdown:>11.2f}")


def characteristic_sort_report():
    portfolios = defaultdict(list)
    with (ROOT / "data/monthly_sorts.csv").open(encoding="utf-8", newline="") as source:
        for row in csv.DictReader(source):
            specification = (row["iv"], row["momentum"], row["illiquidity"])
            portfolios[specification].append(row)

    baseline = {r["expiry_month"]: r for r in portfolios[("raw", "", "")]}
    lines = [
        "# Results for all 26 characteristic sorts",
        "",
        "Every specification uses the same 109 expiry months, December 2006 through December 2015. "
        "Raw uses the signal level. A z-score compares each currency with its own prior 12 observations. "
        "An empty signal column means the portfolio omits that characteristic.",
        "",
        "Active months count dates with positions. Gross vega is average USD exposure per volatility "
        "point across all 109 months. Both P&L columns report cumulative net USD. Matched IV trades "
        "raw IV at the same actual gross vega as the strategy each month, including zero in cash months. "
        "Sharpe ratios are annualized from monthly net P&L. Dollar figures are rounded independently.",
    ]
    for count, heading in enumerate(("Single characteristics", "Two characteristics", "Three characteristics"), 1):
        lines.extend(["", f"## {heading}", "",
                      "| IV | Momentum | Illiquidity | Active months | Mean gross vega | Net P&L | Sharpe | Matched IV P&L | Matched IV Sharpe |",
                      "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |"])
        for spec, rows in portfolios.items():
            if sum(bool(basis) for basis in spec) != count:
                continue
            vega = [float(r["gross_vega_usd_per_vol_point"]) for r in rows]
            pnl = [float(r["net_pnl_usd"]) for r in rows]
            benchmark = [baseline[r["expiry_month"]] for r in rows]
            matched = [float(b["net_pnl_usd"]) * exposure / float(b["gross_vega_usd_per_vol_point"])
                       for b, exposure in zip(benchmark, vega)]
            total, sharpe, _ = metrics(pnl)
            matched_total, matched_sharpe, _ = metrics(matched)
            labels = " | ".join(spec)
            active = sum(exposure > 0 for exposure in vega)
            lines.append(f"| {labels} | {active} | {mean(vega):,.0f} | {total:,.0f} | {sharpe:.3f} "
                         f"| {matched_total:,.0f} | {matched_sharpe:.3f} |")
    return "\n".join(lines)


def prespecified_universe_report():
    by_universe = defaultdict(list)
    with (ROOT / "data/prespecified_universe_monthly_pnl.csv").open(
            encoding="utf-8-sig", newline="") as source:
        for row in csv.DictReader(source):
            by_universe[row["universe"]].append(row)

    print(f"{'Universe':<25} {'Window':<12} {'Months':>6} {'Net USD':>14} "
          f"{'Sharpe':>9} {'Max DD (%)':>11}")
    for name in UNIVERSE_LABELS:
        rows = by_universe[name]
        windows = (
            ("Development", [r for r in rows if r["expiry_month"] <= DEVELOPMENT_END]),
            ("Later", [r for r in rows if r["expiry_month"] > DEVELOPMENT_END]),
            ("Full", rows),
        )
        for window, selected in windows:
            pnl, sharpe, drawdown = metrics([float(r["net_pnl"]) for r in selected])
            print(f"{UNIVERSE_LABELS[name]:<25} {window:<12} {len(selected):>6} "
                  f"{pnl:>14,.0f} {sharpe:>9.2f} {drawdown:>11.2f}")
        print()


def draw_chart(rows):
    from itertools import accumulate
    import matplotlib.dates as mdates
    import matplotlib.pyplot as plt
    from matplotlib.ticker import FuncFormatter

    dates = [date.fromisoformat(r["expiry_month"] + "-01") for r in rows]
    fig, ax = plt.subplots(figsize=(9, 4.2), layout="constrained")
    for (name, column), color in zip(SERIES.items(), ("#176954", "#923d49", "#416ca1")):
        ax.plot(dates, list(accumulate(float(r[column]) for r in rows)), label=name,
                color=color, linewidth=1.9)
    ax.axhline(0, color="#555555", linewidth=0.8)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x / 1000:,.0f}"))
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.set_ylabel("Cumulative net P&L (USD thousands)")
    ax.set_title("Three currency straddle portfolios, December 2005–December 2015", loc="left")
    ax.legend(frameon=False, ncol=3, loc="upper left")
    ax.grid(axis="y", alpha=0.2)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    chart_dir = ROOT / "figures"
    chart_dir.mkdir(exist_ok=True)
    with plt.rc_context({"svg.hashsalt": "fx-straddle-research", "svg.fonttype": "none"}):
        fig.savefig(chart_dir / "cumulative-pnl.svg", metadata={"Date": None})
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plot", action="store_true", help="Regenerate the chart using Matplotlib.")
    parser.add_argument("--sorts", action="store_true", help="Print the common-window tables for all 26 characteristic sorts.")
    parser.add_argument("--universes", action="store_true",
                        help="Print the prespecified Phase 3 universe comparison.")
    args = parser.parse_args()
    with (ROOT / "data/monthly_pnl.csv").open(encoding="utf-8", newline="") as source:
        rows = list(csv.DictReader(source))
    development = [r for r in rows if r["expiry_month"] <= DEVELOPMENT_END]
    common = [r for r in development if all(r[k] != "" for k in SERIES.values())]
    later = [r for r in rows if r["expiry_month"] > DEVELOPMENT_END]
    print(f"{'Portfolio':<20} {'Months':>6} {'Net USD':>14} {'Sharpe':>9} {'Max DD (%)':>11}")
    for name, field in SERIES.items():
        print_row(name, [float(r[field]) for r in common])
    print_row("Raw IV, full dev.", [float(r["raw_iv_usd"]) for r in development])
    print_row("Raw IV, later", [float(r["raw_iv_usd"]) for r in later])
    print()
    for column, unit in (("momentum_premium_spread_pp", "pp on premium"),
                         ("momentum_notional_spread_bp", "bp on notional")):
        print(f"Mean momentum spread: {mean(float(r[column]) for r in common):+.1f} {unit}")
    if args.plot:
        draw_chart(common)
    if args.sorts:
        print()
        print(characteristic_sort_report())
    if args.universes:
        print()
        prespecified_universe_report()


if __name__ == "__main__":
    main()
