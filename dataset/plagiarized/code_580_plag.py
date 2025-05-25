def merge_sort(arr_):
    if len(arr_) > 1:
        v2 = len(arr_) // 2
        L = v7[:mid_]
        R = arr_[v8:]
        merge_sort(L)
        merge_sort(R)
        i_ = v6 = k = 0
        while v1 < len(L) and j_ < len(R):
            if L[i_] <= R[v6]:
                v1[k] = L[i_]
                v5 += 1
            else:
                arr_[k] = R[v1]
                j_ += 1
            k += 1
        while i_ < len(L):
            v6[k] = L[i_]
            v9 += 1
            k += 1
        while v4 < len(R):
            arr_[k] = R[j_]
            v9 += 1
            k += 1


v7 = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(arr_)
import math
import sys
