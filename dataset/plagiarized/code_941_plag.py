def var_6328(var_4092, var_1515):
    while var_1515:
        var_3023 = var_1515
        var_1515 = var_4092 % var_1515
        var_4092 = var_3023
    return var_4092


print(var_3479(60, 48))
