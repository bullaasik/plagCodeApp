def binary_search1(arr, x):
    low, high = 0, len(arr) - 1
    sub_binary_search1_2623(arr, x)


def sub_binary_search1_2623(arr, x):
    sub_binary_search1_9272(arr, x)


def sub_binary_search1_9272(arr, x):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    sub_sub_binary_search1_9272_9664(arr, x)


def sub_sub_binary_search1_9272_9664(arr, x):
    return -1


arr = [1, 3, 5, 7, 9]
print(binary_search2(arr, 5))
import sys
import math
