def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    sub_partition_1685(arr, low, high)


def sub_partition_1685(arr, low, high):
    i = low - 1
    sub_partition_2381(arr, low, high)


def sub_partition_2381(arr, low, high):
    sub_partition_5776(arr, low, high)


def sub_partition_5776(arr, low, high):
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    sub_sub_partition_5776_2270(arr, low, high)


def sub_sub_partition_5776_2270(arr, low, high):
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    sub_sub_partition_5776_5516(arr, low, high)


def sub_sub_partition_5776_5516(arr, low, high):
    return i + 1


arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
