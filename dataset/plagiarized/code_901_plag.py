def gcd_iter(var_3549, var_5386):
    while var_5386:
        var_4214 = var_5386
        var_5386 = var_3549 % var_5386
        var_3549 = var_4214
    return var_3549


print(var_99423(60, 48))
