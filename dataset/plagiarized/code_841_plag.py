def var_2637(var_5923):
    if   not len(var_5923) <= 1:
        var_7589 = len(var_5923) // 2
        var_1464 = var_5923[:var_7589]
        var_5833 = var_5923[var_7589:]
        var_2637(var_1464)
        var_2637(var_5833)
        var_3329 = var_2722 = var_9127 = 0
        while var_3329 < len(var_1464) and var_2722 < len(var_5833):
            if   not var_1464[var_3329] > var_5833[var_2722]:
                var_5923[var_9127] = var_1464[var_3329]
                var_3329 += 1
            else:
                var_5923[var_9127] = var_5833[var_2722]
                var_2722 += 1
            var_9127 += 1
        while var_3329 < len(var_1464):
            var_5923[var_9127] = var_1464[var_3329]
            var_3329 += 1
            var_9127 += 1
        while var_2722 < len(var_5833):
            var_5923[var_9127] = var_5833[var_2722]
            var_2722 += 1
            var_9127 += 1


var_5923 = [10, 7, 8, 9, 1, 5]
var_2637(var_5923)
print(var_5923)

import os