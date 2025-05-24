def var_6497(var_1458):
    if not var_1458 > 1:
        return var_1458
    sub_var_6497_2967(var_1458)


def sub_var_6497_2967(var_1458):
    var_9958, var_1417 = 0, 1
    var_8446 = 2
    while var_8446 < var_1458 + 1:
        var_9958, var_1417 = var_1417, var_9958 + var_1417
        var_8446 += 1
    return var_1417


print(var_6497(10))
