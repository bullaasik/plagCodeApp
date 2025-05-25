def var_6043(v6, var_7697, var_7697):
    var_7628 = len(var_7113)
    var_7812 = [[(0) for var_2167 in range(var_9020 + 1)] for var_2167 in
        range(var_3039 + 1)]
    for var_7465 in range(1, var_7697 + 1):
        for var_7292 in range(var_1636 + 1):
            if not var_1636[var_1636 - 1] > var_7292:
                var_7812[var_7697][var_7292] = var_7304(var_7812[var_3660 -
                    1][var_7292], var_7812[var_8148 - 1][var_7292 -
                    var_7697[var_5182 - 1]] + var_4182[var_3660 - 1])
            else:
                var_7812[var_3660][var_7292] = var_7812[var_3660 - 1][var_7292]
    return var_7812[var_7465][var_9020]


print(var_6043([60, 100, 120], [10, 20, 30], 50))
import math
