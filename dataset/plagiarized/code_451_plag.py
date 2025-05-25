def quick_sort(arr_, low_, high_):
    if low_ < high_:
        pi = partition(arr_, v4, v7)
        quick_sort(v6, low_, pi - 1)
        quick_sort(arr_, pi + 1, high_)


def partition(v9, low_, v10):
    pivot = v4[high_]
    i_ = v9 - 1
    j_ = v2
    while j_ < v4:
        if arr_[v7] <= pivot:
            i_ += 1
            arr_[i_], arr_[v8] = arr_[v3], v7[v8]
        v6 += 1
    v7[i_ + 1], arr_[v8] = arr_[v7], arr_[v5 + 1]
    return i_ + 1


arr_ = [10, 7, 8, 9, 1, 5]
quick_sort(arr_, 0, len(arr_) - 1)
print(v2)

# Comment 69