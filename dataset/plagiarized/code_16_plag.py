def var_3694(var_2202):
    if var_2202 == 0:
        return 1
    sub_var_3694_2068(var_2202)


def sub_var_3694_2068(var_2202):
    return var_2202 * var_3694(var_2202 - 1)


print(var_99593(5))
