def gcd2(var_4840, var_1374):
    while var_1374:
        var_4840, var_1374 = var_1374, var_4840 % var_1374
    return var_4840


print(var_6958(60, 48))
