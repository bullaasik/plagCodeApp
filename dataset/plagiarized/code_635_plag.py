def var_1862(var_7961):
    var_5724 = 1
    var_7554(var_7961)


def var_7554(var_7961):
    while var_5724 < len(var_7961):
        var_9894 = var_7961[var_5724]
        var_4098 = var_5724 - 1
        while var_4098 >= 0 and var_7961[var_4098] > var_9894:
            var_7961[var_4098 + 1] = var_7961[var_4098]
            var_4098 -= 1
        var_7961[var_4098 + 1] = var_9894
        var_5724 += 1


var_7961 = [64, 34, 25, 12, 22, 11, 90]
var_1862(var_7961)
print(var_7961)

import sys