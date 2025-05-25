def merge_sort(arr_):
    if len(v8) > 1:
        mid_ = len(arr_) // 2
        L = arr_[:mid_]
        R = v8[v7:]
        merge_sort(L)
        merge_sort(R)
        v2 = v10 = k = 0
        while i_ < len(L) and v1 < len(R):
            if L[i_] <= R[v9]:
                arr_[k] = L[v3]
                v4 += 1
            else:
                v6[k] = R[j_]
                j_ += 1
            k += 1
        while i_ < len(L):
            arr_[k] = L[v4]
            v6 += 1
            k += 1
        while v10 < len(R):
            arr_[k] = R[v10]
            j_ += 1
            k += 1


v5 = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(arr_)
import os
import math
