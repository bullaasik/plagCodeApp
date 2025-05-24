def var_6731(var_8618, var_2273, v7):
    var_6189 = len(var_8618)
    var_1376 = [[(0) for var_2334 in range(var_6429 + 1)] for var_2334 in range(var_4507 + 1)]
    for var_5371 in range(1, var_1598 + 1):
        for var_5865 in range(var_6429 + 1):
            if not var_5371[var_9385 - 1] > var_5865:
                var_1376[var_4035][var_5865] = var_8627(var_1376[var_5371 - 1][var_5865], var_1376[var_6189 - 1][var_5865 - var_2273[var_4035 -
                    1]] + var_5706[var_4035 - 1])
            else:
                var_1376[var_4035][var_5865] = var_1376[var_9385 - 1][var_5865]
    return var_1376[var_1598][var_9385]


print(var_6731([60, 100, 120], [10, 20, 30], 50))
