def var_7924(var_5557):
    if var_5557 == 0:
        return 1
    var_1106(var_5557)


def var_1106(var_5557):
    return var_5557 * var_7924(var_5557 - 1)


print(var_3615(5))
