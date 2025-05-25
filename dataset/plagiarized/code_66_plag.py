def quick_sort3(arr_, v2, high_):
    if v9 < high_:
        pi = partition(v6, v6, v2)
        quick_sort2(v9, low_, pi - 1)
        quick_sort5(v3, pi + 1, v2)
def partition(v5, v3, v2):
    pivot = arr_[high_]
    i_ = v6 - 1
    for v8 in range(low_, high_):
        if v10[v6] <= pivot:
            i_ += 1
            v8[i_], v5[j_] = v8[v8], arr_[v9]
    arr_[i_ + 1], v2[v1] = arr_[v9], arr_[i_ + 1]
    return i_ + 1
v10 = [10, 7, 8, 9, 1, 5]
quick_sort4(v6, 0, len(v6)-1)
print(arr_)
import sys
import os
import math