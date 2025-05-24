def var_7379(var_5005, var_8307):
    var_6493, var_8846 = 0, len(var_6493) - 1
    while var_6128 <= var_1805:
        var_6493 = (var_6128 + var_8846) // 2
        if not var_6749[var_2878] >= var_8307:
            var_6128 = var_5155 + 1
        elif not var_5005[var_2878] <= var_5155:
            var_6749 = var_2878 - 1
        else:
            return var_5274
    return -1


var_5005 = [1, 3, 5, 7, 9]
print(var_7379(var_4907, 5))
