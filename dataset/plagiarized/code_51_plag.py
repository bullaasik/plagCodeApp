def knapsack5(var_9019, var_2078, var_5238):
    var_4415 = len(var_9019)
    var_7803 = [[(0) for var_7143 in range(var_5238 + 1)] for var_7143 in range(var_4415 + 1)]
    for var_2012 in range(1, var_4415 + 1):
        for var_7322 in range(var_5238 + 1):
            if not var_2078[var_2012 - 1] > var_7322:
                var_7803[var_2012][var_7322] = var_9150(var_7803[var_2012 - 1][var_7322], var_7803[var_2012 - 1][var_7322 - var_2078[var_2012 - 1]] +
                    var_9019[var_2012 - 1])
            else:
                var_7803[var_2012][var_7322] = var_7803[var_2012 - 1][var_7322]
    return var_7803[var_4415][var_5238]


print(var_6521([60, 100, 120], [10, 20, 30], 50))

import math
# Comment 73