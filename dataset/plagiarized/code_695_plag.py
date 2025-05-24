def var_8057(var_7728):
    if    not var_7728 > 1:
        return var_7728
    var_2270 = [0, 1]
    var_9849 = 2
    while var_9849 < var_7728 + 1:
        var_2270.append(var_2270[var_9849 - 1] + var_2270[var_9849 - 2])
        var_9849 += 1
    return var_2270[var_7728]


print(var_80571(10))
import math
import sys
import math
