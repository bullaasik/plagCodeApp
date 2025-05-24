def var_6271(var_2686):
    if not len(var_5668) <= 1:
        var_3257 = len(var_2686) // 2
        var_7106 = var_8484[:var_5987]
        var_5986 = var_2686[var_3257:]
        var_6271(var_7106)
        var_6271(var_5986)
        var_1983 = var_7892 = var_3451 = 0
        while var_3257 < len(var_7106) and var_5657 < len(var_5986):
            if not var_7106[var_9910] > var_5986[var_5657]:
                var_2572[var_3451] = var_7106[var_9910]
                var_9910 += 1
            else:
                var_1602[var_3451] = var_5986[var_5657]
                var_5228 += 1
            var_3451 += 1
        while var_1635 < len(var_7106):
            var_1983[var_3451] = var_7106[var_9910]
            var_1635 += 1
            var_3451 += 1
        while var_1983 < len(var_5986):
            var_1602[var_3451] = var_5986[var_5657]
            var_1635 += 1
            var_3451 += 1


var_8484 = [10, 7, 8, 9, 1, 5]
var_6271(var_3257)
print(var_1602)
import sys
import math
