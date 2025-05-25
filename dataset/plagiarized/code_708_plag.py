def gcd_iter(var_6854, var_6140):
    while var_6140:
        var_1975 = var_6140
        var_6140 = var_6854 % var_6140
        var_6854 = var_1975
    return var_6854


print(var_1173(60, 48))

# Comment 98