def var_2842(var_5548, var_8343, var_1276):
    var_9143 = len(var_5548)
    var_2827 = [[(0) for var_1012 in range(var_1276 + 1)] for var_1012 in
        range(var_9143 + 1)]
    for var_6081 in range(1, var_9143 + 1):
        for var_9920 in range(var_1276 + 1):
            if not var_8343[var_6081 - 1] > var_9920:
                var_2827[var_6081][var_9920] = var_2763(var_2827[var_6081 -
                    1][var_9920], var_2827[var_6081 - 1][var_9920 -
                    var_8343[var_6081 - 1]] + var_5548[var_6081 - 1])
            else:
                var_2827[var_6081][var_9920] = var_2827[var_6081 - 1][var_9920]
    return var_2827[var_9143][var_1276]


print(var_2842([60, 100, 120], [10, 20, 30], 50))
