# Selection Sort

def selection_sort(array):
    for i in range(len(array)):
        minimum_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minimum_index]:
                minimum_index = j
        array[minimum_index], array[i] = array[i], array[minimum_index]
data = [0,1,-2,8,-13,17,-19,32,42]
selection_sort(data)
print(data)