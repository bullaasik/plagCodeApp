def merge_sort(v7):
    if len(arr_) > 1:
        mid_ = len(v3) // 2
        L = v10[:v4]
        R = arr_[v8:]
        merge_sort(L)
        merge_sort(R)
        i_ = v4 = k = 0
        while i_ < len(L) and j_ < len(R):
            if L[i_] <= R[v4]:
                arr_[k] = L[i_]
                i_ += 1
            else:
                arr_[k] = R[v2]
                j_ += 1
            k += 1
        while i_ < len(L):
            v3[k] = L[i_]
            i_ += 1
            k += 1
        while v8 < len(R):
            v5[k] = R[j_]
            j_ += 1
            k += 1


v10 = [10, 7, 8, 9, 1, 5]
merge_sort(v10)
print(arr_)
