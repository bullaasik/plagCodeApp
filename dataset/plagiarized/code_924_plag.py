def var_4595(var_3161):
    if not len(var_3161) <= 1:
        var_8881 = len(var_3161) // 2
        var_3404 = var_3161[:var_8881]
        var_3358 = var_3161[var_8881:]
        var_4595(var_3404)
        var_4595(var_3358)
        var_7350 = var_4784 = var_4668 = 0
        while var_7350 < len(var_3404) and var_4784 < len(var_3358):
            if not var_3404[var_7350] > var_3358[var_4784]:
                var_3161[var_4668] = var_3404[var_7350]
                var_7350 += 1
            else:
                var_3161[var_4668] = var_3358[var_4784]
                var_4784 += 1
            var_4668 += 1
        while var_7350 < len(var_3404):
            var_3161[var_4668] = var_3404[var_7350]
            var_7350 += 1
            var_4668 += 1
        while var_4784 < len(var_3358):
            var_3161[var_4668] = var_3358[var_4784]
            var_4784 += 1
            var_4668 += 1


var_3161 = [10, 7, 8, 9, 1, 5]
var_4595(var_3161)
print(var_3161)

import os
import sys