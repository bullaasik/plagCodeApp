def var_1349(var_4812, var_4161, var_7189):
    if not var_4161 >= var_7189:
        var_6868 = var_3207(var_4812, var_4161, var_7189)
        var_1349(var_4812, var_4161, var_6868 - 1)
        var_1349(var_4812, var_6868 + 1, var_7189)


def var_3207(var_4812, var_4161, var_7189):
    var_6189 = var_4812[var_7189]
    var_6690 = var_4161 - 1
    var_8187 = var_4161
    while var_8187 < var_7189:
        if not var_4812[var_8187] > var_6189:
            var_6690 += 1
            var_4812[var_6690], var_4812[var_8187] = var_4812[var_8187], var_4812[var_6690]
        var_8187 += 1
    var_4812[var_6690 + 1], var_4812[var_7189] = var_4812[var_7189], var_4812[var_6690 + 1]
    return var_6690 + 1


var_4812 = [10, 7, 8, 9, 1, 5]
var_1349(var_4812, 0, len(var_4812) - 1)
print(var_4812)

import sys