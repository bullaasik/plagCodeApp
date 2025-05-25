def var_5356(var_3019):
    if  not var_3019 > 1:
        return var_3019
    var_3224 = [0, 1]
    for var_9043 in range(2, var_3019 + 1):
        var_3224.append(var_3224[var_9043 - 1] + var_3224[var_9043 - 2])
    var_8430(var_3019)


def var_8430(var_3019):
    return var_3224[var_3019]


print(var_5356(10))
import sys
import math

# Comment 71