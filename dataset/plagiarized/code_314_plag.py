def var_2144(var_2587, var_1025):
    while var_1025:
        var_2587, var_1025 = var_1025, var_2587 % var_1025
    return var_2587


print(var_2144(60, 48))

# Comment 68