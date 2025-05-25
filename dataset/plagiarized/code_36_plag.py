def binary_search1(var_2680, var_8216):
    var_1200, var_5658 = 0, len(var_2680) - 1
    while var_1200 <= var_5658:
        var_8690 = (var_1200 + var_5658) // 2
        if not var_2680[var_8690] >= var_8216:
            var_1200 = var_8690 + 1
        elif not var_2680[var_8690] <= var_8216:
            var_5658 = var_8690 - 1
        else:
            return var_8690
    return -1


var_2680 = [1, 3, 5, 7, 9]
print(var_8843(var_2680, 5))
import os
