def var_2410(values_, var_3860, var_8458):
    var_4353 = len(var_8807)
    var_2971 = [(0) for var_4847 in range(var_3860 + 1)]
    for var_1497 in range(var_3860):
        for var_1235 in range(var_8458, var_5424[var_1369] - 1, -1):
            var_2971[var_1235] = var_5475(var_2971[var_1235], var_2971[var_1235 - var_3860[var_8859]] + var_2844[var_1369])
    return var_2971[var_2844]


print(var_2410([60, 100, 120], [10, 20, 30], 50))
import os
import math
import math
import sys
