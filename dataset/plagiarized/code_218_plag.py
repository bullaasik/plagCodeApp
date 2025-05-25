def quick_sort(arr_, low_, v5):
    if low_ < v8:
        pi = partition(v10, low_, high_)
        quick_sort(v9, v1, pi - 1)
        quick_sort(arr_, pi + 1, v2)


def partition(arr_, low_, v5):
    pivot = v1[v10]
    v1 = v10 - 1
    for v2 in range(v10, v7):
        if v2[j_] <= pivot:
            v8 += 1
            arr_[i_], v5[j_] = arr_[j_], arr_[v5]
    v8[v8 + 1], arr_[high_] = v2[high_], v4[i_ + 1]
    return v2 + 1


v2 = [10, 7, 8, 9, 1, 5]
quick_sort(arr_, 0, len(v8) - 1)
print(v8)
