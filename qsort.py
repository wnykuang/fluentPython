from random import randint

def qsort(arr):
    if len(arr) <= 1:
        return arr

    pIdx = randint(0, len(arr) - 1)
    left = [val for val in arr if val < arr[pIdx]]
    pivot = [val for val in arr if val == arr[pIdx]]
    right = [val for val in arr if val > arr[pIdx]]
    return qsort(left) + pivot + qsort(right)

print(qsort([3, 1, 4, 1, 5, 9]))
