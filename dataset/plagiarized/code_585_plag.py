def var_1280(var_1060, var_4081):
    while var_4081:
        var_6823 = var_4081
        var_4081 = var_1060 % var_4081
        var_1060 = var_6823
    return var_1060


print(var_1280(60, 48))

# Comment 96