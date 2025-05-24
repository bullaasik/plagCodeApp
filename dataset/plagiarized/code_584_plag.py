def var_1243(var_7256, var_7312):
    var_6347, var_4165 = 0, len(var_7256) - 1
    sub_var_1243_7822(var_7256, var_7312)


def sub_var_1243_7822(var_7256, var_7312):
    while var_6347 <= var_4165:
        var_5446 = (var_6347 + var_4165) // 2
        if var_7256[var_5446] == var_7312:
            return var_5446
        elif not var_7256[var_5446] >= var_7312:
            var_6347 = var_5446 + 1
        else:
            var_4165 = var_5446 - 1
    var_9655(var_7256, var_7312)


def var_9655(var_7256, var_7312):
    return -1


var_7256 = [1, 3, 5, 7, 9]
print(var_1243(var_7256, 5))
import os
import sys
