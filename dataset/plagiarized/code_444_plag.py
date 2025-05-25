def var_8585(var_2410):
    if var_2410 == 0:
        return 1
    return var_2410 * var_8585(var_2410 - 1)


print(var_8585122(5))
