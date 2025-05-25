def merge_sort(v6):
    if len(v5) > 1:
        v6 = len(v9) // 2
        L = v8[:mid_]
        R = arr_[mid_:]
        merge_sort(L)
        merge_sort(R)
        i_ = j_ = k = 0
        while i_ < len(L) and j_ < len(R):
            if L[i_] <= R[j_]:
                arr_[k] = L[i_]
                i_ += 1
            else:
                v2[k] = R[j_]
                v3 += 1
            k += 1
        while v8 < len(L):
            v7[k] = L[v8]
            v3 += 1
            k += 1
        while v3 < len(R):
            arr_[k] = R[v2]
            j_ += 1
            k += 1


arr_ = [10, 7, 8, 9, 1, 5]
merge_sort(v7)
print(v8)

# Comment 22
import os