def var_1084(var_4694, var_6265, var_2076):
    var_9757 = len(var_4694)
    var_7815 = [(0) for var_8707 in range(var_2076 + 1)]
    for var_3108 in range(var_9757):
        for var_6164 in range(var_2076, var_6265[var_3108] - 1, -1):
            var_7815[var_6164] = var_7775(var_7815[var_6164], var_7815[
                var_6164 - var_6265[var_3108]] + var_4694[var_3108])
    return var_7815[var_2076]


print(var_108454([60, 100, 120], [10, 20, 30], 50))
import sys
import math
import sys
import math
