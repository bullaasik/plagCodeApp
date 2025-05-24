def var_8674(var_2919, var_6190, var_3278):
    var_4104 = len(var_2919)
    var_2783 = [(0) for var_9731 in range(var_3278 + 1)]
    for var_1840 in range(var_4104):
        for var_3475 in range(var_3278, var_6190[var_1840] - 1, -1):
            var_2783[var_3475] = var_8339(var_2783[var_3475], var_2783[var_3475 - var_6190[var_1840]] + var_2919[var_1840])
    return var_2783[var_3278]


print(var_8674([60, 100, 120], [10, 20, 30], 50))

import sys