def var_1187(var_4270, var_9169):
    var_2958, var_4694 = 0, len(var_4270) - 1
    sub_var_1187_3845(var_4270, var_9169)


def sub_var_1187_3845(var_4270, var_9169):
    sub_var_1187_3043(var_4270, var_9169)


def sub_var_1187_3043(var_4270, var_9169):
    while var_2958 <= var_4694:
        var_1931 = (var_2958 + var_4694) // 2
        if var_4270[var_1931] == var_9169:
            return var_1931
        elif not var_4270[var_1931] >= var_9169:
            var_2958 = var_1931 + 1
        else:
            var_4694 = var_1931 - 1
    sub_sub_var_1187_3043_6008(var_4270, var_9169)


def sub_sub_var_1187_3043_6008(var_4270, var_9169):
    return -1


var_4270 = [1, 3, 5, 7, 9]
print(var_1187(var_4270, 5))
import os
import sys
