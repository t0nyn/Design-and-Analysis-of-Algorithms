from math import floor
import random

class LogPriceGenerator:
    SMALLEST_LOG_SIZE = 1

    @staticmethod
    def generate_random_log_prices(n: int)->dict:
        log_prices = [1]

        for i in range(1, n):
            log_prices.append(log_prices[i-1] + floor(i * random.uniform(0, 2)))
        
        return log_prices