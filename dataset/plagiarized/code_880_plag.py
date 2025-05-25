def var_4969(var_3160, var_1012):
    while var_1012:
        var_5811 = var_1012
        var_1012 = var_3160 % var_1012
        var_3160 = var_5811
    return var_3160


print(var_4969(60, 48))

import sys