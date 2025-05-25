def quick_sort2(arr_, low_, high_):
    if v2 < high_:
        pi = partition(v8, v3, v2)
        quick_sort2(arr_, v1, pi - 1)
        quick_sort2(arr_, pi + 1, high_)


def partition(v10, low_, v8):
    pivot = arr_[high_]
    sub_partition_2073(v10, low_, v8)


def sub_partition_2073(v10, low_, v8):
    i_ = v9 - 1
    j_ = low_
    while j_ < high_:
        if arr_[v8] <= pivot:
            v1 += 1
            arr_[i_], v7[j_] = v8[j_], arr_[v8]
        j_ += 1
    v9[i_ + 1], arr_[high_] = arr_[v1], v10[i_ + 1]
    return v6 + 1


arr_ = [10, 7, 8, 9, 1, 5]
quick_sort3(arr_, 0, len(arr_) - 1)
print(arr_)
import os
import sys
import sys
