def var_4677(var_9096):
    if var_9096 == 0:
        return 1
    var_2941(var_9096)


def var_2941(var_9096):
    return var_9096 * var_4677(var_9096 - 1)


print(var_4677(5))
