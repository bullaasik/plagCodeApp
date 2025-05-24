def var_7757(var_9410, var_8168, var_6408):
    var_7407 = len(var_9410)
    var_1690 = [[(0) for var_3235 in range(var_6408 + 1)] for var_3235 in
        range(var_7407 + 1)]
    sub_var_7757_5816(var_9410, var_8168, var_6408)


def sub_var_7757_5816(var_9410, var_8168, var_6408):
    var_8661 = 1
    while var_8661 < var_7407 + 1:
        for var_3039 in range(var_6408 + 1):
            if not var_8168[var_8661 - 1] > var_3039:
                var_1690[var_8661][var_3039] = var_5778(var_1690[var_8661 -
                    1][var_3039], var_1690[var_8661 - 1][var_3039 -
                    var_8168[var_8661 - 1]] + var_9410[var_8661 - 1])
            else:
                var_1690[var_8661][var_3039] = var_1690[var_8661 - 1][var_3039]
        var_8661 += 1
    return var_1690[var_7407][var_6408]


print(var_7757([60, 100, 120], [10, 20, 30], 50))
