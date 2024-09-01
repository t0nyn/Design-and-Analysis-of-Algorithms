import random

class NumberListGenerator:
    LOWER_RANDOM_BOUND = 0
    
    @staticmethod
    def generate_random_numbers(n: int, rpt: int)->list:
        UPPER_RANDOM_BOUND = n**2
        return [[random.randint(NumberListGenerator.LOWER_RANDOM_BOUND, UPPER_RANDOM_BOUND) for number in range(n)]for _ in range(rpt)]

    @staticmethod
    def generate_sorted_numbers(n: int)->list:
        return list(range(1, n+1))

    @staticmethod
    def generate_reversed_numbers(n: int)->list:
        return list(range(n, 0, -1))

    @staticmethod
    def generate_almost_sorted_numbers(n: int)->list:
        sorted_numbers = NumberListGenerator.generate_sorted_numbers(n)
        for i in range(n//20):
            choice1 = sorted_numbers.index(random.choice(sorted_numbers))
            choice2 = sorted_numbers.index(random.choice(sorted_numbers))
            sorted_numbers[choice1], sorted_numbers[choice2] = sorted_numbers[choice2], sorted_numbers[choice1]

        return sorted_numbers
