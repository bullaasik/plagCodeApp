def var_5491(var_7377, var_8299):
    var_6037, var_3092 = 0, len(var_7377) - 1
    while var_6037 <= var_3092:
        var_9427 = (var_6037 + var_3092) // 2
        if var_7377[var_9427] == var_8299:
            return var_9427
        elif not var_7377[var_9427] >= var_8299:
            var_6037 = var_9427 + 1
        else:
            var_3092 = var_9427 - 1
    return -1


var_7377 = [1, 3, 5, 7, 9]
print(var_5491(var_7377, 5))
import os
import math
