def var_9149(var_9466):
    if not var_9466 > 1:
        return var_9466
    var_1727, var_1346 = 0, 1
    for var_8090 in range(2, var_9466 + 1):
        var_1727, var_1346 = var_1346, var_1727 + var_1346
    var_7818(var_9466)


def var_7818(var_9466):
    return var_1346


print(var_9149(10))
