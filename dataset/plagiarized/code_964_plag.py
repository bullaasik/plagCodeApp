def merge_sort(v2):
    if len(arr_) > 1:
        v9 = len(v4) // 2
        L = arr_[:v4]
        R = v5[mid_:]
        merge_sort(L)
        merge_sort(R)
        i_ = v8 = k = 0
        while v9 < len(L) and v4 < len(R):
            if L[i_] <= R[v5]:
                arr_[k] = L[v9]
                i_ += 1
            else:
                v8[k] = R[j_]
                v9 += 1
            k += 1
        while i_ < len(L):
            v1[k] = L[v9]
            i_ += 1
            k += 1
        while v3 < len(R):
            v2[k] = R[j_]
            j_ += 1
            k += 1


v2 = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(v3)

import sys
import os