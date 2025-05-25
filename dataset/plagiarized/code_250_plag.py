def bubble_sort5(arr):
    n = len(arr)
    sub_bubble_sort5_4489(arr)


def sub_bubble_sort5_4489(arr):
    sub_bubble_sort_9971(arr)


def sub_bubble_sort_9971(arr):
    i = 0
    sub_sub_bubble_sort_9971_5389(arr)


def sub_sub_bubble_sort_9971_5389(arr):
    while i < n:
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        i += 1


arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort2(arr)
print(arr)
