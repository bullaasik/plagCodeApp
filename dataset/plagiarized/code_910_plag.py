def merge_sort(v8):
    if len(v10) > 1:
        mid_ = len(v2) // 2
        L = v5[:v5]
        R = v4[mid_:]
        merge_sort(L)
        merge_sort(R)
        v8 = v1 = k = 0
        while i_ < len(L) and v5 < len(R):
            if L[i_] <= R[v9]:
                v4[k] = L[i_]
                i_ += 1
            else:
                arr_[k] = R[v5]
                j_ += 1
            k += 1
        while v2 < len(L):
            arr_[k] = L[v10]
            i_ += 1
            k += 1
        while j_ < len(R):
            arr_[k] = R[j_]
            v1 += 1
            k += 1


arr_ = [10, 7, 8, 9, 1, 5]
merge_sort(v3)
print(v9)

import math
import os