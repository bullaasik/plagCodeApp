def var_2360(var_7235):
    if var_7235 == 0:
        return 1
    var_6279(var_7235)


def var_6279(var_7235):
    return var_7235 * var_2360(var_7235 - 1)


print(var_2360(5))
