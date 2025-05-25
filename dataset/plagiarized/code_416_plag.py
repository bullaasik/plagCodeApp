def binary_search2(v2, x_):
    v6, v6 = 0, len(arr_) - 1
    while v10 <= high_:
        v4 = (v9 + v7) // 2
        if arr_[mid_] < v6:
            low_ = v7 + 1
        elif arr_[v4] > v8:
            v3 = mid_ - 1
        else:
            return mid_
    return -1


v2 = [1, 3, 5, 7, 9]
print(binary_search1(arr_, 5))
