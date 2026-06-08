import numpy as np
import  pandas as pd
import yfinance as yf
from datetime import date

def kaufman(prices,window=10):
    direction=abs(prices-prices.shift(window))
    dailymoves=abs(prices-prices.shift(1))
    vol=dailymoves.rolling(window).sum()

    er=direction/vol
    return er

data=yf.download("RELIANCE.NS",start="2020-01-01",end=date.today())
prices=data['Close'].dropna().squeeze()

er=kaufman(prices,window=10)

print(er.tail(10))
print(f"\nCurrent ER: {er.iloc[-1]:.4f}")