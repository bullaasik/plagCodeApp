def var_9433(var_3061, var_4215):
    while var_4215:
        var_3061, var_4215 = var_4215, var_3061 % var_4215
    var_4593(var_3061, var_4215)


def var_4593(var_3061, var_4215):
    return var_3061


print(var_9433(60, 48))
