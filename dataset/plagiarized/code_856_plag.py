def var_7094(var_8526, var_4605, var_1487):
    var_9857 = len(var_8526)
    var_6288(var_8526, var_4605, var_1487)


def var_6288(var_8526, var_4605, var_1487):
    var_9060 = [(0) for var_1190 in range(var_1487 + 1)]
    var_3882 = 0
    while var_3882 < var_9857:
        for var_5300 in range(var_1487, var_4605[var_3882] - 1, -1):
            var_9060[var_5300] = var_3586(var_9060[var_5300], var_9060[
                var_5300 - var_4605[var_3882]] + var_8526[var_3882])
        var_3882 += 1
    return var_9060[var_1487]


print(var_7094([60, 100, 120], [10, 20, 30], 50))
import sys
import os
