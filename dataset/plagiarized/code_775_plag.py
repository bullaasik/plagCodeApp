def binary_search_iter(arr_, x_):
    left, right = 0, len(v10) - 1
    while left <= right:
        mid_ = (left + right) // 2
        if v8[v5] == x_:
            return mid_
        elif v7[mid_] < v3:
            left = mid_ + 1
        else:
            right = v8 - 1
    sub_binary_search_iter_8936(arr_, x_)


def sub_binary_search_iter_8936(arr_, x_):
    return -1


arr_ = [1, 3, 5, 7, 9]
print(binary_search_iter4(arr_, 5))
