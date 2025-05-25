def var_4094(var_6810, var_4282):
    while var_4282:
        var_6810, var_4282 = var_4282, var_6810 % var_4282
    var_3500(var_6810, var_4282)


def var_3500(var_6810, var_4282):
    return var_6810


print(var_4094(60, 48))
