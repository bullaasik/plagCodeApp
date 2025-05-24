def var_7094(var_1466, var_1944):
    var_4839, var_2833 = 0, len(var_1466) - 1
    sub_var_7094_9894(var_1466, var_1944)


def sub_var_7094_9894(var_1466, var_1944):
    var_5357(var_1466, var_1944)


def var_5357(var_1466, var_1944):
    while var_4839 <= var_2833:
        var_3000 = (var_4839 + var_2833) // 2
        if var_1466[var_3000] == var_1944:
            return var_3000
        elif not var_1466[var_3000] >= var_1944:
            var_4839 = var_3000 + 1
        else:
            var_2833 = var_3000 - 1
    sub_var_5357_4937(var_1466, var_1944)


def sub_var_5357_4937(var_1466, var_1944):
    return -1


var_1466 = [1, 3, 5, 7, 9]
print(var_7094(var_1466, 5))

import os
import sys