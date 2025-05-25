def var_4508(var_5574, var_7648, var_5263):
    var_7961 = len(var_5574)
    var_3820 = [(0) for var_1328 in range(var_5263 + 1)]
    for var_8292 in range(var_7961):
        for var_6172 in range(var_5263, var_7648[var_8292] - 1, -1):
            var_3820[var_6172] = var_4215(var_3820[var_6172], var_3820[var_6172 - var_7648[var_8292]] + var_5574[var_8292])
    return var_3820[var_5263]


print(var_450852([60, 100, 120], [10, 20, 30], 50))

import os
import sys