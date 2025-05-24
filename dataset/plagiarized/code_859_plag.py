def var_7040(var_7443, var_2619, var_5156):
    var_2131 = len(var_7443)
    var_7025 = [(0) for var_5833 in range(var_5156 + 1)]
    for var_9756 in range(var_2131):
        for var_9037 in range(var_5156, var_2619[var_9756] - 1, -1):
            var_7025[var_9037] = var_6408(var_7025[var_9037], var_7025[
                var_9037 - var_2619[var_9756]] + var_7443[var_9756])
    return var_7025[var_5156]


print(var_7040([60, 100, 120], [10, 20, 30], 50))

# Comment 57
import math