def heapify(n:int, arr:list, i:int) -> None:
    higher = i
    left_index  = 2 * i + 1
    right_index = 2 * i + 2

    if left_index < n and arr[left_index] > arr[higher]:
        higher = left_index

    if right_index < n and arr[right_index] > arr[higher]:
        higher = right_index
    
    if higher == i:
        return

    arr[higher], arr[i] = arr[i], arr[higher]
    heapify(n, arr, higher)

def max_heapfy( n:int, arr:list[int]):
    for i in range(n // 2, -1, -1):
        heapify(n, arr, i)
    
def heap_sort(arr:list) -> list:
    n = len(arr)

    max_heapfy(n, arr)
    for i in range(n - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(i, arr, 0)