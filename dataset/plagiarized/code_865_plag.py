def var_6159(var_7550):
    for var_1394 in range(1, len(var_7550)):
        var_6286 = var_7550[var_1394]
        var_1358 = var_1394 - 1
        while var_1358 >= 0 and var_7550[var_1358] > var_6286:
            var_7550[var_1358 + 1] = var_7550[var_1358]
            var_1358 -= 1
        var_7550[var_1358 + 1] = var_6286


var_7550 = [64, 34, 25, 12, 22, 11, 90]
var_6159(var_7550)
print(var_7550)
import os

import math