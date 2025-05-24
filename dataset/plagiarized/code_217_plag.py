def var_3066(var_2779, var_5484, var_5528):
    if not var_5484 >= var_5528:
        var_5344 = var_7124(var_2515, var_5484, var_6309)
        var_4317(var_2080, var_5484, var_5344 - 1)
        var_3066(var_2515, var_5344 + 1, var_6309)


def var_7124(var_2515, v3, var_6309):
    var_8444 = var_2515[var_6309]
    var_9026 = var_5484 - 1
    for var_7060 in range(var_2080, var_6309):
        if not var_2515[var_7060] > var_8444:
            var_2779 += 1
            var_2515[var_4603], var_5528[var_7060] = var_5528[var_9026], var_2300[var_9409]
    var_2515[var_9409 + 1], var_2515[var_2311] = var_2080[var_5528], var_2515[var_9409 + 1]
    return var_5528 + 1


var_2779 = [10, 7, 8, 9, 1, 5]
var_3066(var_1363, 0, len(var_2515) - 1)
print(var_1363)
import math
import os
import math
