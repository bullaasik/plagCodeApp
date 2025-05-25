def var_5703(var_1519):
    if var_1519 == 0:
        return 1
    return var_1519 * var_5703(var_1519 - 1)


print(var_5703(5))
