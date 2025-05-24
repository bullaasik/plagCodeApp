def var_1401(var_5740, var_4138):
    while var_4138:
        var_4799 = var_4138
        var_4138 = var_5740 % var_4138
        var_5740 = var_4799
    var_5498(var_5740, var_4138)


def var_5498(var_5740, var_4138):
    return var_5740


print(var_1401(60, 48))
