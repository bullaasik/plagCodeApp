def var_6839(var_1944, var_1323):
    while var_1323:
        var_1944, var_1323 = var_1323, var_1944 % var_1323
    return var_1944


print(var_6839(60, 48))
