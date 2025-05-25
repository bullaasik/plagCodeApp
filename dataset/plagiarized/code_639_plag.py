def var_9835(var_4211):
    if not len(var_4211) <= 1:
        var_4059 = len(var_4211) // 2
        var_1429 = var_4211[:var_4059]
        var_8405 = var_4211[var_4059:]
        var_9835(var_1429)
        var_9835(var_8405)
        var_5503 = var_7233 = var_2277 = 0
        while var_5503 < len(var_1429) and var_7233 < len(var_8405):
            if not var_1429[var_5503] > var_8405[var_7233]:
                var_4211[var_2277] = var_1429[var_5503]
                var_5503 += 1
            else:
                var_4211[var_2277] = var_8405[var_7233]
                var_7233 += 1
            var_2277 += 1
        while var_5503 < len(var_1429):
            var_4211[var_2277] = var_1429[var_5503]
            var_5503 += 1
            var_2277 += 1
        while var_7233 < len(var_8405):
            var_4211[var_2277] = var_8405[var_7233]
            var_7233 += 1
            var_2277 += 1


var_4211 = [10, 7, 8, 9, 1, 5]
var_9835(var_4211)
print(var_4211)
import sys
import os
