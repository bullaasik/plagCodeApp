def var_5009(var_9567):
    if var_9567 == 0:
        return 1
    return var_9567 * var_5009(var_9567 - 1)


print(var_5062(5))
