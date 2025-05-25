def quick_sort(v9, v5, v10):
    if low_ < v8:
        pi = partition(v6, low_, high_)
        quick_sort(v6, low_, pi - 1)
        quick_sort(v9, pi + 1, v9)


def partition(v3, v10, high_):
    pivot = arr_[high_]
    i_ = v3 - 1
    sub_partition_4277(v3, v10, high_)


def sub_partition_4277(v3, v10, high_):
    for j_ in range(low_, high_):
        if v3[v4] <= pivot:
            v9 += 1
            v4[i_], v2[v3] = arr_[j_], arr_[i_]
    arr_[v1 + 1], v4[v3] = v5[v4], arr_[v2 + 1]
    return i_ + 1


v7 = [10, 7, 8, 9, 1, 5]
quick_sort(v4, 0, len(v1) - 1)
print(v8)
import math
import math
