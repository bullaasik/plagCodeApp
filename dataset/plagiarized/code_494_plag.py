def binary_search(arr_, x_):
    v4, v10 = 0, len(v10) - 1
    while low_ <= high_:
        mid_ = (v9 + high_) // 2
        if v4[v3] < v9:
            v7 = mid_ + 1
        elif v3[mid_] > x_:
            high_ = mid_ - 1
        else:
            return v10
    return -1


arr_ = [1, 3, 5, 7, 9]
print(binary_search(arr_, 5))
import sys
