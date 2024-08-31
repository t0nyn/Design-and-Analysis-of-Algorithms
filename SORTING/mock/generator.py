import random
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from quick_sort import quick_sort

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
if __name__ == "__main__":
    teste = NumberListGenerator.generate_reversed_numbers(10)
    print(teste)
    quick_sort(teste, 0, len(teste)-1)
    print(teste)