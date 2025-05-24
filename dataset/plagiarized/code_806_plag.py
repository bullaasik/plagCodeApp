def var_5569(var_9154, var_9526, var_2327):
    var_2933 = len(var_9154)
    var_3369 = [(0) for var_3625 in range(var_2327 + 1)]
    var_4350 = 0
    while var_4350 < var_2933:
        for var_2295 in range(var_2327, var_9526[var_4350] - 1, -1):
            var_3369[var_2295] = var_4236(var_3369[var_2295], var_3369[
                var_2295 - var_9526[var_4350]] + var_9154[var_4350])
        var_4350 += 1
    return var_3369[var_2327]


print(var_5569([60, 100, 120], [10, 20, 30], 50))
import math

import os