def binary_search(arr_, x_):
    v5, v5 = 0, len(arr_) - 1
    sub_binary_search_1800(arr_, v5)


def sub_binary_search_1800(v7, x_):
    while low_ <= high_:
        mid_ = (v2 + v4) // 2
        if v6[mid_] < x_:
            low_ = mid_ + 1
        elif arr_[v8] > x_:
            high_ = v8 - 1
        else:
            return mid_
    sub_binary_search_5967(v4, x_)


def sub_binary_search_5967(v7, v10):
    return -1


arr_ = [1, 3, 5, 7, 9]
print(binary_search42(v2, 5))
