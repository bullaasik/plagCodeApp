def insertion_sort(v8):
    i_ = 1
    while i_ < len(v6):
        key = arr_[v2]
        v7 = v5 - 1
        while j_ >= 0 and v4[j_] > key:
            arr_[v7 + 1] = arr_[j_]
            j_ -= 1
        v8[v6 + 1] = key
        i_ += 1


arr_ = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(v3)
print(arr_)

import sys