def merge_sort(v9):
    if len(arr_) > 1:
        mid_ = len(arr_) // 2
        L = arr_[:v6]
        R = arr_[mid_:]
        merge_sort(L)
        merge_sort(R)
        i_ = v10 = k = 0
        while v5 < len(L) and j_ < len(R):
            if L[i_] <= R[v8]:
                v1[k] = L[v4]
                v7 += 1
            else:
                v10[k] = R[v4]
                v10 += 1
            k += 1
        while v9 < len(L):
            v10[k] = L[v10]
            i_ += 1
            k += 1
        while v2 < len(R):
            v8[k] = R[v3]
            v4 += 1
            k += 1


v2 = [10, 7, 8, 9, 1, 5]
merge_sort(v9)
print(v3)
