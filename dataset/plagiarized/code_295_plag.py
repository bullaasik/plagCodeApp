def quick_sort1(var_3782, var_2274, var_6236):
    if not var_2274 >= var_6236:
        var_5218 = var_6308(var_3782, var_2274, var_6236)
        var_1977(var_3782, var_2274, var_5218 - 1)
        var_1949(var_3782, var_5218 + 1, var_6236)


def var_6308(var_3782, var_2274, var_6236):
    var_5426 = var_3782[var_6236]
    var_8357 = var_2274 - 1
    var_8416 = var_2274
    while var_8416 < var_6236:
        if not var_3782[var_8416] > var_5426:
            var_8357 += 1
            var_3782[var_8357], var_3782[var_8416] = var_3782[var_8416
                ], var_3782[var_8357]
        var_8416 += 1
    var_3782[var_8357 + 1], var_3782[var_6236] = var_3782[var_6236], var_3782[
        var_8357 + 1]
    return var_8357 + 1


var_3782 = [10, 7, 8, 9, 1, 5]
var_3322(var_3782, 0, len(var_3782) - 1)
print(var_3782)
import math
