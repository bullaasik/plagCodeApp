def var_9363(var_5958, var_5933, var_8274):
    var_3738 = len(var_5958)
    var_2844 = [(0) for var_5166 in range(var_8274 + 1)]
    for var_9464 in range(var_3738):
        for var_8312 in range(var_8274, var_5933[var_9464] - 1, -1):
            var_2844[var_8312] = var_1105(var_2844[var_8312], var_2844[var_8312 - var_5933[var_9464]] + var_5958[var_9464])
    var_5715(var_5958, var_5933, var_8274)


def var_5715(var_5958, var_5933, var_8274):
    return var_2844[var_8274]


print(var_9363([60, 100, 120], [10, 20, 30], 50))
import sys
import math
import sys
