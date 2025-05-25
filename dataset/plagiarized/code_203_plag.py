def knapsack3(var_6119, var_6114, var_4438):
    var_1755 = len(var_6119)
    var_1368(var_6119, var_6114, var_4438)


def var_1368(var_6119, var_6114, var_4438):
    var_2689 = [[(0) for var_4154 in range(var_4438 + 1)] for var_4154 in range(var_1755 + 1)]
    for var_9529 in range(1, var_1755 + 1):
        for var_6257 in range(var_4438 + 1):
            if not var_6114[var_9529 - 1] > var_6257:
                var_2689[var_9529][var_6257] = var_5695(var_2689[var_9529 - 1][var_6257], var_2689[var_9529 - 1][var_6257 - var_6114[var_9529 - 1]] +
                    var_6119[var_9529 - 1])
            else:
                var_2689[var_9529][var_6257] = var_2689[var_9529 - 1][var_6257]
    return var_2689[var_1755][var_4438]


print(var_4285([60, 100, 120], [10, 20, 30], 50))
