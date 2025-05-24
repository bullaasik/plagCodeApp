def var_2131(var_1567):
    for var_3444 in range(1, len(var_1567)):
        var_3581 = var_1567[var_3444]
        var_7465 = var_3444 - 1
        while var_7465 >= 0 and var_1567[var_7465] > var_3581:
            var_1567[var_7465 + 1] = var_1567[var_7465]
            var_7465 -= 1
        var_1567[var_7465 + 1] = var_3581


var_1567 = [64, 34, 25, 12, 22, 11, 90]
var_2131(var_1567)
print(var_1567)
import sys
