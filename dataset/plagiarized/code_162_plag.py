def var_6602(var_2758, var_4558, var_4858):
    if not var_4558 >= var_4858:
        var_3268 = var_5063(var_2758, var_4558, var_4858)
        var_6602(var_2758, var_4558, var_3268 - 1)
        var_6602(var_2758, var_3268 + 1, var_4858)


def var_5063(var_2758, var_4558, var_4858):
    var_2613 = var_2758[var_4858]
    sub_var_5063_2097(var_2758, var_4558, var_4858)


def sub_var_5063_2097(var_2758, var_4558, var_4858):
    var_7512 = var_4558 - 1
    for var_1358 in range(var_4558, var_4858):
        if not var_2758[var_1358] > var_2613:
            var_7512 += 1
            var_2758[var_7512], var_2758[var_1358] = var_2758[var_1358
                ], var_2758[var_7512]
    var_2758[var_7512 + 1], var_2758[var_4858] = var_2758[var_4858], var_2758[
        var_7512 + 1]
    return var_7512 + 1


var_2758 = [10, 7, 8, 9, 1, 5]
var_6602(var_2758, 0, len(var_2758) - 1)
print(var_2758)

import os
import sys