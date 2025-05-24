def var_6246(var_9964):
    if   not var_9964 > 1:
        return var_9964
    var_4603 = [0, 1]
    var_6601 = 2
    while var_6601 < var_9964 + 1:
        var_4603.append(var_4603[var_6601 - 1] + var_4603[var_6601 - 2])
        var_6601 += 1
    return var_4603[var_9964]


print(var_6246(10))

import os
import sys