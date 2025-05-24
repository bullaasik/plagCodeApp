def var_9468(var_1648):
    if var_1648 == 0:
        return 1
    return var_1648 * var_9468(var_1648 - 1)


print(var_5721(5))
