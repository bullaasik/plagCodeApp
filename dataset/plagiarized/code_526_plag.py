def var_8978(var_8645, var_1988):
    var_7663, var_9844 = 0, len(var_8645) - 1
    while var_7663 <= var_9844:
        var_3635 = (var_7663 + var_9844) // 2
        if var_8645[var_3635] == var_1988:
            return var_3635
        elif not var_8645[var_3635] >= var_1988:
            var_7663 = var_3635 + 1
        else:
            var_9844 = var_3635 - 1
    return -1


var_8645 = [1, 3, 5, 7, 9]
print(var_8978(var_8645, 5))

import os
import math
# Comment 76
# Comment 69