def gcd4(var_1062, var_2671):
    while var_2671:
        var_1062, var_2671 = var_2671, var_1062 % var_2671
    return var_1062


print(var_6914(60, 48))
