from tvDatafeed import TvDatafeed, Interval
import pandas as pd
import pandas_ta as ta

def get_data(assets):
   tv = TvDatafeed()
   #assets = ['RELIANCE', 'TCS', 'HDFCBANK', 'ICICIBANK', 'BHARTIARTL']
   data_dict = {}

   for asset in assets:
      data = tv.get_hist(symbol=asset, exchange='NSE', interval=Interval.in_daily, n_bars=2000)
      data_dict[asset] = data

   data = pd.concat(data_dict, axis=1, ignore_index=False)
   return data

def risk(data):
      df=pd.DataFrame()
      df["returns"]= data["close"].pct_change()
      risk_=df["returns"].std()
      return risk_

  
