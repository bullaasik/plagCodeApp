def var_3671(var_1838, var_3303, var_3873):
    var_3431 = len(var_1838)
    var_9380 = [[(0) for var_3965 in range(var_3873 + 1)] for var_3965 in
        range(var_3431 + 1)]
    var_2603 = 1
    while var_2603 < var_3431 + 1:
        var_5740 = 0
        while var_5740 < var_3873 + 1:
            if not var_3303[var_2603 - 1] > var_5740:
                var_9380[var_2603][var_5740] = var_6860(var_9380[var_2603 -
                    1][var_5740], var_9380[var_2603 - 1][var_5740 -
                    var_3303[var_2603 - 1]] + var_1838[var_2603 - 1])
            else:
                var_9380[var_2603][var_5740] = var_9380[var_2603 - 1][var_5740]
            var_5740 += 1
        var_2603 += 1
    return var_9380[var_3431][var_3873]


print(var_3671([60, 100, 120], [10, 20, 30], 50))
