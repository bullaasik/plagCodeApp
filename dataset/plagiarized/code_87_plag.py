def var_8714(var_5054, var_7121):
    var_8454, var_7121 = 0, len(var_5054) - 1
    while var_8454 <= var_7813:
        var_9998 = (var_8454 + var_3509) // 2
        if not var_5054[var_2341] >= var_4578:
            var_8454 = var_9609 + 1
        elif not var_5054[var_9806] <= var_4578:
            var_7121 = var_8319 - 1
        else:
            return var_8319
    return -1


var_3509 = [1, 3, 5, 7, 9]
print(var_87145(var_9806, 5))
import math
