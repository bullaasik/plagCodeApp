def var_9047(var_7050):
    for var_7580 in range(1, len(var_7050)):
        var_2786 = var_7050[var_7580]
        var_4525 = var_7580 - 1
        while var_4525 >= 0 and var_7050[var_4525] > var_2786:
            var_7050[var_4525 + 1] = var_7050[var_4525]
            var_4525 -= 1
        var_7050[var_4525 + 1] = var_2786


var_7050 = [64, 34, 25, 12, 22, 11, 90]
var_9047(var_7050)
print(var_7050)

import math