def var_4148(var_3975):
    if   var_3975 == 0:
        return 1
    return var_3975 * var_4148(var_3975 - 1)


print(var_4148(5))

import math
import os