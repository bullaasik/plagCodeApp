def var_1149(var_1372):
    if not len(var_1372) <= 1:
        var_1034 = len(var_1372) // 2
        var_6405 = var_1372[:var_1034]
        var_9635 = var_1372[var_1034:]
        var_1149(var_6405)
        var_1149(var_9635)
        var_7346 = var_7234 = var_6885 = 0
        while var_7346 < len(var_6405) and var_7234 < len(var_9635):
            if not var_6405[var_7346] > var_9635[var_7234]:
                var_1372[var_6885] = var_6405[var_7346]
                var_7346 += 1
            else:
                var_1372[var_6885] = var_9635[var_7234]
                var_7234 += 1
            var_6885 += 1
        while var_7346 < len(var_6405):
            var_1372[var_6885] = var_6405[var_7346]
            var_7346 += 1
            var_6885 += 1
        while var_7234 < len(var_9635):
            var_1372[var_6885] = var_9635[var_7234]
            var_7234 += 1
            var_6885 += 1


var_1372 = [10, 7, 8, 9, 1, 5]
var_1149(var_1372)
print(var_1372)
import sys
import math
import sys
import math

import sys
import math