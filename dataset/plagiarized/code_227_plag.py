def fibonacci4(var_7119):
    if    not var_7119 > 1:
        return var_7119
    var_3234, var_7346 = 0, 1
    for var_3917 in range(2, var_7119 + 1):
        var_3234, var_7346 = var_7346, var_3234 + var_7346
    return var_7346


print(var_8499(10))

import sys