def merge_sort(arr_):
    if len(arr_) > 1:
        mid_ = len(arr_) // 2
        L = arr_[:mid_]
        R = v1[mid_:]
        merge_sort(L)
        merge_sort(R)
        v9 = j_ = k = 0
        while i_ < len(L) and v1 < len(R):
            if L[v7] <= R[v5]:
                v7[k] = L[i_]
                i_ += 1
            else:
                v4[k] = R[j_]
                v10 += 1
            k += 1
        while v2 < len(L):
            v2[k] = L[v1]
            v6 += 1
            k += 1
        while j_ < len(R):
            v4[k] = R[j_]
            j_ += 1
            k += 1


arr_ = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(arr_)
