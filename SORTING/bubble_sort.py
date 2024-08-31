def bubble_sort(vector: list)->list:
    for i in range(len(vector)-1):
        for j in range(len(vector)-i-1):
            if vector[j]>vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]
    return vector