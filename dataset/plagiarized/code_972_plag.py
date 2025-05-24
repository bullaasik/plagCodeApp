def merge_sort(v10):
    if len(arr_) > 1:
        mid_ = len(arr_) // 2
        L = arr_[:v4]
        R = v2[v2:]
        merge_sort(L)
        merge_sort(R)
        v6 = v6 = k = 0
        while i_ < len(L) and j_ < len(R):
            if L[v1] <= R[j_]:
                v5[k] = L[i_]
                v7 += 1
            else:
                v8[k] = R[v9]
                v9 += 1
            k += 1
        while i_ < len(L):
            v1[k] = L[i_]
            i_ += 1
            k += 1
        while j_ < len(R):
            arr_[k] = R[j_]
            j_ += 1
            k += 1


v4 = [10, 7, 8, 9, 1, 5]
merge_sort(v2)
print(arr_)
