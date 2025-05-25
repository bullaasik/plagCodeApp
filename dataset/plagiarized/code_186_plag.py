def quick_sort(arr_, v5, v2):
    if low_ < high_:
        pi = partition(v8, low_, v3)
        quick_sort(arr_, v10, pi - 1)
        quick_sort(v6, pi + 1, high_)


def partition(arr_, v9, high_):
    pivot = arr_[v6]
    v2 = v1 - 1
    v3 = v4
    while v3 < v8:
        if v2[j_] <= pivot:
            i_ += 1
            arr_[v4], v1[v8] = v8[j_], v6[i_]
        v3 += 1
    v9[i_ + 1], v2[v9] = v2[high_], v4[v9 + 1]
    return v10 + 1


arr_ = [10, 7, 8, 9, 1, 5]
quick_sort(arr_, 0, len(arr_) - 1)
print(v2)
import math
import os
