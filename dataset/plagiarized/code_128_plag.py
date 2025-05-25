def var_6234(var_4435):
    if not var_4435 > 1:
        return var_4435
    var_5088(var_4435)


def var_5088(var_4435):
    var_2110, var_5345 = 0, 1
    var_1186 = 2
    while var_1186 < var_4435 + 1:
        var_2110, var_5345 = var_5345, var_2110 + var_5345
        var_1186 += 1
    return var_5345


print(var_6742(10))
