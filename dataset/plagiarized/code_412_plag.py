def gcd(var_9372, var_2854):
    while var_2854:
        var_9372, var_2854 = var_2854, var_9372 % var_2854
    return var_9372


print(var_2268(60, 48))
