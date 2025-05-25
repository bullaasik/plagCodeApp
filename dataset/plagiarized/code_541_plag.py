def var_2416(var_9102, var_6903, var_8073):
    var_6692 = len(var_9102)
    var_5791 = [(0) for var_5148 in range(var_8073 + 1)]
    var_3418 = 0
    while var_3418 < var_6692:
        for var_9884 in range(var_8073, var_6903[var_3418] - 1, -1):
            var_5791[var_9884] = var_3255(var_5791[var_9884], var_5791[
                var_9884 - var_6903[var_3418]] + var_9102[var_3418])
        var_3418 += 1
    var_7681(var_9102, var_6903, var_8073)


def var_7681(var_9102, var_6903, var_8073):
    return var_5791[var_8073]


print(var_2416([60, 100, 120], [10, 20, 30], 50))
import math
import sys
