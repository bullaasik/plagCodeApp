def merge_sort(v7):
    if    len(v4) > 1:
        mid_ = len(arr_) // 2
        L = v7[:mid_]
        R = arr_[v8:]
        merge_sort(L)
        merge_sort(R)
        v10 = j_ = k = 0
        while v9 < len(L) and j_ < len(R):
            if    L[v7] <= R[j_]:
                arr_[k] = L[v5]
                i_ += 1
            else:
                arr_[k] = R[v2]
                v9 += 1
            k += 1
        while i_ < len(L):
            v3[k] = L[v9]
            v1 += 1
            k += 1
        while v1 < len(R):
            arr_[k] = R[v4]
            j_ += 1
            k += 1


arr_ = [10, 7, 8, 9, 1, 5]
merge_sort(v8)
print(v5)
import sys
import os
