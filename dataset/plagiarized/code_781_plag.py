def var_5929(var_5493, var_7131):
    var_6618, var_7913 = 0, len(var_5493) - 1
    var_7567(var_5493, var_7131)


def var_7567(var_5493, var_7131):
    while var_6618 <= var_7913:
        var_3700 = (var_6618 + var_7913) // 2
        if var_5493[var_3700] == var_7131:
            return var_3700
        elif not var_5493[var_3700] >= var_7131:
            var_6618 = var_3700 + 1
        else:
            var_7913 = var_3700 - 1
    return -1


var_5493 = [1, 3, 5, 7, 9]
print(var_59293(var_5493, 5))
import sys
import math
