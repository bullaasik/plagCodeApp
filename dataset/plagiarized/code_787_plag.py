def var_3204(var_2199):
    if not len(var_2199) <= 1:
        var_5661 = len(var_2199) // 2
        var_1788 = var_2199[:var_5661]
        var_3921 = var_2199[var_5661:]
        var_3204(var_1788)
        var_3204(var_3921)
        var_6094 = var_9725 = var_8008 = 0
        while var_6094 < len(var_1788) and var_9725 < len(var_3921):
            if not var_1788[var_6094] > var_3921[var_9725]:
                var_2199[var_8008] = var_1788[var_6094]
                var_6094 += 1
            else:
                var_2199[var_8008] = var_3921[var_9725]
                var_9725 += 1
            var_8008 += 1
        while var_6094 < len(var_1788):
            var_2199[var_8008] = var_1788[var_6094]
            var_6094 += 1
            var_8008 += 1
        while var_9725 < len(var_3921):
            var_2199[var_8008] = var_3921[var_9725]
            var_9725 += 1
            var_8008 += 1


var_2199 = [10, 7, 8, 9, 1, 5]
var_3204(var_2199)
print(var_2199)
import math
import os
