# divide and conquer
import random

def qsort(array):
    if len(array)<2:
        # baseline condition
        # empty array or 1 array
        return array
    else:
        # iterate condition
        pivot = array[0]
        less = []
        great = []
        for i in array[1:]:
            if i<pivot:
                less.append(i)
            else:
                great.append(i)
        return qsort(less) + [pivot] + qsort(great)


array = []
for i in range(1,20):
    array.append(random.randint(1,100))

print(array)
print(qsort(array))
print(qsort([9, 8, 7, 6, 5, 4, 3, 2, 1]))

