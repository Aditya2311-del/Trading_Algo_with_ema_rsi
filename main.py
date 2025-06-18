from utils import get_data, risk
from strategy import TRAD_STRATEGY
import matplotlib.pyplot as plt
import numpy as np

assets = ['RELIANCE', 'TCS', 'HDFCBANK', 'ICICIBANK', 'BHARTIARTL']
data = get_data(assets)

if not data:
    raise ValueError("No data fetched for any of the assets.")

strategies = {}
for asset in assets:
    print(f"Running strategy for {asset}")
    strategy = TRAD_STRATEGY(data[asset], 0.05, 0.05)
    strategy.run()
    strategies[asset] = strategy

# Plots
for asset, strategy in strategies.items():
    print(f'{asset}\n{strategy.position["holdings"].value_counts()}')
    plt.figure(figsize=(20, 10))
    plt.plot(strategy.data['close'], color='black', label='Close Price')
    plt.plot(strategy.position["ema_50"], color='red', label='ema_50')
    plt.plot(strategy.position["ema_100"], color='green', label='ema_100')
    plt.plot(strategy.position["ema_200"], color='blue', label='ema_200')
    plt.plot(5 * strategy.position["rsi"], color='yellow', label='rsi')
    plt.axhline(y=250, color='red', linestyle='--', label='Overbought/sold line')

    entry_points = strategy.position[strategy.position['holdings'] != 0]
    entry_data = strategy.data.loc[entry_points.index]

    plt.scatter(entry_data.index, entry_data["close"], c=entry_points["holdings"],
                cmap='bwr_r', label='Positions')
    plt.title(f"{asset} Breakout Strategy")
    plt.legend()
    plt.show()

# Returns & Sharpe
total_return = sum(strategy.calculate_returns() for asset, strategy in strategies.items()) * (100 / 5)
print(f'Return on investment of 100 units on portfolio upon equal equity: {total_return}')

sharps = [abs(strategy.calculate_returns() / risk(data[asset])) for asset, strategy in strategies.items()]
weight_sharps = np.array(sharps) / sum(sharps)
print(weight_sharps)

for i, (asset, strategy) in enumerate(strategies.items()):
    print(f'{asset}\n{strategy.calculate_returns() * abs(weight_sharps[i]) * 100}')

total_weighted_return = sum(strategy.calculate_returns() * abs(weight_sharps[i]) for i, (asset, strategy) in enumerate(strategies.items())) * 100
print(f'Total Percentage Return on investment of 100 units on portfolio after proper asset allocation: {total_weighted_return}')
