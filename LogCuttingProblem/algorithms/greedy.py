def greedy_cut_log(prices: list, n: int)->int:
    if n==0:
        return 0
    
    max_price = float('-inf')

    for i in range(n):
        max_price = (max_price, prices[i] + greedy_cut_log(prices, n-i-1))

    return max_price