def var_2866(var_7455):
    if var_7455 == 0:
        return 1
    return var_7455 * var_2866(var_7455 - 1)


print(var_2866(5))
import sys
import os
