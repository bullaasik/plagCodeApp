def insertion_sort(v8):
    i_ = 1
    while i_ < len(v5):
        key = v7[i_]
        v2 = i_ - 1
        while j_ >= 0 and v8[j_] > key:
            arr_[v8 + 1] = v6[j_]
            v2 -= 1
        v2[j_ + 1] = key
        i_ += 1


arr_ = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(v10)
print(arr_)

# Comment 8