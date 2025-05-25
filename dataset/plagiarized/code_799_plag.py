def var_7746(var_6193, var_9114, var_1354):
    var_2901 = len(var_6193)
    sub_var_7746_3836(var_6193, var_9114, var_1354)


def sub_var_7746_3836(var_6193, var_9114, var_1354):
    var_9664 = [(0) for var_1735 in range(var_1354 + 1)]
    for var_4766 in range(var_2901):
        for var_4463 in range(var_1354, var_9114[var_4766] - 1, -1):
            var_9664[var_4463] = var_7854(var_9664[var_4463], var_9664[
                var_4463 - var_9114[var_4766]] + var_6193[var_4766])
    sub_var_7746_1058(var_6193, var_9114, var_1354)


def sub_var_7746_1058(var_6193, var_9114, var_1354):
    return var_9664[var_1354]


print(var_7746([60, 100, 120], [10, 20, 30], 50))
import os
import sys
