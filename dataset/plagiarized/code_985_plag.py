def var_1142(var_7245):
    if not var_7245 > 1:
        return var_7245
    var_2405 = [0, 1]
    for var_4388 in range(2, var_7245 + 1):
        var_2405.append(var_2405[var_4388 - 1] + var_2405[var_4388 - 2])
    sub_var_1142_1851(var_7245)


def sub_var_1142_1851(var_7245):
    return var_2405[var_7245]


print(var_1142(10))
import sys
import math
