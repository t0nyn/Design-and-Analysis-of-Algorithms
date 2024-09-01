from mock.generator import NumberListGenerator
from time import time
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.counting_sort import counting_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from algorithms.heap_sort import heap_sort

sorting_algorithms = [
    bubble_sort,
    insertion_sort,
    counting_sort,
    merge_sort,
    quick_sort,
    heap_sort
]

def generate_cases(initial:int, final:int, step:int):
    return {
        'random'       : {n:NumberListGenerator.generate_random_numbers(n, 10)          for n in range(initial, final, step)},
        'sorted'       : {n:[NumberListGenerator.generate_sorted_numbers(n)]            for n in range(initial, final, step)},
        'reversed'     : {n:[NumberListGenerator.generate_reversed_numbers(n)]          for n in range(initial, final, step)},
        'almost_sorted': {n:[NumberListGenerator.generate_almost_sorted_numbers(n)]     for n in range(initial, final, step)},
    }

def measure_time(list_of_arr:list[list[int]], func) -> int:
    results = []
    for arr in list_of_arr:
        initial_time = time()
        func(arr.copy())
        final_time = time()
        results.append(final_time - initial_time)
    return sum(results)/len(results)

def process_results(initial:int, final:int, step:int):
    cases = generate_cases(initial, final, step)
    results = {}
    for case in cases.keys():
        for n_case in cases[case].keys():
            for algorithm in sorting_algorithms:
                if case not in results.keys():
                    results[case] = {}
                if n_case not in results[case].keys():
                    results[case][n_case] = {}
                results[case][n_case][algorithm.__name__] = measure_time(cases[case][n_case], algorithm)
    return results

def print_results(results):
    for case in results.keys():
        print(f'[[{case.replace('_', ' ').upper()}]]')
        print('      n\t   Bubble\tInsertion\t    Merge\t     Heap\t    Quick\t Counting')
        print('--------------------------------------------------------------------------------------------')
        for n_case in results[case]:
            print(
                '%7d    %2.6f\t%2.6f\t%2.6f\t%2.6f\t%2.6f\t%2.6f' %
                (n_case,
                results[case][n_case]['bubble_sort'],
                results[case][n_case]['insertion_sort'],
                results[case][n_case]['merge_sort'],
                results[case][n_case]['heap_sort'],
                results[case][n_case]['quick_sort'],
                results[case][n_case]['counting_sort'])
            )
        print('\n\n')
            
if __name__ == "__main__":
    results = process_results(100, 1000, 100)
    print_results(results)
   

    
    