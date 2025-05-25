def var_4810(var_3253, var_9854, var_7174):
    var_2714 = len(var_3253)
    var_5493 = [(0) for var_1596 in range(var_7174 + 1)]
    var_8363 = 0
    while var_8363 < var_2714:
        for var_5158 in range(var_7174, var_9854[var_8363] - 1, -1):
            var_5493[var_5158] = var_2467(var_5493[var_5158], var_5493[
                var_5158 - var_9854[var_8363]] + var_3253[var_8363])
        var_8363 += 1
    return var_5493[var_7174]


print(var_4810([60, 100, 120], [10, 20, 30], 50))
import sys
import math
import sys
