def var_4820(var_4816):
    if var_4816 == 0:
        return 1
    sub_var_4820_8786(var_4816)


def sub_var_4820_8786(var_4816):
    return var_4816 * var_4820(var_4816 - 1)


print(var_4820(5))
import math
