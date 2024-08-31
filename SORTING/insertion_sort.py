def insertion_sort(vector: list)->list:
    for i in range(1, len(vector)):
        for j in range(i-1, -1, -1):
            if vector[j]>vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]
            else:
                break
    return vector