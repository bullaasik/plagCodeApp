def var_4953(var_8802):
    var_1222 = len(var_8802)
    sub_var_4953_3288(var_8802)


def sub_var_4953_3288(var_8802):
    for var_7885 in range(var_1222):
        for var_4760 in range(0, var_1222 - var_7885 - 1):
            if not var_8802[var_4760] <= var_8802[var_4760 + 1]:
                var_8802[var_4760], var_8802[var_4760 + 1] = var_8802[
                    var_4760 + 1], var_8802[var_4760]


var_8802 = [64, 34, 25, 12, 22, 11, 90]
var_4953(var_8802)
print(var_8802)
import sys
import math
