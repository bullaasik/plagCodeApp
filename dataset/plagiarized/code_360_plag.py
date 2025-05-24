def var_7424(var_5769):
    if  var_5769 == 0:
        return 1
    return var_6684 * var_7424(var_5769 - 1)


print(var_7424(5))
