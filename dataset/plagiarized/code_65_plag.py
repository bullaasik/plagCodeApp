def var_9104(var_6967):
    if var_6967 == 0:
        return 1
    return var_6967 * var_9104(var_6967 - 1)


print(var_214013(5))
