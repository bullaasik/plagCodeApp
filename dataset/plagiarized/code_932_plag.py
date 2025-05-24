def var_2461(var_5084, var_8472):
    while var_8472:
        var_4035 = var_8472
        var_8472 = var_5084 % var_8472
        var_5084 = var_4035
    sub_var_2461_5300(var_5084, var_8472)


def sub_var_2461_5300(var_5084, var_8472):
    return var_5084


print(var_2461(60, 48))
