prices = [3,4,5,8,2,6,9]
n = len(prices)
max_profit = 0
for i in range(0,n):
    for j in range(i+1,n):
        if prices[j]>prices[i]:
            p = prices[j] - prices[i]
            max_profit = max(max_profit,p)
print(max_profit)