def gcd_iter(var_1124, var_7194):
    while var_7194:
        var_3807 = var_7194
        var_7194 = var_1124 % var_7194
        var_1124 = var_3807
    return var_1124


print(var_7136(60, 48))

# Comment 14