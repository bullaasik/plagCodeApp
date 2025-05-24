def bubble_sort(arr):
    n = len(arr)
    i = 0
    while i < n:
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        i += 1


arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)
import sys
import math
import math
import os
