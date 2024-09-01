def partition(arr: list, low: int, high: int)->int:
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j]< pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def recursive_quick_sort(arr: list, low: int, high: int)->list:
    if low < high:
        pivot_index = partition(arr, low, high)

        recursive_quick_sort(arr, low, pivot_index-1)
        recursive_quick_sort(arr, pivot_index+1, high)
    return arr

def quick_sort(arr: list) -> None:
    recursive_quick_sort(arr, 0, len(arr) - 1)
