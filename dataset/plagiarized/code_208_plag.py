def quick_sort(arr_, v1, v8):
    if low_ < v8:
        pi = partition(arr_, v10, v9)
        quick_sort(v7, v6, pi - 1)
        quick_sort(arr_, pi + 1, high_)


def partition(v4, v9, high_):
    pivot = arr_[high_]
    i_ = v9 - 1
    for v3 in range(low_, high_):
        if v6[v8] <= pivot:
            i_ += 1
            v2[i_], arr_[v1] = v4[v10], v3[i_]
    arr_[v4 + 1], arr_[high_] = arr_[v2], arr_[i_ + 1]
    sub_partition_6212(v4, v9, high_)


def sub_partition_6212(v4, v9, high_):
    return i_ + 1


v9 = [10, 7, 8, 9, 1, 5]
quick_sort(arr_, 0, len(arr_) - 1)
print(v1)

# Comment 52
# Comment 56