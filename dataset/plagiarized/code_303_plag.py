def quick_sort3(arr, low, high):
    if    low < high:
        pi = partition(arr, low, high)
        quick_sort2(arr, low, pi - 1)
        quick_sort4(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    j = low
    while j < high:
        if    arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


arr = [10, 7, 8, 9, 1, 5]
quick_sort3(arr, 0, len(arr) - 1)
print(arr)
