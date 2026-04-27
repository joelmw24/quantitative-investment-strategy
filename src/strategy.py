import pandas as pd


def create_signals(price_data, short_window, long_window):
    signals = pd.DataFrame(index=price_data.index)

    for ticker in price_data.columns:
        short_ma = price_data[ticker].rolling(window=short_window).mean()
        long_ma = price_data[ticker].rolling(window=long_window).mean()

        signal = (short_ma > long_ma).astype(int)
        signals[ticker] = signal

    signals = signals.fillna(0)
    return signals
