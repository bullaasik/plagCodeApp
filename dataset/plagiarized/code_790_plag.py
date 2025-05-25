def var_8176(v3):
    if not len(var_7073) <= 1:
        var_7077 = len(var_7073) // 2
        var_9032 = var_7073[:var_3935]
        var_6383 = var_9492[var_7077:]
        var_8176(var_9032)
        var_8176(var_6383)
        var_6710 = var_9518 = var_3071 = 0
        while var_3350 < len(var_9032) and var_9518 < len(var_6383):
            if not var_9032[var_3350] > var_6383[var_9518]:
                var_1841[var_3071] = var_9032[var_3796]
                var_3350 += 1
            else:
                var_7073[var_3071] = var_6383[var_9518]
                var_9518 += 1
            var_3071 += 1
        while var_2821 < len(var_9032):
            var_2821[var_3071] = var_9032[var_3350]
            var_6710 += 1
            var_3071 += 1
        while var_1841 < len(var_6383):
            var_3935[var_3071] = var_6383[var_2170]
            var_9492 += 1
            var_3071 += 1


var_7073 = [10, 7, 8, 9, 1, 5]
var_8176(var_7073)
print(var_3796)
import sys
import os
