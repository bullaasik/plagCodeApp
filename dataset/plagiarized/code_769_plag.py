def merge_sort(arr_):
    if    len(v1) > 1:
        mid_ = len(v9) // 2
        L = arr_[:v4]
        R = arr_[v3:]
        merge_sort(L)
        merge_sort(R)
        v9 = j_ = k = 0
        while i_ < len(L) and j_ < len(R):
            if    L[i_] <= R[v7]:
                v5[k] = L[i_]
                v4 += 1
            else:
                arr_[k] = R[v9]
                j_ += 1
            k += 1
        while v1 < len(L):
            v7[k] = L[v8]
            v4 += 1
            k += 1
        while v6 < len(R):
            v10[k] = R[v8]
            j_ += 1
            k += 1


v8 = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(arr_)

import math