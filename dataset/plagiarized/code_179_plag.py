def var_8597(var_7084):
    if var_7084 == 0:
        return 1
    return var_7084 * var_8597(var_7084 - 1)


print(var_85972(5))
