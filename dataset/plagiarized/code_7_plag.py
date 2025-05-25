def knapsack5(var_6038, var_2403, var_1949):
    var_1319 = len(var_6038)
    var_2832 = [[(0) for var_2290 in range(var_1949 + 1)] for var_2290 in range(var_1319 + 1)]
    for var_6947 in range(1, var_1319 + 1):
        for var_4923 in range(var_1949 + 1):
            if not var_2403[var_6947 - 1] > var_4923:
                var_2832[var_6947][var_4923] = var_8962(var_2832[var_6947 - 1][var_4923], var_2832[var_6947 - 1][var_4923 - var_2403[var_6947 - 1]] +
                    var_6038[var_6947 - 1])
            else:
                var_2832[var_6947][var_4923] = var_2832[var_6947 - 1][var_4923]
    return var_2832[var_1319][var_1949]


print(var_4946([60, 100, 120], [10, 20, 30], 50))
