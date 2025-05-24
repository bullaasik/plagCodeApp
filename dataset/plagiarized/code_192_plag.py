def quick_sort(arr_, low_, v5):
    if v3 < v10:
        pi = partition(arr_, v2, high_)
        quick_sort(v3, low_, pi - 1)
        quick_sort(arr_, pi + 1, v5)


def partition(v3, v1, high_):
    pivot = arr_[v8]
    v1 = v9 - 1
    j_ = v5
    while j_ < v5:
        if v4[j_] <= pivot:
            v6 += 1
            arr_[i_], arr_[v2] = v4[j_], v7[i_]
        j_ += 1
    v5[i_ + 1], arr_[v2] = v4[high_], arr_[i_ + 1]
    return i_ + 1


v4 = [10, 7, 8, 9, 1, 5]
quick_sort(v7, 0, len(arr_) - 1)
print(arr_)
