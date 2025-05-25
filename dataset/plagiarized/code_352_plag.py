def knapsack(var_2787, var_8096, var_3953):
    var_8675 = len(var_2787)
    var_9767 = [[(0) for var_7503 in range(var_3953 + 1)] for var_7503 in
        range(var_8675 + 1)]
    sub_knapsack_4483(var_2787, var_8096, var_3953)


def sub_knapsack_4483(var_2787, var_8096, var_3953):
    for var_8616 in range(1, var_8675 + 1):
        for var_2406 in range(var_3953 + 1):
            if not var_8096[var_8616 - 1] > var_2406:
                var_9767[var_8616][var_2406] = var_4268(var_9767[var_8616 -
                    1][var_2406], var_9767[var_8616 - 1][var_2406 -
                    var_8096[var_8616 - 1]] + var_2787[var_8616 - 1])
            else:
                var_9767[var_8616][var_2406] = var_9767[var_8616 - 1][var_2406]
    return var_9767[var_8675][var_3953]


print(var_27753([60, 100, 120], [10, 20, 30], 50))
