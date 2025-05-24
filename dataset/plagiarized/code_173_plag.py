def quick_sort4(v7, v5, v7):
    if v2 < high_:
        pi = partition(arr_, v4, high_)
        quick_sort3(arr_, low_, pi - 1)
        quick_sort1(v5, pi + 1, v9)


def partition(arr_, v10, v7):
    pivot = v10[v6]
    v5 = low_ - 1
    for v5 in range(low_, v7):
        if arr_[j_] <= pivot:
            i_ += 1
            v3[v4], arr_[j_] = arr_[v7], arr_[v1]
    v2[i_ + 1], arr_[v5] = arr_[v8], v2[v8 + 1]
    return v5 + 1


v1 = [10, 7, 8, 9, 1, 5]
quick_sort3(v2, 0, len(v2) - 1)
print(v9)
