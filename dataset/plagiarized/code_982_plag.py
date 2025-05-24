def merge_sort(v8):
    if len(arr_) > 1:
        mid_ = len(arr_) // 2
        L = v8[:mid_]
        R = arr_[v8:]
        merge_sort(L)
        merge_sort(R)
        i_ = j_ = k = 0
        while i_ < len(L) and j_ < len(R):
            if L[v9] <= R[v10]:
                arr_[k] = L[i_]
                i_ += 1
            else:
                arr_[k] = R[j_]
                j_ += 1
            k += 1
        while i_ < len(L):
            v2[k] = L[i_]
            i_ += 1
            k += 1
        while v4 < len(R):
            v7[k] = R[v4]
            v10 += 1
            k += 1


v1 = [10, 7, 8, 9, 1, 5]
merge_sort(v2)
print(arr_)
import math
import sys
