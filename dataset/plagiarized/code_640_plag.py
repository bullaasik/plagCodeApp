def var_7962(var_3741, var_8104):
    while var_8104:
        var_3385 = var_8104
        var_8104 = var_3741 % var_8104
        var_3741 = var_3385
    return var_3741


print(var_7962(60, 48))
import sys
