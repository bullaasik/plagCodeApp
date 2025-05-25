def var_8226(var_8356):
    if not var_8356 > 1:
        return var_8356
    var_4638 = [0, 1]
    var_7931 = 2
    while var_7931 < var_8356 + 1:
        var_4638.append(var_4638[var_7931 - 1] + var_4638[var_7931 - 2])
        var_7931 += 1
    return var_4638[var_8356]


print(var_8226(10))
import math
import os
