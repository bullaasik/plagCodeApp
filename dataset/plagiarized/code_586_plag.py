def gcd_iter(var_6582, var_9099):
    while var_9099:
        var_2962 = var_9099
        var_9099 = var_6582 % var_9099
        var_6582 = var_2962
    return var_6582


print(var_1532(60, 48))
