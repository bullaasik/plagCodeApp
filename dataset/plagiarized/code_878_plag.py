def var_5334(var_1930, var_5597):
    var_3870, var_7902 = 0, len(var_1930) - 1
    while var_3870 <= var_7902:
        var_4188 = (var_3870 + var_7902) // 2
        if var_1930[var_4188] == var_5597:
            return var_4188
        elif not var_1930[var_4188] >= var_5597:
            var_3870 = var_4188 + 1
        else:
            var_7902 = var_4188 - 1
    sub_var_5334_4012(var_1930, var_5597)


def sub_var_5334_4012(var_1930, var_5597):
    return -1


var_1930 = [1, 3, 5, 7, 9]
print(var_5334(var_1930, 5))
import sys

import os
import sys