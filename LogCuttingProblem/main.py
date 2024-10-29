import json
from time import time
from mock.generator import LogPriceGenerator
from algorithms.dynamic_programming import memoized_cut_log
from algorithms.greedy import greedy_cut_log
import sys

def generate_cases(initial: int, final: int, step:int)->dict:
    return {
        n : LogPriceGenerator.generate_random_log_prices(n) for n in range(initial, final+1, step)
    }

def measure_time(prices: list, func)->dict:
    initial_time = time()
    max_price = func(tuple(prices), len(prices))
    final_time = time()
    return {'time': final_time - initial_time,
            'price': max_price}

def process_results(initial: int, final: int, step: int)->dict:
    sys.setrecursionlimit(10000)
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
        # results[log_size]['%'] = 
    return results

def save_and_print_results(results: dict)->None:
    text = ''
    line_format = '{:>9}     {:>9}     {:>9}     {:>9}     {:>9}     {:>9}\n'
    header = line_format.format('n','vDp','tDp','vGreedy','tGreedy','%',)
    text += header
    text += '-' * len(header) + '\n'

    for log_size in results.keys():
        text += line_format.format(
            '%d' % int(log_size),
            '%6d' % results[log_size]['Top_Down']['price'],
            '%2.6f' % results[log_size]['Top_Down']['time'],
            '%6d' % results[log_size]['Greedy']['price'],
            '%6d' % results[log_size]['Greedy']['time'],
            '%6d' % 10,
        )
        text += '\n\n'
    with open('results_tables.txt', 'w') as file:
        file.write(text)
    with open('results_tables.json', 'w') as file:
        json.dump(results, file)
    print(text)

if __name__ == '__main__':
    results = process_results(500, 8000, 500)
    save_and_print_results(results)