"""CLI entry points for trading operations."""

from __future__ import annotations

from datetime import datetime

import pandas as pd
import typer

from trading_app.config import Settings

app = typer.Typer(add_completion=False, no_args_is_help=True)


@app.command("trade-live")
def trade_live(
    symbol: str = typer.Option("AAPL", help="Ticker symbol to trade."),
    qty: int = typer.Option(1, min=1, help="Quantity to trade."),
    paper: bool = typer.Option(True, "--paper/--no-paper", help="Run in paper trading mode."),
) -> None:
    """Place a live trade request (paper mode by default)."""
    settings = Settings.from_env()

    mode = "paper" if paper else "live"
    if not paper and settings.paper_mode:
        typer.secho("PAPER_MODE=true in environment; forcing paper trade.", fg=typer.colors.YELLOW)
        mode = "paper"

    typer.echo(
        f"[{datetime.utcnow().isoformat()}Z] submitting {mode} trade: "
        f"symbol={symbol} qty={qty} env={settings.env}"
    )


@app.command()
def backtest(
    symbol: str = typer.Option("AAPL", help="Ticker symbol to backtest."),
    lookback_days: int = typer.Option(30, min=1, help="How many days to evaluate."),
) -> None:
    """Run a simple placeholder backtest."""
    prices = pd.Series(range(100, 100 + lookback_days), name="close")
    returns = prices.pct_change().dropna()
    summary = pd.DataFrame(
        {
            "symbol": [symbol],
            "period_days": [lookback_days],
            "avg_daily_return": [returns.mean()],
            "total_return": [(prices.iloc[-1] / prices.iloc[0]) - 1],
        }
    )
    typer.echo("Backtest complete:")
    typer.echo(summary.to_string(index=False))


def run() -> None:
    """Console script wrapper."""
    app()


if __name__ == "__main__":
    run()
