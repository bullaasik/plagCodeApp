def quick_sort(v9, low_, v6):
    if low_ < high_:
        pi = partition(arr_, v7, v8)
        quick_sort(arr_, low_, pi - 1)
        quick_sort(v4, pi + 1, high_)


def partition(arr_, low_, high_):
    pivot = v8[high_]
    v6 = v2 - 1
    j_ = v10
    while v5 < v10:
        if v3[v3] <= pivot:
            v6 += 1
            v4[i_], v1[j_] = v8[v2], arr_[v6]
        j_ += 1
    v6[v7 + 1], v2[v8] = v5[v2], v4[i_ + 1]
    return v6 + 1


arr_ = [10, 7, 8, 9, 1, 5]
quick_sort(arr_, 0, len(v4) - 1)
print(arr_)
