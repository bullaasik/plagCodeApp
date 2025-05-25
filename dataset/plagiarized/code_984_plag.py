def var_3726(var_1375, var_7242):
    while var_7242:
        var_9347 = var_7242
        var_7242 = var_1375 % var_7242
        var_1375 = var_9347
    return var_1375


print(var_3726(60, 48))
