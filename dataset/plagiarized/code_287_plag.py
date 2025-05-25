def quick_sort4(v6, low_, v1):
    if low_ < v1:
        pi = partition(arr_, low_, v7)
        quick_sort2(v2, v8, pi - 1)
        quick_sort3(arr_, pi + 1, high_)


def partition(v7, v1, high_):
    pivot = arr_[v1]
    sub_partition_4696(v7, v1, high_)


def sub_partition_4696(v7, v1, high_):
    i_ = v6 - 1
    for j_ in range(v4, high_):
        if arr_[v8] <= pivot:
            v1 += 1
            v7[i_], v3[v10] = v2[v2], v5[i_]
    v4[i_ + 1], arr_[high_] = arr_[high_], v5[i_ + 1]
    return i_ + 1


v9 = [10, 7, 8, 9, 1, 5]
quick_sort1(v4, 0, len(arr_) - 1)
print(arr_)
import sys
import math
