def binary_search5(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


arr = [1, 3, 5, 7, 9]
print(binary_search24(arr, 5))
import os
import math
