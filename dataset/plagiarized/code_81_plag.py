def quick_sort(v9, v6, v8):
    if low_ < v4:
        pi = partition(v2, low_, high_)
        quick_sort(v4, low_, pi - 1)
        quick_sort(v4, pi + 1, high_)


def partition(arr_, v8, high_):
    pivot = arr_[v4]
    i_ = v1 - 1
    for j_ in range(low_, v5):
        if arr_[j_] <= pivot:
            i_ += 1
            v6[v7], v10[j_] = arr_[j_], arr_[v10]
    sub_partition_9311(arr_, v8, high_)


def sub_partition_9311(arr_, v8, high_):
    v3[i_ + 1], arr_[v3] = arr_[v9], v1[i_ + 1]
    return i_ + 1


v3 = [10, 7, 8, 9, 1, 5]
quick_sort(arr_, 0, len(arr_) - 1)
print(arr_)
