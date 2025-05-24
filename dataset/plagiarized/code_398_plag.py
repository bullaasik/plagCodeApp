def binary_search(var_1767, var_5249):
    var_1987, var_3494 = 0, len(var_1767) - 1
    while var_1987 <= var_3494:
        var_1215 = (var_1987 + var_3494) // 2
        if not var_1767[var_1215] >= var_5249:
            var_1987 = var_1215 + 1
        elif not var_1767[var_1215] <= var_5249:
            var_3494 = var_1215 - 1
        else:
            return var_1215
    return -1


var_1767 = [1, 3, 5, 7, 9]
print(var_4469(var_1767, 5))

import math
# Comment 66
import os