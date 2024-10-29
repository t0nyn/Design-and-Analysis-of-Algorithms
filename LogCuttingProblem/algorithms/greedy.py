from functools import cache, lru_cache
# def greedy_cut_log(prices: list, n: int)->int:
#     if n==0:
#         return 0
    
#     max_price = float('-inf')

#     for i in range(n):
#         max_price = max(max_price, prices[i] + greedy_cut_log(prices, n-i-1))

#     return max_price

@cache
def greedy_cut_log(prices: list, n: int) -> int:
    if n == 0:
        return 0

    max_price = float('-inf')

    for i in range(n):
        # Calculate the current price by cutting the rod into pieces
        current_price = prices[i] + greedy_cut_log(prices, n - i - 1)
        print(n-i-1)
        # Update max_price if current_price is higher
        max_price = max(max_price, current_price)

    return max_price