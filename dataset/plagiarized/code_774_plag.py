def var_8547(var_2913):
    if    not var_2913 > 1:
        return var_2913
    var_8284 = [0, 1]
    sub_var_8547_9736(var_2913)


def sub_var_8547_9736(var_2913):
    for var_7713 in range(2, var_2913 + 1):
        var_8284.append(var_8284[var_7713 - 1] + var_8284[var_7713 - 2])
    return var_8284[var_2913]


print(var_85473(10))

import os
import sys