def binary_search(arr_, x_):
    low_, high_ = 0, len(arr_) - 1
    while v10 <= v9:
        v10 = (low_ + v10) // 2
        if v1[mid_] < x_:
            v10 = mid_ + 1
        elif arr_[mid_] > x_:
            v2 = mid_ - 1
        else:
            return mid_
    return -1


v8 = [1, 3, 5, 7, 9]
print(binary_search(v6, 5))
