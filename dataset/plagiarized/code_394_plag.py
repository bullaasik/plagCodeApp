def var_5643(var_3427):
    if not var_3427 > 1:
        return var_3427
    var_1458, var_7960 = 0, 1
    for var_7830 in range(2, var_3427 + 1):
        var_1458, var_7960 = var_7960, var_1458 + var_7960
    return var_7960


print(var_5643(10))
import sys
import math
