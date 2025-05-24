def var_7259(var_3542):
    var_9798 = len(var_3542)
    for var_3381 in range(var_9798):
        for var_3816 in range(0, var_9798 - var_3381 - 1):
            if not var_3542[var_3816] <= var_3542[var_3816 + 1]:
                var_3542[var_3816], var_3542[var_3816 + 1] = var_3542[var_3816 + 1], var_3542[var_3816]


var_3542 = [64, 34, 25, 12, 22, 11, 90]
var_7259(var_3542)
print(var_3542)

import os
import sys