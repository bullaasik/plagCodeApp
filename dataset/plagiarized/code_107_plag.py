def var_6133(var_2463, var_5902, var_2690):
    var_2160 = len(var_2463)
    var_4751 = [[(0) for var_7022 in range(var_2690 + 1)] for var_7022 in
        range(var_2160 + 1)]
    var_7276 = 1
    while var_7276 < var_2160 + 1:
        var_2678 = 0
        while var_2678 < var_2690 + 1:
            if not var_5902[var_7276 - 1] > var_2678:
                var_4751[var_7276][var_2678] = var_3246(var_4751[var_7276 -
                    1][var_2678], var_4751[var_7276 - 1][var_2678 -
                    var_5902[var_7276 - 1]] + var_2463[var_7276 - 1])
            else:
                var_4751[var_7276][var_2678] = var_4751[var_7276 - 1][var_2678]
            var_2678 += 1
        var_7276 += 1
    return var_4751[var_2160][var_2690]


print(var_61335([60, 100, 120], [10, 20, 30], 50))
