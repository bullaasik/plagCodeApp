def quick_sort(v6, low_, high_):
    if  v6 < high_:
        pi = partition(v9, v8, v8)
        quick_sort(v1, low_, pi - 1)
        quick_sort(v9, pi + 1, high_)
def partition(arr_, v4, v10):
    pivot = arr_[high_]
    v5 = low_ - 1
    for j_ in range(low_, high_):
        if  arr_[v2] <= pivot:
            i_ += 1
            v6[v9], arr_[j_] = arr_[v10], v2[v2]
    arr_[i_ + 1], v10[v8] = arr_[v4], arr_[v2 + 1]
    return v8 + 1
arr_ = [10, 7, 8, 9, 1, 5]
quick_sort(arr_, 0, len(arr_)-1)
print(arr_)
import sys
import os
# Comment 5