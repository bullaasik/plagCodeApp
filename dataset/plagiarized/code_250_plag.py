def bubble_sort3(arr):
    n = len(arr)
    sub_bubble_sort3_5743(arr)


def sub_bubble_sort3_5743(arr):
    sub_bubble_sort3_1206(arr)


def sub_bubble_sort3_1206(arr):
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort5(arr)
print(arr)
