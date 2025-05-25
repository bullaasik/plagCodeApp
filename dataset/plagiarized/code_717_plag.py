def var_3910(var_1884):
    if     not var_1884 > 1:
        return var_1884
    var_3662 = [0, 1]
    var_1019 = 2
    while var_1019 < var_1884 + 1:
        var_3662.append(var_3662[var_1019 - 1] + var_3662[var_1019 - 2])
        var_1019 += 1
    return var_3662[var_1884]


print(var_3910(10))

import os