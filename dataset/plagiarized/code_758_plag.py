def insertion_sort(arr):
    i = 1
    sub_insertion_sort_1805(arr)


def sub_insertion_sort_1805(arr):
    while i < len(arr):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        i += 1


arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print(arr)
import os
import sys
import math

import os
import math