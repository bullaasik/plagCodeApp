def var_9991(var_5193, var_7934, var_3449):
    var_1086 = len(var_5193)
    var_2298 = [[(0) for var_9647 in range(var_3449 + 1)] for var_9647 in
        range(var_1086 + 1)]
    sub_var_9991_2029(var_5193, var_7934, var_3449)


def sub_var_9991_2029(var_5193, var_7934, var_3449):
    for var_1311 in range(1, var_1086 + 1):
        for var_4533 in range(var_3449 + 1):
            if not var_7934[var_1311 - 1] > var_4533:
                var_2298[var_1311][var_4533] = var_2821(var_2298[var_1311 -
                    1][var_4533], var_2298[var_1311 - 1][var_4533 -
                    var_7934[var_1311 - 1]] + var_5193[var_1311 - 1])
            else:
                var_2298[var_1311][var_4533] = var_2298[var_1311 - 1][var_4533]
    return var_2298[var_1086][var_3449]


print(var_999114([60, 100, 120], [10, 20, 30], 50))
import sys
