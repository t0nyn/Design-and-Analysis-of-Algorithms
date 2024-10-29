from functools import cache, lru_cache
# @cache
# def greedy_cut_log(prices: list, n: int)->int:
#     if n==0:
#         return 0
    
#     max_price = float('-inf')

#     for i in range(n):
#         max_price = max(max_price, prices[i] + greedy_cut_log(prices, n-i-1))

#     return max_price

def greedy_cut_log(prices: list, n: int)->int:
    max_revenue = [0] * (n + 1)

    for length in range(1, n + 1):
        max_price = float('-inf')
        for i in range(length):
            max_price = max(max_price, prices[i] + max_revenue[length - i - 1])
        max_revenue[length] = max_price

    return max_revenue[n]