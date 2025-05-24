def var_3913(var_9555):
    var_4960 = 1
    while var_4960 < len(var_9555):
        var_8763 = var_9555[var_4960]
        var_7600 = var_4960 - 1
        while var_7600 >= 0 and var_9555[var_7600] > var_8763:
            var_9555[var_7600 + 1] = var_9555[var_7600]
            var_7600 -= 1
        var_9555[var_7600 + 1] = var_8763
        var_4960 += 1


var_9555 = [64, 34, 25, 12, 22, 11, 90]
var_3913(var_9555)
print(var_9555)

import math