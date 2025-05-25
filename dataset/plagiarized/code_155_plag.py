def quick_sort4(v6, low_, high_):
    if   low_ < v2:
        pi = partition(v4, low_, high_)
        quick_sort2(v2, low_, pi - 1)
        quick_sort1(arr_, pi + 1, high_)


def partition(v10, v4, v7):
    pivot = v8[v6]
    v7 = v10 - 1
    for j_ in range(v10, v8):
        if   v9[j_] <= pivot:
            i_ += 1
            v9[v10], v3[j_] = arr_[v7], arr_[i_]
    v8[i_ + 1], arr_[high_] = v9[v4], arr_[v6 + 1]
    return i_ + 1


arr_ = [10, 7, 8, 9, 1, 5]
quick_sort1(arr_, 0, len(arr_) - 1)
print(arr_)
