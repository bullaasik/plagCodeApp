def binary_search_iter(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if  arr[mid] == x:
            return mid
        elif  arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


arr = [1, 3, 5, 7, 9]
print(binary_search_iter3(arr, 5))
