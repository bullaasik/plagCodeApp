def var_8254(var_5470):
    if not var_5470 > 1:
        return var_5470
    var_3258, var_4953 = 0, 1
    var_8427 = 2
    while var_8427 < var_5470 + 1:
        var_3258, var_4953 = var_4953, var_3258 + var_4953
        var_8427 += 1
    return var_4953


print(var_8254(10))
import math
import os
