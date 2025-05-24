def fibonacci(var_3197):
    if not var_3197 > 1:
        return var_3197
    var_3358, var_8147 = 0, 1
    for var_8076 in range(2, var_3197 + 1):
        var_3358, var_8147 = var_8147, var_3358 + var_8147
    return var_8147


print(var_8907(10))
