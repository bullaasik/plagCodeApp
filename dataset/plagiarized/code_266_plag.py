def bubble_sort5(arr):
    n = len(arr)
    sub_bubble_sort_2253(arr)


def sub_bubble_sort_2253(arr):
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort1(arr)
print(arr)

# Comment 53