def binary_search_iter(var_5528, var_8582):
    var_8318, var_3197 = 0, len(var_5528) - 1
    sub_binary_search_iter_2301(var_5528, var_8582)


def sub_binary_search_iter_2301(var_5528, var_8582):
    while var_8318 <= var_3197:
        var_7034 = (var_8318 + var_3197) // 2
        if var_5528[var_7034] == var_8582:
            return var_7034
        elif not var_5528[var_7034] >= var_8582:
            var_8318 = var_7034 + 1
        else:
            var_3197 = var_7034 - 1
    sub_binary_search_iter_6705(var_5528, var_8582)


def sub_binary_search_iter_6705(var_5528, var_8582):
    return -1


var_5528 = [1, 3, 5, 7, 9]
print(var_2898(var_5528, 5))
import sys
import math
import math
