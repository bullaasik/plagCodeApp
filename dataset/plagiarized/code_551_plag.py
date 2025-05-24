def var_1897(var_6469, var_1114):
    while var_1114:
        var_5215 = var_1114
        var_1114 = var_6469 % var_1114
        var_6469 = var_5215
    return var_6469


print(var_1897(60, 48))

import math
import sys
import os
import sys