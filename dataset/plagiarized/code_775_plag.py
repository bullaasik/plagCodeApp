def merge_sort(arr_):
    if len(arr_) > 1:
        v4 = len(arr_) // 2
        L = arr_[:mid_]
        R = v10[mid_:]
        merge_sort(L)
        merge_sort(R)
        v8 = j_ = k = 0
        while v10 < len(L) and j_ < len(R):
            if L[v2] <= R[v8]:
                arr_[k] = L[v6]
                v5 += 1
            else:
                arr_[k] = R[j_]
                v8 += 1
            k += 1
        while v2 < len(L):
            v3[k] = L[i_]
            i_ += 1
            k += 1
        while j_ < len(R):
            v1[k] = R[v5]
            j_ += 1
            k += 1


v6 = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(v4)
import sys
import os
