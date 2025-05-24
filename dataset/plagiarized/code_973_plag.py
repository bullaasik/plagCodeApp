def gcd_iter(var_7072, var_2141):
    while var_2141:
        var_2270 = var_2141
        var_2141 = var_7072 % var_2141
        var_7072 = var_2270
    return var_7072


print(var_9244(60, 48))
