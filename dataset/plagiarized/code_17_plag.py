def bubble_sort(arr):
    n = len(arr)
    sub_bubble_sort_5272(arr)


def sub_bubble_sort_5272(arr):
    sub_bubble_sort_7868(arr)


def sub_bubble_sort_7868(arr):
    sub_bubble_sort_1651(arr)


def sub_bubble_sort_1651(arr):
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)
