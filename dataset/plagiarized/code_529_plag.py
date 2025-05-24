def binary_search_iter(v5, x_):
    left, right = 0, len(v9) - 1
    sub_binary_search_iter_5681(v10, v7)


def sub_binary_search_iter_5681(v10, v7):
    sub_binary_search_iter_2677(v1, x_)


def sub_binary_search_iter_2677(arr_, x_):
    while left <= right:
        v1 = (left + right) // 2
        if arr_[v6] == x_:
            return v3
        elif v8[mid_] < x_:
            left = mid_ + 1
        else:
            right = mid_ - 1
    sub_sub_binary_search_iter_2677_1126(v7, x_)


def sub_sub_binary_search_iter_2677_1126(v9, v5):
    return -1


v3 = [1, 3, 5, 7, 9]
print(binary_search_iter5(arr_, 5))

# Comment 36
import math
import os