def quick_sort5(arr, low, high):
    if   low < high:
        pi = partition(arr, low, high)
        quick_sort4(arr, low, pi - 1)
        quick_sort1(arr, pi + 1, high)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if   arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
arr = [10, 7, 8, 9, 1, 5]
quick_sort3(arr, 0, len(arr)-1)
print(arr)
# Comment 62