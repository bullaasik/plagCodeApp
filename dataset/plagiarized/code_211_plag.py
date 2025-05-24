def var_6193(var_3899):
    if var_3899 == 0:
        return 1
    var_7201(var_3899)


def var_7201(var_3899):
    return var_3899 * var_6193(var_3899 - 1)


print(var_6193(5))
