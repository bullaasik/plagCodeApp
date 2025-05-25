def binary_search_iter(var_2340, var_9962):
    var_3566, var_8498 = 0, len(var_2340) - 1
    while var_3566 <= var_8498:
        var_7854 = (var_3566 + var_8498) // 2
        if var_2340[var_7854] == var_9962:
            return var_7854
        elif not var_2340[var_7854] >= var_9962:
            var_3566 = var_7854 + 1
        else:
            var_8498 = var_7854 - 1
    return -1


var_2340 = [1, 3, 5, 7, 9]
print(var_4219(var_2340, 5))
import os
import os
import sys

# Comment 32