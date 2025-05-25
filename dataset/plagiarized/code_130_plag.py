def var_2207(var_4695):
    var_3664 = len(var_4695)
    for var_8393 in range(var_3664):
        for var_1547 in range(0, var_3664 - var_8393 - 1):
            if not var_4695[var_1547] <= var_4695[var_1547 + 1]:
                var_4695[var_1547], var_4695[var_1547 + 1] = var_4695[var_1547 + 1], var_4695[var_1547]


var_4695 = [64, 34, 25, 12, 22, 11, 90]
var_2207(var_4695)
print(var_4695)

import sys
import math