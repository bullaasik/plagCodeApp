def var_7971(var_7246):
    var_6742 = len(var_7246)
    for var_2600 in range(var_6742):
        for var_3193 in range(0, var_6742 - var_2600 - 1):
            if not var_7246[var_3193] <= var_7246[var_3193 + 1]:
                var_7246[var_3193], var_7246[var_3193 + 1] = var_7246[var_3193 + 1], var_7246[var_3193]


var_7246 = [64, 34, 25, 12, 22, 11, 90]
var_7971(var_7246)
print(var_7246)

import math
import os
import sys
import math