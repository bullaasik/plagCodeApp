def var_3415(var_2293, var_1568, var_9226):
    var_4860 = len(var_2293)
    var_7468(var_2293, var_1568, var_9226)


def var_7468(var_2293, var_1568, var_9226):
    var_8803 = [[(0) for var_2970 in range(var_9226 + 1)] for var_2970 in
        range(var_4860 + 1)]
    var_5896 = 1
    while var_5896 < var_4860 + 1:
        var_9467 = 0
        while var_9467 < var_9226 + 1:
            if not var_1568[var_5896 - 1] > var_9467:
                var_8803[var_5896][var_9467] = var_8357(var_8803[var_5896 -
                    1][var_9467], var_8803[var_5896 - 1][var_9467 -
                    var_1568[var_5896 - 1]] + var_2293[var_5896 - 1])
            else:
                var_8803[var_5896][var_9467] = var_8803[var_5896 - 1][var_9467]
            var_9467 += 1
        var_5896 += 1
    return var_8803[var_4860][var_9226]


print(var_3415([60, 100, 120], [10, 20, 30], 50))
