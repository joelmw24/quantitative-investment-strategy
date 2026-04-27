import os

import pandas as pd
import yfinance as yf


def download_prices(tickers, start_date, end_date):
    data = yf.download(
        tickers,
        start=start_date,
        end=end_date,
        auto_adjust=True,
        progress=False,
        group_by="ticker",
    )

    close_data = pd.DataFrame()

    if len(tickers) == 1:
        close_data[tickers[0]] = data["Close"]
    else:
        for ticker in tickers:
            if ticker in data.columns.get_level_values(0):
                close_data[ticker] = data[ticker]["Close"]

    close_data = close_data.dropna(how="all")
    close_data = close_data.ffill()
    return close_data


def download_benchmark(ticker, start_date, end_date):
    data = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        auto_adjust=True,
        progress=False,
    )
    benchmark = pd.DataFrame()
    benchmark["Close"] = data["Close"]
    benchmark = benchmark.dropna()
    return benchmark


def save_dataframe(df, output_dir, file_name):
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, file_name)
    df.to_csv(path)
