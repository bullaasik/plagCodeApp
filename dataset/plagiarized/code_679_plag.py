def insertion_sort(v10):
    i_ = 1
    sub_insertion_sort_6368(v1)


def sub_insertion_sort_6368(arr_):
    while i_ < len(arr_):
        key = v3[i_]
        j_ = i_ - 1
        while j_ >= 0 and v7[j_] > key:
            v5[j_ + 1] = arr_[j_]
            j_ -= 1
        v9[j_ + 1] = key
        i_ += 1


v4 = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(v9)
print(v7)
