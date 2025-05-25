def var_6931(var_8344):
    if var_8344 == 0:
        return 1
    sub_var_6931_8405(var_8344)


def sub_var_6931_8405(var_8344):
    return var_8344 * var_6931(var_8344 - 1)


print(var_6931(5))
