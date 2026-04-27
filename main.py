import pandas as pd

from src.backtest import (
    create_summary,
    extract_trades,
    run_backtest,
    run_benchmark_backtest,
    save_summary,
)
from src.config import (
    BENCHMARK,
    END_DATE,
    INITIAL_CAPITAL,
    LONG_WINDOW,
    MAX_STOCKS,
    OUTPUT_DIR,
    REBALANCE_FREQUENCY,
    SHORT_WINDOW,
    START_DATE,
    TICKERS,
)
from src.data_loader import download_benchmark, download_prices, save_dataframe
from src.portfolio import build_portfolio_weights
from src.strategy import create_signals


def main():
    print("Telechargement des donnees...")
    warmup_start = (
        pd.to_datetime(START_DATE) - pd.Timedelta(days=120)
    ).strftime("%Y-%m-%d")

    price_data = download_prices(TICKERS, warmup_start, END_DATE)
    benchmark_data = download_benchmark(BENCHMARK, START_DATE, END_DATE)

    print("Creation des signaux...")
    signals = create_signals(price_data, SHORT_WINDOW, LONG_WINDOW)

    price_data = price_data.loc[START_DATE:END_DATE].copy()
    signals = signals.loc[START_DATE:END_DATE].copy()

    print("Construction du portefeuille...")
    weights = build_portfolio_weights(signals, MAX_STOCKS, REBALANCE_FREQUENCY)

    print("Lancement du backtest...")
    backtest_result = run_backtest(price_data, weights, INITIAL_CAPITAL)
    benchmark_result = run_benchmark_backtest(benchmark_data, INITIAL_CAPITAL)

    print("Analyse des trades...")
    trades_df = extract_trades(price_data, weights)
    summary_text = create_summary(backtest_result, benchmark_result, trades_df)

    print("Sauvegarde des resultats...")
    save_dataframe(price_data, OUTPUT_DIR, "price_data.csv")
    save_dataframe(benchmark_data, OUTPUT_DIR, "benchmark_data.csv")
    save_dataframe(signals, OUTPUT_DIR, "signals.csv")
    save_dataframe(weights, OUTPUT_DIR, "portfolio_weights.csv")
    save_dataframe(backtest_result, OUTPUT_DIR, "portfolio_value.csv")
    save_dataframe(trades_df, OUTPUT_DIR, "trade_results.csv")
    save_summary(summary_text, OUTPUT_DIR, "summary.txt")

    print("")
    print(summary_text)


if __name__ == "__main__":
    main()
