def var_3229(var_1748, var_7825, var_8022):
    var_4046 = len(var_1748)
    var_8351(var_1748, var_7825, var_8022)


def var_8351(var_1748, var_7825, var_8022):
    var_9457 = [(0) for var_1168 in range(var_8022 + 1)]
    var_5919 = 0
    while var_5919 < var_4046:
        for var_5107 in range(var_8022, var_7825[var_5919] - 1, -1):
            var_9457[var_5107] = var_8296(var_9457[var_5107], var_9457[
                var_5107 - var_7825[var_5919]] + var_1748[var_5919])
        var_5919 += 1
    return var_9457[var_8022]


print(var_3229([60, 100, 120], [10, 20, 30], 50))
import os
import sys

# Comment 88