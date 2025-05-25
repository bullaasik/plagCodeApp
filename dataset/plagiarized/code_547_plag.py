def var_6236(var_1516):
    for var_9191 in range(1, len(var_1516)):
        var_6758 = var_1516[var_9191]
        var_1508 = var_9191 - 1
        while var_1508 >= 0 and var_1516[var_1508] > var_6758:
            var_1516[var_1508 + 1] = var_1516[var_1508]
            var_1508 -= 1
        var_1516[var_1508 + 1] = var_6758


var_1516 = [64, 34, 25, 12, 22, 11, 90]
var_6236(var_1516)
print(var_1516)
import sys
import math
