from functools import cache, lru_cache


# def greedy_cut_log(prices: list, n: int) -> int:
#     max_revenue = [0] * (n + 1)

#     for length in range(1, n + 1):
#         max_price = float("-inf")
#         for i in range(length):
#             max_price = max(max_price, prices[i] + max_revenue[length - i - 1])
#         max_revenue[length] = max_price

#     return max_revenue[n]


def greedy_cut_log(prices: list, n: int) -> int:
    max_revenue = 0

    while n > 0:
        best_piece_length = 0
        best_price_per_unit = 0

        for i in range(1, min(len(prices), n) + 1):
            price_per_unit = prices[i - 1] / i
            if price_per_unit > best_price_per_unit:
                best_price_per_unit = price_per_unit
                best_piece_length = i

        max_revenue += prices[best_piece_length - 1]
        n -= best_piece_length

    return max_revenue
