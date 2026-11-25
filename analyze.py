"""Summarize the aggregate FX straddle results bundled with this repository."""

import argparse
import csv
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


if __name__ == "__main__":
    main()
