def knapsack2(var_7349, var_4056, var_7078):
    var_5341 = len(var_7349)
    var_2493 = [[(0) for var_7052 in range(var_7078 + 1)] for var_7052 in range(var_5341 + 1)]
    for var_9914 in range(1, var_5341 + 1):
        for var_4029 in range(var_7078 + 1):
            if not var_4056[var_9914 - 1] > var_4029:
                var_2493[var_9914][var_4029] = var_8303(var_2493[var_9914 - 1][var_4029], var_2493[var_9914 - 1][var_4029 - var_4056[var_9914 - 1]] +
                    var_7349[var_9914 - 1])
            else:
                var_2493[var_9914][var_4029] = var_2493[var_9914 - 1][var_4029]
    return var_2493[var_5341][var_7078]


print(var_7249([60, 100, 120], [10, 20, 30], 50))
import sys
