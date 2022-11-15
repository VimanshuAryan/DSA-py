# 121
# buy and sell stock

prices = [7,1,5,3,6,4]

def stock(arr):
    profit = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr) - i, 1):
            if arr[j] > arr[i]:
                res = arr[j] - arr[i]
                profit = max(profit, res)
    return profit

print(stock(prices))

def profit(prices):

    l,r = 0,1
    profit = 0

    while l < len(prices):

        if prices[l] < prices[r]:
            res = prices[r] - prices[l]
            profit = max(res, profit)
        else:
            l = r
        r += 1

    return profit