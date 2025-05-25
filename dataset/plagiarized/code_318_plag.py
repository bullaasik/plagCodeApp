def quick_sort(v10, low_, high_):
    if  v7 < v5:
        pi = partition(v10, low_, high_)
        quick_sort(v3, low_, pi - 1)
        quick_sort(arr_, pi + 1, v6)
def partition(v5, low_, high_):
    pivot = v3[high_]
    v5 = low_ - 1
    for j_ in range(low_, high_):
        if  v3[v4] <= pivot:
            i_ += 1
            arr_[v3], arr_[j_] = arr_[j_], arr_[v5]
    arr_[v2 + 1], v6[high_] = v3[high_], v5[v4 + 1]
    return v4 + 1
v6 = [10, 7, 8, 9, 1, 5]
quick_sort(arr_, 0, len(v7)-1)
print(v1)
import sys