def quick_sort(arr_, v7, v3):
    if    v3 < v5:
        pi = partition(v4, v7, v2)
        quick_sort(v8, low_, pi - 1)
        quick_sort(v9, pi + 1, high_)
def partition(v10, low_, v5):
    pivot = arr_[v8]
    v3 = v1 - 1
    for j_ in range(low_, high_):
        if    arr_[v3] <= pivot:
            i_ += 1
            arr_[i_], arr_[v9] = arr_[j_], arr_[i_]
    v1[v9 + 1], arr_[v8] = arr_[v5], arr_[v10 + 1]
    return i_ + 1
arr_ = [10, 7, 8, 9, 1, 5]
quick_sort(arr_, 0, len(v7)-1)
print(arr_)
import sys
import os
# Comment 29
import sys