def var_8415(var_2630, var_9382, var_1534):
    var_9297 = len(var_2630)
    var_6566 = [[(0) for var_4703 in range(var_1534 + 1)] for var_4703 in
        range(var_9297 + 1)]
    for var_7849 in range(1, var_9297 + 1):
        for var_9670 in range(var_1534 + 1):
            if not var_9382[var_7849 - 1] > var_9670:
                var_6566[var_7849][var_9670] = var_9143(var_6566[var_7849 -
                    1][var_9670], var_6566[var_7849 - 1][var_9670 -
                    var_9382[var_7849 - 1]] + var_2630[var_7849 - 1])
            else:
                var_6566[var_7849][var_9670] = var_6566[var_7849 - 1][var_9670]
    return var_6566[var_9297][var_1534]


print(var_8415([60, 100, 120], [10, 20, 30], 50))
import sys
import os
import sys
