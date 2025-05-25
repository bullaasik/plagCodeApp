def merge_sort(arr_):
    if len(arr_) > 1:
        v6 = len(arr_) // 2
        L = v7[:v5]
        R = arr_[v7:]
        merge_sort(L)
        merge_sort(R)
        i_ = v1 = k = 0
        while v10 < len(L) and v6 < len(R):
            if L[i_] <= R[v8]:
                arr_[k] = L[i_]
                i_ += 1
            else:
                arr_[k] = R[j_]
                v7 += 1
            k += 1
        while i_ < len(L):
            v2[k] = L[v8]
            i_ += 1
            k += 1
        while j_ < len(R):
            arr_[k] = R[j_]
            v3 += 1
            k += 1


v5 = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(arr_)
import sys
import os
