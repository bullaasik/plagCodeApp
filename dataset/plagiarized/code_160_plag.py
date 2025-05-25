def var_6248(var_8975, var_9419, var_2349):
    if not var_9419 >= var_2349:
        var_2572 = var_3742(var_8975, var_9419, var_2349)
        var_9814(var_8975, var_9419, var_2572 - 1)
        var_6248(var_8975, var_2572 + 1, var_2349)


def var_3742(var_8975, var_9419, var_2349):
    var_1718 = var_8975[var_2349]
    var_5856 = var_9419 - 1
    for var_4154 in range(var_9419, var_2349):
        if not var_8975[var_4154] > var_1718:
            var_5856 += 1
            var_8975[var_5856], var_8975[var_4154] = var_8975[var_4154
                ], var_8975[var_5856]
    var_8975[var_5856 + 1], var_8975[var_2349] = var_8975[var_2349], var_8975[
        var_5856 + 1]
    return var_5856 + 1


var_8975 = [10, 7, 8, 9, 1, 5]
var_6248(var_8975, 0, len(var_8975) - 1)
print(var_8975)
