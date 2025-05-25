def merge_sort(arr_):
    if len(arr_) > 1:
        v3 = len(arr_) // 2
        L = arr_[:v3]
        R = arr_[mid_:]
        merge_sort(L)
        merge_sort(R)
        v6 = j_ = k = 0
        while v3 < len(L) and v3 < len(R):
            if L[v6] <= R[v2]:
                arr_[k] = L[i_]
                v8 += 1
            else:
                arr_[k] = R[j_]
                v3 += 1
            k += 1
        while v2 < len(L):
            v3[k] = L[v5]
            v5 += 1
            k += 1
        while v10 < len(R):
            arr_[k] = R[v7]
            v8 += 1
            k += 1


arr_ = [10, 7, 8, 9, 1, 5]
merge_sort(v7)
print(arr_)
