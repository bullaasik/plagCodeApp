def bubble_sort2(arr):
    n = len(arr)
    sub_bubble_sort2_9325(arr)


def sub_bubble_sort2_9325(arr):
    i = 0
    while i < n:
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        i += 1


arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort3(arr)
print(arr)
