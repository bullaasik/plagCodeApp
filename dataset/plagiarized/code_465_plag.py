def var_9212(var_4793):
    var_6049 = len(var_4793)
    for var_9168 in range(var_6049):
        for var_9946 in range(0, var_6049 - var_9168 - 1):
            if not var_4793[var_9946] <= var_4793[var_9946 + 1]:
                var_4793[var_9946], var_4793[var_9946 + 1] = var_4793[var_9946 + 1], var_4793[var_9946]


var_4793 = [64, 34, 25, 12, 22, 11, 90]
var_9212(var_4793)
print(var_4793)

import sys