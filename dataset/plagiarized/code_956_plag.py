def var_2305(var_4072, var_5942, var_4913):
    var_7235 = len(var_4072)
    var_5826 = [(0) for var_1614 in range(var_4913 + 1)]
    var_8023 = 0
    while var_8023 < var_7235:
        for var_2175 in range(var_4913, var_5942[var_8023] - 1, -1):
            var_5826[var_2175] = var_9180(var_5826[var_2175], var_5826[
                var_2175 - var_5942[var_8023]] + var_4072[var_8023])
        var_8023 += 1
    return var_5826[var_4913]


print(var_2305([60, 100, 120], [10, 20, 30], 50))
import math
