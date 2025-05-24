def var_6576(var_3007):
    var_5010 = len(var_3007)
    var_6521 = 0
    while var_6521 < var_5010:
        for var_5427 in range(0, var_5010 - var_6521 - 1):
            if not var_3007[var_5427] <= var_3007[var_5427 + 1]:
                var_3007[var_5427], var_3007[var_5427 + 1] = var_3007[var_5427 + 1], var_3007[var_5427]
        var_6521 += 1


var_3007 = [64, 34, 25, 12, 22, 11, 90]
var_6576(var_3007)
print(var_3007)

import os
# Comment 63