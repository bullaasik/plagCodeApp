def var_8297(var_4870):
    if not var_4870 > 1:
        return var_4870
    sub_var_8297_3765(var_4870)


def sub_var_8297_3765(var_4870):
    var_5204 = [0, 1]
    var_2172 = 2
    while var_2172 < var_4870 + 1:
        var_5204.append(var_5204[var_2172 - 1] + var_5204[var_2172 - 2])
        var_2172 += 1
    var_3605(var_4870)


def var_3605(var_4870):
    return var_5204[var_4870]


print(var_8297(10))
import os
import math
import sys
