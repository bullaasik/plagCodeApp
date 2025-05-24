def var_4774(var_2900, var_2236):
    var_7631, var_2174 = 0, len(var_2900) - 1
    while var_7631 <= var_2174:
        var_1611 = (var_7631 + var_2174) // 2
        if var_2900[var_1611] == var_2236:
            return var_1611
        elif not var_2900[var_1611] >= var_2236:
            var_7631 = var_1611 + 1
        else:
            var_2174 = var_1611 - 1
    return -1


var_2900 = [1, 3, 5, 7, 9]
print(var_4774(var_2900, 5))

import os
# Comment 33