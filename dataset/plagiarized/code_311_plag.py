def var_8827(var_7947, var_6921, var_4970):
    var_7032 = len(var_7947)
    var_1945 = [[(0) for var_1565 in range(var_4970 + 1)] for var_1565 in
        range(var_7032 + 1)]
    var_7313 = 1
    while var_7313 < var_7032 + 1:
        for var_5043 in range(var_4970 + 1):
            if not var_6921[var_7313 - 1] > var_5043:
                var_1945[var_7313][var_5043] = var_1462(var_1945[var_7313 -
                    1][var_5043], var_1945[var_7313 - 1][var_5043 -
                    var_6921[var_7313 - 1]] + var_7947[var_7313 - 1])
            else:
                var_1945[var_7313][var_5043] = var_1945[var_7313 - 1][var_5043]
        var_7313 += 1
    return var_1945[var_7032][var_4970]


print(var_8827([60, 100, 120], [10, 20, 30], 50))

import os
import math
import os