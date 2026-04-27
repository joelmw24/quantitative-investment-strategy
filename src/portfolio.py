import pandas as pd


def build_portfolio_weights(signals, max_stocks, rebalancing_frequency):
    if rebalancing_frequency == "MS":
        rebalancing_dates = signals.groupby(signals.index.to_period("M")).head(1).index
    else:
        rebalancing_dates = signals.resample(rebalancing_frequency).first().index

    weights = pd.DataFrame(0.0, index=signals.index, columns=signals.columns)

    last_weights = pd.Series(0.0, index=signals.columns)

    for date in signals.index:
        if date in rebalancing_dates:
            active_stocks = []

            for ticker in signals.columns:
                if signals.loc[date, ticker] == 1:
                    active_stocks.append(ticker)

            active_stocks = active_stocks[:max_stocks]
            new_weights = pd.Series(0.0, index=signals.columns)

            if len(active_stocks) > 0:
                equal_weight = 1 / len(active_stocks)
                for ticker in active_stocks:
                    new_weights[ticker] = equal_weight

            last_weights = new_weights

        weights.loc[date] = last_weights

    return weights
