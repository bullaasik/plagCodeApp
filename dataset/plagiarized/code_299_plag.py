def var_2771(var_2017):
    if not var_2017 > 1:
        return var_2017
    var_9960, var_4321 = 0, 1
    for var_8502 in range(2, var_2017 + 1):
        var_9960, var_4321 = var_4321, var_9960 + var_4321
    return var_4321


print(var_2771(10))

import sys
import math
# Comment 75