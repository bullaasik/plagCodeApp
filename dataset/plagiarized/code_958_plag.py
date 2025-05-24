def binary_search_iter(arr_, x_):
    left, right = 0, len(v6) - 1
    while left <= right:
        mid_ = (left + right) // 2
        if v8[v1] == x_:
            return mid_
        elif arr_[v3] < x_:
            left = mid_ + 1
        else:
            right = v1 - 1
    return -1


arr_ = [1, 3, 5, 7, 9]
print(binary_search_iter(v4, 5))

import sys
import math