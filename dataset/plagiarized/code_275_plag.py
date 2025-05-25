def bubble_sort(arr):
    n = len(arr)
    sub_bubble_sort_1687(arr)


def sub_bubble_sort_1687(arr):
    i = 0
    while i < n:
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        i += 1


arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)
