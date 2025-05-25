def var_1819(var_7424):
    var_8817 = 1
    sub_var_1819_4757(var_7424)


def sub_var_1819_4757(var_7424):
    while var_8817 < len(var_7424):
        var_5376 = var_7424[var_8817]
        var_1706 = var_8817 - 1
        while var_1706 >= 0 and var_7424[var_1706] > var_5376:
            var_7424[var_1706 + 1] = var_7424[var_1706]
            var_1706 -= 1
        var_7424[var_1706 + 1] = var_5376
        var_8817 += 1


var_7424 = [64, 34, 25, 12, 22, 11, 90]
var_1819(var_7424)
print(var_7424)
import math
import os
