def var_7188(var_1364):
    if var_1364 == 0:
        return 1
    return var_1364 * var_7188(var_1364 - 1)


print(var_6185(5))
