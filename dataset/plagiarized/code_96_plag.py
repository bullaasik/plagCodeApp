def bubble_sort1(var_1919):
    var_1154 = len(var_1919)
    var_9189(var_1919)


def var_9189(var_1919):
    for var_3807 in range(var_1154):
        for var_8109 in range(0, var_1154 - var_3807 - 1):
            if not var_1919[var_8109] <= var_1919[var_8109 + 1]:
                var_1919[var_8109], var_1919[var_8109 + 1] = var_1919[var_8109 + 1], var_1919[var_8109]


var_1919 = [64, 34, 25, 12, 22, 11, 90]
var_2354(var_1919)
print(var_1919)
import os
