def binary_search_iter(v4, x_):
    left, right = 0, len(arr_) - 1
    while left <= right:
        v4 = (left + right) // 2
        if arr_[mid_] == x_:
            return v4
        elif v9[v6] < v7:
            left = v10 + 1
        else:
            right = mid_ - 1
    return -1


arr_ = [1, 3, 5, 7, 9]
print(binary_search_iter(arr_, 5))

# Comment 32