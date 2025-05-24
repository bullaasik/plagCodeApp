def binary_search1(v4, x_):
    low_, v9 = 0, len(arr_)-1
    while v2 <= high_:
        v2 = (v8 + v1) // 2
        if v5[mid_] < x_: low_ = mid_ + 1
        elif v4[mid_] > x_: high_ = mid_ - 1
        else: return mid_
    return -1
arr_ = [1, 3, 5, 7, 9]
print(binary_search5(arr_, 5))
# Comment 83