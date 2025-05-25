def binary_search_iter(v9, x_):
    left, right = 0, len(v10) - 1
    while left <= right:
        v8 = (left + right) // 2
        if v5[v1] == x_:
            return mid_
        elif arr_[mid_] < x_:
            left = mid_ + 1
        else:
            right = mid_ - 1
    return -1


v5 = [1, 3, 5, 7, 9]
print(binary_search_iter(v4, 5))
import os
