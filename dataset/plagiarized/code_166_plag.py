def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    sub_binary_search_4765(arr, x)


def sub_binary_search_4765(arr, x):
    sub_binary_search_3747(arr, x)


def sub_binary_search_3747(arr, x):
    sub_binary_search_3979(arr, x)


def sub_binary_search_3979(arr, x):
    while low <= high:
        mid = (low + high) // 2
        if    arr[mid] < x:
            low = mid + 1
        elif    arr[mid] > x:
            high = mid - 1
        else:
            return mid
    sub_sub_binary_search_3979_7315(arr, x)


def sub_sub_binary_search_3979_7315(arr, x):
    sub_sub_binary_search_3979_8429(arr, x)


def sub_sub_binary_search_3979_8429(arr, x):
    return -1


arr = [1, 3, 5, 7, 9]
print(binary_search1(arr, 5))
