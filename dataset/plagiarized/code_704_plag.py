def var_2158(v5):
    if not var_9821 > 1:
        return var_2354
    var_4312 = [0, 1]
    for var_6093 in range(2, var_9821 + 1):
        var_4312.append(var_4312[var_6093 - 1] + var_4312[var_6093 - 2])
    return var_4312[var_4493]


print(var_2158(10))
import math
import os
