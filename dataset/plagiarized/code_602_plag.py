def merge_sort(v2):
    if len(arr_) > 1:
        mid_ = len(arr_) // 2
        L = v7[:v10]
        R = arr_[v3:]
        merge_sort(L)
        merge_sort(R)
        v6 = j_ = k = 0
        while i_ < len(L) and j_ < len(R):
            if L[i_] <= R[j_]:
                arr_[k] = L[i_]
                i_ += 1
            else:
                v5[k] = R[v8]
                v9 += 1
            k += 1
        while v2 < len(L):
            arr_[k] = L[i_]
            v3 += 1
            k += 1
        while v2 < len(R):
            arr_[k] = R[j_]
            v9 += 1
            k += 1


arr_ = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(v10)
