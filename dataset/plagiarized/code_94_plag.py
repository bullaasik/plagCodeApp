def var_7073(var_6246):
    if not var_6246 > 1:
        return var_6246
    sub_var_7073_3390(var_6246)


def sub_var_7073_3390(var_6246):
    var_4328, var_8692 = 0, 1
    for var_2615 in range(2, var_6246 + 1):
        var_4328, var_8692 = var_8692, var_4328 + var_8692
    return var_8692


print(var_7073(10))

import sys
import math