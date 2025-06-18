from utils import get_data
from strategy import TRAD_STRATEGY
import matplotlib.pyplot as plt
%matplotlib inline



data = get_data()
strategies = {}
for asset in assets:
    print(f"Running strategy for {asset}")
    strategy = TRAD_STRATEGY(data[asset],0.05,0.05)
    strategy.run()
    strategies[asset] = strategy

#plots
for asset, strategy in strategies.items():
 print(f'{asset}\n{strategy.position["holdings"].value_counts()}')
 plt.figure(figsize=(20, 10))
 plt.plot(strategy.data['close'], color='black', label='Close Price')
 plt.plot(strategy.position["ema_50"], color='red', label='ema_50')
 plt.plot(strategy.position["ema_100"], color='green', label='ema_100')
 plt.plot(strategy.position["ema_200"], color='blue', label='ema_200')
 plt.plot(5*strategy.position["rsi"], color='yellow', label='rsi')
 plt.axhline(y=250, color='red', linestyle='--',label=' over brought/sold line')

 entry_points = strategy.position[strategy.position['holdings'] != 0]
 entry_data = strategy.data.loc[entry_points.index]

 plt.scatter(entry_data.index, entry_data["close"], c=entry_points["holdings"],
                cmap='bwr_r', label='Positions')
 plt.title(f"{asset} Breakout Strategy")
 plt.legend()
 plt.show()

print(f'Return on investment of 100 units on portfolio upon equal equity : {sum(strategy.calculate_returns() for asset, strategy in strategies.items())*(100/5)}')

sharps=[abs(strategy.calculate_returns()/risk(data[asset])) for asset, strategy in strategies.items()]
weigth_sharps=sharps/sum(sharps)
print(weigth_sharps)
i=0
for asset, strategy in strategies.items():
  print(f'{asset}\n{strategy.calculate_returns()*abs(weigth_sharps[i])*100}')
  i+=1

print(f'Total Percentage Return on investment of 100 units on portfolio after proper asset allocation : {sum(strategy.calculate_returns()*abs(weigth_sharps[i]) for i ,(asset, strategy) in enumerate(strategies.items()))*100}')
