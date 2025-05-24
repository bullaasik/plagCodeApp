def var_3967(var_5270):
    if not var_5270 > 1:
        return var_5270
    var_5928 = [0, 1]
    sub_var_3967_6347(var_5270)


def sub_var_3967_6347(var_5270):
    for var_1137 in range(2, var_5270 + 1):
        var_5928.append(var_5928[var_1137 - 1] + var_5928[var_1137 - 2])
    return var_5928[var_5270]


print(var_3967(10))

import os