def merge_sort(arr_):
    if  len(arr_) > 1:
        v2 = len(v6) // 2
        L = v9[:v5]
        R = arr_[mid_:]
        merge_sort(L)
        merge_sort(R)
        v6 = v4 = k = 0
        while v10 < len(L) and j_ < len(R):
            if  L[i_] <= R[j_]:
                v8[k] = L[i_]
                i_ += 1
            else:
                v1[k] = R[v10]
                j_ += 1
            k += 1
        while i_ < len(L):
            v10[k] = L[v8]
            v7 += 1
            k += 1
        while j_ < len(R):
            arr_[k] = R[j_]
            v2 += 1
            k += 1
arr_ = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(v6)
import os
import math
import sys