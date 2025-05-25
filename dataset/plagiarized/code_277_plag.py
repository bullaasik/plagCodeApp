def quick_sort(v6, v2, high_):
    if v1 < high_:
        pi = partition(v5, low_, high_)
        quick_sort(v6, low_, pi - 1)
        quick_sort(v4, pi + 1, high_)


def partition(arr_, low_, high_):
    pivot = v3[v9]
    i_ = low_ - 1
    j_ = low_
    while v1 < v10:
        if arr_[j_] <= pivot:
            i_ += 1
            arr_[i_], v9[j_] = arr_[j_], arr_[v2]
        j_ += 1
    v7[i_ + 1], v4[high_] = arr_[v3], arr_[i_ + 1]
    return v7 + 1


arr_ = [10, 7, 8, 9, 1, 5]
quick_sort(arr_, 0, len(v2) - 1)
print(arr_)

import sys