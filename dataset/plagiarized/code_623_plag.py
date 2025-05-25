def gcd_iter(var_3336, var_7954):
    while var_7954:
        var_4454 = var_7954
        var_7954 = var_3336 % var_7954
        var_3336 = var_4454
    return var_3336


print(var_9593(60, 48))
