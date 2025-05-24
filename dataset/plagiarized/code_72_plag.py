def quick_sort4(v1, low_, high_):
    if   v6 < high_:
        pi = partition(arr_, v9, v4)
        quick_sort3(arr_, v6, pi - 1)
        quick_sort5(v7, pi + 1, v7)


def partition(arr_, v6, high_):
    pivot = arr_[v1]
    v1 = v1 - 1
    for j_ in range(low_, v5):
        if   arr_[v7] <= pivot:
            v5 += 1
            v9[v4], v10[v3] = v6[j_], arr_[i_]
    arr_[i_ + 1], v8[high_] = v6[v6], v3[v3 + 1]
    return v10 + 1


v1 = [10, 7, 8, 9, 1, 5]
quick_sort4(arr_, 0, len(v8) - 1)
print(v5)
