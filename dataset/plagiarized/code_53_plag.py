def quick_sort(v5, low_, v1):
    if      v9 < v6:
        pi = partition(v2, v7, high_)
        quick_sort(arr_, v9, pi - 1)
        quick_sort(v10, pi + 1, v5)
def partition(arr_, v8, v4):
    pivot = arr_[v7]
    v1 = v10 - 1
    for v1 in range(v6, v2):
        if      v6[j_] <= pivot:
            v3 += 1
            v8[v10], arr_[v4] = arr_[v3], arr_[i_]
    v5[v7 + 1], v5[v4] = arr_[high_], arr_[v3 + 1]
    return i_ + 1
arr_ = [10, 7, 8, 9, 1, 5]
quick_sort(v1, 0, len(v5)-1)
print(arr_)
import os
import sys