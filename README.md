# Quantitative investment strategy 
This project provides a simple, complete and accessible solution for a finance project in Python.
> ⚠️ This project is for academic and educational purposes only

## Project objectives
The project is divided into 4 parts:

1. Building a financial database
2. Defining an investment strategy
3. Allocating and managing a portfolio
4. Backtesting over more than 5 years

The code style is intentionally kept simple to remain close to a beginner level.

---

## Project Choices

- **Data source:** Yahoo Finance via `yfinance`
- **Number of companies:** 30 American stocks
- **Time period:** January 1, 2020 to March 1, 2026
- **Frequency:** Daily
- **Benchmark:** S&P 500 (`^GSPC`)

---

## Strategy

The strategy is a straightforward trend-following approach:

- A **short moving average** is calculated over **20 days**
- A **long moving average** is calculated over **50 days**
- If the 20-day moving average is **above** the 50-day moving average, the stock is selected
- Otherwise, the stock is excluded

Additional rules:

- The portfolio is **rebalanced at the start of each month**
- A **maximum of 10 stocks** are held at any time
- Selected stocks are assigned **equal weights**

---

## File structure

- `src/config.py` — project parameters
- `src/data_loader.py` — data download and preparation
- `src/strategy.py` — signal computation
- `src/portfolio.py` — portfolio allocation
- `src/backtest.py` — simulation and results
- `rapport_projet.md` — written project report

---

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the main script:
```bash
python main.py
```

## Output files

The script generates an `outputs/` folder containing:

| File | Description |
|------|-------------|
| `price_data.csv` | Historical stock prices |
| `benchmark_data.csv` | Historical benchmark prices |
| `signals.csv` | Buy signals |
| `portfolio_weights.csv` | Portfolio weights over time |
| `portfolio_value.csv` | Portfolio value evolution |
| `trade_results.csv` | Detailed trade records |
| `summary.txt` | Final performance summary |

## Note

```bash
Data download requires an active internet connection at runtime.
```

## Author

**Joël Mwemba**
Engineering Student

