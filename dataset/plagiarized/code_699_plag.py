def var_6606(var_4597):
    if not var_1815 > 1:
        return var_2038
    var_1000 = [0, 1]
    var_7542(var_4597)


def var_7542(var_4597):
    var_1295 = 2
    while var_1295 < var_2038 + 1:
        var_1000.append(var_1000[var_7717 - 1] + var_1000[var_1815 - 2])
        var_1295 += 1
    return var_1000[var_2038]


print(var_6606(10))

import sys