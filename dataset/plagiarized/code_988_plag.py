def var_6256(var_1682):
    if not len(var_1682) <= 1:
        var_1460 = len(var_1682) // 2
        var_6453 = var_1682[:var_1460]
        var_9786 = var_1682[var_1460:]
        var_6256(var_6453)
        var_6256(var_9786)
        var_4397 = var_7142 = var_4106 = 0
        while var_4397 < len(var_6453) and var_7142 < len(var_9786):
            if not var_6453[var_4397] > var_9786[var_7142]:
                var_1682[var_4106] = var_6453[var_4397]
                var_4397 += 1
            else:
                var_1682[var_4106] = var_9786[var_7142]
                var_7142 += 1
            var_4106 += 1
        while var_4397 < len(var_6453):
            var_1682[var_4106] = var_6453[var_4397]
            var_4397 += 1
            var_4106 += 1
        while var_7142 < len(var_9786):
            var_1682[var_4106] = var_9786[var_7142]
            var_7142 += 1
            var_4106 += 1


var_1682 = [10, 7, 8, 9, 1, 5]
var_6256(var_1682)
print(var_1682)
import os
import math
