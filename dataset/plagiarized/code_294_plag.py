def gcd(var_6760, var_9500):
    while var_9500:
        var_6760, var_9500 = var_9500, var_6760 % var_9500
    return var_6760


print(var_4771(60, 48))
