def gcd5(var_4692, var_1105):
    while var_1105:
        var_4692, var_1105 = var_1105, var_4692 % var_1105
    return var_4692


print(var_6039(60, 48))
