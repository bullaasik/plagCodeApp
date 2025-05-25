def var_6473(var_3323, var_1341):
    var_1208, var_8775 = 0, len(var_3323) - 1
    while var_1208 <= var_8775:
        var_8011 = (var_1208 + var_8775) // 2
        if not var_3323[var_8011] >= var_1341:
            var_1208 = var_8011 + 1
        elif not var_3323[var_8011] <= var_1341:
            var_8775 = var_8011 - 1
        else:
            return var_8011
    sub_var_6473_8763(var_3323, var_1341)


def sub_var_6473_8763(var_3323, var_1341):
    return -1


var_3323 = [1, 3, 5, 7, 9]
print(var_6473(var_3323, 5))
import math
