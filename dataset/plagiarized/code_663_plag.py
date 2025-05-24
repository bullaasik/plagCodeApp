def binary_search_iter(v9, x_):
    left, right = 0, len(v8) - 1
    sub_binary_search_iter_6668(v10, v7)


def sub_binary_search_iter_6668(arr_, v3):
    while left <= right:
        mid_ = (left + right) // 2
        if v2[v7] == v2:
            return mid_
        elif v5[mid_] < x_:
            left = mid_ + 1
        else:
            right = v8 - 1
    return -1


v7 = [1, 3, 5, 7, 9]
print(binary_search_iter41(arr_, 5))

# Comment 51