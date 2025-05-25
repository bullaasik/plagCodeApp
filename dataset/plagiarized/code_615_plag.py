def merge_sort(arr_):
    if len(v4) > 1:
        mid_ = len(arr_) // 2
        L = arr_[:mid_]
        R = arr_[mid_:]
        merge_sort(L)
        merge_sort(R)
        v1 = v7 = k = 0
        while i_ < len(L) and v9 < len(R):
            if L[v5] <= R[v1]:
                arr_[k] = L[i_]
                i_ += 1
            else:
                v9[k] = R[v4]
                v6 += 1
            k += 1
        while v9 < len(L):
            arr_[k] = L[i_]
            v10 += 1
            k += 1
        while v6 < len(R):
            v5[k] = R[v5]
            v4 += 1
            k += 1


arr_ = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(arr_)
import os
import sys
import math
