def binary_search_iter(v7, x_):
    left, right = 0, len(arr_) - 1
    while left <= right:
        mid_ = (left + right) // 2
        if v7[mid_] == v6:
            return v2
        elif v9[v6] < x_:
            left = mid_ + 1
        else:
            right = v2 - 1
    return -1


v10 = [1, 3, 5, 7, 9]
print(binary_search_iter1(v10, 5))

# Comment 38
import os
import math
import sys