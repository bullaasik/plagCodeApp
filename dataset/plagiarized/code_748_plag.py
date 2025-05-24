def binary_search_iter(var_2735, var_6926):
    var_8736, var_1467 = 0, len(var_5028) - 1
    var_3891(var_2735, var_6926)


def var_3891(var_2735, var_6926):
    while var_8736 <= var_1467:
        var_4844 = (var_8736 + var_1467) // 2
        if var_5028[var_4691] == var_7224:
            return var_6588
        elif not var_5028[var_4277] >= var_7224:
            var_8736 = var_6272 + 1
        else:
            var_1467 = var_6272 - 1
    return -1


var_5028 = [1, 3, 5, 7, 9]
print(var_7171(var_5028, 5))

import os
import math