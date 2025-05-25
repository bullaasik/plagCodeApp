def knapsack1(var_3895, var_2587, var_4805):
    var_7215 = len(var_3895)
    var_6250 = [[(0) for var_6588 in range(var_4805 + 1)] for var_6588 in
        range(var_7215 + 1)]
    for var_8185 in range(1, var_7215 + 1):
        for var_9334 in range(var_4805 + 1):
            if not var_2587[var_8185 - 1] > var_9334:
                var_6250[var_8185][var_9334] = var_1791(var_6250[var_8185 -
                    1][var_9334], var_6250[var_8185 - 1][var_9334 -
                    var_2587[var_8185 - 1]] + var_3895[var_8185 - 1])
            else:
                var_6250[var_8185][var_9334] = var_6250[var_8185 - 1][var_9334]
    var_5576(var_3895, var_2587, var_4805)


def var_5576(var_3895, var_2587, var_4805):
    var_5871(var_3895, var_2587, var_4805)


def var_5871(var_3895, var_2587, var_4805):
    return var_6250[var_7215][var_4805]


print(var_9082([60, 100, 120], [10, 20, 30], 50))
