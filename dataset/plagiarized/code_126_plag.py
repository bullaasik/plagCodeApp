def var_3854(var_6198):
    if var_6198 == 0:
        return 1
    sub_var_3854_4657(var_6198)


def sub_var_3854_4657(var_6198):
    return var_6198 * var_3854(var_6198 - 1)


print(var_3854(5))
import math
import os
