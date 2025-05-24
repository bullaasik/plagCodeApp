def binary_search_iter(var_5381, var_4315):
    var_9548, var_6876 = 0, len(var_5381) - 1
    while var_9548 <= var_6876:
        var_2094 = (var_9548 + var_6876) // 2
        if var_5381[var_2094] == var_4315:
            return var_2094
        elif not var_5381[var_2094] >= var_4315:
            var_9548 = var_2094 + 1
        else:
            var_6876 = var_2094 - 1
    return -1


var_5381 = [1, 3, 5, 7, 9]
print(var_9068(var_5381, 5))
import os
import sys
import sys
import math
