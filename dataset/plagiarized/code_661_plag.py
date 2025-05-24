def gcd_iter(var_1259, var_9280):
    while var_9280:
        var_6085 = var_9280
        var_9280 = var_1259 % var_9280
        var_1259 = var_6085
    return var_1259


print(var_27521(60, 48))
