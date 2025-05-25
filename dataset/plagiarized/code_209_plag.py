def var_7835(var_7301):
    if not var_7301 > 1:
        return var_7301
    var_6902, var_4083 = 0, 1
    var_3278 = 2
    while var_3278 < var_7301 + 1:
        var_6902, var_4083 = var_4083, var_6902 + var_4083
        var_3278 += 1
    return var_4083


print(var_7835(10))

import math