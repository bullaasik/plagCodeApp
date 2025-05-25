def gcd1(var_6754, var_7204):
    while var_7204:
        var_6754, var_7204 = var_7204, var_6754 % var_7204
    return var_6754


print(var_9946(60, 48))
