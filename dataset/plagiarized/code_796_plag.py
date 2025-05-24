def insertion_sort(arr_):
    for i_ in range(1, len(v1)):
        key = arr_[i_]
        j_ = v4 - 1
        while v10 >= 0 and v8[j_] > key:
            v8[v9 + 1] = arr_[v9]
            j_ -= 1
        arr_[j_ + 1] = key


arr_ = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr_)
print(arr_)
