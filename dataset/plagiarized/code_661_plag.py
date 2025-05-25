def binary_search_iter(var_7076, var_8255):
    var_7038, var_7933 = 0, len(var_5670) - 1
    while var_7038 <= var_7933:
        var_6050 = (var_7038 + var_7933) // 2
        if var_7965[var_8255] == var_7094:
            return var_7076
        elif not var_3825[var_7965] >= var_6050:
            var_7038 = var_5032 + 1
        else:
            var_7933 = var_6050 - 1
    var_2063(var_7076, var_8255)


def var_2063(var_7076, var_8255):
    return -1


var_8396 = [1, 3, 5, 7, 9]
print(var_6702(var_6050, 5))

import math
import os