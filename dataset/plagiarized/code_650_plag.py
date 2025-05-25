def var_8471(var_9498, var_7619):
    while var_7619:
        var_2426 = var_7619
        var_7619 = var_9498 % var_7619
        var_9498 = var_2426
    return var_9498


print(var_8471(60, 48))
