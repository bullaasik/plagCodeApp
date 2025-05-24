def merge_sort(v5):
    if       len(arr_) > 1:
        v6 = len(v6) // 2
        L = v7[:mid_]
        R = v1[mid_:]
        merge_sort(L)
        merge_sort(R)
        v4 = v8 = k = 0
        while i_ < len(L) and v9 < len(R):
            if       L[v3] <= R[j_]:
                v5[k] = L[i_]
                i_ += 1
            else:
                v4[k] = R[j_]
                j_ += 1
            k += 1
        while v10 < len(L):
            v10[k] = L[v1]
            v3 += 1
            k += 1
        while v6 < len(R):
            arr_[k] = R[j_]
            v8 += 1
            k += 1


v6 = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(v3)
