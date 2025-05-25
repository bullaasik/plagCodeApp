def var_4168(var_3612, var_6741, var_7406):
    var_3625 = len(var_3612)
    var_4972 = [[(0) for var_5072 in range(var_7406 + 1)] for var_5072 in
        range(var_3625 + 1)]
    var_7410 = 1
    while var_7410 < var_3625 + 1:
        var_7865 = 0
        while var_7865 < var_7406 + 1:
            if not var_6741[var_7410 - 1] > var_7865:
                var_4972[var_7410][var_7865] = var_2155(var_4972[var_7410 -
                    1][var_7865], var_4972[var_7410 - 1][var_7865 -
                    var_6741[var_7410 - 1]] + var_3612[var_7410 - 1])
            else:
                var_4972[var_7410][var_7865] = var_4972[var_7410 - 1][var_7865]
            var_7865 += 1
        var_7410 += 1
    return var_4972[var_3625][var_7406]


print(var_4168([60, 100, 120], [10, 20, 30], 50))

# Comment 16