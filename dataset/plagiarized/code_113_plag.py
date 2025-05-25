def var_5295(var_2106):
    if  not var_2106 > 1:
        return var_2106
    var_1225, var_1273 = 0, 1
    for var_2195 in range(2, var_2106 + 1):
        var_1225, var_1273 = var_1273, var_1225 + var_1273
    return var_1273


print(var_5295(10))

# Comment 65