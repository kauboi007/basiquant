import numpy as np
import pandas as pd
import yfinance as yf
from datetime import date

def garch_11(returns, omega, alpha, beta):
    n = len(returns)
    sigma2 = np.zeros(n)
    sigma2[0] = np.var(returns)
    for t in range(1, n):
        sigma2[t] = omega + alpha * returns[t-1]**2 + beta * sigma2[t-1]
    return sigma2

data = yf.download("RELIANCE.NS", start="2020-01-01", end=date.today())
prices = data['Close'].squeeze().dropna()
returns = np.diff(np.log(prices.values))

omega = 0.000001
alpha = 0.05
beta  = 0.90

sigma2 = garch_11(returns, omega, alpha, beta)
sigma  = np.sqrt(sigma2)  

print(f"Today's estimated daily vol: {sigma[-1]:.4f}")
print(f"Annualized vol: {sigma[-1] * np.sqrt(252):.4f}")


from arch import arch_model
model = arch_model(returns * 100, vol='Garch', p=1, q=1)
result = model.fit(disp='off')
print(result.summary())