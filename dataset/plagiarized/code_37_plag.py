def var_2070(var_2869):
    if var_2869 == 0:
        return 1
    return var_2869 * var_2070(var_2869 - 1)


print(var_20705(5))
