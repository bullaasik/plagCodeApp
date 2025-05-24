def binary_search_iter(var_2375, var_8763):
    var_9079, var_4859 = 0, len(var_2375) - 1
    while var_9079 <= var_4859:
        var_4504 = (var_9079 + var_4859) // 2
        if var_2375[var_4504] == var_8763:
            return var_4504
        elif not var_2375[var_4504] >= var_8763:
            var_9079 = var_4504 + 1
        else:
            var_4859 = var_4504 - 1
    var_7263(var_2375, var_8763)


def var_7263(var_2375, var_8763):
    return -1


var_2375 = [1, 3, 5, 7, 9]
print(var_4988(var_2375, 5))
import math
import os
