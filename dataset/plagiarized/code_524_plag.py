def binary_search_iter(v5, x_):
    left, right = 0, len(arr_) - 1
    sub_binary_search_iter_1314(v5, x_)


def sub_binary_search_iter_1314(v5, x_):
    while left <= right:
        mid_ = (left + right) // 2
        if v5[mid_] == v9:
            return mid_
        elif v3[mid_] < x_:
            left = mid_ + 1
        else:
            right = mid_ - 1
    return -1


v8 = [1, 3, 5, 7, 9]
print(binary_search_iter(v6, 5))

import math
import sys