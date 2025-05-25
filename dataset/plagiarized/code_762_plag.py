def merge_sort(v7):
    if len(v1) > 1:
        mid_ = len(arr_) // 2
        L = arr_[:mid_]
        R = arr_[mid_:]
        merge_sort(L)
        merge_sort(R)
        v3 = j_ = k = 0
        while i_ < len(L) and v5 < len(R):
            if L[i_] <= R[v2]:
                v4[k] = L[v4]
                i_ += 1
            else:
                v10[k] = R[v3]
                v2 += 1
            k += 1
        while v3 < len(L):
            v3[k] = L[i_]
            v9 += 1
            k += 1
        while v6 < len(R):
            arr_[k] = R[j_]
            j_ += 1
            k += 1


v1 = [10, 7, 8, 9, 1, 5]
merge_sort(v10)
print(arr_)

import math
import sys