def var_4446(var_7801):
    if not var_7801 > 1:
        return var_7801
    var_4129, var_6191 = 0, 1
    var_6871 = 2
    while var_6871 < var_7801 + 1:
        var_4129, var_6191 = var_6191, var_4129 + var_6191
        var_6871 += 1
    return var_6191


print(var_4446(10))
