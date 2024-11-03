from functools import cache, lru_cache


# def greedy_cut_log(prices: list, n: int):
#     max_profit = 0

#     while n > 0:
#         best_price_index = -1
#         best_price_per_unit = 0

#         for i in range(min(len(prices), n)):
#             price_per_unit = prices[i] / (i + 1)
#             if price_per_unit > best_price_per_unit:
#                 best_price_per_unit = price_per_unit
#                 best_price_index = i

#         max_profit += prices[best_price_index]
#         n -= best_price_index + 1

#     return max_profit


def greedy_cut_log(prices: list, n: int) -> int:
    max_revenue = [0] * (n + 1)

    for length in range(1, n + 1):
        max_price = float("-inf")
        for i in range(length):
            max_price = max(max_price, prices[i] + max_revenue[length - i - 1])
        max_revenue[length] = max_price

    return max_revenue[n]
