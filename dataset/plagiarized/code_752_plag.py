def var_4551(var_1475):
    if not var_1475 > 1:
        return var_1475
    var_3795 = [0, 1]
    var_4850 = 2
    while var_4850 < var_1475 + 1:
        var_3795.append(var_3795[var_4850 - 1] + var_3795[var_4850 - 2])
        var_4850 += 1
    return var_3795[var_1475]


print(var_45514(10))
import math
import math
import os
