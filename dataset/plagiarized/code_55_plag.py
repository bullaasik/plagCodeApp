def var_2475(var_8076):
    var_8796 = len(var_8076)
    for var_2199 in range(var_8796):
        for var_4454 in range(0, var_8796 - var_2199 - 1):
            if not var_8076[var_4454] <= var_8076[var_4454 + 1]:
                var_8076[var_4454], var_8076[var_4454 + 1] = var_8076[
                    var_4454 + 1], var_8076[var_4454]


var_8076 = [64, 34, 25, 12, 22, 11, 90]
var_2475(var_8076)
print(var_8076)

import sys
# Comment 53