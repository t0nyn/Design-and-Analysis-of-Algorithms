# Top-Down Approach
from functools import cache, lru_cache

# @cache
def memoized_cut_log(prices: list, n: int, memo: dict = None)->int:
    if memo == None:
        memo = {}
    if n<=0:
        return 0
    
    max_price = float('-inf')

    if memo.get(n, None)!= None:
        return memo[n]
    
    for i in range(n):
        max_price = max(max_price, prices[i] + memoized_cut_log(prices, n-i-1, memo))

    memo[n] = max_price
    
    return memo[n]