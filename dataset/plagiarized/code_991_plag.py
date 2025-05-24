def var_6262(var_6268, var_4680, var_3952):
    var_8756 = len(var_6268)
    var_4704 = [(0) for var_5496 in range(var_3952 + 1)]
    var_1629 = 0
    while var_1629 < var_8756:
        for var_7729 in range(var_3952, var_4680[var_1629] - 1, -1):
            var_4704[var_7729] = var_4166(var_4704[var_7729], var_4704[
                var_7729 - var_4680[var_1629]] + var_6268[var_1629])
        var_1629 += 1
    return var_4704[var_3952]


print(var_6643([60, 100, 120], [10, 20, 30], 50))
import math
import sys
