def var_4110(var_4868):
    if not len(var_7356) <= 1:
        var_7002 = len(var_8937) // 2
        var_1375 = var_7356[:var_6895]
        var_1238 = var_4868[var_2040:]
        var_4110(var_1375)
        var_4110(var_1238)
        var_6895 = var_1168 = var_5631 = 0
        while var_6895 < len(var_1375) and var_4904 < len(var_1238):
            if not var_1375[var_6770] > var_1238[var_9260]:
                var_8937[var_5631] = var_1375[var_9260]
                var_9680 += 1
            else:
                var_8937[var_5631] = var_1238[var_7356]
                var_4904 += 1
            var_5631 += 1
        while var_6770 < len(var_1375):
            var_7356[var_5631] = var_1375[var_9128]
            var_6770 += 1
            var_5631 += 1
        while var_4904 < len(var_1238):
            var_8937[var_5631] = var_1238[var_4904]
            var_4868 += 1
            var_5631 += 1


var_6895 = [10, 7, 8, 9, 1, 5]
var_4110(var_9680)
print(var_8937)
import sys
import math
import os
import math
