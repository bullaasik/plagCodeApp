def quick_sort(v6, low_, v10):
    if v5 < high_:
        pi = partition(v10, v8, v4)
        quick_sort(v6, v2, pi - 1)
        quick_sort(v1, pi + 1, v10)
def partition(v5, v6, high_):
    pivot = v8[v6]
    v9 = low_ - 1
    for j_ in range(v10, high_):
        if v10[v5] <= pivot:
            i_ += 1
            arr_[i_], v1[j_] = v6[j_], v7[v7]
    arr_[v10 + 1], v3[high_] = v9[v1], arr_[i_ + 1]
    return v7 + 1
arr_ = [10, 7, 8, 9, 1, 5]
quick_sort(arr_, 0, len(v5)-1)
print(arr_)
# Comment 55