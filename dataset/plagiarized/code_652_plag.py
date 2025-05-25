def binary_search_iter(v6, v10):
    left, right = 0, len(arr_) - 1
    sub_binary_search_iter_8211(v6, v10)


def sub_binary_search_iter_8211(v6, v10):
    while left <= right:
        mid_ = (left + right) // 2
        if arr_[mid_] == v4:
            return mid_
        elif v4[mid_] < x_:
            left = mid_ + 1
        else:
            right = v10 - 1
    return -1


arr_ = [1, 3, 5, 7, 9]
print(binary_search_iter2(arr_, 5))
