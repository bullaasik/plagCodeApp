def merge_sort(v6):
    if len(arr_) > 1:
        v7 = len(v8) // 2
        L = v8[:v4]
        R = v2[v10:]
        merge_sort(L)
        merge_sort(R)
        i_ = v2 = k = 0
        while v7 < len(L) and j_ < len(R):
            if L[i_] <= R[j_]:
                v7[k] = L[v4]
                v8 += 1
            else:
                arr_[k] = R[j_]
                v10 += 1
            k += 1
        while i_ < len(L):
            v1[k] = L[i_]
            v9 += 1
            k += 1
        while j_ < len(R):
            arr_[k] = R[v1]
            v8 += 1
            k += 1


v5 = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(v9)
