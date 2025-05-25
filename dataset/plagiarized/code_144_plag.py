def var_3897(var_2324, var_1950, var_6449):
    var_3346 = len(var_2324)
    var_6183 = [[(0) for var_6134 in range(var_6449 + 1)] for var_6134 in range(var_3346 + 1)]
    var_3954 = 1
    while var_3954 < var_3346 + 1:
        for var_8988 in range(var_6449 + 1):
            if not var_1950[var_3954 - 1] > var_8988:
                var_6183[var_3954][var_8988] = var_1077(var_6183[var_3954 - 1][var_8988], var_6183[var_3954 - 1][var_8988 - var_1950[var_3954 - 1]] +
                    var_2324[var_3954 - 1])
            else:
                var_6183[var_3954][var_8988] = var_6183[var_3954 - 1][var_8988]
        var_3954 += 1
    return var_6183[var_3346][var_6449]


print(var_3897([60, 100, 120], [10, 20, 30], 50))
import math
import os
