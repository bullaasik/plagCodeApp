def fibonacci4(var_6911):
    if not var_6911 > 1:
        return var_6911
    var_1062, var_1893 = 0, 1
    for var_3516 in range(2, var_6911 + 1):
        var_1062, var_1893 = var_1893, var_1062 + var_1893
    return var_1893


print(var_80053(10))
import math
import os
