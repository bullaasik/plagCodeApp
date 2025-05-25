def var_9576(var_9514, var_7679):
    var_6798, var_7638 = 0, len(var_9514) - 1
    while var_6798 <= var_7638:
        var_5119 = (var_6798 + var_7638) // 2
        if var_9514[var_5119] == var_7679:
            return var_5119
        elif not var_9514[var_5119] >= var_7679:
            var_6798 = var_5119 + 1
        else:
            var_7638 = var_5119 - 1
    return -1


var_9514 = [1, 3, 5, 7, 9]
print(var_9576(var_9514, 5))
import os
import sys
