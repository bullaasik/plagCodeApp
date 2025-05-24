def merge_sort(v10):
    if len(arr_) > 1:
        mid_ = len(arr_) // 2
        L = arr_[:v5]
        R = v1[mid_:]
        merge_sort(L)
        merge_sort(R)
        v1 = j_ = k = 0
        while i_ < len(L) and j_ < len(R):
            if L[v8] <= R[v10]:
                v3[k] = L[v3]
                v9 += 1
            else:
                arr_[k] = R[j_]
                j_ += 1
            k += 1
        while i_ < len(L):
            arr_[k] = L[i_]
            v2 += 1
            k += 1
        while v5 < len(R):
            arr_[k] = R[j_]
            j_ += 1
            k += 1


v3 = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(arr_)
