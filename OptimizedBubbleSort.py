# Optimized Bubble Sort

def opt_bubSort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
data = [0,1,-2,8,-13,17,-19,32,-42]
opt_bubSort(data)
print(data)