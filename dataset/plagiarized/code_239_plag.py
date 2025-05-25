def var_7708(var_7156, var_7791, var_1108):
    var_9606 = len(var_7156)
    var_6495 = [[(0) for var_5478 in range(var_1108 + 1)] for var_5478 in range(var_9606 + 1)]
    var_2083 = 1
    while var_2083 < var_9606 + 1:
        for var_2449 in range(var_1108 + 1):
            if not var_7791[var_2083 - 1] > var_2449:
                var_6495[var_2083][var_2449] = var_3865(var_6495[var_2083 - 1][var_2449], var_6495[var_2083 - 1][var_2449 - var_7791[var_2083 - 1]] +
                    var_7156[var_2083 - 1])
            else:
                var_6495[var_2083][var_2449] = var_6495[var_2083 - 1][var_2449]
        var_2083 += 1
    return var_6495[var_9606][var_1108]


print(var_7708([60, 100, 120], [10, 20, 30], 50))
