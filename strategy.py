class TRAD_STRATEGY():
  def __init__(self,data,stop_loss,target):
    self.data=data
    self.stop_loss= stop_loss
    self.target=target
    self.position=pd.DataFrame(index=data.index)
    self.position["holdings"]=0
    self.data=data.copy()


  def cal_indi(self):
     self.position["ema_50"]=ta.ema(self.data["close"], length=50)
     self.position["ema_100"]=ta.ema(self.data["close"], length=100)
     self.position["ema_200"]=ta.ema(self.data["close"], length=200)
     self.position["rsi"]=ta.rsi(self.data["close"], length=50)
     self.position["ATR"]=ta.atr(high=self.data["high"],low=self.data["low"],close=self.data["close"],length=14)

  def run(self):
    self.cal_indi()
    self.position.fillna(0,inplace=True)
    for day in range(2,self.position.shape[0]):
      df=self.data.iloc[:day]
      buy_condition = (
        ((self.position["ema_50"].iloc[day] > self.position["ema_100"].iloc[day]) &
        (self.position["ema_100"].iloc[day] > self.position["ema_200"].iloc[day]))& (self.position["rsi"].iloc[day]<50))

      sell_condition = (
        ((self.position["ema_50"].iloc[day] < self.position["ema_100"].iloc[day]) &
        (self.position["ema_100"].iloc[day] < self.position["ema_200"].iloc[day])) & (self.position["rsi"].iloc[day]>50))

      '''if df["close"].iloc[-1] < (1 + self.stop_loss-0.1*self.position["ATR"].iloc[day]) * df["close"].iloc[-2]:
       self.position["holdings"].iloc[day] = -1
       continue'''

      if buy_condition:
        self.position["holdings"].iloc[day]=1
      elif sell_condition:
        self.position["holdings"].iloc[day]=-1
      else:
        self.position["holdings"].iloc[day]=0

  def calculate_returns(self):
      self.data["returns"] = self.data['close'].pct_change()
      self.position['strategy_returns'] = self.position['holdings'].shift(1)*self.data['returns']
      self.position['cumulative_returns'] = (1 + self.position['strategy_returns'].fillna(0)).cumprod()
      final_return = self.position['cumulative_returns'].iloc[-1] - 1
      return final_return

