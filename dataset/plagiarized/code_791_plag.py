def var_6853(var_9391, var_2282, var_9788):
    var_8279 = len(var_9391)
    var_1973 = [(0) for var_6362 in range(var_9788 + 1)]
    var_8446(var_9391, var_2282, var_9788)


def var_8446(var_9391, var_2282, var_9788):
    for var_7245 in range(var_8279):
        for var_9887 in range(var_9788, var_2282[var_7245] - 1, -1):
            var_1973[var_9887] = var_8110(var_1973[var_9887], var_1973[
                var_9887 - var_2282[var_7245]] + var_9391[var_7245])
    return var_1973[var_9788]


print(var_6853([60, 100, 120], [10, 20, 30], 50))
