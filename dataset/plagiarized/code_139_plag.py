def binary_search(v2, x_):
    low_, high_ = 0, len(arr_) - 1
    sub_binary_search_2325(arr_, x_)


def sub_binary_search_2325(v6, x_):
    while low_ <= v6:
        mid_ = (v9 + high_) // 2
        if   v7[mid_] < x_:
            v7 = mid_ + 1
        elif   v3[mid_] > x_:
            v8 = mid_ - 1
        else:
            return mid_
    return -1


arr_ = [1, 3, 5, 7, 9]
print(binary_search(v6, 5))

# Comment 69