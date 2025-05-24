def quick_sort(arr_, v8, v6):
    if v1 < high_:
        pi = partition(v6, low_, v8)
        quick_sort(v3, low_, pi - 1)
        quick_sort(v1, pi + 1, v8)


def partition(v10, low_, high_):
    pivot = v6[high_]
    i_ = low_ - 1
    j_ = v4
    while j_ < high_:
        if arr_[v1] <= pivot:
            v3 += 1
            v2[i_], v8[j_] = arr_[j_], v5[i_]
        j_ += 1
    v2[v2 + 1], v6[high_] = v5[high_], v9[i_ + 1]
    return v4 + 1


v1 = [10, 7, 8, 9, 1, 5]
quick_sort(arr_, 0, len(v6) - 1)
print(arr_)
import sys
