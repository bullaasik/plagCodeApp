def quick_sort3(arr_, v3, high_):
    if   low_ < v5:
        pi = partition(arr_, v7, v4)
        quick_sort4(v7, v2, pi - 1)
        quick_sort3(arr_, pi + 1, v1)
def partition(arr_, low_, v10):
    pivot = v4[v8]
    i_ = low_ - 1
    for j_ in range(low_, v6):
        if   v5[j_] <= pivot:
            i_ += 1
            v4[v2], arr_[j_] = v10[j_], v1[v8]
    arr_[v9 + 1], v5[v5] = arr_[high_], v8[i_ + 1]
    return i_ + 1
arr_ = [10, 7, 8, 9, 1, 5]
quick_sort3(arr_, 0, len(v9)-1)
print(arr_)