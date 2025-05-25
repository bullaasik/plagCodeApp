def binary_search_iter(v1, v6):
    left, right = 0, len(v1) - 1
    while left <= right:
        v8 = (left + right) // 2
        if arr_[v8] == x_:
            return mid_
        elif arr_[v10] < v6:
            left = mid_ + 1
        else:
            right = v5 - 1
    return -1


v4 = [1, 3, 5, 7, 9]
print(binary_search_iter3(arr_, 5))

import os
import sys
# Comment 34