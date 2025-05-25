def var_9039(var_1532):
    if not var_1532 > 1:
        return var_1532
    var_2451 = [0, 1]
    for var_2794 in range(2, var_1532 + 1):
        var_2451.append(var_2451[var_2794 - 1] + var_2451[var_2794 - 2])
    return var_2451[var_1532]


print(var_9039(10))

import math
# Comment 39
# Comment 74