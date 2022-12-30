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

# print(stock(prices))


def maxProfit (prices):
    left = 0
    right = 1
    max_profit=0
    while right < len(prices):
        
        if prices[right]>prices[left]:
        #we always need the left value to be smaller
            profit=prices[right] - prices[left]
            max_profit = max(profit,max_profit)
        else:
            left=right
        right+=1
    return max_profit
        

print(maxProfit(prices))