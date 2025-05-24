def merge_sort(arr_):
    if len(arr_) > 1:
        mid_ = len(arr_) // 2
        L = arr_[:v3]
        R = arr_[mid_:]
        merge_sort(L)
        merge_sort(R)
        i_ = v3 = k = 0
        while v8 < len(L) and j_ < len(R):
            if L[v2] <= R[v7]:
                arr_[k] = L[i_]
                v6 += 1
            else:
                v3[k] = R[v2]
                v2 += 1
            k += 1
        while v9 < len(L):
            arr_[k] = L[i_]
            i_ += 1
            k += 1
        while j_ < len(R):
            arr_[k] = R[v5]
            v10 += 1
            k += 1


v1 = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(arr_)
import os
import sys

# Comment 41