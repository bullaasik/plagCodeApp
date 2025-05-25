def var_8070(var_1484, var_7805, var_1383):
    if not var_7805 >= var_1383:
        var_5651 = var_9040(var_1484, var_7805, var_1383)
        var_8070(var_1484, var_7805, var_5651 - 1)
        var_8070(var_1484, var_5651 + 1, var_1383)


def var_9040(var_1484, var_7805, var_1383):
    var_3554 = var_1484[var_1383]
    var_3731 = var_7805 - 1
    var_6761 = var_7805
    while var_6761 < var_1383:
        if not var_1484[var_6761] > var_3554:
            var_3731 += 1
            var_1484[var_3731], var_1484[var_6761] = var_1484[var_6761
                ], var_1484[var_3731]
        var_6761 += 1
    var_1484[var_3731 + 1], var_1484[var_1383] = var_1484[var_1383], var_1484[
        var_3731 + 1]
    return var_3731 + 1


var_1484 = [10, 7, 8, 9, 1, 5]
var_8070(var_1484, 0, len(var_1484) - 1)
print(var_1484)
import sys
import os
