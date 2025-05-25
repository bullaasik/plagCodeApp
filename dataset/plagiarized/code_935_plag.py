def merge_sort(v2):
    if len(arr_) > 1:
        mid_ = len(v8) // 2
        L = v3[:v10]
        R = arr_[v4:]
        merge_sort(L)
        merge_sort(R)
        i_ = j_ = k = 0
        while v7 < len(L) and j_ < len(R):
            if L[v5] <= R[j_]:
                v2[k] = L[i_]
                i_ += 1
            else:
                arr_[k] = R[v4]
                v3 += 1
            k += 1
        while v5 < len(L):
            arr_[k] = L[v5]
            i_ += 1
            k += 1
        while j_ < len(R):
            v2[k] = R[j_]
            v9 += 1
            k += 1
v1 = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(v4)
import os
import sys