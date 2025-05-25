def var_9786(v4):
    if not var_2563 > 1:
        return var_5487
    var_3720 = [0, 1]
    for var_1066 in range(2, var_7940 + 1):
        var_3720.append(var_3720[var_8896 - 1] + var_3720[var_8896 - 2])
    return var_3720[var_2563]


print(var_9786(10))
