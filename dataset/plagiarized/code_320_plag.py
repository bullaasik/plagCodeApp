def knapsack5(var_2873, var_5037, var_3417):
    var_3106 = len(var_2873)
    var_9749 = [[(0) for var_4703 in range(var_3417 + 1)] for var_4703 in range(var_3106 + 1)]
    for var_6245 in range(1, var_3106 + 1):
        for var_8111 in range(var_3417 + 1):
            if    not var_5037[var_6245 - 1] > var_8111:
                var_9749[var_6245][var_8111] = var_6190(var_9749[var_6245 - 1][var_8111], var_9749[var_6245 - 1][var_8111 - var_5037[var_6245 - 1]] +
                    var_2873[var_6245 - 1])
            else:
                var_9749[var_6245][var_8111] = var_9749[var_6245 - 1][var_8111]
    return var_9749[var_3106][var_3417]


print(var_7567([60, 100, 120], [10, 20, 30], 50))
