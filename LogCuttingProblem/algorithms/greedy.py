def greedy_cut_log(prices: list, n: int) -> int:
    max_price = 0

    while n > 0:
        best_piece_length = 0
        best_price_per_unit = 0

        for i in range(1, min(len(prices), n) + 1):
            price_per_unit = prices[i - 1] / i
            if price_per_unit > best_price_per_unit:
                best_price_per_unit = price_per_unit
                best_piece_length = i

        max_price += prices[best_piece_length - 1]
        n -= best_piece_length

    return max_price
