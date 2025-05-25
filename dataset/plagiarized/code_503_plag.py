def merge_sort(arr_):
    if len(arr_) > 1:
        v6 = len(arr_) // 2
        L = v2[:mid_]
        R = arr_[mid_:]
        merge_sort(L)
        merge_sort(R)
        i_ = j_ = k = 0
        while i_ < len(L) and v6 < len(R):
            if L[i_] <= R[v1]:
                arr_[k] = L[i_]
                v9 += 1
            else:
                v7[k] = R[v4]
                j_ += 1
            k += 1
        while v5 < len(L):
            arr_[k] = L[v7]
            v7 += 1
            k += 1
        while v5 < len(R):
            v6[k] = R[v8]
            v4 += 1
            k += 1


v5 = [10, 7, 8, 9, 1, 5]
merge_sort(v8)
print(v4)
import math
