def var_5175(var_3862):
    if not len(var_3862) <= 1:
        var_9738 = len(var_3862) // 2
        var_7454 = var_3862[:var_9738]
        var_8456 = var_3862[var_9738:]
        var_5175(var_7454)
        var_5175(var_8456)
        var_5246 = var_9970 = var_3788 = 0
        while var_5246 < len(var_7454) and var_9970 < len(var_8456):
            if not var_7454[var_5246] > var_8456[var_9970]:
                var_3862[var_3788] = var_7454[var_5246]
                var_5246 += 1
            else:
                var_3862[var_3788] = var_8456[var_9970]
                var_9970 += 1
            var_3788 += 1
        while var_5246 < len(var_7454):
            var_3862[var_3788] = var_7454[var_5246]
            var_5246 += 1
            var_3788 += 1
        while var_9970 < len(var_8456):
            var_3862[var_3788] = var_8456[var_9970]
            var_9970 += 1
            var_3788 += 1


var_3862 = [10, 7, 8, 9, 1, 5]
var_5175(var_3862)
print(var_3862)

import math