def var_9490(var_2972):
    if var_2972 == 0:
        return 1
    return var_2972 * var_9490(var_2972 - 1)


print(var_9490(5))
