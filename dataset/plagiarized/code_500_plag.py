def var_1928(var_8085):
    if var_8085 == 0:
        return 1
    var_7908(var_8085)


def var_7908(var_8085):
    return var_8085 * var_1928(var_8085 - 1)


print(var_19283(5))
