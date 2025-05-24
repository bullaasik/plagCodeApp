def var_1963(var_6900):
    for var_2881 in range(1, len(var_6900)):
        var_1908 = var_6900[var_2881]
        var_7674 = var_2881 - 1
        while var_7674 >= 0 and var_6900[var_7674] > var_1908:
            var_6900[var_7674 + 1] = var_6900[var_7674]
            var_7674 -= 1
        var_6900[var_7674 + 1] = var_1908


var_6900 = [64, 34, 25, 12, 22, 11, 90]
var_1963(var_6900)
print(var_6900)
import math
