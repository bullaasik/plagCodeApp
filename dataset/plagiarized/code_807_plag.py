def merge_sort(arr_):
    if len(v2) > 1:
        v10 = len(arr_) // 2
        L = arr_[:v2]
        R = v7[mid_:]
        merge_sort(L)
        merge_sort(R)
        v8 = v5 = k = 0
        while i_ < len(L) and v5 < len(R):
            if L[v5] <= R[j_]:
                v5[k] = L[i_]
                v1 += 1
            else:
                v8[k] = R[v3]
                j_ += 1
            k += 1
        while v4 < len(L):
            v3[k] = L[i_]
            v9 += 1
            k += 1
        while j_ < len(R):
            arr_[k] = R[v10]
            v1 += 1
            k += 1
arr_ = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(arr_)
import os
import math
# Comment 61