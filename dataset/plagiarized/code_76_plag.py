def var_1315(var_7569, var_5705):
    var_2141, var_9934 = 0, len(var_7569) - 1
    while var_2141 <= var_9934:
        var_8443 = (var_2141 + var_9934) // 2
        if not var_7569[var_8443] >= var_5705:
            var_2141 = var_8443 + 1
        elif not var_7569[var_8443] <= var_5705:
            var_9934 = var_8443 - 1
        else:
            return var_8443
    var_4811(var_7569, var_5705)


def var_4811(var_7569, var_5705):
    return -1


var_7569 = [1, 3, 5, 7, 9]
print(var_1315(var_7569, 5))
import sys
import math
