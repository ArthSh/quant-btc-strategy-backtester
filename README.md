# Quantitative Bitcoin Trading Strategy & Backtesting Framework

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![TA-Lib](https://img.shields.io/badge/TA--Lib-Technical%20Indicators-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

A quantitative trading framework for Bitcoin that combines technical indicator engineering, systematic trend-following strategies, parameter optimization, and backtesting. The project implements a Donchian Breakout strategy with ATR-based risk management and evaluates multiple strategy configurations using exhaustive grid search to identify robust trading parameters.

---

## Project Overview

This project was developed to explore systematic trading strategies for Bitcoin using historical OHLCV market data. Rather than relying on discretionary trading decisions, the framework generates trading signals using rule-based technical indicators and evaluates them through historical backtesting.

The project follows a quantitative research workflow consisting of:

- Feature engineering using technical indicators
- Rule-based strategy development
- Historical backtesting
- Hyperparameter optimization
- Performance evaluation using financial risk metrics

---

## Dataset

- **Asset:** Bitcoin (BTC)
- **Frequency:** Daily OHLCV
- **Time Period:** 2019 – 2023
- **Columns Used**
  - Open
  - High
  - Low
  - Close
  - Volume

---

# Strategy

The final strategy implements a **Donchian Breakout Trend Following System**.

### Long Entry

- Price breaks above the 25-day Donchian High
- EMA(50) > EMA(200)
- ATR-based volatility confirmation

### Short Entry

- Price breaks below the 25-day Donchian Low
- EMA(50) < EMA(200)
- ATR-based volatility confirmation

### Exit Rules

Long positions are closed when:

- Price falls below the exit Donchian channel
- ATR trailing stop is triggered

Short positions are closed when:

- Price rises above the exit Donchian channel
- ATR trailing stop is triggered

---

# Technical Indicators

The framework computes a comprehensive feature library including:

### Trend Indicators

- EMA (10, 20, 50, 100, 200)
- SMA
- Donchian Channels

### Momentum Indicators

- RSI
- MACD
- Rate of Change (ROC)
- Momentum

### Volatility Indicators

- ATR
- Bollinger Bands
- Rolling Volatility

### Trend Strength

- ADX

### Volume Indicators

- Relative Volume
- OBV

### Additional Features

- Log Returns
- Daily Returns
- Candle Body
- Upper & Lower Wick

---

# Hyperparameter Optimization

Instead of manually selecting strategy parameters, an exhaustive grid search was implemented.

The optimizer evaluates multiple combinations of:

- ATR Trailing Stop Multiplier
- Donchian Entry Window
- Donchian Exit Window

A total of **196 strategy configurations** were evaluated.

Each configuration was ranked using:

- Sharpe Ratio
- Net Profit
- Maximum Drawdown
- Win Rate
- Number of Trades

---

# Performance Metrics

The framework evaluates each strategy using:

- Total Trades
- Win Rate
- Gross Profit
- Net Profit
- Average Profit
- Largest Win/Loss
- Maximum Drawdown
- Average Drawdown
- Sharpe Ratio
- Holding Period Statistics

The final optimized strategy achieved:

| Metric | Value |
|---------|--------|
| Sharpe Ratio | **1.06** |
| Net Profit | **3731.94** |
| Maximum Drawdown | **46.43%** |
| Total Trades | **20** |

---
# Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/quant-btc-strategy-backtester.git

cd quant-btc-strategy-backtester
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Strategy

Generate trading signals

```bash
python strategies/main.py
```

Run hyperparameter optimization

```bash
python optimization/optimizer.py
```

---

# Methodology

The development process followed an iterative quantitative research workflow:

1. Constructed a technical indicator feature library.
2. Developed multiple systematic trading strategies.
3. Backtested each strategy using historical BTC data.
4. Eliminated look-ahead bias through sequential validation.
5. Performed exhaustive grid search across strategy parameters.
6. Selected the final configuration using risk-adjusted performance metrics.

---

# Future Improvements

Potential extensions include:

- Walk-forward optimization
- Multi-asset portfolio support
- Position sizing using volatility targeting
- Transaction cost and slippage modeling
- Bayesian parameter optimization
- Machine learning based signal generation
- Live trading integration using exchange APIs

---

# Disclaimer

This project is intended solely for educational and learning purposes, taken by me under the umbrella of Summer of Quant (2026) hosted by Quant Community of IIT Bombay. It should not be interpreted as financial advice or a recommendation to trade any financial instrument.

---

