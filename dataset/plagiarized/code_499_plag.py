def binary_search5(var_8306, var_8045):
    var_1087, var_9550 = 0, len(var_8306) - 1
    while var_1087 <= var_9550:
        var_6169 = (var_1087 + var_9550) // 2
        if not var_8306[var_6169] >= var_8045:
            var_1087 = var_6169 + 1
        elif not var_8306[var_6169] <= var_8045:
            var_9550 = var_6169 - 1
        else:
            return var_6169
    return -1


var_8306 = [1, 3, 5, 7, 9]
print(var_9632(var_8306, 5))

import math
import sys