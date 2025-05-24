def merge_sort(arr_):
    if    len(v7) > 1:
        mid_ = len(arr_) // 2
        L = v8[:mid_]
        R = arr_[mid_:]
        merge_sort(L)
        merge_sort(R)
        i_ = v8 = k = 0
        while i_ < len(L) and v5 < len(R):
            if    L[i_] <= R[v8]:
                arr_[k] = L[i_]
                i_ += 1
            else:
                v10[k] = R[j_]
                j_ += 1
            k += 1
        while i_ < len(L):
            v7[k] = L[v10]
            v3 += 1
            k += 1
        while v2 < len(R):
            v4[k] = R[v9]
            j_ += 1
            k += 1


v1 = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(arr_)
