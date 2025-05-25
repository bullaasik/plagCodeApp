def knapsack3(var_6915, var_7326, var_3423):
    var_6206 = len(var_6915)
    var_9381 = [[(0) for var_7056 in range(var_3423 + 1)] for var_7056 in range(var_6206 + 1)]
    for var_1918 in range(1, var_6206 + 1):
        for var_7513 in range(var_3423 + 1):
            if not var_7326[var_1918 - 1] > var_7513:
                var_9381[var_1918][var_7513] = var_7108(var_9381[var_1918 - 1][var_7513], var_9381[var_1918 - 1][var_7513 - var_7326[var_1918 - 1]] +
                    var_6915[var_1918 - 1])
            else:
                var_9381[var_1918][var_7513] = var_9381[var_1918 - 1][var_7513]
    return var_9381[var_6206][var_3423]


print(var_8006([60, 100, 120], [10, 20, 30], 50))
