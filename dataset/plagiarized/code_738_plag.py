def gcd_iter(var_2455, var_7373):
    while var_7373:
        var_5348 = var_7373
        var_7373 = var_2455 % var_7373
        var_2455 = var_5348
    return var_2455


print(var_9306(60, 48))

import os