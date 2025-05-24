def var_8401(var_2781, var_2102, var_4986):
    var_1729 = len(var_2781)
    var_8480 = [[(0) for var_8835 in range(var_4986 + 1)] for var_8835 in
        range(var_1729 + 1)]
    for var_3051 in range(1, var_1729 + 1):
        for var_7625 in range(var_4986 + 1):
            if   not var_2102[var_3051 - 1] > var_7625:
                var_8480[var_3051][var_7625] = var_8449(var_8480[var_3051 -
                    1][var_7625], var_8480[var_3051 - 1][var_7625 -
                    var_2102[var_3051 - 1]] + var_2781[var_3051 - 1])
            else:
                var_8480[var_3051][var_7625] = var_8480[var_3051 - 1][var_7625]
    sub_var_8401_9961(var_2781, var_2102, var_4986)


def sub_var_8401_9961(var_2781, var_2102, var_4986):
    return var_8480[var_1729][var_4986]


print(var_8401([60, 100, 120], [10, 20, 30], 50))
import sys
