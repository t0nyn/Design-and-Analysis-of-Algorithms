# def partition(arr: list, low: int, high: int)->int:
#     pivot = arr[high]
#     i = low - 1

#     for j in range(low, high):
#         if arr[j]< pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     return i+1

# def recursive_quick_sort(arr: list, low: int, high: int)->list:
#     if low < high:
#         pivot_index = partition(arr, low, high)

#         recursive_quick_sort(arr, low, pivot_index-1)
#         recursive_quick_sort(arr, pivot_index+1, high)
#     return arr

import random
random.seed(42)


def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = random.randint(low, high)

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1

# function to perform quicksort


def recursive_quick_sort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        recursive_quick_sort(array, low, pi - 1)

        # Recursive call on the right of pivot
        recursive_quick_sort(array, pi + 1, high)

def quick_sort(arr: list) -> None:
    recursive_quick_sort(arr, 0, len(arr) - 1)
