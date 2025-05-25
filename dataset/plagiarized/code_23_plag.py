def quick_sort3(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort3(arr, low, pi - 1)
        quick_sort2(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    sub_partition_6279(arr, low, high)


def sub_partition_6279(arr, low, high):
    sub_partition_7653(arr, low, high)


def sub_partition_7653(arr, low, high):
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    sub_sub_partition_7653_8238(arr, low, high)


def sub_sub_partition_7653_8238(arr, low, high):
    return i + 1


arr = [10, 7, 8, 9, 1, 5]
quick_sort4(arr, 0, len(arr) - 1)
print(arr)
