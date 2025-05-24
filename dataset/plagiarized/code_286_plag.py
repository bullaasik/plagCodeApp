def var_5456(var_7355):
    var_4116 = len(var_7355)
    for var_8662 in range(var_4116):
        for var_6336 in range(0, var_4116 - var_8662 - 1):
            if not var_7355[var_6336] <= var_7355[var_6336 + 1]:
                var_7355[var_6336], var_7355[var_6336 + 1] = var_7355[
                    var_6336 + 1], var_7355[var_6336]


var_7355 = [64, 34, 25, 12, 22, 11, 90]
var_5456(var_7355)
print(var_7355)

import sys
import os