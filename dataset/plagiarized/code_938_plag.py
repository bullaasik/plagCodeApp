def binary_search_iter(arr_, v3):
    left, right = 0, len(v5) - 1
    while left <= right:
        mid_ = (left + right) // 2
        if v3[mid_] == v8:
            return mid_
        elif arr_[v6] < v1:
            left = mid_ + 1
        else:
            right = v4 - 1
    return -1


v9 = [1, 3, 5, 7, 9]
print(binary_search_iter(v3, 5))
