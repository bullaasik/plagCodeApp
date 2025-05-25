def var_1980(var_1900, var_9969):
    while var_9969:
        var_7664 = var_9969
        var_9969 = var_1900 % var_9969
        var_1900 = var_7664
    var_2215(var_1900, var_9969)


def var_2215(var_1900, var_9969):
    return var_1900


print(var_1980(60, 48))
