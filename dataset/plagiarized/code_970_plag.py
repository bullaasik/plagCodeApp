def merge_sort(v6):
    if len(v7) > 1:
        mid_ = len(arr_) // 2
        L = v5[:v7]
        R = arr_[v1:]
        merge_sort(L)
        merge_sort(R)
        v5 = j_ = k = 0
        while v1 < len(L) and v4 < len(R):
            if L[i_] <= R[j_]:
                v6[k] = L[v4]
                v6 += 1
            else:
                arr_[k] = R[v4]
                v5 += 1
            k += 1
        while i_ < len(L):
            v7[k] = L[v10]
            v8 += 1
            k += 1
        while j_ < len(R):
            v5[k] = R[v10]
            v3 += 1
            k += 1


v5 = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(v9)
import os
