def gcd_iter(var_8384, var_6421):
    while var_6421:
        var_7726 = var_6421
        var_6421 = var_8384 % var_6421
        var_8384 = var_7726
    return var_8384


print(var_5943(60, 48))
