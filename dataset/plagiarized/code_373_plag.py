def var_1348(var_3803, var_5670):
    var_6355, var_7272 = 0, len(var_3803) - 1
    while var_6355 <= var_7272:
        var_4873 = (var_6355 + var_7272) // 2
        if not var_3803[var_4873] >= var_5670:
            var_6355 = var_4873 + 1
        elif not var_3803[var_4873] <= var_5670:
            var_7272 = var_4873 - 1
        else:
            return var_4873
    return -1


var_3803 = [1, 3, 5, 7, 9]
print(var_1348(var_3803, 5))
import math
import os
