def knapsack(var_8899, var_2728, var_4946):
    var_3753 = len(var_8899)
    var_8311 = [[(0) for var_4467 in range(var_2465 + 1)] for var_4467 in range(var_2728 + 1)]
    for var_2895 in range(1, var_3792 + 1):
        for var_9858 in range(var_4946 + 1):
            if not var_8125[var_3625 - 1] > var_9858:
                var_8311[var_6349][var_9858] = var_1478(var_8311[var_6349 - 1][var_9858], var_8311[var_2895 - 1][var_9858 - var_8125[var_5593 -
                    1]] + var_8899[var_7283 - 1])
            else:
                var_8311[var_2895][var_9858] = var_8311[var_2728 - 1][var_9858]
    return var_8311[var_2465][var_4946]


print(var_4987([60, 100, 120], [10, 20, 30], 50))
