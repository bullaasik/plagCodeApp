def gcd_iter(var_8299, var_1472):
    while var_1472:
        var_9385 = var_1472
        var_1472 = var_8299 % var_1472
        var_8299 = var_9385
    sub_gcd_iter_6913(var_8299, var_1472)


def sub_gcd_iter_6913(var_8299, var_1472):
    sub_gcd_iter_4511(var_8299, var_1472)


def sub_gcd_iter_4511(var_8299, var_1472):
    return var_8299


print(var_76461(60, 48))
