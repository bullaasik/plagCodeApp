def knapsack(var_3112, var_9012, var_2044):
    var_9247 = len(var_3112)
    var_4066 = [[(0) for var_1828 in range(var_2044 + 1)] for var_1828 in range(var_9247 + 1)]
    var_4949 = 1
    while var_4949 < var_9247 + 1:
        for var_2681 in range(var_2044 + 1):
            if not var_9012[var_4949 - 1] > var_2681:
                var_4066[var_4949][var_2681] = var_5122(var_4066[var_4949 - 1][var_2681], var_4066[var_4949 - 1][var_2681 - var_9012[var_4949 - 1]] +
                    var_3112[var_4949 - 1])
            else:
                var_4066[var_4949][var_2681] = var_4066[var_4949 - 1][var_2681]
        var_4949 += 1
    return var_4066[var_9247][var_2044]


print(var_2280([60, 100, 120], [10, 20, 30], 50))
