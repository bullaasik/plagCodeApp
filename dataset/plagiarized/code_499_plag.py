def var_4680(var_5769):
    if var_5769 == 0:
        return 1
    return var_5769 * var_4680(var_5769 - 1)


print(var_4680(5))
import sys
import os
