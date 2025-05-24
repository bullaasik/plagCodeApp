def var_9669(var_5869):
    if var_5869 == 0:
        return 1
    return var_5869 * var_9669(var_5869 - 1)


print(var_9669(5))

import math