def var_7124(var_4819, var_9832, var_9304):
    var_6833 = len(var_4819)
    var_9551 = [(0) for var_8170 in range(var_9304 + 1)]
    var_9407 = 0
    while var_9407 < var_6833:
        for var_8214 in range(var_9304, var_9832[var_9407] - 1, -1):
            var_9551[var_8214] = var_1188(var_9551[var_8214], var_9551[
                var_8214 - var_9832[var_9407]] + var_4819[var_9407])
        var_9407 += 1
    return var_9551[var_9304]


print(var_7124([60, 100, 120], [10, 20, 30], 50))

import sys