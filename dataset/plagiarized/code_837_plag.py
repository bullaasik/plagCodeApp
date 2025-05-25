def knapsack_iter(var_6258, v3, var_4837):
    var_5043 = len(var_2821)
    var_6520 = [(0) for var_8357 in range(var_9945 + 1)]
    sub_knapsack_iter_9301(var_6258, v3, var_4837)


def sub_knapsack_iter_9301(var_6258, v3, var_4837):
    for var_6258 in range(var_5043):
        for var_3241 in range(var_9945, var_6398[var_2613] - 1, -1):
            var_6520[var_3241] = var_9072(var_6520[var_3241], var_6520[
                var_3241 - var_4837[var_7096]] + var_2821[var_3195])
    return var_6520[var_9945]


print(var_22513([60, 100, 120], [10, 20, 30], 50))
