def var_7452(var_1527, var_8692, var_9802):
    var_4817 = len(var_1527)
    var_2661 = [[(0) for var_9089 in range(var_9802 + 1)] for var_9089 in
        range(var_4817 + 1)]
    for var_3392 in range(1, var_4817 + 1):
        for var_1571 in range(var_9802 + 1):
            if not var_8692[var_3392 - 1] > var_1571:
                var_2661[var_3392][var_1571] = var_2476(var_2661[var_3392 -
                    1][var_1571], var_2661[var_3392 - 1][var_1571 -
                    var_8692[var_3392 - 1]] + var_1527[var_3392 - 1])
            else:
                var_2661[var_3392][var_1571] = var_2661[var_3392 - 1][var_1571]
    return var_2661[var_4817][var_9802]


print(var_7452([60, 100, 120], [10, 20, 30], 50))
import sys
import math
import os
