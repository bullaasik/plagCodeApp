def var_1019(var_2925, var_8901, var_3135):
    var_1639 = len(var_2925)
    var_2526(var_2925, var_8901, var_3135)


def var_2526(var_2925, var_8901, var_3135):
    var_9706 = [[(0) for var_8069 in range(var_3135 + 1)] for var_8069 in
        range(var_1639 + 1)]
    var_9246 = 1
    while var_9246 < var_1639 + 1:
        for var_9835 in range(var_3135 + 1):
            if not var_8901[var_9246 - 1] > var_9835:
                var_9706[var_9246][var_9835] = var_9553(var_9706[var_9246 -
                    1][var_9835], var_9706[var_9246 - 1][var_9835 -
                    var_8901[var_9246 - 1]] + var_2925[var_9246 - 1])
            else:
                var_9706[var_9246][var_9835] = var_9706[var_9246 - 1][var_9835]
        var_9246 += 1
    return var_9706[var_1639][var_3135]


print(var_1019([60, 100, 120], [10, 20, 30], 50))
