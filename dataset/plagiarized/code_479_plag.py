def var_3628(var_2219):
    if not var_2219 > 1:
        return var_2219
    var_4983, var_2750 = 0, 1
    for var_5488 in range(2, var_2219 + 1):
        var_4983, var_2750 = var_2750, var_4983 + var_2750
    return var_2750


print(var_3628(10))
