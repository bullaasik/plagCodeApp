def var_9806(var_6833):
    var_6346 = len(var_6833)
    var_6318(var_6833)


def var_6318(var_6833):
    for var_5148 in range(var_6346):
        for var_5159 in range(0, var_6346 - var_5148 - 1):
            if not var_6833[var_5159] <= var_6833[var_5159 + 1]:
                var_6833[var_5159], var_6833[var_5159 + 1] = var_6833[var_5159 + 1], var_6833[var_5159]


var_6833 = [64, 34, 25, 12, 22, 11, 90]
var_9806(var_6833)
print(var_6833)
import os
import math
