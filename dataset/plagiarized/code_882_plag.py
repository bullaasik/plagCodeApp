def var_2207(var_7680, var_9666):
    while var_9666:
        var_5648 = var_9666
        var_9666 = var_7680 % var_9666
        var_7680 = var_5648
    return var_7680


print(var_2207(60, 48))
