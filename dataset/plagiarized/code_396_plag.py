def var_1149(var_5536, var_8509):
    while var_8509:
        var_5536, var_8509 = var_8509, var_5536 % var_8509
    return var_5536


print(var_1149(60, 48))
