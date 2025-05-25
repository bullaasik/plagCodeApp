def var_3147(var_5659):
    if var_5659 == 0:
        return 1
    return var_5659 * var_3147(var_5659 - 1)


print(var_3147(5))
