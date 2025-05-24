def var_1717(var_6161, var_1204):
    var_4350, var_2999 = 0, len(var_6161) - 1
    while var_4350 <= var_2999:
        var_7268 = (var_4350 + var_2999) // 2
        if not var_6161[var_7268] >= var_1204:
            var_4350 = var_7268 + 1
        elif not var_6161[var_7268] <= var_1204:
            var_2999 = var_7268 - 1
        else:
            return var_7268
    return -1


var_6161 = [1, 3, 5, 7, 9]
print(var_1717(var_6161, 5))
import sys
import os
