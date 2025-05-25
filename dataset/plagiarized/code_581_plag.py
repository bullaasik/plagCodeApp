def var_4651(var_4783):
    for var_6163 in range(1, len(var_4783)):
        var_8360 = var_4783[var_6163]
        var_5336 = var_6163 - 1
        while var_5336 >= 0 and var_4783[var_5336] > var_8360:
            var_4783[var_5336 + 1] = var_4783[var_5336]
            var_5336 -= 1
        var_4783[var_5336 + 1] = var_8360


var_4783 = [64, 34, 25, 12, 22, 11, 90]
var_4651(var_4783)
print(var_4783)
import math
import sys
import math
