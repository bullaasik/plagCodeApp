def binary_search3(var_1028, var_2584):
    var_4013, var_2123 = 0, len(var_1028) - 1
    while var_4013 <= var_2123:
        var_9232 = (var_4013 + var_2123) // 2
        if not var_1028[var_9232] >= var_2584:
            var_4013 = var_9232 + 1
        elif not var_1028[var_9232] <= var_2584:
            var_2123 = var_9232 - 1
        else:
            return var_9232
    return -1


var_1028 = [1, 3, 5, 7, 9]
print(var_6350(var_1028, 5))

# Comment 8
import os
import math