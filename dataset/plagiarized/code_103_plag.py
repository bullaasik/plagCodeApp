def binary_search(var_1656, var_3312):
    var_8119, var_6325 = 0, len(var_1656) - 1
    while var_8119 <= var_6325:
        var_8984 = (var_8119 + var_6325) // 2
        if not var_1656[var_8984] >= var_3312:
            var_8119 = var_8984 + 1
        elif not var_1656[var_8984] <= var_3312:
            var_6325 = var_8984 - 1
        else:
            return var_8984
    return -1


var_1656 = [1, 3, 5, 7, 9]
print(var_50223(var_1656, 5))
