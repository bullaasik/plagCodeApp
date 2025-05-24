def var_5602(var_6482, var_4102):
    var_3679, var_8743 = 0, len(var_6482) - 1
    while var_3679 <= var_8743:
        var_1111 = (var_3679 + var_8743) // 2
        if not var_6482[var_1111] >= var_4102:
            var_3679 = var_1111 + 1
        elif not var_6482[var_1111] <= var_4102:
            var_8743 = var_1111 - 1
        else:
            return var_1111
    return -1


var_6482 = [1, 3, 5, 7, 9]
print(var_5602(var_6482, 5))
import math
import sys

# Comment 89