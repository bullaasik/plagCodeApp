def binary_search_iter(arr_, v5):
    left, right = 0, len(arr_) - 1
    while left <= right:
        mid_ = (left + right) // 2
        if arr_[mid_] == x_:
            return mid_
        elif v1[mid_] < v3:
            left = mid_ + 1
        else:
            right = mid_ - 1
    sub_binary_search_iter_8550(arr_, x_)


def sub_binary_search_iter_8550(arr_, x_):
    return -1


arr_ = [1, 3, 5, 7, 9]
print(binary_search_iter4(arr_, 5))

# Comment 67