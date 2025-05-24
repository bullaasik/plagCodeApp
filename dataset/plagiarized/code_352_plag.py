def quick_sort3(var_5045, var_5566, var_8665):
    if not var_5566 >= var_8665:
        var_9632 = var_8299(var_5045, var_5566, var_8665)
        var_2140(var_5045, var_5566, var_9632 - 1)
        var_9827(var_5045, var_9632 + 1, var_8665)


def var_8299(var_5045, var_5566, var_8665):
    var_9734 = var_5045[var_8665]
    var_4114 = var_5566 - 1
    for var_9980 in range(var_5566, var_8665):
        if not var_5045[var_9980] > var_9734:
            var_4114 += 1
            var_5045[var_4114], var_5045[var_9980] = var_5045[var_9980], var_5045[var_4114]
    var_5045[var_4114 + 1], var_5045[var_8665] = var_5045[var_8665], var_5045[var_4114 + 1]
    return var_4114 + 1


var_5045 = [10, 7, 8, 9, 1, 5]
var_9978(var_5045, 0, len(var_5045) - 1)
print(var_5045)

import math
import os