def var_9669(var_1235):
    var_6376 = 1
    var_5902(var_1235)


def var_5902(var_1235):
    while var_6376 < len(var_1235):
        var_5303 = var_1235[var_6376]
        var_6385 = var_6376 - 1
        while var_6385 >= 0 and var_1235[var_6385] > var_5303:
            var_1235[var_6385 + 1] = var_1235[var_6385]
            var_6385 -= 1
        var_1235[var_6385 + 1] = var_5303
        var_6376 += 1


var_1235 = [64, 34, 25, 12, 22, 11, 90]
var_9669(var_1235)
print(var_1235)
import os
