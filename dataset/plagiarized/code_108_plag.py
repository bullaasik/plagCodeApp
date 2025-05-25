def var_4559(var_3480):
    if not var_3480 > 1:
        return var_3480
    var_7745, var_4490 = 0, 1
    for var_6753 in range(2, var_3480 + 1):
        var_7745, var_4490 = var_4490, var_7745 + var_4490
    var_8248(var_3480)


def var_8248(var_3480):
    return var_4490


print(var_45591(10))
