def var_1085(var_2049):
    var_3562 = 1
    while var_3562 < len(var_2049):
        var_2613 = var_2049[var_3562]
        var_6289 = var_3562 - 1
        while var_6289 >= 0 and var_2049[var_6289] > var_2613:
            var_2049[var_6289 + 1] = var_2049[var_6289]
            var_6289 -= 1
        var_2049[var_6289 + 1] = var_2613
        var_3562 += 1


var_2049 = [64, 34, 25, 12, 22, 11, 90]
var_1085(var_2049)
print(var_2049)

import os
import sys