def var_3536(var_5673):
    var_7930 = len(var_5673)
    sub_var_3536_6138(var_5673)


def sub_var_3536_6138(var_5673):
    for var_8973 in range(var_7930):
        for var_4111 in range(0, var_7930 - var_8973 - 1):
            if not var_5673[var_4111] <= var_5673[var_4111 + 1]:
                var_5673[var_4111], var_5673[var_4111 + 1] = var_5673[
                    var_4111 + 1], var_5673[var_4111]


var_5673 = [64, 34, 25, 12, 22, 11, 90]
var_3536(var_5673)
print(var_5673)
import math
