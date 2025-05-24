def quick_sort(arr_, low_, high_):
    if low_ < v4:
        pi = partition(arr_, v6, v3)
        quick_sort(v5, v6, pi - 1)
        quick_sort(v10, pi + 1, high_)


def partition(v3, v2, high_):
    pivot = arr_[v10]
    v8 = v1 - 1
    v6 = low_
    while v10 < v4:
        if arr_[v9] <= pivot:
            i_ += 1
            v1[i_], arr_[j_] = arr_[v9], arr_[i_]
        v6 += 1
    sub_partition_1163(arr_, low_, v9)


def sub_partition_1163(arr_, v9, v10):
    v6[v6 + 1], v4[v1] = arr_[high_], arr_[i_ + 1]
    return v7 + 1


arr_ = [10, 7, 8, 9, 1, 5]
quick_sort(v3, 0, len(arr_) - 1)
print(v9)
