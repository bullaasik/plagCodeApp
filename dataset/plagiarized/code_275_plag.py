def knapsack3(var_8793, var_3142, var_4155):
    var_7141 = len(var_8793)
    var_3628 = [[(0) for var_6796 in range(var_4155 + 1)] for var_6796 in range(var_7141 + 1)]
    var_5027 = 1
    while var_5027 < var_7141 + 1:
        var_5530 = 0
        while var_5530 < var_4155 + 1:
            if not var_3142[var_5027 - 1] > var_5530:
                var_3628[var_5027][var_5530] = var_2931(var_3628[var_5027 - 1][var_5530], var_3628[var_5027 - 1][var_5530 - var_3142[var_5027 - 1]] +
                    var_8793[var_5027 - 1])
            else:
                var_3628[var_5027][var_5530] = var_3628[var_5027 - 1][var_5530]
            var_5530 += 1
        var_5027 += 1
    return var_3628[var_7141][var_4155]


print(var_6414([60, 100, 120], [10, 20, 30], 50))
