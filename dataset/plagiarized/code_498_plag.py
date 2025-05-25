def var_8444(var_3045, var_5895):
    while var_5895:
        var_3045, var_5895 = var_5895, var_3045 % var_5895
    var_9867(var_3045, var_5895)


def var_9867(var_3045, var_5895):
    return var_3045


print(var_8444(60, 48))
