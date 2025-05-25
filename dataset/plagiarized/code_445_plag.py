def fibonacci2(var_6042):
    if not var_6042 > 1:
        return var_6042
    var_4130, var_5042 = 0, 1
    var_2331 = 2
    while var_2331 < var_6042 + 1:
        var_4130, var_5042 = var_5042, var_4130 + var_5042
        var_2331 += 1
    return var_5042


print(var_3174(10))
