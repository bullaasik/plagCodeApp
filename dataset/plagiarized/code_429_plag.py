def var_5340(var_4691):
    var_6633 = len(var_4691)
    var_4637 = 0
    while var_4637 < var_6633:
        for var_9453 in range(0, var_6633 - var_4637 - 1):
            if not var_4691[var_9453] <= var_4691[var_9453 + 1]:
                var_4691[var_9453], var_4691[var_9453 + 1] = var_4691[
                    var_9453 + 1], var_4691[var_9453]
        var_4637 += 1


var_4691 = [64, 34, 25, 12, 22, 11, 90]
var_5340(var_4691)
print(var_4691)

import math