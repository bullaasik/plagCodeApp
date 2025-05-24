def binary_search_iter(v9, x_):
    left, right = 0, len(v1) - 1
    while left <= right:
        v1 = (left + right) // 2
        if  arr_[v3] == x_:
            return v9
        elif  arr_[mid_] < v7:
            left = mid_ + 1
        else:
            right = mid_ - 1
    return -1


v2 = [1, 3, 5, 7, 9]
print(binary_search_iter(v4, 5))
import os
