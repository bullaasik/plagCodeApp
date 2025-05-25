def var_2624(var_9282):
    if var_9282 == 0:
        return 1
    var_8048(var_9282)


def var_8048(var_9282):
    return var_9282 * var_2624(var_9282 - 1)


print(var_2624(5))
import sys
import os
