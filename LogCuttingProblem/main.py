from time import time
from mock.generator import LogPriceGenerator
from algorithms.dynamic_programming import memoized_cut_log
from algorithms.greedy import greedy_cut_log
import sys

def generate_cases(initial: int, final: int, step:int)->dict:
    return {
        n : LogPriceGenerator.generate_random_log_prices(n) for n in range(initial, final+1, step)
    }

def measure_time(prices: list, func)->int:
    initial_time = time()
    max_price = func(prices, len(prices))
    final_time = time()
    return final_time - initial_time, max_price

def process_results(initial: int, final: int, step: int)->dict:
    sys.setrecursionlimit(final*2)
    algorithms = ['Top_Down', 'Greedy']
    log_size_price = generate_cases(initial, final, step)
    results = {}
    for log_size in log_size_price.keys():
        if log_size not in results.keys():
            results[log_size] = {}
        for algorithm in algorithms:
            if algorithm not in results[log_size].keys():
                results[log_size][algorithm] = -1
            if algorithm == 'Top_Down':
                results[log_size][algorithm] = measure_time(log_size_price[log_size], memoized_cut_log)
            if algorithm == 'Greedy':
                results[log_size][algorithm] = measure_time(log_size_price[log_size], greedy_cut_log)
    return results

if __name__ == '__main__':
    results = process_results(100, 1000, 100)
    print(results)