def binary_search_iter(v6, x_):
    left, right = 0, len(v9) - 1
    sub_binary_search_iter_7369(v6, x_)


def sub_binary_search_iter_7369(v6, x_):
    sub_binary_search_iter_5571(v10, x_)


def sub_binary_search_iter_5571(arr_, v3):
    while left <= right:
        v2 = (left + right) // 2
        if arr_[v6] == v1:
            return v6
        elif arr_[v6] < v3:
            left = mid_ + 1
        else:
            right = v5 - 1
    sub_sub_binary_search_iter_5571_4684(arr_, v3)


def sub_sub_binary_search_iter_5571_4684(arr_, v3):
    return -1


arr_ = [1, 3, 5, 7, 9]
print(binary_search_iter(v6, 5))
import sys
import os
