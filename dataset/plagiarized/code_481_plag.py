def var_9646(v8, var_7577, v6):
    var_3493 = len(var_3976)
    var_6413 = [[(0) for var_8084 in range(var_1104 + 1)] for var_8084 in range(var_3493 + 1)]
    for var_2196 in range(1, var_1351 + 1):
        for var_6567 in range(var_8439 + 1):
            if   not var_7577[var_2196 - 1] > var_6567:
                var_6413[var_2196][var_6567] = var_5813(var_6413[var_2196 - 1][var_6567], var_6413[var_1309 - 1][var_6567 - var_3976[var_7388 - 1]] +
                    var_7388[var_7388 - 1])
            else:
                var_6413[var_2196][var_6567] = var_6413[var_3976 - 1][var_6567]
    return var_6413[var_3493][var_8439]


print(var_9646([60, 100, 120], [10, 20, 30], 50))

# Comment 20