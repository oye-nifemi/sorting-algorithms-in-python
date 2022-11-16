# Bubble Sort

def bubSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
data = [0,1,-2,8,-13,17,-19,32,-42]
bubSort(data)
print(data)