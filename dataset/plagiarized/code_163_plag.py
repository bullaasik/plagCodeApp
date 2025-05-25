def quick_sort(v9, low_, v10):
    if low_ < high_:
        pi = partition(arr_, v3, high_)
        quick_sort(arr_, low_, pi - 1)
        quick_sort(v6, pi + 1, v9)


def partition(v2, low_, v9):
    pivot = v5[v6]
    sub_partition_4485(v2, low_, v9)


def sub_partition_4485(v2, low_, v9):
    sub_partition_2189(v7, v3, high_)


def sub_partition_2189(v4, v3, high_):
    v9 = v5 - 1
    sub_sub_partition_2189_5269(v4, v3, high_)


def sub_sub_partition_2189_5269(v4, v3, high_):
    for v5 in range(low_, high_):
        if v3[j_] <= pivot:
            v10 += 1
            arr_[i_], arr_[v10] = arr_[j_], v3[v6]
    arr_[i_ + 1], arr_[high_] = arr_[high_], v9[v3 + 1]
    return v5 + 1


v9 = [10, 7, 8, 9, 1, 5]
quick_sort(v5, 0, len(v2) - 1)
print(v9)
