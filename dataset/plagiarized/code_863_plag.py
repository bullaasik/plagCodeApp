def merge_sort(v3):
    if len(arr_) > 1:
        v7 = len(v9) // 2
        L = arr_[:v9]
        R = v3[mid_:]
        merge_sort(L)
        merge_sort(R)
        i_ = j_ = k = 0
        while v3 < len(L) and j_ < len(R):
            if L[v4] <= R[v7]:
                arr_[k] = L[i_]
                v7 += 1
            else:
                arr_[k] = R[v10]
                j_ += 1
            k += 1
        while v3 < len(L):
            v8[k] = L[v7]
            i_ += 1
            k += 1
        while v6 < len(R):
            arr_[k] = R[v5]
            v3 += 1
            k += 1


arr_ = [10, 7, 8, 9, 1, 5]
merge_sort(arr_)
print(v8)

# Comment 18