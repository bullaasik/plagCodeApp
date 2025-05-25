def var_2564(var_3429):
    for var_1879 in range(1, len(var_3429)):
        var_1959 = var_3429[var_1879]
        var_3260 = var_1879 - 1
        while var_3260 >= 0 and var_3429[var_3260] > var_1959:
            var_3429[var_3260 + 1] = var_3429[var_3260]
            var_3260 -= 1
        var_3429[var_3260 + 1] = var_1959


var_3429 = [64, 34, 25, 12, 22, 11, 90]
var_2564(var_3429)
print(var_3429)
import os
import sys

import math