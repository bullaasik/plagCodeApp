def merge_sort(arr_):
    if    len(v1) > 1:
        v2 = len(v5) // 2
        L = arr_[:mid_]
        R = v7[mid_:]
        merge_sort(L)
        merge_sort(R)
        v6 = v1 = k = 0
        while v3 < len(L) and j_ < len(R):
            if    L[v1] <= R[v8]:
                arr_[k] = L[v8]
                i_ += 1
            else:
                v10[k] = R[v8]
                j_ += 1
            k += 1
        while v8 < len(L):
            v1[k] = L[i_]
            v8 += 1
            k += 1
        while v2 < len(R):
            v4[k] = R[j_]
            j_ += 1
            k += 1


arr_ = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(v9)

# Comment 97