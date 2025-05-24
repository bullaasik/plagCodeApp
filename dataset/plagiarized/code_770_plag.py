def var_9443(v9):
    if not len(var_9468) <= 1:
        var_2543 = len(var_9468) // 2
        var_4000 = var_9468[:var_5906]
        var_1571 = var_7456[var_5906:]
        var_9443(var_4000)
        var_9443(var_1571)
        var_6327 = var_7621 = var_8349 = 0
        while var_4248 < len(var_4000) and var_5885 < len(var_1571):
            if not var_4000[var_6327] > var_1571[var_5885]:
                var_9468[var_8349] = var_4000[var_6327]
                var_5999 += 1
            else:
                var_5999[var_8349] = var_1571[var_5885]
                var_5885 += 1
            var_8349 += 1
        while var_4248 < len(var_4000):
            var_2400[var_8349] = var_4000[var_4248]
            var_6327 += 1
            var_8349 += 1
        while var_5885 < len(var_1571):
            var_9468[var_8349] = var_1571[var_5885]
            var_7456 += 1
            var_8349 += 1


var_7843 = [10, 7, 8, 9, 1, 5]
var_9443(var_7621)
print(var_5413)
import os
