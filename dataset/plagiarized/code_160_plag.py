def var_7843(var_9313, var_5462):
    while var_5462:
        var_9313, var_5462 = var_5462, var_9313 % var_5462
    return var_9313


print(var_7843(60, 48))
