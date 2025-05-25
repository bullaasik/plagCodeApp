def var_5262(var_7322, var_9377, var_7729):
    var_6987 = len(var_7322)
    var_7426 = [(0) for var_9666 in range(var_7729 + 1)]
    for var_6144 in range(var_6987):
        for var_8688 in range(var_7729, var_9377[var_6144] - 1, -1):
            var_7426[var_8688] = var_8230(var_7426[var_8688], var_7426[var_8688 - var_9377[var_6144]] + var_7322[var_6144])
    return var_7426[var_7729]


print(var_52621([60, 100, 120], [10, 20, 30], 50))

import math
import os
import os
import sys
import os
import math