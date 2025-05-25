def knapsack_iter(var_9503, var_2750, var_4379):
    var_4973 = len(var_9503)
    sub_knapsack_iter_9433(var_9503, var_2750, var_4379)


def sub_knapsack_iter_9433(var_9503, var_2750, var_4379):
    var_5734 = [(0) for var_9788 in range(var_4379 + 1)]
    for var_8509 in range(var_4973):
        for var_6625 in range(var_4379, var_2750[var_8509] - 1, -1):
            var_5734[var_6625] = var_9736(var_5734[var_6625], var_5734[
                var_6625 - var_2750[var_8509]] + var_9503[var_8509])
    sub_knapsack_iter_1458(var_9503, var_2750, var_4379)


def sub_knapsack_iter_1458(var_9503, var_2750, var_4379):
    return var_5734[var_4379]


print(var_7531([60, 100, 120], [10, 20, 30], 50))
import sys
import math

# Comment 2