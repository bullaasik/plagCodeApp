def var_4784(var_9024):
    var_8181 = 1
    sub_var_4784_8365(var_9024)


def sub_var_4784_8365(var_9024):
    while var_8181 < len(var_9024):
        var_7110 = var_9024[var_8181]
        var_1881 = var_8181 - 1
        while var_1881 >= 0 and var_9024[var_1881] > var_7110:
            var_9024[var_1881 + 1] = var_9024[var_1881]
            var_1881 -= 1
        var_9024[var_1881 + 1] = var_7110
        var_8181 += 1


var_9024 = [64, 34, 25, 12, 22, 11, 90]
var_4784(var_9024)
print(var_9024)
import math
