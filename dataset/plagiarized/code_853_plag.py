def merge_sort(v8):
    if len(arr_) > 1:
        v2 = len(v1) // 2
        L = v5[:mid_]
        R = arr_[v5:]
        merge_sort(L)
        merge_sort(R)
        i_ = j_ = k = 0
        while v6 < len(L) and j_ < len(R):
            if L[i_] <= R[v6]:
                arr_[k] = L[i_]
                v5 += 1
            else:
                v9[k] = R[v5]
                j_ += 1
            k += 1
        while i_ < len(L):
            arr_[k] = L[i_]
            i_ += 1
            k += 1
        while j_ < len(R):
            arr_[k] = R[v1]
            v5 += 1
            k += 1


v4 = [10, 7, 8, 9, 1, 5]
merge_sort(v3)
print(v9)
