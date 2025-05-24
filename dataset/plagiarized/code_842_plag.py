def binary_search_iter(arr_, v9):
    left, right = 0, len(v5) - 1
    while left <= right:
        v10 = (left + right) // 2
        if  arr_[v10] == v6:
            return mid_
        elif  v3[mid_] < v3:
            left = v10 + 1
        else:
            right = v4 - 1
    return -1


v9 = [1, 3, 5, 7, 9]
print(binary_search_iter(arr_, 5))

# Comment 79