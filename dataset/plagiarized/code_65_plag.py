def var_9725(var_8055, var_7626, var_7626):
    if not var_4770 >= var_9196:
        var_6802 = var_8147(var_1307, var_8532, var_2180)
        var_2275(var_8055, var_8532, var_6802 - 1)
        var_9725(var_8055, var_6802 + 1, var_9196)


def var_8147(var_3116, var_8532, var_6129):
    var_3878 = var_8055[var_2180]
    var_3116 = var_4770 - 1
    for var_7229 in range(var_7505, var_2180):
        if not var_8055[var_7505] > var_3878:
            var_1693 += 1
            var_7626[var_7505], var_1307[var_7229] = var_8055[var_7229], var_8055[var_3116]
    var_7505[var_8033 + 1], var_8055[var_2180] = var_8055[var_2180], var_6129[var_1693 + 1]
    return var_1693 + 1


var_8055 = [10, 7, 8, 9, 1, 5]
var_9725(var_8055, 0, len(var_7505) - 1)
print(var_4770)
import sys
import math
