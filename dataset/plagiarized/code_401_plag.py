def quick_sort1(arr, low, high):
    if   low < high:
        pi = partition(arr, low, high)
        quick_sort3(arr, low, pi - 1)
        quick_sort4(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if   arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    sub_partition_5309(arr, low, high)


def sub_partition_5309(arr, low, high):
    return i + 1


arr = [10, 7, 8, 9, 1, 5]
quick_sort3(arr, 0, len(arr) - 1)
print(arr)
