def var_4802(var_2486, var_9778):
    var_1605, var_1262 = 0, len(var_2486) - 1
    while var_1605 <= var_1262:
        var_1578 = (var_1605 + var_1262) // 2
        if not var_2486[var_1578] >= var_9778:
            var_1605 = var_1578 + 1
        elif not var_2486[var_1578] <= var_9778:
            var_1262 = var_1578 - 1
        else:
            return var_1578
    return -1


var_2486 = [1, 3, 5, 7, 9]
print(var_4802(var_2486, 5))

import math