def var_9886(var_2393, var_1900):
    while var_1900:
        var_4819 = var_1900
        var_1900 = var_2393 % var_1900
        var_2393 = var_4819
    var_3075(var_2393, var_1900)


def var_3075(var_2393, var_1900):
    return var_2393


print(var_98865(60, 48))
