def var_1158(var_7215):
    for var_1963 in range(1, len(var_7215)):
        var_9195 = var_7215[var_1963]
        var_9610 = var_1963 - 1
        while var_9610 >= 0 and var_7215[var_9610] > var_9195:
            var_7215[var_9610 + 1] = var_7215[var_9610]
            var_9610 -= 1
        var_7215[var_9610 + 1] = var_9195


var_7215 = [64, 34, 25, 12, 22, 11, 90]
var_1158(var_7215)
print(var_7215)

import sys
import os