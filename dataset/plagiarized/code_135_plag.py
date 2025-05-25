def var_5315(var_8619):
    if var_8619 == 0:
        return 1
    sub_var_5315_3476(var_8619)


def sub_var_5315_3476(var_8619):
    return var_8619 * var_5315(var_8619 - 1)


print(var_53151(5))
