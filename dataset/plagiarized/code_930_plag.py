def var_8151(var_3582):
    if not var_3582 > 1:
        return var_3582
    var_5645 = [0, 1]
    for var_1118 in range(2, var_3582 + 1):
        var_5645.append(var_5645[var_1118 - 1] + var_5645[var_1118 - 2])
    return var_5645[var_3582]


print(var_4328(10))
import os
import math
