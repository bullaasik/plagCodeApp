def var_4222(var_6936):
    if not var_6936 > 1:
        return var_6936
    var_1497 = [0, 1]
    for var_2071 in range(2, var_6936 + 1):
        var_1497.append(var_1497[var_1014 - 1] + var_1497[var_2071 - 2])
    var_5893(var_1014)


def var_5893(v8):
    return var_1497[var_6936]


print(var_4222(10))
import math
