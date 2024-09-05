from mock.generator import NumberListGenerator
from time import time
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.counting_sort import counting_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from algorithms.heap_sort import heap_sort
import json
import matplotlib.pyplot as plt
import sys


sorting_algorithms = [
    bubble_sort,
    insertion_sort,
    counting_sort,
    merge_sort,
    quick_sort,
    heap_sort
]

def generate_cases(initial:int, final:int, step:int)->dict:
    sys.setrecursionlimit(final*2)
    return {
        'random'       : {n:NumberListGenerator.generate_random_numbers(n, 10)          for n in range(initial, final, step)},
        'sorted'       : {n:[NumberListGenerator.generate_sorted_numbers(n)]            for n in range(initial, final, step)},
        'reversed'     : {n:[NumberListGenerator.generate_reversed_numbers(n)]          for n in range(initial, final, step)},
        'nearly_sorted': {n:[NumberListGenerator.generate_nearly_sorted_numbers(n)]     for n in range(initial, final, step)},
    }

def measure_time(list_of_arr:list[list[int]], func) -> int:
    results = []
    for arr in list_of_arr:
        initial_time = time()
        func(arr.copy())
        final_time = time()
        results.append(final_time - initial_time)
    return sum(results)/len(results)

def process_results(initial:int, final:int, step:int)->dict:
    cases = generate_cases(initial, final, step)
    results = {}
    for case in cases.keys():
        if case not in results.keys():
            results[case] = {}
        for n_case in cases[case].keys():
            if n_case not in results[case].keys():
                    results[case][n_case] = {}
            for algorithm in sorting_algorithms:
                results[case][n_case][algorithm.__name__] = measure_time(cases[case][n_case], algorithm)
    return results

def print_and_save_results(results: dict)->None:
    text = ''
    for case in results.keys():
        text += f'[[{case.replace('_', ' ').upper()}]]\n\n'
        line_format = '{:>9}     {:>9}     {:>9}     {:>9}     {:>9}     {:>9}     {:>9}\n'
        header = line_format.format('n','Bubble','Insertion','Merge','Heap','Quick','Counting')
        text += header
        text += '-' * len(header) + '\n'
        for n_case in results[case]:
            text += line_format .format(
                    '%d' % n_case,
                    '%2.6f' % results[case][n_case]['bubble_sort'],
                    '%2.6f' % results[case][n_case]['insertion_sort'],
                    '%2.6f' % results[case][n_case]['merge_sort'],
                    '%2.6f' % results[case][n_case]['heap_sort'],
                    '%2.6f' % results[case][n_case]['quick_sort'],
                    '%2.6f' % results[case][n_case]['counting_sort']
                )
        text += '\n\n' 
    with open('./result_tables.txt', 'w') as file:
        file.write(text)
    with open('./result_tables.json', 'w') as file:
        json.dump(results, file)
    print(text)

def plot_all_graphics(results: dict)->None:
    i = 0
    for test_type, test_size in results.items():
        plt.figure(i, figsize=(10,6))
        i+=1
        n_values = []
        algorithm_time = {}
        
        for n, sorting_algorithms in test_size.items():
            n_values.append(n)
            for sorting_algorithm, timestamp in sorting_algorithms.items():
                if sorting_algorithm not in algorithm_time:
                    algorithm_time[f'{sorting_algorithm}'] = []
                algorithm_time[f'{sorting_algorithm}'].append(timestamp)
        
        for algorithm, timestamp in algorithm_time.items():
            plt.plot(n_values, timestamp, label=f'{algorithm}')

        plt.xlabel('n')
        plt.ylabel('time')
        plt.title(f'{test_type}')
        plt.grid(True)
        plt.tight_layout()
        plt.legend()
        plt.show()

if __name__ == "__main__":
    results = process_results(10000, 50000, 10000)
    print_and_save_results(results)
    plot_all_graphics(results)