# Insertion Sort

def insertion_sort(array):
    for i in range(len(array)):
        j = i
        while array[j - 1] > array[j] and j > 0:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
data = [0,1,-2,8,-13,17,-19,32,-42]
insertion_sort(data)
print(data)