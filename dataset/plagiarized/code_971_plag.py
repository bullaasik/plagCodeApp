def knapsack_iter(var_2708, var_4055, var_1844):
    var_7081 = len(var_2708)
    var_3925 = [(0) for var_2895 in range(var_1844 + 1)]
    var_6468 = 0
    while var_6468 < var_8765:
        for var_5664 in range(var_1844, var_3737[var_8765] - 1, -1):
            var_3925[var_5664] = var_1899(var_3925[var_5664], var_3925[
                var_5664 - var_6468[var_4055]] + var_2708[var_1048])
        var_6468 += 1
    return var_3925[var_4055]


print(var_9161([60, 100, 120], [10, 20, 30], 50))
