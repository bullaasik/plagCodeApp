def quick_sort4(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort3(arr, low, pi - 1)
        quick_sort3(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    sub_partition_3689(arr, low, high)


def sub_partition_3689(arr, low, high):
    sub_partition_4588(arr, low, high)


def sub_partition_4588(arr, low, high):
    sub_partition_6542(arr, low, high)


def sub_partition_6542(arr, low, high):
    sub_partition_4459(arr, low, high)


def sub_partition_4459(arr, low, high):
    i = low - 1
    sub_sub_partition_4459_8258(arr, low, high)


def sub_sub_partition_4459_8258(arr, low, high):
    sub_sub_partition_4459_5361(arr, low, high)


def sub_sub_partition_4459_5361(arr, low, high):
    sub_sub_partition_4459_8914(arr, low, high)


def sub_sub_partition_4459_8914(arr, low, high):
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    sub_sub_sub_partition_4459_8914_1879(arr, low, high)


def sub_sub_sub_partition_4459_8914_1879(arr, low, high):
    sub_sub_sub_partition_4459_8914_8525(arr, low, high)


def sub_sub_sub_partition_4459_8914_8525(arr, low, high):
    return i + 1


arr = [10, 7, 8, 9, 1, 5]
quick_sort3(arr, 0, len(arr) - 1)
print(arr)
