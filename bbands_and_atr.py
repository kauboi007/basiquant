import numpy as np
import pandas as pd
import yfinance as yf
from datetime import date

data = yf.download("RELIANCE.NS", start="2023-01-01", end=date.today())
df = data[['High', 'Low', 'Close']].squeeze()

def bollinger_bands(close, n=20, k=2):
    sma = close.rolling(n).mean()
    std = close.rolling(n).std()
    upper = sma + k * std
    lower = sma - k * std
    percent_b = (close - lower) / (upper - lower)
    bandwidth = (upper - lower) / sma
    return upper, sma, lower, percent_b, bandwidth

upper, mid, lower, pct_b, bw = bollinger_bands(df['Close'])

def atr(high, low, close, n=14):
    prev_close = close.shift(1)
    tr = pd.concat([
        high - low,
        (high - prev_close).abs(),
        (low  - prev_close).abs()
    ], axis=1).max(axis=1)
    return tr.rolling(n).mean()

atr_values = atr(df['High'], df['Low'], df['Close'])
atr_ratio  = atr_values / df['Close'] 

print(f"Current %B:        {pct_b.iloc[-1]:.4f}")
print(f"Current Bandwidth: {bw.iloc[-1]:.4f}")
print(f"Current ATR:       {atr_values.iloc[-1]:.2f}")
print(f"ATR/Price Ratio:   {atr_ratio.iloc[-1]:.4f}")