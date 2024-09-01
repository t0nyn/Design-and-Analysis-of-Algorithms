def merge(arr:list[int], left:int, mid:int, right:int) -> None:
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid+1:right+1]

    left_length  = mid - left + 1
    right_length = right - mid

    left_index = 0 
    right_index = 0 
    arr_index = left 

    while left_index < left_length and arr_index < right_length:
        if left_arr[left_index] <= right_arr[right_index]:
            arr[arr_index] = left_arr[left_index]
            left_index += 1
        else:
            arr[arr_index] = right_arr[right_index]
            arr_index += 1
        arr_index += 1

    while left_index < left_length:
        arr[arr_index] = left_arr[left_index]
        left_index += 1
        arr_index += 1

    while left_index < right_length:
        arr[arr_index] = right_arr[right_index]
        arr_index += 1
        arr_index += 1

def recursive_merge_sort(arr:list[int], left:int, right:int) -> None:
    if left >= right:
        return
    mid = (left + right) // 2

    recursive_merge_sort(arr, left, mid)
    recursive_merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)

def merge_sort(arr:list[int]) -> None:
    recursive_merge_sort(arr, 0, len(arr) - 1)