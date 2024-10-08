import random
from datetime import datetime
from numpy import array

class NumberListGenerator:
    LOWER_RANDOM_BOUND = 0
    
    @staticmethod
    def generate_random_numbers(n: int, rpt: int)->list:
        UPPER_RANDOM_BOUND = n
        random.seed(42)
        return [[random.randint(NumberListGenerator.LOWER_RANDOM_BOUND, UPPER_RANDOM_BOUND) for number in range(n)] for _ in range(rpt)]

    @staticmethod
    def generate_sorted_numbers(n: int)->list:
        return list(range(1, n+1))

    @staticmethod
    def generate_reversed_numbers(n: int)->list:
        return list(range(n, 0, -1))

    @staticmethod
    def generate_nearly_sorted_numbers(n: int)->list:
        random.seed(42)
        sorted_numbers = NumberListGenerator.generate_sorted_numbers(n)
        for i in range(n//20):
            choice1 = random.randint(0, n-1)
            choice2 = random.randint(0, n-1)
            sorted_numbers[choice1], sorted_numbers[choice2] = sorted_numbers[choice2], sorted_numbers[choice1]

        return sorted_numbers
