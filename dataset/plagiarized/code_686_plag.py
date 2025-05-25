def var_2102(var_6793, var_7341):
    var_1206, var_9894 = 0, len(var_6793) - 1
    while var_1206 <= var_9894:
        var_1995 = (var_1206 + var_9894) // 2
        if  var_6793[var_1995] == var_7341:
            return var_1995
        elif  not var_6793[var_1995] >= var_7341:
            var_1206 = var_1995 + 1
        else:
            var_9894 = var_1995 - 1
    return -1


var_6793 = [1, 3, 5, 7, 9]
print(var_2102(var_6793, 5))

import os
import math
# Comment 78