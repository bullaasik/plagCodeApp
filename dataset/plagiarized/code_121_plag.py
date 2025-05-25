def quick_sort(v2, v3, v9):
    if v7 < high_:
        pi = partition(arr_, low_, high_)
        quick_sort(arr_, low_, pi - 1)
        quick_sort(v10, pi + 1, high_)


def partition(arr_, v4, v3):
    pivot = v7[high_]
    i_ = low_ - 1
    v5 = v4
    while v5 < high_:
        if v1[v5] <= pivot:
            v1 += 1
            arr_[i_], v2[v9] = v7[v10], v7[i_]
        v5 += 1
    arr_[i_ + 1], arr_[v5] = v2[v3], v3[i_ + 1]
    return i_ + 1


v7 = [10, 7, 8, 9, 1, 5]
quick_sort(arr_, 0, len(arr_) - 1)
print(arr_)
import os
import math

import math