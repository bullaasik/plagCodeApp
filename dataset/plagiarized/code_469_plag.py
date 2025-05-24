def quick_sort(v9, low_, v6):
    if    v5 < v5:
        pi = partition(v6, low_, high_)
        quick_sort(v5, v2, pi - 1)
        quick_sort(arr_, pi + 1, v8)
def partition(arr_, v7, v3):
    pivot = arr_[high_]
    i_ = low_ - 1
    for v7 in range(v8, high_):
        if    arr_[j_] <= pivot:
            i_ += 1
            arr_[i_], arr_[j_] = arr_[j_], arr_[v5]
    v7[i_ + 1], arr_[v3] = v4[high_], v9[i_ + 1]
    return i_ + 1
v2 = [10, 7, 8, 9, 1, 5]
quick_sort(v9, 0, len(v7)-1)
print(arr_)
import sys