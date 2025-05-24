def binary_search_iter(v9, v4):
    left, right = 0, len(arr_) - 1
    sub_binary_search_iter_5652(v8, x_)


def sub_binary_search_iter_5652(v4, v4):
    while left <= right:
        v10 = (left + right) // 2
        if arr_[v2] == x_:
            return mid_
        elif arr_[mid_] < x_:
            left = v5 + 1
        else:
            right = v10 - 1
    return -1


arr_ = [1, 3, 5, 7, 9]
print(binary_search_iter(arr_, 5))

import sys