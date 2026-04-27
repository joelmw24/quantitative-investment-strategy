import os

import pandas as pd


def compute_daily_returns(price_data):
    returns = price_data.pct_change()
    returns = returns.fillna(0)
    return returns


def run_backtest(price_data, weights, initial_capital):
    asset_returns = compute_daily_returns(price_data)
    shifted_weights = weights.shift(1).fillna(0)

    portfolio_returns = (shifted_weights * asset_returns).sum(axis=1)
    portfolio_value = initial_capital * (1 + portfolio_returns).cumprod()

    result = pd.DataFrame(index=price_data.index)
    result["portfolio_return"] = portfolio_returns
    result["portfolio_value"] = portfolio_value
    return result


def run_benchmark_backtest(benchmark_data, initial_capital):
    benchmark_returns = benchmark_data["Close"].pct_change().fillna(0)
    benchmark_value = initial_capital * (1 + benchmark_returns).cumprod()

    result = pd.DataFrame(index=benchmark_data.index)
    result["benchmark_return"] = benchmark_returns
    result["benchmark_value"] = benchmark_value
    return result


def extract_trades(price_data, weights):
    trades = []
    current_trades = {}

    for date in price_data.index:
        current_weights = weights.loc[date]

        for ticker in price_data.columns:
            price = price_data.loc[date, ticker]
            weight = current_weights[ticker]

            if weight > 0 and ticker not in current_trades:
                current_trades[ticker] = {
                    "entry_date": date,
                    "entry_price": price,
                }

            if weight == 0 and ticker in current_trades:
                entry_price = current_trades[ticker]["entry_price"]
                trade_return = (price - entry_price) / entry_price

                trades.append(
                    {
                        "ticker": ticker,
                        "entry_date": current_trades[ticker]["entry_date"],
                        "exit_date": date,
                        "entry_price": entry_price,
                        "exit_price": price,
                        "return": trade_return,
                    }
                )

                del current_trades[ticker]

    last_date = price_data.index[-1]
    for ticker in list(current_trades.keys()):
        entry_price = current_trades[ticker]["entry_price"]
        exit_price = price_data.loc[last_date, ticker]
        trade_return = (exit_price - entry_price) / entry_price

        trades.append(
            {
                "ticker": ticker,
                "entry_date": current_trades[ticker]["entry_date"],
                "exit_date": last_date,
                "entry_price": entry_price,
                "exit_price": exit_price,
                "return": trade_return,
            }
        )

    trades_df = pd.DataFrame(trades)
    return trades_df


def create_summary(backtest_result, benchmark_result, trades_df):
    final_portfolio_value = backtest_result["portfolio_value"].iloc[-1]
    final_benchmark_value = benchmark_result["benchmark_value"].iloc[-1]

    portfolio_total_return = (
        (final_portfolio_value / backtest_result["portfolio_value"].iloc[0]) - 1
    ) * 100
    benchmark_total_return = (
        (final_benchmark_value / benchmark_result["benchmark_value"].iloc[0]) - 1
    ) * 100

    number_of_trades = len(trades_df)

    if number_of_trades > 0:
        winning_trades = trades_df[trades_df["return"] > 0]
        losing_trades = trades_df[trades_df["return"] <= 0]

        win_rate = (len(winning_trades) / number_of_trades) * 100

        if len(winning_trades) > 0:
            average_gain = winning_trades["return"].mean() * 100
        else:
            average_gain = 0

        if len(losing_trades) > 0:
            average_loss = losing_trades["return"].mean() * 100
        else:
            average_loss = 0
    else:
        win_rate = 0
        average_gain = 0
        average_loss = 0

    lines = [
        "RESUME DU BACKTEST",
        "",
        f"Valeur finale du portefeuille : {final_portfolio_value:.2f}",
        f"Valeur finale du benchmark : {final_benchmark_value:.2f}",
        f"Rendement total du portefeuille : {portfolio_total_return:.2f} %",
        f"Rendement total du benchmark : {benchmark_total_return:.2f} %",
        f"Nombre de trades : {number_of_trades}",
        f"Probabilite de reussite des trades : {win_rate:.2f} %",
        f"Gain moyen des trades gagnants : {average_gain:.2f} %",
        f"Perte moyenne des trades perdants : {average_loss:.2f} %",
    ]

    return "\n".join(lines)


def save_summary(summary_text, output_dir, file_name):
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, file_name)
    with open(path, "w", encoding="utf-8") as file:
        file.write(summary_text)
