# Trading_Algo_with_ema_rsi
to run this code you need python 3.11.x because we need numpy 1.24.4 to use pandas-ta and latest python version 3.13.x do not support it.
if tvDatafeed not able to install try this one: !pip install --upgrade --no-cache-dir git+https://github.com/rongardF/tvdatafeed.git\\

This project implements a simple breakout strategy using EMA and RSI indicators for selected NSE stocks using Python.

---

##  Features:
- Fetches live historical stock data from TradingView via `tvdatafeed`
- Calculates EMA50, EMA100, EMA200, RSI, and ATR indicators
- Implements a trading strategy based on breakout conditions
- Visualizes positions, EMAs, RSI overlays, and strategy performance
- Computes returns and a basic Sharpe ratio-based portfolio weighting

---

##  Requirements:
- Python 3.9+
- Libraries:
  - tvdatafeed  
  - pandas  
  - pandas-ta  
  - numpy==1.24.4  
  - matplotlib  

Install dependencies:
```bash
pip install -r requirements.txt
