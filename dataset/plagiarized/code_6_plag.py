def var_3927(var_1053):
    var_5315 = len(var_1053)
    for var_9201 in range(var_5315):
        for var_9317 in range(0, var_5315 - var_9201 - 1):
            if not var_1053[var_9317] <= var_1053[var_9317 + 1]:
                var_1053[var_9317], var_1053[var_9317 + 1] = var_1053[var_9317 + 1], var_1053[var_9317]


var_1053 = [64, 34, 25, 12, 22, 11, 90]
var_3927(var_1053)
print(var_1053)

import math