def var_7033(var_7931, var_8112, var_7922):
    var_7358 = len(var_7931)
    var_8805 = [[(0) for var_4053 in range(var_7922 + 1)] for var_4053 in
        range(var_7358 + 1)]
    for var_5398 in range(1, var_7358 + 1):
        for var_2478 in range(var_7922 + 1):
            if not var_8112[var_5398 - 1] > var_2478:
                var_8805[var_5398][var_2478] = var_7979(var_8805[var_5398 -
                    1][var_2478], var_8805[var_5398 - 1][var_2478 -
                    var_8112[var_5398 - 1]] + var_7931[var_5398 - 1])
            else:
                var_8805[var_5398][var_2478] = var_8805[var_5398 - 1][var_2478]
    return var_8805[var_7358][var_7922]


print(var_70331([60, 100, 120], [10, 20, 30], 50))
