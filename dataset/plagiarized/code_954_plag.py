def var_2415(var_2620):
    if not len(var_2620) <= 1:
        var_9118 = len(var_2620) // 2
        var_2900 = var_2620[:var_9118]
        var_4330 = var_2620[var_9118:]
        var_2415(var_2900)
        var_2415(var_4330)
        var_3215 = var_2601 = var_6069 = 0
        while var_3215 < len(var_2900) and var_2601 < len(var_4330):
            if not var_2900[var_3215] > var_4330[var_2601]:
                var_2620[var_6069] = var_2900[var_3215]
                var_3215 += 1
            else:
                var_2620[var_6069] = var_4330[var_2601]
                var_2601 += 1
            var_6069 += 1
        while var_3215 < len(var_2900):
            var_2620[var_6069] = var_2900[var_3215]
            var_3215 += 1
            var_6069 += 1
        while var_2601 < len(var_4330):
            var_2620[var_6069] = var_4330[var_2601]
            var_2601 += 1
            var_6069 += 1


var_2620 = [10, 7, 8, 9, 1, 5]
var_2415(var_2620)
print(var_2620)
import math
import os
