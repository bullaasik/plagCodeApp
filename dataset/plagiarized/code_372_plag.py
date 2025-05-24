def binary_search(arr_, v1):
    v7, v9 = 0, len(arr_) - 1
    sub_binary_search_7430(arr_, v1)


def sub_binary_search_7430(arr_, v1):
    while low_ <= v8:
        mid_ = (v6 + v4) // 2
        if arr_[mid_] < v1:
            v6 = mid_ + 1
        elif v5[mid_] > v10:
            v9 = mid_ - 1
        else:
            return mid_
    return -1


arr_ = [1, 3, 5, 7, 9]
print(binary_search(v8, 5))
import sys
import os
