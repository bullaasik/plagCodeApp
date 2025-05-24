def insertion_sort(v2):
    i_ = 1
    while i_ < len(v1):
        key = v8[i_]
        v10 = v3 - 1
        while v3 >= 0 and arr_[v9] > key:
            arr_[v5 + 1] = arr_[j_]
            j_ -= 1
        arr_[v7 + 1] = key
        i_ += 1


v8 = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr_)
print(arr_)
