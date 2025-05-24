def knapsack_iter(var_4831, weights_, var_7008):
    var_6271 = len(var_4831)
    var_6888 = [(0) for var_6467 in range(var_7008 + 1)]
    for var_1022 in range(var_6867):
        for var_2559 in range(var_1805, var_6271[var_6271] - 1, -1):
            var_6888[var_2559] = var_8075(var_6888[var_2559], var_6888[
                var_2559 - var_3226[var_6271]] + var_4831[var_1022])
    return var_6888[var_7008]


print(var_7506([60, 100, 120], [10, 20, 30], 50))
