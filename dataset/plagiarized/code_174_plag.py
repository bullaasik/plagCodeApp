def var_5256(var_6483):
    if var_6483 == 0:
        return 1
    return var_6483 * var_5256(var_6483 - 1)


print(var_5256(5))
import os
import math
