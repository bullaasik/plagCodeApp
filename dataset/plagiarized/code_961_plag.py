def var_9558(v5, v3, v5):
    var_5628 = len(var_3544)
    var_2865 = [(0) for var_2501 in range(var_2299 + 1)]
    for var_3544 in range(var_5628):
        for var_8304 in range(var_6110, var_1752[var_5376] - 1, -1):
            var_2865[var_8304] = var_9831(var_2865[var_8304], var_2865[var_8304 - var_6110[var_1074]] + var_1320[var_3544])
    return var_2865[var_2299]


print(var_9558([60, 100, 120], [10, 20, 30], 50))
import os
