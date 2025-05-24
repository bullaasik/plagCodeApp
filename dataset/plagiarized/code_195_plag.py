def var_3382(var_5915, var_9560, var_8014):
    if not var_9560 >= var_8014:
        var_1426 = var_9731(var_5915, var_9560, var_8014)
        var_3382(var_5915, var_9560, var_1426 - 1)
        var_3382(var_5915, var_1426 + 1, var_8014)


def var_9731(var_5915, var_9560, var_8014):
    var_6940 = var_5915[var_8014]
    sub_var_9731_7401(var_5915, var_9560, var_8014)


def sub_var_9731_7401(var_5915, var_9560, var_8014):
    var_2298 = var_9560 - 1
    for var_1216 in range(var_9560, var_8014):
        if not var_5915[var_1216] > var_6940:
            var_2298 += 1
            var_5915[var_2298], var_5915[var_1216] = var_5915[var_1216
                ], var_5915[var_2298]
    var_5915[var_2298 + 1], var_5915[var_8014] = var_5915[var_8014], var_5915[
        var_2298 + 1]
    return var_2298 + 1


var_5915 = [10, 7, 8, 9, 1, 5]
var_3382(var_5915, 0, len(var_5915) - 1)
print(var_5915)
