def var_4685(var_9351):
    if var_9351 == 0:
        return 1
    sub_var_4685_5484(var_9351)


def sub_var_4685_5484(var_9351):
    return var_9351 * var_4685(var_9351 - 1)


print(var_4685(5))
