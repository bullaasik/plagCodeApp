def var_4982(var_9183):
    if not var_9183 > 1:
        return var_9183
    var_1004, var_9147 = 0, 1
    for var_1052 in range(2, var_9183 + 1):
        var_1004, var_9147 = var_9147, var_1004 + var_9147
    return var_9147


print(var_4982(10))
