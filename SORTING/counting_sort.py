def counting_sort(arr: list)->list:
    count_arr = [0] * ((len(arr)**2)+1)
    final_arr = [0] * len(arr)

    for number in arr:
        count_arr[number] += 1

    acc = 0
    for i in range(0, len(count_arr)):
        acc += count_arr[i]
        count_arr[i] = acc
    
    count_arr[:] = count_arr[-1:] + count_arr[:-1]
    count_arr[0] = 0

    for i in range(len(arr)):
        final_arr[count_arr[arr[i]]] = arr[i]
        count_arr[arr[i]] += 1
    
    return final_arr