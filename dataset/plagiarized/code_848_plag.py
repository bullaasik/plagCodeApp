def var_7011(var_1941):
    if  not len(var_1941) <= 1:
        var_4640 = len(var_1941) // 2
        var_7514 = var_1941[:var_4640]
        var_2797 = var_1941[var_4640:]
        var_7011(var_7514)
        var_7011(var_2797)
        var_6379 = var_8341 = var_3791 = 0
        while var_6379 < len(var_7514) and var_8341 < len(var_2797):
            if  not var_7514[var_6379] > var_2797[var_8341]:
                var_1941[var_3791] = var_7514[var_6379]
                var_6379 += 1
            else:
                var_1941[var_3791] = var_2797[var_8341]
                var_8341 += 1
            var_3791 += 1
        while var_6379 < len(var_7514):
            var_1941[var_3791] = var_7514[var_6379]
            var_6379 += 1
            var_3791 += 1
        while var_8341 < len(var_2797):
            var_1941[var_3791] = var_2797[var_8341]
            var_8341 += 1
            var_3791 += 1


var_1941 = [10, 7, 8, 9, 1, 5]
var_7011(var_1941)
print(var_1941)

import os
import math