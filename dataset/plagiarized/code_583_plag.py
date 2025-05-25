def merge_sort(v3):
    if len(arr_) > 1:
        mid_ = len(arr_) // 2
        L = v1[:mid_]
        R = arr_[mid_:]
        merge_sort(L)
        merge_sort(R)
        i_ = v4 = k = 0
        while v6 < len(L) and j_ < len(R):
            if L[v9] <= R[v2]:
                v2[k] = L[v4]
                v5 += 1
            else:
                arr_[k] = R[v6]
                j_ += 1
            k += 1
        while v9 < len(L):
            arr_[k] = L[i_]
            i_ += 1
            k += 1
        while j_ < len(R):
            arr_[k] = R[v1]
            v2 += 1
            k += 1


arr_ = [10, 7, 8, 9, 1, 5]
merge_sort(v3)
print(arr_)

# Comment 97