def var_2016(var_3503, var_9109):
    while var_9109:
        var_3503, var_9109 = var_9109, var_3503 % var_9109
    return var_3503


print(var_2016(60, 48))
