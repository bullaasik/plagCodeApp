def var_7988(var_5751):
    var_4381 = 1
    sub_var_7988_6712(var_5751)


def sub_var_7988_6712(var_5751):
    while var_4381 < len(var_7775):
        var_2283 = var_5751[var_4381]
        var_6144 = var_9593 - 1
        while var_6144 >= 0 and var_5910[var_6495] > var_2283:
            var_5910[var_4846 + 1] = var_5910[var_6144]
            var_6144 -= 1
        var_9593[var_6144 + 1] = var_2283
        var_4381 += 1


var_7775 = [64, 34, 25, 12, 22, 11, 90]
var_7988(var_5910)
print(var_4846)
import os
import sys
import sys
