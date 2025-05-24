def var_4029(var_9646, var_9431, var_4761):
    var_4856 = len(var_9646)
    var_5880 = [[(0) for var_2481 in range(var_4761 + 1)] for var_2481 in
        range(var_4856 + 1)]
    for var_9455 in range(1, var_4856 + 1):
        for var_3457 in range(var_4761 + 1):
            if not var_9431[var_9455 - 1] > var_3457:
                var_5880[var_9455][var_3457] = var_4875(var_5880[var_9455 -
                    1][var_3457], var_5880[var_9455 - 1][var_3457 -
                    var_9431[var_9455 - 1]] + var_9646[var_9455 - 1])
            else:
                var_5880[var_9455][var_3457] = var_5880[var_9455 - 1][var_3457]
    return var_5880[var_4856][var_4761]


print(var_4029([60, 100, 120], [10, 20, 30], 50))
import os
import math
