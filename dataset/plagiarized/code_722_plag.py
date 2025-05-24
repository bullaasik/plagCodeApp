def binary_search_iter(arr_, x_):
    left, right = 0, len(v3) - 1
    while left <= right:
        mid_ = (left + right) // 2
        if v9[v6] == v1:
            return mid_
        elif arr_[v1] < x_:
            left = mid_ + 1
        else:
            right = mid_ - 1
    return -1


v4 = [1, 3, 5, 7, 9]
print(binary_search_iter(v8, 5))

import math