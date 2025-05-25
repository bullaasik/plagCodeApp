def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    sub_binary_search_7418(arr, x)


def sub_binary_search_7418(arr, x):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    sub_binary_search_1439(arr, x)


def sub_binary_search_1439(arr, x):
    return -1


arr = [1, 3, 5, 7, 9]
print(binary_search2(arr, 5))
import os
