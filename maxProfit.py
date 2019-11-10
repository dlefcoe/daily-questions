'''

This problem was asked by Facebook.

Given an array of numbers representing the stock prices of a company in chronological order and an integer k, 
return the maximum profit you can make from k buys and sells. 

You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.

'''


class profit:
    start = 0
    end = 0
    gain = 0
    pass

def main():
    
    k = 2
    arr = [5, 2, 4, 0, 1]

    answer = maxProfit(k, arr)    

    print(answer)

    # find lowest k points
    arrSort = arr.copy()
    arrSort.sort()
    bestBuys = arrSort[0:k]

    arrSort.sort(reverse=True)
    bestSells = arrSort[0:k]

    print(bestBuys, bestSells)

    #b = bestBuys[:k-1]
    print(arr)
    

    

    pass

def maxProfit(k, a):
    ''' find the max profit in array 
    
    args:
        k: integer, number of buys and sells
        a: array, stock prices in order

    return:
        maximum profit
    '''

    # boundary conditions
    if 2*k > len(a):
        return 'buys and sells are too large'
    
    if len(a) < 2:
        return 'array is too small'
    




    # # seek the lows and highs
    # small = a[0]
    # for i, v in enumerate(a):
    #     for j in a[i:]:
    #         if j > v:
    #             # a profit is made

         


    pass




from itertools import combinations
import random

def solve(market, k, best=None):
    """Get best outcome for k buys and sells using market history list."""

    # get indices of all possible buy and sells
    # and calculate profit for all buy/sell pairs
    k *= 2
    for trade_times in combinations(range(len(market)), k):
        prices = [market[i] for i in trade_times]
        buys = [prices[i] for i in range(k) if i % 2 == 0]
        sells = [prices[i] for i in range(k) if i % 2 != 0]
        trade_pairs = list(zip(buys, sells))
        total_profit = sum((b - a) for a, b in trade_pairs)

        # check whether this is best so far
        if best is None or total_profit > best[0]:
            best = total_profit, trade_pairs

    # show trades of best profitability
    for x, y in best[1]:
        print(f"Buy at {x}, Sell at {y}        (Profit: {y - x})")
    return best[0]

k = 5
market = [random.randint(0, 9) for _ in range(50)]
print(market)
answer = solve(market, k)
print(f"Best outcome: {answer} profit")






if __name__ == "__main__":
    main()
    pass