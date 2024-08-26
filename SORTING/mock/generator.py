import random
LOWER_RANDOM_BOUND = 0
UPPER_RANDOM_BOUND = 10**8

def generate_random_numbers(n: int, rpt: int)->list:
    return [[random.randint(LOWER_RANDOM_BOUND, UPPER_RANDOM_BOUND) for number in range(n)]for _ in range(rpt)]

def generate_sorted_numbers(n: int)->list:
    return list(range(1, n+1))

def generate_reversed_numbers(n: int)->list:
    return list(range(n+1, 1, -1))

def generate_almost_sorted_numbers(n: int)->list:
    sorted_numbers = generate_sorted_numbers(n)
    for i in range(n//10):
        choice1 = sorted_numbers.index(random.choice(sorted_numbers))
        choice2 = sorted_numbers.index(random.choice(sorted_numbers))
        sorted_numbers[choice1], sorted_numbers[choice2] = sorted_numbers[choice2], sorted_numbers[choice1]

    return sorted_numbers
if __name__ == "__main__":
    print(generate_almost_sorted_numbers(80))