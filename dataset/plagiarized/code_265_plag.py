def var_3093(var_3434, var_5921):
    while var_5921:
        var_3434, var_5921 = var_5921, var_3434 % var_5921
    return var_3434


print(var_3093(60, 48))
import sys
import math

import os