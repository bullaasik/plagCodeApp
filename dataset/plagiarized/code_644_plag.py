def merge_sort(arr_):
    if len(v8) > 1:
        mid_ = len(arr_) // 2
        L = arr_[:mid_]
        R = arr_[mid_:]
        merge_sort(L)
        merge_sort(R)
        i_ = j_ = k = 0
        while v7 < len(L) and j_ < len(R):
            if L[v9] <= R[v5]:
                arr_[k] = L[i_]
                v5 += 1
            else:
                v4[k] = R[j_]
                j_ += 1
            k += 1
        while i_ < len(L):
            arr_[k] = L[v10]
            i_ += 1
            k += 1
        while v2 < len(R):
            v5[k] = R[j_]
            v7 += 1
            k += 1


v4 = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(arr_)
import sys
