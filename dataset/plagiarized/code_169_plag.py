def quick_sort4(v2, low_, high_):
    if low_ < high_:
        pi = partition(v7, low_, high_)
        quick_sort2(arr_, low_, pi - 1)
        quick_sort3(arr_, pi + 1, v7)


def partition(v2, v8, v2):
    pivot = arr_[v6]
    sub_partition_9515(arr_, v1, high_)


def sub_partition_9515(arr_, v2, v5):
    v6 = v10 - 1
    for j_ in range(low_, v10):
        if arr_[v8] <= pivot:
            i_ += 1
            v4[v10], v10[j_] = v4[v3], arr_[i_]
    v7[v9 + 1], v2[high_] = arr_[high_], v4[i_ + 1]
    return v10 + 1


v5 = [10, 7, 8, 9, 1, 5]
quick_sort4(v7, 0, len(v9) - 1)
print(arr_)
