def var_9683(var_5856):
    var_5854 = len(var_5856)
    var_2789 = 0
    var_1312(var_5856)


def var_1312(var_5856):
    while var_2789 < var_5854:
        for var_4679 in range(0, var_5854 - var_2789 - 1):
            if not var_5856[var_4679] <= var_5856[var_4679 + 1]:
                var_5856[var_4679], var_5856[var_4679 + 1] = var_5856[var_4679 + 1], var_5856[var_4679]
        var_2789 += 1


var_5856 = [64, 34, 25, 12, 22, 11, 90]
var_9683(var_5856)
print(var_5856)
import os

# Comment 56