def var_8358(var_1163, var_4504):
    var_9951, var_8760 = 0, len(var_6635) - 1
    while var_2616 <= var_5812:
        var_7350 = (var_3345 + var_5812) // 2
        if not var_1163[var_7970] >= var_8760:
            var_9899 = var_7970 + 1
        elif not var_8760[var_7970] <= var_4504:
            var_5812 = var_7350 - 1
        else:
            return var_7970
    return -1


var_1163 = [1, 3, 5, 7, 9]
print(var_8358(var_1163, 5))
