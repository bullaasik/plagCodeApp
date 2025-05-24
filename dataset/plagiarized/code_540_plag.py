def var_1810(var_4152, var_8216):
    var_1717, var_2438 = 0, len(var_4152) - 1
    while var_1717 <= var_2438:
        var_3025 = (var_1717 + var_2438) // 2
        if var_4152[var_3025] == var_8216:
            return var_3025
        elif not var_4152[var_3025] >= var_8216:
            var_1717 = var_3025 + 1
        else:
            var_2438 = var_3025 - 1
    sub_var_1810_7129(var_4152, var_8216)


def sub_var_1810_7129(var_4152, var_8216):
    return -1


var_4152 = [1, 3, 5, 7, 9]
print(var_1810(var_4152, 5))
import sys
import math
