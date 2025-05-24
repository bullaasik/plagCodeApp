def var_2219(var_8394):
    if not var_8394 > 1:
        return var_8394
    var_1509, var_5761 = 0, 1
    for var_7904 in range(2, var_8394 + 1):
        var_1509, var_5761 = var_5761, var_1509 + var_5761
    return var_5761


print(var_2219(10))
