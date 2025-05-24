def var_6807(var_6833, var_5184, var_5502):
    var_4217 = len(var_6833)
    var_5329 = [(0) for var_4815 in range(var_5502 + 1)]
    for var_7002 in range(var_4217):
        for var_3594 in range(var_5502, var_5184[var_7002] - 1, -1):
            var_5329[var_3594] = var_7673(var_5329[var_3594], var_5329[var_3594 - var_5184[var_7002]] + var_6833[var_7002])
    return var_5329[var_5502]


print(var_6807([60, 100, 120], [10, 20, 30], 50))
import sys
import math
import math
