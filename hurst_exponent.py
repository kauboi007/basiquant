import numpy as np

def hurst_expo(price_series):
    returns=np.array(price_series)
    logreturns=np.log(returns)
    window=[]
    rsval=[]
    n=len(logreturns)
    windows=[2,4,8,16,32,64,128]
    for i in windows:
        if(i>n):
            break
        rslist=[]
        for start in range(0,n-i,i):
            chunk=logreturns[start:start+i]
            meanchunk=np.mean(chunk)
            demeaned=chunk-meanchunk
            cumilative=np.cumsum(demeaned)

            r=np.max(cumilative)-np.min(cumilative)
            s=np.std(cumilative)
            if(s>0):
                rslist.append(r/s)

        if rslist:
            window.append(np.log(i))
            rsval.append(np.log(np.mean(rslist)))
    h,x=np.polyfit(window,rsval,1)
    return h

import yfinance as yf
data=yf.download("RELIANCE.NS",start="2020-01-01",end="2026-06-01")
prices=data['Close'].dropna().values

h=hurst_expo(price_series=prices)
print(f"hurst value: {h:.4f}")
if h > 0.55:
    print("Trending — momentum strategies applicable")
elif h < 0.45:
    print("Mean-reverting — stat arb / pairs trading applicable")
else:
    print("Near random walk — be careful")



