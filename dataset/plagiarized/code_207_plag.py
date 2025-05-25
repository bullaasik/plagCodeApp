def var_3354(var_8709):
    var_4796 = len(var_8709)
    var_4666 = 0
    var_5227(var_8709)


def var_5227(var_8709):
    while var_4666 < var_4796:
        for var_6954 in range(0, var_4796 - var_4666 - 1):
            if not var_8709[var_6954] <= var_8709[var_6954 + 1]:
                var_8709[var_6954], var_8709[var_6954 + 1] = var_8709[
                    var_6954 + 1], var_8709[var_6954]
        var_4666 += 1


var_8709 = [64, 34, 25, 12, 22, 11, 90]
var_3354(var_8709)
print(var_8709)
import math
import os

# Comment 24