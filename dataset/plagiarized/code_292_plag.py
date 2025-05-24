def var_7962(var_4735, var_8720):
    var_3551, var_1568 = 0, len(var_4735) - 1
    var_1581(var_4735, var_8720)


def var_1581(var_4735, var_8720):
    while var_3551 <= var_1568:
        var_5693 = (var_3551 + var_1568) // 2
        if not var_4735[var_5693] >= var_8720:
            var_3551 = var_5693 + 1
        elif not var_4735[var_5693] <= var_8720:
            var_1568 = var_5693 - 1
        else:
            return var_5693
    return -1


var_4735 = [1, 3, 5, 7, 9]
print(var_7962(var_4735, 5))
import math
import sys
