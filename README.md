# Trading app

Baseline Python CLI for live (paper-first) trading workflows and backtesting.

## Project structure

```
.
├── .env.example
├── pyproject.toml
└── src/
    └── trading_app/
        ├── __init__.py
        ├── config.py
        └── main.py
```

## Setup

1. Create and activate a virtual environment.
2. Install the project in editable mode:

```bash
pip install -e .
```

3. Copy environment defaults and customize credentials:

```bash
cp .env.example .env
```

## CLI usage

Show available commands:

```bash
trading-app --help
```

Run a paper trade (default behavior):

```bash
trading-app trade-live --symbol AAPL --qty 2
```

Force non-paper execution (unless `PAPER_MODE=true` in environment):

```bash
trading-app trade-live --symbol MSFT --qty 1 --no-paper
```

Run a basic backtest:

```bash
trading-app backtest --symbol AAPL --lookback-days 90
```
