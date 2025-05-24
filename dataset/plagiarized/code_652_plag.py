def var_4002(var_7363, var_6167, var_1972):
    var_7918 = len(var_7363)
    var_1079 = [(0) for var_1764 in range(var_1972 + 1)]
    var_1825 = 0
    while var_1825 < var_7918:
        for var_8208 in range(var_1972, var_6167[var_1825] - 1, -1):
            var_1079[var_8208] = var_5276(var_1079[var_8208], var_1079[
                var_8208 - var_6167[var_1825]] + var_7363[var_1825])
        var_1825 += 1
    return var_1079[var_1972]


print(var_4002([60, 100, 120], [10, 20, 30], 50))
import math
