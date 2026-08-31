prices = [3,4,5,8,2,6,9]
n = len(prices)
max_profit = 0
min_prices = float("inf")
for i in range(0,n):
    min_prices = min(min_prices ,prices[i])
    max_profit = max(max_profit,prices[i] - min_prices)
print(max_profit)