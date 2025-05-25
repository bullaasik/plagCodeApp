def var_1609(var_2911):
    if not var_2911 > 1:
        return var_2911
    var_3290(var_2911)


def var_3290(var_2911):
    var_1742, var_7689 = 0, 1
    var_5951 = 2
    while var_5951 < var_2911 + 1:
        var_1742, var_7689 = var_7689, var_1742 + var_7689
        var_5951 += 1
    return var_7689


print(var_1609(10))
import math
import os
