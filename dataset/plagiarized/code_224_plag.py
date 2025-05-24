def var_9766(var_3814):
    if var_3814 == 0:
        return 1
    return var_3814 * var_9766(var_3814 - 1)


print(var_9766(5))
