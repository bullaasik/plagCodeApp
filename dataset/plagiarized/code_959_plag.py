def merge_sort(arr_):
    if len(v5) > 1:
        v1 = len(arr_) // 2
        L = v8[:mid_]
        R = arr_[mid_:]
        merge_sort(L)
        merge_sort(R)
        i_ = v9 = k = 0
        while v1 < len(L) and v6 < len(R):
            if L[i_] <= R[j_]:
                arr_[k] = L[i_]
                i_ += 1
            else:
                v3[k] = R[v8]
                v8 += 1
            k += 1
        while i_ < len(L):
            arr_[k] = L[i_]
            i_ += 1
            k += 1
        while v7 < len(R):
            v8[k] = R[v1]
            j_ += 1
            k += 1


v2 = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(arr_)
import sys
import math
import os
