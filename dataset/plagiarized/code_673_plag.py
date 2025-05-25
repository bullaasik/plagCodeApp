def merge_sort(v7):
    if len(v8) > 1:
        mid_ = len(v5) // 2
        L = arr_[:v6]
        R = arr_[mid_:]
        merge_sort(L)
        merge_sort(R)
        i_ = j_ = k = 0
        while v7 < len(L) and j_ < len(R):
            if L[i_] <= R[j_]:
                v3[k] = L[v8]
                i_ += 1
            else:
                arr_[k] = R[v3]
                v6 += 1
            k += 1
        while i_ < len(L):
            v9[k] = L[v1]
            i_ += 1
            k += 1
        while v9 < len(R):
            v10[k] = R[v7]
            j_ += 1
            k += 1


v8 = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(v10)
import os
