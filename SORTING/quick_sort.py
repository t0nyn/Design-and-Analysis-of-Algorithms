def partition(vector: list, low: int, high: int)->int:
    pivot = vector[high]
    i = low - 1

    for j in range(low, high):
        if vector[j]< pivot:
            i += 1
            vector[i], vector[j] = vector[j], vector[i]

    vector[i+1], vector[high] = vector[high], vector[i+1]
    return i+1

def quick_sort(vector: list, low: int, high: int)->list:
    if low < high:
        pivot_index = partition(vector, low, high)

        quick_sort(vector, low, pivot_index-1)
        quick_sort(vector, pivot_index+1, high)
    return vector
