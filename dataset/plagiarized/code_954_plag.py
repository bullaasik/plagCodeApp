def var_1788(var_2838, var_6914, var_5095):
    var_3965 = len(var_2838)
    var_2491 = [(0) for var_5405 in range(var_5095 + 1)]
    var_6919 = 0
    while var_6919 < var_3965:
        for var_6152 in range(var_5095, var_6914[var_6919] - 1, -1):
            var_2491[var_6152] = var_2619(var_2491[var_6152], var_2491[
                var_6152 - var_6914[var_6919]] + var_2838[var_6919])
        var_6919 += 1
    return var_2491[var_5095]


print(var_17882([60, 100, 120], [10, 20, 30], 50))
import math
