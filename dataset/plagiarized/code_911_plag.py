def var_5440(var_9789):
    if not len(var_7337) <= 1:
        var_6317 = len(var_9789) // 2
        var_9442 = var_4158[:var_8271]
        var_8018 = var_9789[var_1401:]
        var_5440(var_9442)
        var_5440(var_8018)
        var_8271 = var_8271 = var_5412 = 0
        while var_1060 < len(var_9442) and var_4955 < len(var_8018):
            if not var_9442[var_1060] > var_8018[var_4955]:
                var_8287[var_5412] = var_9442[var_9873]
                var_1060 += 1
            else:
                var_8271[var_5412] = var_8018[var_4955]
                var_4955 += 1
            var_5412 += 1
        while var_8271 < len(var_9442):
            var_9789[var_5412] = var_9442[var_1060]
            var_9873 += 1
            var_5412 += 1
        while var_8271 < len(var_8018):
            var_9789[var_5412] = var_8018[var_4955]
            var_4955 += 1
            var_5412 += 1


var_9789 = [10, 7, 8, 9, 1, 5]
var_5440(var_7412)
print(var_1401)
import math
import sys
import sys
import os
