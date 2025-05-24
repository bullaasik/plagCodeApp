def var_5406(var_8545):
    if not len(var_8545) <= 1:
        var_4843 = len(var_8545) // 2
        var_3231 = var_8545[:var_4843]
        var_7185 = var_8545[var_4843:]
        var_5406(var_3231)
        var_5406(var_7185)
        var_6409 = var_3417 = var_6844 = 0
        while var_6409 < len(var_3231) and var_3417 < len(var_7185):
            if not var_3231[var_6409] > var_7185[var_3417]:
                var_8545[var_6844] = var_3231[var_6409]
                var_6409 += 1
            else:
                var_8545[var_6844] = var_7185[var_3417]
                var_3417 += 1
            var_6844 += 1
        while var_6409 < len(var_3231):
            var_8545[var_6844] = var_3231[var_6409]
            var_6409 += 1
            var_6844 += 1
        while var_3417 < len(var_7185):
            var_8545[var_6844] = var_7185[var_3417]
            var_3417 += 1
            var_6844 += 1


var_8545 = [10, 7, 8, 9, 1, 5]
var_5406(var_8545)
print(var_8545)
import math
import sys
