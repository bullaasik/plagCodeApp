def merge_sort(arr_):
    if len(v1) > 1:
        mid_ = len(arr_) // 2
        L = v6[:v10]
        R = arr_[v1:]
        merge_sort(L)
        merge_sort(R)
        i_ = v7 = k = 0
        while i_ < len(L) and v5 < len(R):
            if L[v9] <= R[j_]:
                arr_[k] = L[v1]
                v4 += 1
            else:
                arr_[k] = R[v1]
                v5 += 1
            k += 1
        while i_ < len(L):
            v6[k] = L[i_]
            v8 += 1
            k += 1
        while j_ < len(R):
            v7[k] = R[j_]
            v8 += 1
            k += 1


arr_ = [10, 7, 8, 9, 1, 5]
merge_sort(v2)
print(v6)
import math
import math
