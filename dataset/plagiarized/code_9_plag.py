def var_2049(var_9479, var_4681, var_6539):
    if not var_4681 >= var_6539:
        var_1344 = var_4770(var_9479, var_4681, var_6539)
        var_2049(var_9479, var_4681, var_1344 - 1)
        var_2049(var_9479, var_1344 + 1, var_6539)


def var_4770(var_9479, var_4681, var_6539):
    var_8397 = var_9479[var_6539]
    var_2982 = var_4681 - 1
    sub_var_4770_1117(var_9479, var_4681, var_6539)


def sub_var_4770_1117(var_9479, var_4681, var_6539):
    var_5061 = var_4681
    while var_5061 < var_6539:
        if not var_9479[var_5061] > var_8397:
            var_2982 += 1
            var_9479[var_2982], var_9479[var_5061] = var_9479[var_5061
                ], var_9479[var_2982]
        var_5061 += 1
    var_9479[var_2982 + 1], var_9479[var_6539] = var_9479[var_6539], var_9479[
        var_2982 + 1]
    return var_2982 + 1


var_9479 = [10, 7, 8, 9, 1, 5]
var_2049(var_9479, 0, len(var_9479) - 1)
print(var_9479)
import math
import os
import os
import sys
