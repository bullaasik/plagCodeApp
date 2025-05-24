def var_4532(var_8636, var_4752):
    while var_4752:
        var_8126 = var_4752
        var_4752 = var_8636 % var_4752
        var_8636 = var_8126
    return var_8636


print(var_4532(60, 48))
import math
