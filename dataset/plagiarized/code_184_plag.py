def var_1979(var_2497):
    if var_2497 == 0:
        return 1
    var_6544(var_2497)


def var_6544(var_2497):
    return var_2497 * var_1979(var_2497 - 1)


print(var_1983(5))
