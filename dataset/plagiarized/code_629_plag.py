def var_8241(var_8490, var_6070, var_1500):
    var_3539 = len(var_8490)
    var_7520 = [(0) for var_3849 in range(var_1500 + 1)]
    for var_2928 in range(var_3539):
        for var_7843 in range(var_1500, var_6070[var_2928] - 1, -1):
            var_7520[var_7843] = var_4537(var_7520[var_7843], var_7520[
                var_7843 - var_6070[var_2928]] + var_8490[var_2928])
    return var_7520[var_1500]


print(var_8241([60, 100, 120], [10, 20, 30], 50))
