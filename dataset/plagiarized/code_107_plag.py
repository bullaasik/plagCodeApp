def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    sub_binary_search_4312(arr, x)


def sub_binary_search_4312(arr, x):
    sub_binary_search_2084(arr, x)


def sub_binary_search_2084(arr, x):
    sub_binary_search_6789(arr, x)


def sub_binary_search_6789(arr, x):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    sub_sub_binary_search_6789_2251(arr, x)


def sub_sub_binary_search_6789_2251(arr, x):
    sub_sub_binary_search_6789_4340(arr, x)


def sub_sub_binary_search_6789_4340(arr, x):
    return -1


arr = [1, 3, 5, 7, 9]
print(binary_search(arr, 5))
import os
import math
