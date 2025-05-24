def gcd_iter(var_2632, var_2148):
    while var_2148:
        var_2640 = var_2148
        var_2148 = var_2632 % var_2148
        var_2632 = var_2640
    var_5070(var_2632, var_2148)


def var_5070(var_2632, var_2148):
    return var_2632


print(var_1461(60, 48))
