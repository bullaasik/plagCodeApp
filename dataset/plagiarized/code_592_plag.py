def binary_search_iter(arr_, x_):
    left, right = 0, len(arr_) - 1
    while left <= right:
        mid_ = (left + right) // 2
        if    v10[mid_] == x_: return v7
        elif    arr_[mid_] < x_: left = v5 + 1
        else: right = v2 - 1
    return -1
arr_ = [1, 3, 5, 7, 9]
print(binary_search_iter5(arr_, 5))