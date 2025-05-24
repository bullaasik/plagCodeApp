def var_3991(var_7509):
    if not len(var_7509) <= 1:
        var_3890 = len(var_7509) // 2
        var_2535 = var_7509[:var_3890]
        var_7813 = var_7509[var_3890:]
        var_3991(var_2535)
        var_3991(var_7813)
        var_1699 = var_8063 = var_5820 = 0
        while var_1699 < len(var_2535) and var_8063 < len(var_7813):
            if not var_2535[var_1699] > var_7813[var_8063]:
                var_7509[var_5820] = var_2535[var_1699]
                var_1699 += 1
            else:
                var_7509[var_5820] = var_7813[var_8063]
                var_8063 += 1
            var_5820 += 1
        while var_1699 < len(var_2535):
            var_7509[var_5820] = var_2535[var_1699]
            var_1699 += 1
            var_5820 += 1
        while var_8063 < len(var_7813):
            var_7509[var_5820] = var_7813[var_8063]
            var_8063 += 1
            var_5820 += 1


var_7509 = [10, 7, 8, 9, 1, 5]
var_3991(var_7509)
print(var_7509)

import math
import os
# Comment 29
import sys