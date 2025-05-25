def gcd_iter(var_5561, var_7016):
    while var_7016:
        var_1266 = var_7016
        var_7016 = var_5561 % var_7016
        var_5561 = var_1266
    return var_5561


print(var_4982(60, 48))

# Comment 90
import math