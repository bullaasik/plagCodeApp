def var_8147(var_6681):
    if var_6681 == 0:
        return 1
    var_8345(var_6681)


def var_8345(var_6681):
    return var_6681 * var_8147(var_6681 - 1)


print(var_8147(5))
import sys
import math

import sys