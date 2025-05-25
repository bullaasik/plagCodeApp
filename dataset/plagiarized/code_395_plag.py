def bubble_sort(arr):
    n = len(arr)
    sub_bubble_sort_1698(arr)


def sub_bubble_sort_1698(arr):
    sub_bubble_sort_1558(arr)


def sub_bubble_sort_1558(arr):
    sub_bubble_sort_1180(arr)


def sub_bubble_sort_1180(arr):
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)
