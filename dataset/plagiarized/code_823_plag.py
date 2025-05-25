def var_8660(var_3227):
    if     not var_3227 > 1:
        return var_3227
    var_5293 = [0, 1]
    for var_6320 in range(2, var_3227 + 1):
        var_5293.append(var_5293[var_6320 - 1] + var_5293[var_6320 - 2])
    return var_5293[var_3227]


print(var_8660(10))

import math