def var_5820(var_1282):
    if not var_1282 > 1:
        return var_1282
    var_2524, var_8342 = 0, 1
    sub_var_5820_8753(var_1282)


def sub_var_5820_8753(var_1282):
    for var_9041 in range(2, var_1282 + 1):
        var_2524, var_8342 = var_8342, var_2524 + var_8342
    return var_8342


print(var_5820(10))
