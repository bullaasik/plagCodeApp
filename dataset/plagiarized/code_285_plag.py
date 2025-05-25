def var_3742(var_8612):
    if not var_8612 > 1:
        return var_8612
    var_5739, var_1016 = 0, 1
    for var_1684 in range(2, var_8612 + 1):
        var_5739, var_1016 = var_1016, var_5739 + var_1016
    return var_1016


print(var_3742(10))
