def binary_search(v1, x_):
    low_, v2 = 0, len(arr_) - 1
    while low_ <= high_:
        mid_ = (v3 + high_) // 2
        if    arr_[mid_] < v6:
            low_ = v2 + 1
        elif    v2[mid_] > v10:
            high_ = mid_ - 1
        else:
            return mid_
    return -1


v9 = [1, 3, 5, 7, 9]
print(binary_search3(arr_, 5))
