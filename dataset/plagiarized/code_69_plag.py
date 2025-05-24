def var_9004(var_9629):
    if var_9629 == 0:
        return 1
    return var_9629 * var_9004(var_9629 - 1)


print(var_9004(5))
